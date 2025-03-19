import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Marketing House - MVP Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Set Home to default page
if "active_section" not in st.session_state:
    st.session_state.active_section = "Home"


# Main content area based on active section
if st.session_state.active_section == "Home":
    from pages.home import controller

    controller.render()

elif st.session_state.active_section == "Dashboards":
    from pages.dashboards import controller

    controller.render()

elif st.session_state.active_section == "Reports":
    from pages.reports import controller

    controller.render()

elif st.session_state.active_section == "Tools":
    from pages.tools import controller

    controller.render()
