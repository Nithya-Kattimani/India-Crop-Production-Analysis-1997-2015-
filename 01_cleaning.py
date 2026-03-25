import pandas as pd
import numpy as np

# Load raw data
df = pd.read_csv(r'C:\Users\Lenovo\Downloads\crop_production.csv')
print(f"Raw shape: {df.shape}")

# ── 1. Strip whitespace from string columns ──
df['Season'] = df['Season'].str.strip()
df['Crop'] = df['Crop'].str.strip()
df['State_Name'] = df['State_Name'].str.strip()
df['District_Name'] = df['District_Name'].str.strip()

# ── 2. Handle nulls in Production ──
df['Production'] = df.groupby(['Crop', 'Season'])['Production']\
                     .transform(lambda x: x.fillna(x.median()))
df['Production'] = df['Production'].fillna(df['Production'].median())

print(f"Nulls after cleaning: {df.isnull().sum().sum()}")

# ── 3. Add Yield column ──
df['Yield'] = (df['Production'] / df['Area']).round(2)
df['Yield'] = df['Yield'].replace([np.inf, -np.inf], np.nan).fillna(0)

# ── 4. Rename columns ──
df.rename(columns={
    'State_Name': 'state',
    'District_Name': 'district',
    'Crop_Year': 'crop_year',
    'Season': 'season',
    'Crop': 'crop',
    'Area': 'area_hectares',
    'Production': 'production_tonnes',
    'Yield': 'yield_per_hectare'
}, inplace=True)

# ── 5. Save cleaned file ──
df.to_csv(r'C:\Users\Lenovo\Downloads\archive (1)\data\cleaned\crop_cleaned.csv', index=False)
print(f"Cleaned shape: {df.shape}")
print(df.head())
print(df.dtypes)