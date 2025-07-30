
import streamlit as st
import joblib
import pandas as pd

# Load the saved model (no scaler needed for raw model)
model = joblib.load('raw_model.pkl')

# Streamlit App Config
st.set_page_config(page_title="Prototype Predictor", layout="centered")
st.title("🌤️ Solar Prototype Prediction App")
st.subheader("Predict Prototype Irradiance and Temperature")

# Input fields
hour = st.number_input("Enter Hour (0–23):", min_value=0, max_value=23, step=1)
temp_raw = st.number_input("Enter Ambient Temperature (°C):")
irr_raw = st.number_input("Enter Reference Irradiance (W/m²):")

# Predict button
if st.button("Predict Prototype Values"):
    # Prepare input DataFrame
    input_df = pd.DataFrame([[hour, temp_raw, irr_raw]],
                            columns=['Hour', 'Ref.Temp(℃)', 'Ref. Irr (W/㎡)'])

    # Make prediction
    prediction = model.predict(input_df)

    # Display results
    st.success("Prediction Successful ✅")
    st.write(f"🔆 **Predicted Prototype Irradiance:** `{round(prediction[0][0], 2)} W/m²`")
    st.write(f"🌡️ **Predicted Prototype Temperature:** `{round(prediction[0][1], 2)} °C`")
