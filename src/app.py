import streamlit as st
import joblib
import pandas as pd
import gzip

# Load the trained model and scaler
compressed_file_path = '../models/best_model.pkl.gz'

# Decompress the file and load the model
with gzip.open(compressed_file_path, 'rb') as f:
    # Load the best model
    rf_regressor = joblib.load(f)
    
scaler = joblib.load('../models/scaler.pkl')

@st.cache_data
def predict_median_house_value(user_input):
    # Map to let the user know which number corresponds to each ocean proximity category
    ocean_proximity_mapping = {
        'NEAR BAY': 3,
        '<1H OCEAN': 0,
        'INLAND': 1,
        'NEAR OCEAN': 4,
        'ISLAND': 2
    }

    # Convert user input to corresponding number
    user_input['ocean_proximity'] = ocean_proximity_mapping.get(user_input['ocean_proximity'].upper(), None)

    # Check if the input is valid
    if user_input['ocean_proximity'] is None:
        return "Invalid input for ocean proximity!"
    else:
        # Convert user input to DataFrame
        user_input_df = pd.DataFrame(user_input, index=[0])

        # Transform user input using StandardScaler
        scaled_user_input = scaler.transform(user_input_df)

        # Make prediction
        predicted_value = rf_regressor.predict(scaled_user_input)

        # Round the predicted value to remove decimal places
        predicted_value_rounded = round(predicted_value[0])

        return predicted_value_rounded

st.title("Median House Price")

# User input section
st.sidebar.title("Let's Predict Median House Price")
longitude = st.sidebar.number_input("Longitude", value=-122.25)
latitude = st.sidebar.number_input("Latitude", value=37.85)
housing_median_age = st.sidebar.number_input("Housing Median Age")
total_rooms = st.sidebar.number_input("Total Rooms")
total_bedrooms = st.sidebar.number_input("Total Bedrooms")
population = st.sidebar.number_input("Population")
households = st.sidebar.number_input("Households")
median_income = st.sidebar.number_input("Median Income")
ocean_proximity = st.sidebar.selectbox("Ocean Proximity", ['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'])

user_input = {
    'longitude': longitude,
    'latitude': latitude,
    'housing_median_age': housing_median_age,
    'total_rooms': total_rooms,
    'total_bedrooms': total_bedrooms,
    'population': population,
    'households': households,
    'median_income': median_income,
    'ocean_proximity': ocean_proximity
}

# Make prediction and display result
predicted_value = predict_median_house_value(user_input)
st.write("Predicted Median House Price: $", predicted_value)
