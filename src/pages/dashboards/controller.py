import streamlit as st


def render():
    """Render the main dashboard landing page"""
    from . import sidebar

    sidebar.render()

    if (
        "active_dashboard" not in st.session_state
        or st.session_state.active_dashboard == "Landing"
    ):
        from . import landing

        landing.render()

    elif st.session_state.active_dashboard == "CustomerValue":
        from . import customer_value

        customer_value.render()

    elif st.session_state.active_dashboard == "DemandNavigator":
        st.title("Demand Navigator Center")
        st.info("Under development")

    elif st.session_state.active_dashboard == "MarketingPerformance":
        st.title("Marketing Performance Center")
        st.info("Under development")

    elif st.session_state.active_dashboard == "PricingAssortment":
        st.title("Pricing & Assortment Analyzer")
        st.info("Under development")
