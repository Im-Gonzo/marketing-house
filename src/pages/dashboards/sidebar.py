import streamlit as st


def render():
    """Render the dashboard sidebar with navigation and settings"""

    with st.sidebar:
        st.image("images/logo.png", width=40)

        # Main navigation
        st.subheader("Dashboards", divider="grey")

        # Back to Home button
        if st.sidebar.button(
            "← Back to Home",
            key="nav_back_home",
            use_container_width=True,
            help="Return to Home",
        ):
            st.session_state.active_section = "Home"
            st.rerun()

        # Back to dashboards button
        if st.sidebar.button(
            ":material/dashboard: Dashboard overview",
            key="nav_dashboard",
            use_container_width=True,
            help="Return to dashboards overview",
        ):
            st.session_state.active_dashboard = "Landing"
            st.rerun()

        # Customer Value section
        if st.sidebar.button(
            "Customer Value Hub",
            key="nav_customer",
            use_container_width=True,
            help="Customer Dashboards section",
            icon=":material/insert_chart:",
        ):
            st.session_state.active_dashboard = "CustomerValue"
            st.rerun()

        # Demand Navigator section
        if st.sidebar.button(
            "Demand Navigator",
            key="nav_demand",
            use_container_width=True,
            help="Demand Forecast section",
            icon=":material/insights:",
        ):
            st.session_state.active_dashboard = "DemandNavigator"
            st.rerun()

        # Marketing Performance
        if st.sidebar.button(
            "Marketing Performance Center",
            key="nav_marketing",
            use_container_width=True,
            help="Marketing Performance section",
            icon=":material/score:",
        ):
            st.session_state.active_dashboard = "MarketingPerformance"
            st.rerun()

        # Pricing & Assortment
        if st.sidebar.button(
            "Pricing & Assortment Analyzer",
            key="nav_pricing",
            use_container_width=True,
            help="Pricing & Assortment section",
            icon=":material/currency_bitcoin:",
        ):
            st.session_state.active_dashboard = "PricingAssortment"
            st.rerun()
