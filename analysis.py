"""
Airbnb Open Data Analysis
Author: Priya Kumari
Internship ID: INTERNSHIP_172663295366ea53f910591
This script reproduces the EDA and plots created in the project folder.
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path

proj = Path(__file__).resolve().parent
images = proj / "images"
images.mkdir(exist_ok=True)

df = pd.read_excel(r"/mnt/data/1730285881-Airbnb_Open_Data.xlsx", sheet_name=0)

def clean_price(x):
    if pd.isna(x):
        return np.nan
    if isinstance(x, str):
        x = x.replace("$","").replace(",","").strip()
    try:
        return float(x)
    except:
        return np.nan

price_cols = [c for c in df.columns if 'price' in str(c).lower() or 'rent' in str(c).lower() or 'amount' in str(c).lower()]

for c in price_cols:
    df[c + "_clean"] = df[c].apply(clean_price)

# Example plot: price distribution
if price_cols:
    pc = price_cols[0] + "_clean"
    series = df[pc].dropna()
    if len(series) > 0:
        plt.figure(figsize=(8,5))
        plt.hist(series.clip(lower=0), bins=40)
        plt.title(f"Distribution of {price_cols[0]}")
        plt.xlabel("Price")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(images / "price_distribution.png")
        plt.close()
print("Done. Check the images folder for outputs.")
