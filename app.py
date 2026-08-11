import pandas as pd
import plotly.express as px
import streamlit as st

# Título
st.header('Dashboard de vehículos en venta 🚗')

# 👇 Mensaje inicial
st.write("Selecciona una opción para ver los gráficos 👇")

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Checkbox histograma
hist_checkbox = st.checkbox('Mostrar histograma del odómetro')

if hist_checkbox:
    st.write('Distribución del odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox scatter
scatter_checkbox = st.checkbox('Mostrar gráfico de dispersión (precio vs odómetro)')

if scatter_checkbox:
    st.write('Relación entre precio y odómetro')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)