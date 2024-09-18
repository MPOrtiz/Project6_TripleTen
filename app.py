import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

car_data=pd.read_csv('./vehicles_us.csv')
print(car_data.info())

#Fill data  
car_data['model_year'].fillna('NoData',inplace=True)
car_data['cylinders'].fillna('NoData',inplace=True)
car_data['odometer'].fillna('NoData',inplace=True)
car_data['paint_color'].fillna('NoData',inplace=True)
car_data['is_4wd'].fillna('NoData',inplace=True)

#Data Verification
print(car_data.info())

#Encabezado
st.header("Graficos de venta de Automóviles")
# Creación de 1er botón ODOMETER
hist_button = st.button('Histograma anuncios') 
# al hacer clic en el botón
if hist_button: 
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#Creación de 2ndo botón Price
scatterprice_button = st.button('Gráfico de Dispersión de precio')
if scatterprice_button:
    st.write('Creación de gráfico de dispersión de datos para precio de autos')
    fig=px.scatter(car_data, x="model_year", y="price")
    fig.show() 

# Creación de una casilla de verificación
build_histogram = st.checkbox('Gráfico de Cilindros de Gasolina')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="cylinders")
    st.plotly_chart(fig, use_container_width=True)

#Graficas
#fig=px.histograma(data,'cylinders')
#fig.show()

