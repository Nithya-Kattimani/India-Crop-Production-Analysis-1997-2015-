# 🌾 India Crop Production Analysis (1997–2015)

## 📌 Project Overview
An end-to-end data analysis project examining crop production trends 
across Indian states from 1997 to 2015. The project covers data cleaning, 
exploratory data analysis, SQL querying and interactive dashboard building.

## 🛠️ Tools & Technologies
| Tool | Purpose |
|---|---|
| Python (pandas, numpy, matplotlib, seaborn) | Data cleaning & EDA |
| PostgreSQL / pgAdmin | Data storage & SQL analysis |
| Power BI Desktop | Interactive dashboard |
| GitHub | Version control & portfolio |

## 📂 Project Structure
```
india-crop-yield-analysis/
│
├── data/
│   ├── raw/
│   │   └── crop_production.csv
│   └── cleaned/
│       └── crop_cleaned.csv
│
├── python/
│   ├── 01_cleaning.py
│   └── 02_eda.py
│
├── sql/
│   └── analysis_queries.sql
│
├── charts/
│   ├── 01_top10_crops.png
│   ├── 02_top10_states.png
│   ├── 03_production_by_season.png
│   ├── 04_yearly_trend.png
│   └── 05_top10_yield_states.png
│
├── powerbi/
│   └── crop_dashboard.pbix
│
└── README.md
```

## 📊 Dataset
- **Source:** [Kaggle — Crop Production in India](https://www.kaggle.com/datasets/abhinand05/crop-production-in-india)
- **Records:** 2,46,091 rows
- **Period:** 1997–2015
- **Coverage:** 33 states, 124 crops, 6 seasons

## 🧹 Data Cleaning (Python)
- Stripped whitespace from all string columns
- Handled 3,730 null values in `Production` column using 
  crop+season median imputation
- Added derived column — `yield_per_hectare` (Production / Area)
- Renamed all columns to clean snake_case format
- Final cleaned dataset: 2,46,091 rows × 8 columns, zero nulls

## 🔍 Key Insights
1. 🌴 **Kerala dominates** — contributes 95%+ of total production 
   driven entirely by Coconut farming
2. ⚡ **Punjab is most efficient** — highest yield among large states 
   despite having smaller cultivated area
3. 🌾 **Kharif is most diverse** — 95,000+ crop records, highest 
   variety of any season
4. 📉 **Production peaked in 2011** then declined sharply — 
   possible drought years or data gaps post 2013
5. 🍬 **Sugarcane leads yield efficiency** among food crops 
   with average yield of 811 tonnes/hectare
6. 🏘️ **Small states punch above weight** — Puducherry and 
   Andaman & Nicobar rank among India's top yield-efficient regions

## 📈 Power BI Dashboard Pages
| Page | Contents |
|---|---|
| Overview | KPI cards, Top 10 crops, Season distribution donut |
| State Analysis | Top states by production & yield, Treemap, Season slicer |
| Crop & Season Trends | Year-wise trend line, Season bar chart, Crop & State slicers |
| Key Insights | Dominant crop per state table, Scatter plot, Insight cards |

## 🚀 How to Reproduce
1. Clone this repository
2. Download dataset from Kaggle link above
3. Run `python/01_cleaning.py` to clean the data
4. Run `python/02_eda.py` to generate EDA charts
5. Create PostgreSQL database `crop_analysis`
6. Import `crop_cleaned.csv` into `crop_data` table
7. Run `sql/analysis_queries.sql` for insights
8. Open `powerbi/crop_dashboard.pbix` in Power BI Desktop

## 👩‍💻 Author
**Nithya Kattimani**  

