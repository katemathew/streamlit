import streamlit as st
import pandas as pd

st.title('Hello Streamlit!')
st.write('If you see this message, your setup works.')

# Load the dataset
car_data = pd.read_csv('car_data.csv')

# Setup the sidebar
# a. Text box for car name input
car_name = st.sidebar.text_input('Car Name')

# b. Multiselect for choosing between Manual and/or Automatic
transmission_choice = st.sidebar.multiselect('Choose Transmission Type', 
                                             ['Manual', 'Automatic'], 
                                             default=['Manual', 'Automatic'])

# c. Slider for selling price range
selling_price_range = st.sidebar.slider('Selling Price Range', 
                                        min_value=0, 
                                        max_value=20, 
                                        value=(0, 20))

# d. Slider for year range
year_range = st.sidebar.slider('Year Range', 
                               min_value=2000, 
                               max_value=2024, 
                               value=(2000, 2024))

# e. Submit button
submit = st.sidebar.button('Submit')

# Filter data based on selections
def filter_data(data, car_name, transmission_choice, selling_price_range, year_range):
    filtered_data = data
    
    # Filter by car name if specified
    if car_name:
        filtered_data = filtered_data[filtered_data['Car_Name'].str.contains(car_name, case=False)]
    
    # Filter by transmission type
    if transmission_choice:
        filtered_data = filtered_data[filtered_data['Transmission'].isin(transmission_choice)]
    
    # Filter by selling price range
    filtered_data = filtered_data[(filtered_data['Selling_Price'] >= selling_price_range[0]) & 
                                  (filtered_data['Selling_Price'] <= selling_price_range[1])]
    
    # Filter by year range
    filtered_data = filtered_data[(filtered_data['Year'] >= year_range[0]) & 
                                  (filtered_data['Year'] <= year_range[1])]
    
    return filtered_data

if submit:
    # Show filtered data
    st.write(filter_data(car_data, car_name, transmission_choice, selling_price_range, year_range))
else:
    # Show original data
    st.write(car_data)
