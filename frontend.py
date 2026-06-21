import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Health Insurance Premium Prediction")

st.markdown("Enter the details of the patient to predict the health insurance premium category.")

#input fields
age = st.number_input("Age", min_value=1, max_value=120, value=30)
weight = st.number_input("Weight (kg)", min_value=0.0, value=70.5)
height = st.number_input("Height (m)", min_value=0.0, value=1.75)
income_lpa = st.number_input("Income (LPA)", min_value=0.0, value=5.0)
smoker = st.selectbox("Smoker", options=["yes", "no"])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox("Occupation", options=["retired", "freelancer", "student", "government_job","business_owner", "unemployed","private_job"])

if st.button("Predict Premium"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }
    try:
        response = requests.post(API_URL, json=input_data)
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Health Insurance Premium Category: **{result['prediction']}**")
        else:
            st.error(f"{response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError as e:
        st.error(f"An error occurred: {e}")