import pandas as pd
import streamlit as st

# Load car data
data = pd.read_csv("car_data.csv")

# Define filter functions
def filter_by_car_name(df, car_name):
    if car_name:
        return df[df["car_name"].str.lower().contains(car_name.lower())]
    return df

def filter_by_transmission(df, selected_options):
    if len(selected_options) == 0:
        return df
    return df[df["transmission"].isin(selected_options)]

def filter_by_price_range(df, min_price, max_price):
    return df[(df["selling_price"] >= min_price) & (df["selling_price"] <= max_price)]

def filter_by_year_range(df, min_year, max_year):
    return df[(df["year"] >= min_year) & (df["year"] <= max_year)]

# Sidebar filters
st.sidebar.header("Car Filters")

car_name = st.sidebar.text_input("Car Name (Optional)")

transmission_options = ["Manual", "Automatic"]
selected_transmission = st.sidebar.multiselect("Transmission", transmission_options, default=transmission_options)

price_min, price_max = st.sidebar.slider(
    "Selling Price Range", min_value=0, max_value=data["selling_price"].max(), value=(0, 20)
)

year_min, year_max = st.sidebar.slider(
    "Year Range", min_value=2000, max_value=2024, value=(2000, 2024)
)

# Apply filters
filtered_data = data.copy()
filtered_data = filter_by_car_name(filtered_data, car_name)
filtered_data = filter_by_transmission(filtered_data, selected_transmission)
filtered_data = filter_by_price_range(filtered_data, price_min, price_max)
filtered_data = filter_by_year_range(filtered_data, year_min, year_max)

# Display data on main screen
st.header("Filtered Cars")
if filtered_data.empty:
    st.write("No cars found matching the filters.")
else:
    st.dataframe(filtered_data)

