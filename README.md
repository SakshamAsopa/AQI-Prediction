# AQI-Prediction
# Overview
This project focuses on developing a Deep Learning model to predict the Air Quality Index (AQI) using various environmental factors. By leveraging historical AQI data and related features, the model aims to provide accurate predictions that can help in monitoring and managing air quality.

# Features
Predict AQI based on environmental parameters such as temperature, humidity, wind speed, and pollutant levels.
Implement a deep learning model with various layers for enhanced prediction accuracy.
Visualize predictions against actual AQI values.
Technologies Used
Python
TensorFlow / Keras
Pandas
NumPy
Matplotlib
Jupyter Notebook

# Data
The dataset used for this project is sourced from https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india?select=city_day.csv. It contains information on:

Date and time
PM2.5, PM10, CO, CO2, NO, NO2, NOx, NH3, SO2, Ozone, Xylene and Benzene levels
Temperature
Humidity
Wind speed
AQI values

# Data Preprocessing
Handled missing values
Normalized features for better model performance
Split data into training, validation, and test sets
Averaged and merged data of diiferent dates into a single Column

# Model Architecture
The model architecture consists of:
Input Layer: Accepts the environmental feature inputs.

Hidden Layers: Multiple dense layers with activation functions (e.g., ReLU) for feature extraction.

Output Layer: A single neuron to predict the AQI value.

The model is compiled using Mean Squared Error (MSE) as the loss function and an optimizer like Adam.

# Results
The model was evaluated using metrics such as Mean Absolute Error (MAE) and R² score. A comparative analysis of predicted vs. actual AQI values is included in the Jupyter Notebook, along with visualizations.

# Contributing
Contributions are welcome! Please fork the repository and submit a pull request.
