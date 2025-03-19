import pandas as pd
import streamlit as st
import plotly.express as px

seg_map = {
    r"[1-2][1-2]": "Hibernando",
    r"[1-2][3-4]": "En_riesgo",
    r"[1-2]5": "No_se_les_puede_perder",
    r"3[1-2]": "About_to_sleep",
    r"33": "Clientes_que_necesitan_atencion",
    r"[3-4][4-5]": "Clientes_fieles",
    r"41": "Prometedores",
    r"51": "Clientes_recientes",
    r"[4-5][2-3]": "Cliente_fidelizado_potencial",
    r"5[4-5]": "Campeones",
}


def display_segments_info(segments_path):
    segments = pd.read_csv(segments_path, delimiter=";")

    # Add a title and description
    st.header("🏆 Analisis de Segmentos de Clientes")

    # Apply custom styling to the dataframe
    def highlight_segment_type(val):
        """Add color to different segment types"""
        if "Campeones" in str(val) or "fieles" in str(val):
            return "background-color: #A8E6CF; color: #1D3557"  # Green for high-value
        elif "riesgo" in str(val) or "perder" in str(val) or "Sleep" in str(val):
            return "background-color: #FFD3B6; color: #1D3557"  # Orange for at-risk
        elif "Hibernando" in str(val) or "Perdido" in str(val):
            return "background-color: #FFAAA5; color: #1D3557"  # Red for lost
        else:
            return "background-color: #DAE7FE; color: #1D3557"  # Blue for others

    # Apply the styling to the first column only
    styled_df = (
        segments.style.applymap(highlight_segment_type, subset=["Segmento de clientes"])
        .set_properties(
            **{
                "font-size": "14px",
                "font-family": "Arial",
                "text-align": "left",
                "border": "1px solid #EEEEEE",
                "padding": "10px",
            }
        )
        .set_table_styles(
            [
                {
                    "selector": "th",
                    "props": [
                        ("font-size", "15px"),
                        ("font-weight", "bold"),
                        ("background-color", "#F0F2F6"),
                        ("color", "#1E3A8A"),
                        ("text-align", "left"),
                        ("padding", "12px"),
                    ],
                }
            ]
        )
    )

    with st.expander("Categorias"):
        st.dataframe(styled_df, use_container_width=True, height=450)


def generate_scores(df) -> pd.DataFrame:
    df_rfm = df.copy()

    df_rfm["recency_score"] = pd.qcut(df_rfm["recency"], 5, labels=[5, 4, 3, 2, 1])
    df_rfm["frequency_score"] = pd.qcut(
        df_rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]
    )
    df_rfm["segment"] = df_rfm["recency_score"].astype(str) + df_rfm[
        "frequency_score"
    ].astype(str)

    df_rfm["segment"] = df_rfm["segment"].replace(seg_map, regex=True)
    df_rfm.index = df_rfm.index.astype(str)

    return df_rfm


def display_pie_chart(df_rfm):
    """Display a pie chart showing the distribution of monetary value across segments."""
    st.subheader("Distribución de Valor por Segmentos de Clientes")

    # Calculate total monetary value for each segment
    segment_data = df_rfm.groupby("segment")["monetary_value"].sum().reset_index()

    # Calculate percentages
    total = segment_data["monetary_value"].sum()
    segment_data["percentage"] = (segment_data["monetary_value"] / total * 100).round(1)

    # Sort by value for better visualization
    segment_data = segment_data.sort_values("monetary_value", ascending=False)

    # Define segment colors
    segment_colors = {
        "Campeones": "#1f77b4",
        "Clientes_fieles": "#17becf",
        "Cliente_fidelizado_potencial": "#9467bd",
        "Clientes_recientes": "#2ca02c",
        "Prometedores": "#8c564b",
        "Clientes_que_necesitan_atencion": "#e377c2",
        "About_to_sleep": "#ff7f0e",
        "En_riesgo": "#d62728",
        "No_se_les_puede_perder": "#bcbd22",
        "Hibernando": "#7f7f7f",
    }

    # Create the pie chart
    fig = px.pie(
        segment_data,
        values="monetary_value",
        names="segment",
        color="segment",
        color_discrete_map=segment_colors,
        title="Distribución del Valor Monetario por Segmento",
        hover_data=["percentage"],
        labels={
            "monetary_value": "Valor Monetario",
            "percentage": "Porcentaje del Total",
        },
    )

    # Update traces for better appearance
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        texttemplate="%{label}<br>%{percent:.1f}%",
        hovertemplate="<b>%{label}</b><br>Valor: $%{value:.2f}<br>Porcentaje: %{customdata[0]:.1f}%",
    )

    # Update layout
    fig.update_layout(
        height=600,
        width=800,
        legend_title="Segmentos",
        uniformtext_minsize=12,
        uniformtext_mode="hide",
    )

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)


def display_value_distribution(df_rfm):
    segment_data = df_rfm.groupby("segment")["monetary_value"].sum().reset_index()
    total = segment_data["monetary_value"].sum()
    segment_data["percentage"] = (segment_data["monetary_value"] / total * 100).round(1)
    segment_data = segment_data.sort_values("monetary_value", ascending=False)

    # Add a summary table below
    st.subheader("Detalle de Distribución de Valor")

    # Add formatted table with monetary values
    display_df = segment_data.copy()

    # Format monetary value in currency format
    display_df["valor_formato"] = display_df["monetary_value"].apply(
        lambda x: f"${x:,.2f}"
    )

    # Display table
    st.dataframe(
        display_df[["segment", "valor_formato", "percentage"]],
        hide_index=True,
        column_config={
            "segment": "Segmento",
            "valor_formato": "Valor Monetario",
            "percentage": st.column_config.ProgressColumn(
                "Porcentaje del Total", format="%.1f%%", min_value=0, max_value=100
            ),
        },
    )
