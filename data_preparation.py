import pandas as pd
import numpy as np

# Load your raw housing dataset (Replace 'raw_housing_data.csv' with your actual file)
df = pd.read_csv('raw_housing_data.csv')

# --- Basic Cleaning ---
# Remove duplicates
df = df.drop_duplicates()

# Drop rows with missing critical values (e.g., sales price, bedrooms, bathrooms, year built)
df = df.dropna(subset=['sale_price', 'bedrooms', 'bathrooms', 'floors', 'yr_built'])

# Fill missing non-critical data (e.g., basement area)
df['basement_sqft'] = df['basement_sqft'].fillna(0)

# Feature Engineering
# 1. Years Since Renovation
df['renovated'] = np.where(df['yr_renovated'] > 0, 1, 0)
df['years_since_renovation'] = np.where(
    df['yr_renovated'] > 0,
    df['date'].str[:4].astype(int) - df['yr_renovated'],
    df['date'].str[:4].astype(int) - df['yr_built']
)

# 2. House Age
df['house_age'] = df['date'].str[:4].astype(int) - df['yr_built']

# 3. Age Groups for Pie Chart
bins = [0, 10, 20, 40, 60, 100]
labels = ['0-10 yrs', '11-20 yrs', '21-40 yrs', '41-60 yrs', '60+ yrs']
df['age_group'] = pd.cut(df['house_age'], bins=bins, labels=labels, right=False)

# Results Overview
overview = {
    "total_records": len(df),
    "average_sale_price": df['sale_price'].mean(),
    "total_basement_area_sqft": df['basement_sqft'].sum()
}

# Save prepared dataset
df.to_csv('prepared_housing_data.csv', index=False)

# Save overview metrics
with open('dataset_overview.txt', 'w') as f:
    for k, v in overview.items():
        f.write(f"{k}: {v}\n")

print(f"Data preparation complete.\nOverview:\n{overview}\n")
print("Prepared dataset saved as 'prepared_housing_data.csv'.")
print("Overview saved as 'dataset_overview.txt'.")