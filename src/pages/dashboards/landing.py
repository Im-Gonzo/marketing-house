import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta


def render():
    """Dummy Landing Page"""

    st.session_state.active_dashboard = "Landing"
    st.title("Marketing House Dashboards")

    # Introduction section
    st.markdown("""
    Bienvenido al hub de dashboards de Marketing House. 
    Aquí encontrarás visualizaciones interactivas e insights que te ayudarán a entender el 
    comportamiento del cliente, predecir tendencias futuras y optimizar tus estrategias de marketing.
    """)

    # Dashboard cards section
    st.subheader("Dashboards Disponibles")
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("🧩 Customer Value Hub")
            st.markdown("""
            Analiza el valor de vida del cliente, segmentación y comportamientos
            de compra utilizando modelos CLTV y BTYD.
            
            **Key insights:**
            - Segmentación de clientes
            - Predicción de retención y churn
            - Probabilidad de compras futuras
            """)
            if st.button(
                "Ir a Customer Value Hub", key="open_cust_val", use_container_width=True
            ):
                st.session_state.active_dashboard = "CustomerValue"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.subheader("📈 Demand Navigator")
            st.markdown("""
            Proyecta la demanda futura de productos, identifica
            patrones estacionales y optimiza la planificación de inventario.
            
            **Key insights:**
            - Pronósticos de demanda a corto y largo plazo
            - Análisis de demanda
            - Tendencias por categoría de producto
            """)
            if st.button(
                "Ir a Demand Navigator", key="open_demand", use_container_width=True
            ):
                st.session_state.active_dashboard = "DemandNavigator"
                st.rerun()

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("🎯 Marketing Performance Center")
            st.markdown("""
            Evalúa la efectividad de campañas de marketing, performance de canales y 
            retorno de inversión en marketing.
            
            **Key insights:**
            - Comparación de performance de campañas
            - Análisis de atribución de canales
            - Oportunidades de optimización de ROI
            """)
            if st.button(
                "Ir a Marketing Performance",
                key="open_marketing",
                use_container_width=True,
            ):
                st.session_state.active_dashboard = "MarketingPerformance"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.subheader("💰 Analizador de Precios e Inventario")
            st.markdown("""
            Optimiza estrategias de pricing, analiza el mix de productos e identifica 
            oportunidades de optimización de ingresos.
            
            **Key insights:**
            - Análisis de elasticidad de precios
            - Efectividad del inventario de productos
            - Performance de bundles y promociones
            """)
            if st.button(
                "Ir a Pricing & Assortment",
                key="open_pricing",
                use_container_width=True,
            ):
                st.session_state.active_dashboard = "PricingAssortment"
                st.rerun()
