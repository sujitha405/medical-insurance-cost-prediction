import streamlit as st
import numpy as np
import joblib

model = joblib.load("insurance_model.pkl")

st.title("Medical Insurance Cost Prediction")

age = st.slider("Age",18,65)

sex = st.selectbox("Sex",["Male","Female"])

bmi = st.number_input("BMI",10.0,50.0)

children = st.slider("Children",0,5)

smoker = st.selectbox("Smoker",["Yes","No"])

region = st.selectbox("Region",["southwest","southeast","northwest","northeast"])

sex = 1 if sex=="Male" else 0
smoker = 1 if smoker=="Yes" else 0

region_dict={
"southwest":0,
"southeast":1,
"northwest":2,
"northeast":3
}

region=region_dict[region]

if st.button("Predict Insurance Cost"):
    data=np.array([[age,sex,bmi,children,smoker,region]])
    prediction=model.predict(data)
    st.success(f"Estimated Insurance Cost: ${prediction[0]:.2f}")
