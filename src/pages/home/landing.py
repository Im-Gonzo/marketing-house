import streamlit as st


def render():
    """Dummy Landing Page"""

    # Page header
    st.title("Marketing House Demo")
    st.markdown("Tu plataforma centralizada para el análisis de negocio y clientes")

    # Key metrics overview
    st.subheader("Monthly Performance Overview")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_metric_card("Clientes", "1,245", "+12.3%", "last month")
    with col2:
        display_metric_card("MRR", "$48,750", "+5.7%", "last month")
    with col3:
        display_metric_card("Avg CAC", "$125", "-3.2%", "last month")
    with col4:
        display_metric_card("Conversion Rate", "23.4%", "+2.1%", "last month")

    # Two column layout for additional content
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top Customer Segments")
        segments_data = {
            "Enterprise": 42,
            "Mid-Market": 28,
            "Small Business": 18,
            "Startup": 12,
        }
        # Placeholder for segment chart
        st.bar_chart(segments_data)

    with col2:
        st.subheader("Marketing Channel Performance")
        channel_data = {
            "Organic Search": 35,
            "Paid Search": 25,
            "Social Media": 20,
            "Email": 15,
            "Referral": 5,
        }
        # Placeholder for channel performance chart
        st.bar_chart(channel_data)

    # Quick access section
    st.subheader("Quick Access")
    quick_col1, quick_col2, quick_col3 = st.columns(3)

    with quick_col1:
        st.markdown("##### Recently Viewed")
        st.markdown("- Customer Segmentation Dashboard")
        st.markdown("- Monthly Performance Report")
        st.markdown("- Customer Acquisition Analysis")

    with quick_col2:
        st.markdown("##### Important Updates")
        st.markdown("- New customer segment available")
        st.markdown("- Monthly report ready for review")
        st.markdown("- 15% increase in social conversions")

    with quick_col3:
        st.markdown("##### Suggested Actions")
        st.markdown("- Review underperforming channels")
        st.markdown("- Analyze customer churn factors")
        st.markdown("- Update targeting parameters")


def display_metric_card(title, value, change, period):
    """Display a metric card with title, value, change and period"""

    # Determine if change is positive or negative
    is_positive = not change.startswith("-")
    color = "green" if is_positive else "red"
    arrow = "↑" if is_positive else "↓"

    # Create card with HTML/CSS
    st.markdown(
        f"""
    <div style="border-radius:5px; border:1px solid #e0e0e0; padding:10px; text-align:center;">
        <h3 style="margin:0; font-size:14px; color:gray;">{title}</h3>
        <h2 style="margin:10px 0; font-size:24px;">{value}</h2>
        <p style="margin:0;">
            <span style="color:{color};">{arrow} {change}</span>
            <span style="font-size:12px; color:gray;"> {period}</span>
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )
