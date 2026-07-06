"""
Interactive Car Price Predictor demo app.
Run locally with:  streamlit run app.py
This is the screen you'll want to screen-record for your LinkedIn video.
"""
import pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_data
def load_data():
    return pd.read_csv("Cleaned_Car_data.csv")

model = load_model()
car = load_data()

st.title("🚗 Car Price Predictor")
st.write("Predict the resale price of a used car using a model trained on real Quikr listings.")

companies = sorted(car['company'].unique())
company = st.selectbox("Company", companies)

names = sorted(car[car['company'] == company]['name'].unique())
name = st.selectbox("Model", names)

year = st.slider("Year of purchase", int(car['year'].min()), 2026, 2018)
kms_driven = st.number_input("Kilometers driven", min_value=0, max_value=500000, value=30000, step=1000)
fuel_type = st.selectbox("Fuel type", sorted(car['fuel_type'].unique()))

if st.button("Predict Price"):
    input_df = pd.DataFrame(
        [[name, company, year, kms_driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Price: ₹ {prediction:,.0f}")

st.caption("Model: Random Forest Regression | Data: Quikr used-car listings (~800 rows, scraped & cleaned)")
