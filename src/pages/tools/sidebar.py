import streamlit as st


def render():
    """Render the tools sidebar with navigation and settings"""

    with st.sidebar:
        st.image("images/logo.png", width=40)

        # Main navigation
        st.subheader("Tools", divider="grey")

        # Back to Home button
        if st.sidebar.button(
            "← Back to Home",
            key="nav_back_home",
            use_container_width=True,
            help="Return to Home",
        ):
            st.session_state.active_section = "Home"
            st.rerun()
