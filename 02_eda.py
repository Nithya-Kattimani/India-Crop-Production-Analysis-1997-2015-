import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
df = pd.read_csv(r'C:\Users\Lenovo\Downloads\archive (1)\data\cleaned\crop_cleaned.csv')

# Create charts folder
os.makedirs(r'C:\Users\Lenovo\Downloads\archive (1)\charts', exist_ok=True)
charts = r'C:\Users\Lenovo\Downloads\archive (1)\charts'

sns.set_theme(style='whitegrid')

# ── 1. Top 10 crops by total production ──
fig, ax = plt.subplots(figsize=(12, 6))
top_crops = df.groupby('crop')['production_tonnes'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_crops.values, y=top_crops.index, palette='viridis', ax=ax)
ax.set_title('Top 10 Crops by Total Production (1997–2015)', fontsize=14)
ax.set_xlabel('Total Production (Tonnes)')
plt.tight_layout()
plt.savefig(f'{charts}/01_top10_crops.png')
plt.close()
print("Chart 1 saved ✅")

# ── 2. Top 10 states by total production ──
fig, ax = plt.subplots(figsize=(12, 6))
top_states = df.groupby('state')['production_tonnes'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_states.values, y=top_states.index, palette='magma', ax=ax)
ax.set_title('Top 10 States by Total Production (1997–2015)', fontsize=14)
ax.set_xlabel('Total Production (Tonnes)')
plt.tight_layout()
plt.savefig(f'{charts}/02_top10_states.png')
plt.close()
print("Chart 2 saved ✅")

# ── 3. Production by Season ──
fig, ax = plt.subplots(figsize=(10, 5))
season_prod = df.groupby('season')['production_tonnes'].sum().sort_values(ascending=False)
sns.barplot(x=season_prod.index, y=season_prod.values, palette='coolwarm', ax=ax)
ax.set_title('Total Production by Season', fontsize=14)
ax.set_ylabel('Total Production (Tonnes)')
plt.tight_layout()
plt.savefig(f'{charts}/03_production_by_season.png')
plt.close()
print("Chart 3 saved ✅")

# ── 4. Year-wise production trend ──
fig, ax = plt.subplots(figsize=(12, 5))
yearly = df.groupby('crop_year')['production_tonnes'].sum()
ax.plot(yearly.index, yearly.values, marker='o', color='green', linewidth=2)
ax.set_title('Year-wise Total Production Trend (1997–2015)', fontsize=14)
ax.set_xlabel('Year')
ax.set_ylabel('Total Production (Tonnes)')
plt.tight_layout()
plt.savefig(f'{charts}/04_yearly_trend.png')
plt.close()
print("Chart 4 saved ✅")

# ── 5. Top 10 states by yield efficiency ──
fig, ax = plt.subplots(figsize=(12, 6))
top_yield = df.groupby('state')['yield_per_hectare'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=top_yield.values, y=top_yield.index, palette='Blues_r', ax=ax)
ax.set_title('Top 10 States by Average Yield Efficiency', fontsize=14)
ax.set_xlabel('Avg Yield (Tonnes per Hectare)')
plt.tight_layout()
plt.savefig(f'{charts}/05_top10_yield_states.png')
plt.close()
print("Chart 5 saved ✅")

print("\nAll charts saved to charts folder!")