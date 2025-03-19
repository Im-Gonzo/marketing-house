import os
import numpy as np
import seaborn as sns
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from pathlib import Path
from lib.customer.cltv.btyd_model import BTYDModel
from lib.customer.segmentation.rfm_model import RFMModel
from lib.customer.segmentation.kmeans_model import KMeansModel


def render():
    """Customer Value Dashboard Page"""

    st.title("Customer  Value Hub")

    file_path = Path(os.path.join(os.getcwd(), "data/customer/preprocessed/test.csv"))
    segments_path = Path(os.path.join(os.getcwd(), "data/customer/segments.csv"))

    if not file_path:
        st.info("Upload CSV file first")

        with st.expander("Expected Data Format"):
            st.markdown("""
            The CSV file should contain the following columns:
            - **CustomerID**: Unique identifier for each customer
            - **InvoiceDate**: Date of purchase (YYYY-MM-DD)
            - **Invoice**: Invoice number
            - **Quantity**: Number of items purchased
            - **Price**: Price per item
            
            Additional columns will be used as features for clustering.
            """)

        return

    if file_path is not None:
        df = pd.read_csv(file_path)

    tab1, tab2, tab3 = st.tabs(
        ["RFM Analysis", "Customer Lifetime Value", "Customer Segmentation"]
    )

    # RFM Analysis
    with tab1:
        with st.spinner("Ejecutando Análisis RFM..."):
            rfm_model = RFMModel(file_path)
            rfm_data = rfm_model.calculate()

            st.subheader("Análisis RFM")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Recencia Promedio (días)", f"{rfm_data['recency'].mean():.1f}"
                )
            with col2:
                st.metric("Frecuencia Promedio", f"{rfm_data['frequency'].mean():.1f}")
            with col3:
                st.metric(
                    "Valor Monetario Promedio",
                    f"{rfm_data['monetary_value'].mean():.1f}",
                )

            st.subheader("Distribuciones RFM")
            recency_fig = px.histogram(
                rfm_data,
                x="recency",
                nbins=20,
                title="Distribución de Recencia",
                labels={"recency": "Recencia (Días)"},
                color_discrete_sequence=["#3366CC"],
            )

            recency_fig.update_layout(
                xaxis_title="Recencia (Días)", yaxis_title="Cantidad", showlegend=False
            )

            col1, col2 = st.columns(2)

            with col1:
                freq_fig = px.histogram(
                    rfm_data,
                    x="frequency",
                    nbins=20,
                    title="Distribución de Frecuencia",
                    color_discrete_sequence=["#FF9900"],
                )
                freq_fig.update_layout(
                    xaxis_title="Frecuencia (compras)",
                    yaxis_title="Cantidad",
                    showlegend=False,
                )
                st.plotly_chart(freq_fig, use_container_width=True)

            with col2:
                monetary_fig = px.histogram(
                    rfm_data,
                    x="monetary_value",
                    nbins=20,
                    title="Distribución de Valor Monetario",
                    color_discrete_sequence=["#109618"],
                )
                monetary_fig.update_layout(
                    xaxis_title="Valor Monetario ($)",
                    yaxis_title="Cantidad",
                    showlegend=False,
                )
                st.plotly_chart(monetary_fig, use_container_width=True)

            st.subheader("Relaciones RFM")
            heatmap_fig = px.density_heatmap(
                rfm_data,
                x="recency",
                y="frequency",
                z="monetary_value",
                title="Frecuencia vs Recencia (color = Valor Monetario)",
                color_continuous_scale="Viridis",
            )
            st.plotly_chart(heatmap_fig, use_container_width=True)

    # Customer Lifetime Value
    with tab2:
        with st.spinner("Ejecutando Análisis de CLTV..."):
            btyd_model = BTYDModel()
            btyd_data = btyd_model.calculate(rfm_data, prediction_period=180)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(f"CLTV Promedio", f"{btyd_data['cltv'].mean():.2f}")
            with col2:
                st.metric(f"CLTV Mediano", f"{btyd_data['cltv'].median():.2f}")
            with col3:
                st.metric(f"CLTV Máximo", f"{btyd_data['cltv'].max():.2f}")

            clv_dist_fig = px.histogram(
                btyd_data,
                x="cltv",
                nbins=30,
                title="Distribuciones de Valor de Vida del Cliente",
                color_discrete_sequence=["#DC3912"],
            )
            clv_dist_fig.update_layout(
                xaxis_title="Valor de Vida del Cliente ($)",
                yaxis_title="Cantidad",
                showlegend=False,
            )
            st.plotly_chart(clv_dist_fig, use_container_width=True)

            st.subheader("Relaciones de CLV con Métricas RFM")

            relationships = [
                "CLV vs Recencia",
                "CLV vs Frecuencia",
                "CLV vs Valor Monetario",
            ]
            relationship = st.selectbox(
                "Selecciona relación para visualizar", relationships
            )

            if relationship == relationships[0]:  # CLV vs Recency
                fig = px.scatter(
                    btyd_data,
                    x="recency",
                    y="cltv",
                    title=relationships[0],
                    trendline="ols",
                    labels={
                        "recency": "Recencia (días)",
                        "cltv": "Valor de Vida del Cliente ($)",
                    },
                )
            elif relationship == relationships[1]:  # CLV vs Frequency
                fig = px.scatter(
                    btyd_data,
                    x="frequency",
                    y="cltv",
                    title=relationships[1],
                    trendline="ols",
                    labels={
                        "frequency": "Frecuencia (compras)",
                        "cltv": "Valor de Vida del Cliente ($)",
                    },
                )
            else:  # CLV vs Monetary Value
                fig = px.scatter(
                    btyd_data,
                    x="monetary_value",
                    y="cltv",
                    title=relationships[2],
                    trendline="ols",
                    labels={
                        "monetary_value": "Valor Monetario ($)",
                        "cltv": "Valor de Vida del Cliente ($)",
                    },
                )

            st.plotly_chart(fig, use_container_width=True)

            st.subheader("Top 10 Clientes por CLV")
            top_customers = btyd_data.sort_values("cltv", ascending=False).head(10)
            st.dataframe(
                top_customers[["cltv", "recency", "frequency", "monetary_value"]],
                use_container_width=True,
            )

    with tab3:
        from .components import display_segments_info, generate_scores, display_pie_chart, display_value_distribution

        display_segments_info(segments_path)

        df_rfm = generate_scores(btyd_data)
        
        display_pie_chart(df_rfm)

        display_value_distribution(df_rfm)

        