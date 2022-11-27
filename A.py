import streamlit as st
import pandas as pd



data = pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')

st.title("TEMA 2: Interacción con otros componentes")
st.subheader("José Luis Quevedo Orrantia")
st.write('Desarrollo de un código sobre la estructura de una aplicación web que contenga 3 controles para la predicción de ventas de productos de Walmart en el noroeste de los Estados Unidos')

st.subheader("Control: Radio")
genre = st.radio(
    "What's your Ship Mode",
    ('Second Class', 'Standard Class', 'First Class', 'Same Day'))

if genre == 'Second Class':
    st.write('You selected Second Class.')

if genre == 'Standard Class':
    st.write('You selected Standard Class.')

if genre == 'First Class':
    st.write('You selected First Class.')

if genre == 'Same Day':
    st.write('You selected Same Day.')

st.subheader("Control: Select Box")


option = st.selectbox(
    'What category would you like?',
    ('Furniture', 'Office Supplies', 'Technology'))

st.write('You selected:', option)

st.subheader("Control: Slider")
age = st.slider('How much Discount?', 0.0,0.15)
st.write("Discount: ", age)
