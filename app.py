import streamlit as st
import pandas as pd

# Function for unit conversion
def convert_units(value, from_unit, to_unit, unit_type):
    CONVERSION_FACTORS = {
        'length': {
            'meter': 1, 'kilometer': 0.001, 'centimeter': 100, 'millimeter': 1000,
            'inch': 39.3701, 'foot': 3.28084, 'yard': 1.09361, 'mile': 0.000621371
        },
        'mass': {
            'kilogram': 1, 'gram': 1000, 'milligram': 1e6, 'pound': 2.20462, 'ounce': 35.274
        },
        'temperature': {
            'celsius': 1, 'fahrenheit': lambda c: (c * 9/5) + 32, 'kelvin': lambda c: c + 273.15
        }
    }
    if unit_type == 'temperature':
        if from_unit == 'celsius':
            return CONVERSION_FACTORS[unit_type][to_unit](value)
        elif from_unit == 'fahrenheit':
            return (value - 32) * 5/9 if to_unit == 'celsius' else (value - 32) * 5/9 + 273.15
        elif from_unit == 'kelvin':
            return value - 273.15 if to_unit == 'celsius' else (value - 273.15) * 9/5 + 32
    else:
        return value * (CONVERSION_FACTORS[unit_type][to_unit] / CONVERSION_FACTORS[unit_type][from_unit])

# Streamlit UI Configuration
st.set_page_config(page_title="Unit Converter", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        .stApp { background-color: #f5f5f5; }
        .block-container { text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Sidebar for Conversion Type Selection
st.sidebar.title("🔄 Conversion Type")
unit_types = {"Length": "length", "Mass": "mass", "Temperature": "temperature"}
unit_type = st.sidebar.selectbox("Select Unit Type", list(unit_types.keys()))

# Main Content (Centered)
st.title("Unit Converter")
units = {
    'length': ['meter', 'kilometer', 'centimeter', 'millimeter', 'inch', 'foot', 'yard', 'mile'],
    'mass': ['kilogram', 'gram', 'milligram', 'pound', 'ounce'],
    'temperature': ['celsius', 'fahrenheit', 'kelvin']
}[unit_types[unit_type]]

value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, unit_types[unit_type])
    st.success(f"Converted Value: {result:.2f} {to_unit}")