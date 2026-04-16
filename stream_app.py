import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Insurance Premium Category Predictor")

st.markdown("Enter your details below")

age = st.number_input("Age", min_value=0, max_value=100)
weight = st.number_input("Weight (kg)", min_value=0.5)
height = st.number_input("Height (m)", min_value=0.5, value=5.0)
income_lpa = st.number_input("Income LPA", min_value=0.5, value=10.0)
smoker = st.radio("Are you a smoker?", options=[True, False])
city = st.text_input("City", value = "Mumbai")
occupation = st.selectbox("Occupation", options=['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'])

if st.button("Premium Predict"):
    input_data = {
        'age': age,
        'weight': weight,
        'height': height,
        'income_lpa': income_lpa,
        'smoker': smoker,
        'city': city,
        'occupation': occupation
    }
    
    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            print(result)
            st.success(f"Predicted Insurance Premium Category: **{result['prediction_category']}**")
        else:
            st.error(f"{response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect ot the FastAPI server. Make sure it's running on port 8000")