# 🚗 Car Price Predictor — ML Project

Predicts the resale price of a used car based on its brand, model, year, kilometers driven, and fuel type — trained on real, scraped Quikr car listings.

## Project files
| File | Purpose |
|---|---|
| `quikr_car.csv` | Raw scraped dataset (~890 rows, messy) |
| `Car_Price_Predictor.ipynb` | Full walkthrough: cleaning → EDA → model training → evaluation |
| `clean_data.py` | Standalone cleaning script → `Cleaned_Car_data.csv` |
| `train_model.py` | Trains & compares Linear Regression vs Random Forest → `model.pkl` |
| `app.py` | Streamlit demo app for live predictions (use this for your video!) |
| `plots/` | Saved EDA charts |

## Results
| Model | R² Score | MAE |
|---|---|---|
| Linear Regression | 0.82 | ₹117,651 |
| **Random Forest (selected)** | **0.89** | **₹83,937** |

## How to run it yourself
```bash
pip install pandas scikit-learn matplotlib seaborn streamlit
python clean_data.py       # cleans quikr_car.csv -> Cleaned_Car_data.csv
python train_model.py      # trains models -> model.pkl
streamlit run app.py       # opens the interactive predictor in your browser
```

## Data cleaning highlights
The raw scrape had several real-world data quality problems, all handled in `clean_data.py`:
- `year` contained non-numeric junk values
- `Price` had `"Ask For Price"` entries and comma-formatted strings
- `kms_driven` had `" kms"` suffixes and a few corrupted rows
- `fuel_type` had missing values
- `name` was long, inconsistent free text — trimmed to the first 3 words (brand + model + variant)

## Tech stack
Python · pandas · scikit-learn (OneHotEncoder, Linear Regression, Random Forest) · matplotlib/seaborn · Streamlit
