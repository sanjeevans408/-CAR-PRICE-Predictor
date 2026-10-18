# 🏎️ AutoValuate AI — Next-Gen Used Car Price Predictor & Market Intelligence Hub

An end-to-end Machine Learning web application that predicts used car resale values and provides deep market analytics. Powered by a **Random Forest Regressor Pipeline** trained on real scraped listings from Quikr, wrapped in a **luxurious glassmorphic automotive interface** built with Streamlit and Plotly.

---

## ✨ Features & Highlights

### 1. 🔮 Smart Instant Valuation
- **Dynamic Dependent Dropdowns:** Select brand (e.g. Maruti, Hyundai, BMW, Audi) to immediately see matching car trims.
- **Interactive Year Slider & Age Badge:** Automatic calculation of vehicle age with visual status badges.
- **Odometer Quick-Presets:** One-click presets for Low (~20k km), Average (~45k km), and High (~85k km) mileage.
- **Tri-Tier Valuation:**
  - 🏪 **Dealer Trade-In Range** (Instant exchange estimate)
  - 🏷️ **Fair Market Retail Value** (Primary ML estimation in Lakhs & INR)
  - 🤝 **Private Party Sale Range** (Peer-to-peer transaction estimate)
- **5-Year Future Depreciation Curve:** Interactive Plotly area chart visualizing expected vehicle value decay over the next 5 years.

### 2. 📈 Interactive Market Analytics & Visualizations
- **Price vs. Manufacturing Year:** Scatter plot with interactive hover cards and fuel type breakdown.
- **Price vs. Kilometers Driven:** Mileage sensitivity analysis with trendline.
- **Brand Value Rankings:** Horizontal ranked bar chart comparing average resale prices across 25+ manufacturers.
- **Fuel Type Market Share & Spread:** Interactive donut chart and comparative distribution.
- **Quartile & Price Distribution:** Interactive histogram with integrated box plot.

### 3. ⚖️ Side-by-Side Vehicle Comparator
- Compare two cars (e.g. Honda City Petrol vs Hyundai Verna Diesel) with independent parameters.
- Instant valuation delta calculation showing exact price difference and percentage spread.
- Head-to-head comparison bar chart.

### 4. 💳 Auto Loan & Monthly EMI Calculator
- Live monthly EMI calculation based on vehicle purchase price.
- Sliders for Down Payment %, Loan Duration (1-7 years), and Annual Interest Rate.
- Financial cost breakdown donut chart (Principal vs. Total Interest Payable).

### 5. 🔍 Dataset Explorer & Model Architecture
- Interactive, searchable dataset viewer with multi-select filters for manufacturer and fuel type.
- Filtered data export to CSV with one click.
- Full technical specifications and evaluation metrics ($R^2$, MAE, estimator depth).

---

## 🎨 UI/UX & Design Enhancements

- **Glassmorphic Automotive Aesthetic:** Sleek dark-mode palette (`#0B0F19`, `#1E293B`) with frosted glass panels, glowing borders, and modern typography (`Plus Jakarta Sans` & `JetBrains Mono`).
- **CSS Keyframe Animations:**
  - `@keyframes floatEmblem`: Floating vehicle badges for dynamic flair.
  - `@keyframes pulseGlow`: Glowing ambient effects for high-confidence predictions.
  - `@keyframes shimmerEffect`: Light streak across the hero header.
  - Smooth hover lifts (`transform: translateY(-4px)`) on cards and interactive elements.
- **Responsive Layout:** Works smoothly on desktop and mobile screens.

---

## 📊 Machine Learning Model Benchmarks

Trained on 815 cleaned real-world car listings using an 80/20 train-test split:

| Metric | Random Forest (Selected) | Linear Regression |
|---|---|---|
| **$R^2$ Score** | **0.8873 (88.7%)** | 0.8189 (81.9%) |
| **Mean Absolute Error (MAE)** | **₹ 83,937** | ₹ 117,650 |
| **Estimators** | 300 Trees | N/A |
| **Preprocessing** | One-Hot Encoding (`handle_unknown='ignore'`) | One-Hot Encoding |

---

## 🚀 Quick Start Guide

### 1. Activate Environment
```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 3. Run the Web Application
```powershell
streamlit run app.py
```
Open `http://localhost:8501` in your browser.

---

## 📁 Project Architecture

```
car_price_predict/
├── app.py                     # Modernized Streamlit web application
├── model.pkl                  # Trained Random Forest pipeline
├── Cleaned_Car_data.csv       # Cleaned dataset (815 rows)
├── quikr_car.csv              # Raw scraped listings
├── clean_data.py              # Data preprocessing and cleaning pipeline
├── train_model.py             # Model training, split evaluation, and serialization
├── requirements.txt           # Python dependency specifications
├── Car_Price_Predictor.ipynb  # Interactive Jupyter notebook for EDA & experimentation
└── car_price_predictor/       # Modular package mirror
    └── car_price_predictor/
        ├── app.py
        ├── model.pkl
        ├── Cleaned_Car_data.csv
        └── plots/
```

---

## 🛠️ Tech Stack
- **Frontend / UI:** Streamlit 1.66 · Custom CSS3 (Glassmorphism & Keyframe Animations)
- **Visualizations:** Plotly Express & Plotly Graph Objects 7.1
- **Machine Learning:** Scikit-Learn 1.9 · NumPy · Pandas · Statsmodels
- **Environment:** Python 3.12 (Windows x64)
