import streamlit as st


def render():
    """Render the simplified sidebar with navigation and settings"""

    with st.sidebar:
        st.image("images/logo.png", width=40)

        # Main navigation
        st.subheader("Navigation", divider="grey")

        # Home section
        if st.sidebar.button(
            "Home",
            key="nav_home",
            use_container_width=True,
            help="Home section",
            icon=":material/home:",
        ):
            st.session_state.active_section = "Home"

        # Dashboard section
        if st.sidebar.button(
            "Dashboards",
            key="nav_dashboard",
            use_container_width=True,
            help="View MVP performance visualizations",
            icon=":material/assessment:",
        ):
            st.session_state.active_section = "Dashboards"
            st.session_state.active_dashboard = "Landing"
            st.rerun()

        # Reports section
        if st.sidebar.button(
            "Reports",
            key="nav_reports",
            use_container_width=True,
            help="Access detailed analysis reports",
            icon=":material/file_copy:",
        ):
            st.session_state.active_section = "Reports"
            st.session_state.active_report = "Landing"
            st.rerun()

        # Tools section
        if st.sidebar.button(
            "Tools",
            key="nav_tools",
            use_container_width=True,
            help="Use analytical tools and customer search",
            icon=":material/build_circle:",
        ):
            st.session_state.active_section = "Tools"
            st.session_state.active_tool = "Landing"
            st.rerun()
