import streamlit as st


def render():
    """Render the main tools landing page"""
    from . import sidebar

    sidebar.render()

    if (
        "active_tool" not in st.session_state
        or st.session_state.active_tool == "Landing"
    ):
        from . import landing

        landing.render()
