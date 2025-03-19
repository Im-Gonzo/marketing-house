import streamlit as st


def render():
    """Render the landing/home page with overview metrics and introduction"""
    from . import sidebar, landing

    sidebar.render()
    landing.render()
