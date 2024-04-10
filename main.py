import streamlit as st
import pandas as pd

file_path = 'car_data.csv'

try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    st.error('car_data.csv file not found. Please make sure it is located in the correct directory.')
    st.stop()

def filter_data(car_name, transmission_type, selling_price_range, year_range):
    filtered_data = data
    if car_name:
        filtered_data = filtered_data[filtered_data['Car_Name'].str.contains(Car_Name, case=False)]
    if transmission_type:
        filtered_data = filtered_data[filtered_data['Transmission'].isin(transmission_type)]
    filtered_data = filtered_data[
        (filtered_data['Selling_Price'] >= selling_price_range[0]) &
        (filtered_data['Selling_Price'] <= selling_price_range[1])
    ]
    filtered_data = filtered_data[
        (filtered_data['Year'] >= year_range[0]) &
        (filtered_data['Year'] <= year_range[1])
    ]
    return filtered_data

st.sidebar.header('Filter Options')
car_name = st.sidebar.text_input('Car Name')
transmission_type = st.sidebar.multiselect('Transmission Type', ['Manual', 'Automatic'], default=['Manual', 'Automatic'])
selling_price_range = st.sidebar.slider('Selling Price Range', 0, 20, (0, 20))
year_range = st.sidebar.slider('Year Range', 2000, 2024, (2000, 2024))

if st.sidebar.button('Submit'):
    filtered_data = filter_data(car_name, transmission_type, selling_price_range, year_range)
    st.write(filtered_data)
else:
    st.write(data)
