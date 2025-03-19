import streamlit as st


def render():
    """Render the main reports landing page"""
    from . import sidebar

    sidebar.render()

    if (
        "active_report" not in st.session_state
        or st.session_state.active_report == "Landing"
    ):
        from . import landing

        landing.render()
