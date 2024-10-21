import streamlit as st
import pickle
import numpy as np
import pandas as pd


modell=pickle.load(open('model2.pkl','rb'))

def predict_aqi(pm25,pm10,no,no2,nox,nh3,co,so2,o3,benzene,toluene,xylene):
    
    input_features=np.array([[pm25,pm10,no,no2,nox,nh3,co,so2,o3,benzene,toluene,xylene]])
    aqi=modell.predict(input_features)
    return aqi
def main():
   
    st.title("Air Quality Index (AQI) Prediction")
    
    
    st.write("Welcome to the AQI Prediction Tool!")
    st.write("Please adjust the sliders below to input your parameters.")
    # User inputs using sliders
    pm25 = st.slider("pm25 (°C)", min_value=-30, max_value=50, value=25)
    pm10 = st.slider("pm10 (%)", min_value=0, max_value=100, value=50)
    no = st.slider(" no (m/s)", min_value=0.0, max_value=20.0, value=5.0)
    no2 = st.slider("no2(µg/m³)", min_value=0, max_value=1000, value=100)
    nox = st.slider("nox (°C)", min_value=-30, max_value=50, value=25)
    nh3 = st.slider("nh3 (%)", min_value=0, max_value=100, value=50)
    co = st.slider("co (m/s)", min_value=0.0, max_value=20.0, value=5.0)
    so2 = st.slider("so2 (µg/m³)", min_value=0, max_value=1000, value=100)
    o3 = st.slider("o3(µg/m³)", min_value=0, max_value=1000, value=100)
    benzene = st.slider("benzene (µg/m³)", min_value=0, max_value=1000, value=100)
    toluene = st.slider("toluene (µg/m³)", min_value=0, max_value=1000, value=100)
    xylene = st.slider("xylene (µg/m³)", min_value=0, max_value=1000, value=100)

    # Predict button
    if st.button("Predict AQI"):
        aqi = predict_aqi(pm25,pm10,no,no2,nox,nh3,co,so2,o3,benzene,toluene,xylene)
        st.success(f"The predicted AQI is: {aqi}")

if __name__ == "__main__":
    main()
