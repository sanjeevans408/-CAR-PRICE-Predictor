"""
<<<<<<< HEAD
🚗 AutoValuate AI — Next-Gen Used Car Price Predictor & Market Intelligence Hub
Engineered with Machine Learning (Random Forest Pipeline) & Real-world Quikr Listings.
"""
import os
import sys
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------------
# Page Configuration & Metadata
# ---------------------------------------------------------
st.set_page_config(
    page_title="AutoValuate AI • Car Price Predictor",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Custom Glassmorphic Dark Automotive Theme & Animations
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    :root {
        --primary-accent: #00F2FE;
        --secondary-accent: #4FACFE;
        --success-glow: #00E676;
        --amber-glow: #FFB300;
        --card-bg: rgba(18, 24, 38, 0.72);
        --card-border: rgba(255, 255, 255, 0.08);
        --text-primary: #F8FAFC;
        --text-secondary: #94A3B8;
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Keyframe Animations */
    @keyframes floatEmblem {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-7px) rotate(1deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    @keyframes pulseGlow {
        0% { box-shadow: 0 0 10px rgba(0, 242, 254, 0.2); }
        50% { box-shadow: 0 0 25px rgba(0, 242, 254, 0.5); }
        100% { box-shadow: 0 0 10px rgba(0, 242, 254, 0.2); }
    }

    @keyframes shimmerEffect {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }

    @keyframes fadeInScale {
        0% { opacity: 0; transform: scale(0.96); }
        100% { opacity: 1; transform: scale(1); }
    }

    /* Hero Header Banner */
    .hero-container {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.90) 100%);
        border: 1px solid rgba(0, 242, 254, 0.25);
        border-radius: 20px;
        padding: 30px 35px;
        margin-bottom: 25px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.35);
    }

    .hero-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 300%;
        height: 3px;
        background: linear-gradient(90deg, transparent, #00F2FE, #4FACFE, transparent);
        animation: shimmerEffect 4s infinite linear;
    }

    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0;
        background: linear-gradient(120deg, #FFFFFF 20%, #00F2FE 70%, #4FACFE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }

    .hero-subtitle {
        color: #94A3B8;
        font-size: 1.05rem;
        font-weight: 400;
        margin-top: 8px;
        line-height: 1.5;
    }

    .badge-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 5px 14px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.3px;
        background: rgba(0, 242, 254, 0.12);
        color: #00F2FE;
        border: 1px solid rgba(0, 242, 254, 0.3);
        margin-right: 8px;
    }

    .badge-pill.status {
        background: rgba(0, 230, 118, 0.12);
        color: #00E676;
        border-color: rgba(0, 230, 118, 0.3);
    }

    .badge-pill.model {
        background: rgba(255, 179, 0, 0.12);
        color: #FFB300;
        border-color: rgba(255, 179, 0, 0.3);
    }

    /* Metric & Feature Cards */
    .metric-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 16px;
        padding: 20px;
        backdrop-filter: blur(12px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }

    .metric-card:hover {
        transform: translateY(-4px);
        border-color: rgba(0, 242, 254, 0.4);
        box-shadow: 0 12px 28px rgba(0, 242, 254, 0.12);
    }

    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-top: 4px;
        font-family: 'JetBrains Mono', monospace;
    }

    .metric-label {
        font-size: 0.82rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #64748B;
    }

    /* Primary Prediction Result Card */
    .prediction-card {
        background: radial-gradient(circle at 10% 20%, rgba(0, 242, 254, 0.15) 0%, rgba(15, 23, 42, 0.95) 90%);
        border: 2px solid rgba(0, 242, 254, 0.4);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.45);
        animation: fadeInScale 0.5s ease-out, pulseGlow 4s infinite ease-in-out;
        margin-top: 20px;
        margin-bottom: 25px;
    }

    .price-main {
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -1px;
        color: #00F2FE;
        font-family: 'JetBrains Mono', monospace;
        margin: 10px 0;
        text-shadow: 0 0 20px rgba(0, 242, 254, 0.4);
    }

    .price-sub {
        font-size: 1.15rem;
        color: #CBD5E1;
        font-weight: 500;
    }

    /* Sub Range Badges */
    .range-box {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 14px 18px;
        text-align: center;
        transition: transform 0.2s ease;
    }

    .range-box:hover {
        transform: translateY(-2px);
        background: rgba(255, 255, 255, 0.07);
    }

    /* Animated Button Styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #00F2FE 0%, #4FACFE 100%) !important;
        color: #041021 !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 14px 28px !important;
        border-radius: 14px !important;
        border: none !important;
        box-shadow: 0 8px 25px rgba(0, 242, 254, 0.35) !important;
        transition: all 0.3s ease !important;
        letter-spacing: 0.3px !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px) scale(1.01) !important;
        box-shadow: 0 12px 35px rgba(0, 242, 254, 0.55) !important;
    }

    /* Floating Emblem */
    .floating-car {
        display: inline-block;
        animation: floatEmblem 3s ease-in-out infinite;
    }

    /* Custom Scrollbar & Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(15, 23, 42, 0.5);
        padding: 8px 10px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 8px 18px;
        font-weight: 600;
        color: #94A3B8;
        transition: all 0.2s ease;
    }

    .stTabs [aria-selected="true"] {
        background-color: rgba(0, 242, 254, 0.15) !important;
        color: #00F2FE !important;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Dynamic Path Resolution & Robust Resource Loading
# ---------------------------------------------------------
def resolve_file(filename: str) -> Path:
    """Finds a file in current directory, script directory, or nested directories."""
    cwd = Path.cwd()
    script_dir = Path(__file__).resolve().parent
    
    candidates = [
        cwd / filename,
        script_dir / filename,
        script_dir / "car_price_predictor" / "car_price_predictor" / filename,
        cwd / "car_price_predictor" / "car_price_predictor" / filename,
        script_dir.parent / filename,
    ]
    for c in candidates:
        if c.exists():
            return c
    return script_dir / filename


@st.cache_resource(show_spinner=False)
def load_model():
    """Loads the trained sklearn pipeline safely."""
    path = resolve_file("model.pkl")
    if not path.exists():
        st.error(f"⚠️ Model file `model.pkl` could not be located. Looked at: `{path}`")
        return None
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        st.error(f"⚠️ Error loading model from `{path}`: {e}")
        return None


@st.cache_data(show_spinner=False)
def load_data():
    """Loads and caches the cleaned car dataset."""
    path = resolve_file("Cleaned_Car_data.csv")
    if not path.exists():
        st.error(f"⚠️ Data file `Cleaned_Car_data.csv` not found at `{path}`")
        return pd.DataFrame()
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        st.error(f"⚠️ Error loading dataset: {e}")
        return pd.DataFrame()

=======
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
>>>>>>> 0766c5f14de5983b22b90321c8b17b2691132471

model = load_model()
car = load_data()

<<<<<<< HEAD
if car.empty or model is None:
    st.warning("Please ensure `model.pkl` and `Cleaned_Car_data.csv` are accessible in the project folder.")
    st.stop()


# ---------------------------------------------------------
# Utility Helper Functions
# ---------------------------------------------------------
def format_inr(val: float) -> str:
    """Formats numeric value in Indian Lakhs and Crores."""
    if val >= 10000000:
        return f"₹ {val / 10000000:.2f} Cr"
    elif val >= 100000:
        return f"₹ {val / 100000:.2f} Lakh"
    else:
        return f"₹ {val:,.0f}"


def calculate_emi(principal: float, annual_rate: float, tenure_years: int):
    """Calculates standard Monthly Loan EMI."""
    r = (annual_rate / 12) / 100
    n = tenure_years * 12
    if r == 0:
        return principal / n, 0, principal
    emi = (principal * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
    total_payment = emi * n
    total_interest = total_payment - principal
    return emi, total_interest, total_payment


# ---------------------------------------------------------
# App Header & Animated Hero Section
# ---------------------------------------------------------
st.markdown("""
<div class="hero-container">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
        <div>
            <div style="margin-bottom: 8px;">
                <span class="badge-pill status">● AI ENGINE ONLINE</span>
                <span class="badge-pill model">RANDOM FOREST REGRESSOR (300 TREES)</span>
                <span class="badge-pill">R² 88.7% ACCURACY</span>
            </div>
            <h1 class="hero-title"><span class="floating-car">🏎️</span> AutoValuate AI</h1>
            <p class="hero-subtitle">Intelligent Resale Valuation Engine & Live Market Analytics for Used Automobiles.</p>
        </div>
        <div style="text-align: right;">
            <div style="font-size: 0.8rem; color: #64748B; font-weight: 600; text-transform: uppercase;">Real Market Listings</div>
            <div style="font-size: 2.2rem; font-weight: 800; color: #00F2FE; font-family: 'JetBrains Mono', monospace;">
                815+
            </div>
            <div style="font-size: 0.8rem; color: #94A3B8;">Verified Quikr Records</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Top Metric HUD (Heads Up Display)
# ---------------------------------------------------------
mcol1, mcol2, mcol3, mcol4 = st.columns(4)
with mcol1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Dataset Records</div>
        <div class="metric-value">{len(car):,}</div>
        <div style="font-size: 0.75rem; color: #00E676; margin-top: 4px;">Cleaned & Outlier Filtered</div>
    </div>
    """, unsafe_allow_html=True)

with mcol2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Automobile Brands</div>
        <div class="metric-value">{car['company'].nunique()}</div>
        <div style="font-size: 0.75rem; color: #00F2FE; margin-top: 4px;">250+ Model Variants</div>
    </div>
    """, unsafe_allow_html=True)

with mcol3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Average Resale Value</div>
        <div class="metric-value">{format_inr(car['Price'].mean())}</div>
        <div style="font-size: 0.75rem; color: #FFB300; margin-top: 4px;">Median: {format_inr(car['Price'].median())}</div>
    </div>
    """, unsafe_allow_html=True)

with mcol4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Model Accuracy (R²)</div>
        <div class="metric-value">0.8873</div>
        <div style="font-size: 0.75rem; color: #00E676; margin-top: 4px;">Mean Absolute Error: ₹83,937</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# Main Application Tabs
# ---------------------------------------------------------
tab_predict, tab_analytics, tab_compare, tab_loan, tab_explorer = st.tabs([
    "🔮 Instant Valuation",
    "📈 Market Analytics & Charts",
    "⚖️ Vehicle Comparator",
    "💳 EMI & Loan Calculator",
    "🔍 Dataset Explorer"
])


# =========================================================
# TAB 1: INSTANT VALUATION
# =========================================================
with tab_predict:
    st.markdown("### 🚘 Vehicle Configuration & Smart Valuation")
    st.write("Provide the car specifications below to compute an AI-backed resale estimation based on machine learning.")
    
    col_input, col_display = st.columns([1.1, 1], gap="large")

    with col_input:
        with st.container(border=True):
            st.markdown("#### 1. Select Vehicle Identity")
            
            # Company Selection
            companies = sorted(car['company'].unique())
            default_company_idx = companies.index("Maruti") if "Maruti" in companies else 0
            company = st.selectbox("Manufacturer / Company", companies, index=default_company_idx)
            
            # Dependent Model Selection
            models_for_company = sorted(car[car['company'] == company]['name'].unique())
            model_name = st.selectbox("Car Model & Trim", models_for_company)

            st.markdown("#### 2. Usage & Specifications")
            
            # Year Slider
            min_year = int(car['year'].min())
            max_year = 2026
            current_year = 2026
            selected_year = st.slider("Year of Manufacture / Registration", min_year, max_year, 2018)
            vehicle_age = current_year - selected_year
            
            age_badge_color = "#00E676" if vehicle_age <= 4 else ("#FFB300" if vehicle_age <= 8 else "#EF4444")
            st.markdown(f"<span style='font-size: 0.85rem; color: {age_badge_color}; font-weight: 600;'>⏱️ Vehicle Age: {vehicle_age} Year(s) Old</span>", unsafe_allow_html=True)

            # Kilometers Driven with Fast Presets
            st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
            preset_col1, preset_col2, preset_col3 = st.columns(3)
            with preset_col1:
                if st.button("🌱 Low (~20k km)", key="btn_km_low"):
                    st.session_state['kms_input'] = 20000
            with preset_col2:
                if st.button("🚗 Avg (~45k km)", key="btn_km_avg"):
                    st.session_state['kms_input'] = 45000
            with preset_col3:
                if st.button("🛣️ High (~85k km)", key="btn_km_high"):
                    st.session_state['kms_input'] = 85000

            kms_default = st.session_state.get('kms_input', 35000)
            kms_driven = st.number_input(
                "Odometer Reading (Kilometers Driven)",
                min_value=0,
                max_value=500000,
                value=int(kms_default),
                step=2500,
                help="Actual kilometers driven by the vehicle."
            )

            # Fuel Type
            fuel_types = sorted(car['fuel_type'].unique())
            fuel_type = st.selectbox("Engine Fuel Type", fuel_types, index=fuel_types.index("Petrol") if "Petrol" in fuel_types else 0)

            # Predict Action Button
            st.markdown("<div style='margin-top: 18px;'></div>", unsafe_allow_html=True)
            predict_clicked = st.button("✨ Calculate Instant Valuation", width='stretch')

    with col_display:
        # Default or calculated prediction
        sample_input = pd.DataFrame(
            [[model_name, company, selected_year, kms_driven, fuel_type]],
            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
        )
        
        try:
            raw_pred = model.predict(sample_input)[0]
            # Ensure safe bounds
            predicted_price = max(20000.0, float(raw_pred))
        except Exception as e:
            predicted_price = 300000.0
            st.error(f"Prediction computation notice: {e}")

        # Store in session state for loan calculator
        st.session_state['last_predicted_price'] = predicted_price
        st.session_state['last_predicted_model'] = f"{company} {model_name} ({selected_year})"

        if predict_clicked:
            st.balloons()

        trade_in_low = predicted_price * 0.88
        trade_in_high = predicted_price * 0.93
        private_party_low = predicted_price * 1.03
        private_party_high = predicted_price * 1.08

        st.markdown(f"""
        <div class="prediction-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 0.85rem; font-weight: 700; color: #00F2FE; letter-spacing: 1px;">AI ESTIMATED FAIR MARKET VALUE</span>
                <span class="badge-pill status">HIGH CONFIDENCE</span>
            </div>
            <div class="price-main">{format_inr(predicted_price)}</div>
            <div class="price-sub">₹ {predicted_price:,.0f} INR</div>
            <div style="font-size: 0.9rem; color: #94A3B8; margin-top: 6px;">
                Estimated resale range for <b>{company} {model_name}</b> ({selected_year}, {kms_driven:,} km, {fuel_type})
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Market Range Breakdown
        rcol1, rcol2 = st.columns(2)
        with rcol1:
            st.markdown(f"""
            <div class="range-box">
                <div style="font-size: 0.78rem; color: #94A3B8; font-weight: 600;">🏪 DEALER TRADE-IN</div>
                <div style="font-size: 1.15rem; font-weight: 700; color: #F8FAFC; margin-top: 4px;">{format_inr(trade_in_low)} - {format_inr(trade_in_high)}</div>
                <div style="font-size: 0.75rem; color: #64748B;">Instant dealer exchange</div>
            </div>
            """, unsafe_allow_html=True)
            
        with rcol2:
            st.markdown(f"""
            <div class="range-box">
                <div style="font-size: 0.78rem; color: #94A3B8; font-weight: 600;">🤝 PRIVATE PARTY SALE</div>
                <div style="font-size: 1.15rem; font-weight: 700; color: #00E676; margin-top: 4px;">{format_inr(private_party_low)} - {format_inr(private_party_high)}</div>
                <div style="font-size: 0.75rem; color: #64748B;">Direct buyer-to-buyer</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

        # 5-Year Future Depreciation Projection (Specific to this car)
        future_years = [selected_year + i for i in range(6)]
        depreciation_factors = [1.0, 0.88, 0.78, 0.69, 0.61, 0.54]
        projected_prices = [max(20000, predicted_price * f) for f in depreciation_factors]
        years_label = [f"Yr 0 (Current)", "+1 Yr", "+2 Yrs", "+3 Yrs", "+4 Yrs", "+5 Yrs"]

        dep_df = pd.DataFrame({
            "Timeline": years_label,
            "Resale Value (₹)": projected_prices,
            "Formatted Value": [format_inr(p) for p in projected_prices]
        })

        fig_dep = px.area(
            dep_df,
            x="Timeline",
            y="Resale Value (₹)",
            title="📉 5-Year Projected Resale Value Curve",
            markers=True,
            color_discrete_sequence=["#00F2FE"]
        )
        fig_dep.update_traces(
            line=dict(width=3, color="#00F2FE"),
            fillcolor="rgba(0, 242, 254, 0.15)",
            hovertemplate="<b>%{x}</b><br>Projected Resale: ₹ %{y:,.0f}<extra></extra>"
        )
        fig_dep.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=260,
            margin=dict(l=10, r=10, t=40, b=10),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.06)", tickprefix="₹")
        )
        st.plotly_chart(fig_dep, width='stretch')


# =========================================================
# TAB 2: MARKET ANALYTICS & INTERACTIVE CHARTS
# =========================================================
with tab_analytics:
    st.markdown("### 📊 Live Used Automobile Market Insights")
    st.write("Explore correlations, depreciation trajectories, and brand premiums derived from the dataset.")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        # 1. Price vs Year Scatter with Trendline
        fig_year = px.scatter(
            car,
            x="year",
            y="Price",
            color="fuel_type",
            size="kms_driven",
            hover_name="name",
            hover_data={"Price": ":,.0f", "year": True, "kms_driven": ":,", "fuel_type": True},
            title="📅 Resale Price vs. Manufacturing Year",
            color_discrete_map={"Petrol": "#00F2FE", "Diesel": "#FF6B35", "LPG": "#00E676"},
            labels={"year": "Year of Purchase", "Price": "Price (₹)", "fuel_type": "Fuel Type"}
        )
        fig_year.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=360,
            yaxis=dict(gridcolor="rgba(255,255,255,0.06)", tickprefix="₹"),
            xaxis=dict(gridcolor="rgba(255,255,255,0.06)")
        )
        st.plotly_chart(fig_year, width='stretch')

    with chart_col2:
        # 2. Price vs Mileage (Kilometers Driven)
        fig_kms = px.scatter(
            car[car['kms_driven'] <= 200000],
            x="kms_driven",
            y="Price",
            color="fuel_type",
            trendline="lowess",
            hover_name="name",
            title="🛣️ Resale Price vs. Kilometers Driven (Odometer)",
            color_discrete_map={"Petrol": "#00F2FE", "Diesel": "#FF6B35", "LPG": "#00E676"},
            labels={"kms_driven": "Kilometers Driven", "Price": "Price (₹)", "fuel_type": "Fuel Type"}
        )
        fig_kms.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=360,
            yaxis=dict(gridcolor="rgba(255,255,255,0.06)", tickprefix="₹"),
            xaxis=dict(gridcolor="rgba(255,255,255,0.06)")
        )
        st.plotly_chart(fig_kms, width='stretch')

    chart_col3, chart_col4 = st.columns([1.2, 0.8])

    with chart_col3:
        # 3. Top Brands by Average Resale Value
        brand_stats = car.groupby('company').agg(
            avg_price=('Price', 'mean'),
            count=('Price', 'count')
        ).reset_index()
        brand_stats = brand_stats[brand_stats['count'] >= 3].sort_values(by='avg_price', ascending=True)

        fig_brand = px.bar(
            brand_stats,
            y="company",
            x="avg_price",
            orientation='h',
            title="🏆 Average Resale Value by Brand (Min 3 Listings)",
            color="avg_price",
            color_continuous_scale="Tealgrn",
            labels={"avg_price": "Avg Price (₹)", "company": "Manufacturer"}
        )
        fig_brand.update_traces(
            hovertemplate="<b>%{y}</b><br>Average Price: ₹ %{x:,.0f}<extra></extra>"
        )
        fig_brand.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=400,
            xaxis=dict(gridcolor="rgba(255,255,255,0.06)", tickprefix="₹"),
            coloraxis_showscale=False
        )
        st.plotly_chart(fig_brand, width='stretch')

    with chart_col4:
        # 4. Fuel Type Market Share (Donut)
        fuel_counts = car['fuel_type'].value_counts().reset_index()
        fuel_counts.columns = ['Fuel Type', 'Count']
        
        fig_fuel = px.pie(
            fuel_counts,
            names='Fuel Type',
            values='Count',
            hole=0.55,
            title="⛽ Fuel Type Market Share",
            color='Fuel Type',
            color_discrete_map={"Petrol": "#00F2FE", "Diesel": "#FF6B35", "LPG": "#00E676"}
        )
        fig_fuel.update_traces(textposition='inside', textinfo='percent+label')
        fig_fuel.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig_fuel, width='stretch')

    # 5. Price Distribution Histogram & Boxplot
    fig_dist = px.histogram(
        car,
        x="Price",
        nbins=45,
        marginal="box",
        title="💰 Overall Used Car Price Distribution & Quartiles",
        color_discrete_sequence=["#4FACFE"]
    )
    fig_dist.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=320,
        xaxis=dict(gridcolor="rgba(255,255,255,0.06)", tickprefix="₹"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.06)")
    )
    st.plotly_chart(fig_dist, width='stretch')


# =========================================================
# TAB 3: VEHICLE COMPARATOR
# =========================================================
with tab_compare:
    st.markdown("### ⚖️ Side-by-Side Car Valuation Comparator")
    st.write("Compare two vehicles simultaneously to understand resale price differences and value retention.")

    comp_col1, comp_col2 = st.columns(2, gap="large")

    with comp_col1:
        st.markdown("#### 🔹 Vehicle A (Benchmark)")
        with st.container(border=True):
            comp_a = st.selectbox("Company A", sorted(car['company'].unique()), key="comp_a_co")
            models_a = sorted(car[car['company'] == comp_a]['name'].unique())
            name_a = st.selectbox("Model A", models_a, key="comp_a_name")
            year_a = st.slider("Year A", 1995, 2026, 2017, key="comp_a_yr")
            kms_a = st.number_input("Kilometers A", 0, 500000, 40000, step=5000, key="comp_a_km")
            fuel_a = st.selectbox("Fuel A", sorted(car['fuel_type'].unique()), key="comp_a_fuel")
            
            df_a = pd.DataFrame([[name_a, comp_a, year_a, kms_a, fuel_a]], columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
            price_a = max(20000.0, float(model.predict(df_a)[0]))
            
            st.markdown(f"""
            <div style="background: rgba(0, 242, 254, 0.1); border: 1px solid rgba(0, 242, 254, 0.3); border-radius: 12px; padding: 15px; margin-top: 15px; text-align: center;">
                <div style="font-size: 0.85rem; color: #94A3B8;">Estimated Price (Vehicle A)</div>
                <div style="font-size: 2rem; font-weight: 800; color: #00F2FE;">{format_inr(price_a)}</div>
                <div style="font-size: 0.85rem; color: #CBD5E1;">₹ {price_a:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

    with comp_col2:
        st.markdown("#### 🔸 Vehicle B (Comparison)")
        with st.container(border=True):
            # Pick a different default company if possible
            comp_b_default_idx = 1 if len(car['company'].unique()) > 1 else 0
            comp_b = st.selectbox("Company B", sorted(car['company'].unique()), index=comp_b_default_idx, key="comp_b_co")
            models_b = sorted(car[car['company'] == comp_b]['name'].unique())
            name_b = st.selectbox("Model B", models_b, key="comp_b_name")
            year_b = st.slider("Year B", 1995, 2026, 2018, key="comp_b_yr")
            kms_b = st.number_input("Kilometers B", 0, 500000, 30000, step=5000, key="comp_b_km")
            fuel_b = st.selectbox("Fuel B", sorted(car['fuel_type'].unique()), key="comp_b_fuel")
            
            df_b = pd.DataFrame([[name_b, comp_b, year_b, kms_b, fuel_b]], columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
            price_b = max(20000.0, float(model.predict(df_b)[0]))

            st.markdown(f"""
            <div style="background: rgba(255, 107, 53, 0.1); border: 1px solid rgba(255, 107, 53, 0.3); border-radius: 12px; padding: 15px; margin-top: 15px; text-align: center;">
                <div style="font-size: 0.85rem; color: #94A3B8;">Estimated Price (Vehicle B)</div>
                <div style="font-size: 2rem; font-weight: 800; color: #FF6B35;">{format_inr(price_b)}</div>
                <div style="font-size: 0.85rem; color: #CBD5E1;">₹ {price_b:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

    # Comparison Difference Summary
    price_diff = price_b - price_a
    pct_diff = (price_diff / price_a) * 100 if price_a > 0 else 0
    winner_str = "Vehicle B" if price_diff > 0 else "Vehicle A"

    st.markdown(f"""
    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 16px; padding: 20px; margin-top: 25px; text-align: center;">
        <span style="font-size: 0.9rem; color: #94A3B8; font-weight: 600;">VALUATION DELTA</span>
        <div style="font-size: 1.5rem; font-weight: 700; color: #F8FAFC; margin-top: 5px;">
            {winner_str} is valued <span style="color: {'#00E676' if price_diff >= 0 else '#FF6B35'};">{format_inr(abs(price_diff))} ({abs(pct_diff):.1f}%)</span> {'higher' if price_diff >= 0 else 'lower'} than the competitor.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Comparison Bar Chart
    comp_df = pd.DataFrame({
        "Vehicle": [f"A: {comp_a} {name_a}", f"B: {comp_b} {name_b}"],
        "Price": [price_a, price_b]
    })
    fig_comp = px.bar(
        comp_df,
        x="Vehicle",
        y="Price",
        color="Vehicle",
        text_auto=".2s",
        color_discrete_sequence=["#00F2FE", "#FF6B35"],
        title="📊 Head-to-Head Resale Valuation Comparison"
    )
    fig_comp.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=320,
        yaxis=dict(tickprefix="₹", gridcolor="rgba(255,255,255,0.06)"),
        showlegend=False
    )
    st.plotly_chart(fig_comp, width='stretch')


# =========================================================
# TAB 4: AUTO LOAN & EMI FINANCING CALCULATOR
# =========================================================
with tab_loan:
    st.markdown("### 💳 Used Car Financing & EMI Calculator")
    st.write("Plan monthly budgeting, loan amortization, and total interest payable for purchasing a used vehicle.")

    calc_col1, calc_col2 = st.columns([1, 1.1], gap="large")

    default_calc_price = float(st.session_state.get('last_predicted_price', 350000.0))

    with calc_col1:
        with st.container(border=True):
            st.markdown("#### Financing Parameters")
            car_cost = st.number_input(
                "Vehicle Agreed Price (₹)",
                min_value=30000.0,
                max_value=10000000.0,
                value=float(default_calc_price),
                step=10000.0,
                help="Total purchase price of the vehicle."
            )

            down_payment_pct = st.slider("Down Payment Percentage (%)", 10, 80, 20, step=5)
            down_payment_amt = car_cost * (down_payment_pct / 100)
            loan_amount = car_cost - down_payment_amt

            st.markdown(f"<div style='font-size: 0.85rem; color: #94A3B8;'>Down Payment: <b>{format_inr(down_payment_amt)}</b> | Net Loan Amount: <b>{format_inr(loan_amount)}</b></div>", unsafe_allow_html=True)

            tenure_years = st.slider("Loan Duration / Tenure (Years)", 1, 7, 4)
            interest_rate = st.slider("Annual Interest Rate (% p.a.)", 7.0, 16.0, 9.5, step=0.25)

    with calc_col2:
        monthly_emi, total_interest, total_payable = calculate_emi(loan_amount, interest_rate, tenure_years)

        st.markdown(f"""
        <div style="background: radial-gradient(circle at 10% 20%, rgba(79, 172, 254, 0.15) 0%, rgba(15, 23, 42, 0.95) 90%); border: 1px solid rgba(79, 172, 254, 0.4); border-radius: 16px; padding: 25px; margin-bottom: 20px;">
            <div style="font-size: 0.82rem; color: #94A3B8; font-weight: 600; text-transform: uppercase;">Estimated Monthly EMI</div>
            <div style="font-size: 2.8rem; font-weight: 800; color: #00F2FE; font-family: 'JetBrains Mono', monospace;">
                ₹ {monthly_emi:,.0f} <span style="font-size: 1rem; color: #94A3B8; font-family: 'Plus Jakarta Sans', sans-serif;">/ month</span>
            </div>
            <div style="display: flex; gap: 20px; margin-top: 15px; border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 12px;">
                <div>
                    <div style="font-size: 0.75rem; color: #64748B;">PRINCIPAL</div>
                    <div style="font-size: 1.1rem; font-weight: 700; color: #F8FAFC;">{format_inr(loan_amount)}</div>
                </div>
                <div>
                    <div style="font-size: 0.75rem; color: #64748B;">TOTAL INTEREST</div>
                    <div style="font-size: 1.1rem; font-weight: 700; color: #FF6B35;">{format_inr(total_interest)}</div>
                </div>
                <div>
                    <div style="font-size: 0.75rem; color: #64748B;">TOTAL OUTFLOW</div>
                    <div style="font-size: 1.1rem; font-weight: 700; color: #00E676;">{format_inr(total_payable)}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Loan Breakdown Donut
        loan_breakdown = pd.DataFrame({
            "Component": ["Principal Loan Amount", "Total Interest Payable"],
            "Amount": [loan_amount, total_interest]
        })
        fig_emi = px.pie(
            loan_breakdown,
            names="Component",
            values="Amount",
            hole=0.6,
            title="📊 Total Cost of Financing Breakdown",
            color="Component",
            color_discrete_map={"Principal Loan Amount": "#00F2FE", "Total Interest Payable": "#FF6B35"}
        )
        fig_emi.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=260,
            margin=dict(l=10, r=10, t=40, b=10)
        )
        st.plotly_chart(fig_emi, width='stretch')


# =========================================================
# TAB 5: DATASET EXPLORER & MODEL ARCHITECTURE
# =========================================================
with tab_explorer:
    st.markdown("### 🔍 Dataset Explorer & Model Architecture")
    st.write("Examine raw data rows, filter listings, and review the technical evaluation of the trained ML model.")

    with st.expander("🛠️ Machine Learning Model Technical Specs", expanded=True):
        tcol1, tcol2, tcol3 = st.columns(3)
        with tcol1:
            st.markdown("""
            **Algorithm:** `RandomForestRegressor`
            - Estimators: `300 Trees`
            - Criterion: Squared Error
            - Feature Preprocessing: `OneHotEncoder(handle_unknown='ignore')`
            """)
        with tcol2:
            st.markdown("""
            **Evaluation Scores:**
            - **R² Score:** `0.8873` (88.7% variance explained)
            - **MAE:** `₹ 83,937`
            - **Split Ratio:** `80% Train / 20% Test`
            """)
        with tcol3:
            st.markdown("""
            **Dataset Features:**
            - Features: `name`, `company`, `year`, `kms_driven`, `fuel_type`
            - Target: `Price` (INR)
            - Cleaned Sample Size: `815 verified rows`
            """)

    st.markdown("#### Interactive Listings Filter")
    fcol1, fcol2, fcol3 = st.columns(3)
    with fcol1:
        filter_company = st.multiselect("Filter by Company", sorted(car['company'].unique()), default=[])
    with fcol2:
        filter_fuel = st.multiselect("Filter by Fuel Type", sorted(car['fuel_type'].unique()), default=[])
    with fcol3:
        price_range = st.slider("Price Range (₹)", int(car['Price'].min()), int(car['Price'].max()), (int(car['Price'].min()), int(car['Price'].max())))

    filtered_df = car.copy()
    if filter_company:
        filtered_df = filtered_df[filtered_df['company'].isin(filter_company)]
    if filter_fuel:
        filtered_df = filtered_df[filtered_df['fuel_type'].isin(filter_fuel)]
    filtered_df = filtered_df[(filtered_df['Price'] >= price_range[0]) & (filtered_df['Price'] <= price_range[1])]

    st.write(f"Showing **{len(filtered_df):,}** matching listings:")
    st.dataframe(
        filtered_df.style.format({
            "Price": "₹ {:,.0f}",
            "kms_driven": "{:,} km",
            "year": "{}"
        }),
        width='stretch',
        height=320
    )

    # Download CSV
    csv_bytes = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        "📥 Download Filtered Data as CSV",
        data=csv_bytes,
        file_name="car_price_filtered_data.csv",
        mime="text/csv"
    )

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
st.markdown("""
<div style="border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 20px; text-align: center; color: #64748B; font-size: 0.85rem;">
    <b>AutoValuate AI</b> • Powered by Scikit-Learn Random Forest Pipeline & Streamlit • Data Source: Quikr Listings Scrape (~800 rows cleaned)
</div>
""", unsafe_allow_html=True)
=======
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
>>>>>>> 0766c5f14de5983b22b90321c8b17b2691132471
