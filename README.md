# EV-Market-Forecast-Dashboard
The **EV Market Forecast Dashboard** is an interactive application that analyzes global electric vehicle trends using Python, Pandas, Plotly, and Dash. It visualizes EV sales, adoption rates, charging infrastructure, and government policies while using machine learning to forecast future market growth through interactive charts, maps and dashboard.
For your project **"EV Market Forecast Dashboard"**, here is a complete project plan that is suitable for a college final-year project or portfolio.

# EV Market Forecast Dashboard

## Objective

Develop an interactive dashboard to analyze and forecast the growth of the global Electric Vehicle (EV) market using historical data, government policies, and EV adoption rates.

The dashboard should help users:

* Analyze historical EV sales
* Compare countries
* Study government incentives
* Predict future EV adoption
* Understand market growth trends


---

# Technology Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Plotly
* Dash
* Scikit-Learn
* Prophet (optional for forecasting)

### Dataset Sources

* International Energy Agency (IEA) Global EV Data Explorer
* Atlas EV Hub
* Kaggle Global EV datasets


---

# Project Architecture

```
Dataset
     │
     ▼
Data Cleaning (Pandas)
     │
     ▼
Feature Engineering
     │
     ▼
Forecast Model
(Random Forest / Linear Regression / Prophet)
     │
     ▼
Interactive Dashboard
(Dash + Plotly)
```

---

# Dashboard Pages

## 1. Home Dashboard

KPIs

* Total EV Sales
* EV Growth %
* Number of Countries
* Charging Stations
* Market Size

---

## 2. Global EV Sales Trend

Charts

* Line Chart
* Area Chart

Shows

* EV Sales (2010–2025)
* Annual Growth Rate

---

## 3. Country Comparison

Filters

* Country
* Year

Visualizations

* Bar Chart
* Pie Chart
* Heatmap

Compare

* China
* USA
* India
* Germany
* Norway
* UK

---

## 4. Government Policy Analysis

Visualizations

* Incentives
* Tax Benefits
* Subsidies
* Charging Infrastructure

Example

| Country | Subsidy    | Tax Benefit |
| ------- | ---------- | ----------- |
| India   | ₹1.5 Lakh  | Yes         |
| USA     | Tax Credit | Yes         |
| China   | High       | Yes         |
| Norway  | High       | Yes         |


---

## 5. EV Adoption Map

Interactive World Map

Color Based On

* EV Market Share
* Adoption %
* Sales

Hover

Country

Sales

Growth

Population

---

## 6. Charging Infrastructure

Charts

* Bubble Chart
* Bar Graph

Compare

Charging Stations

Fast Chargers

Growth

---

## 7. Forecast Dashboard

Machine Learning

Input

```
Country
Current Sales
Government Incentive
GDP
Population
Charging Stations
```

Output

```
Predicted EV Sales

2030

2035

2040
```

---

# Machine Learning Models

### Linear Regression

Predict

Future EV Sales

---

### Random Forest

Predict

EV Adoption

---

### Prophet

Time Series Forecast

Future Market Growth

---

# Dashboard Filters

* Country
* Year
* Vehicle Type
* BEV
* PHEV
* Government Policy
* Region

---

# Important Visualizations

### Line Graph

EV Sales Growth

---

### Bar Chart

Country Comparison

---

### Pie Chart

Vehicle Type Distribution

---

### Choropleth Map

Global Adoption

---

### Scatter Plot

Charging Stations vs EV Sales

---

### Heatmap

Government Policy Impact

---

### Forecast Line

2030 Prediction

---

# Dataset Columns

```
Year
Country
EV Sales
EV Stock
Charging Stations
Population
GDP
Government Incentive
Fuel Price
CO₂ Emissions
Vehicle Type
Market Share
```

---

# Dashboard Features

✔ Search Country

✔ Year Slider

✔ Interactive Charts

✔ Download CSV

✔ Dark Mode

✔ Forecast Button

✔ Live Filtering

---

# Folder Structure

```
EV-Dashboard/

│
├── data/
│     ev_data.csv
│
├── assets/
│     style.css
│
├── models/
│     forecast.py
│
├── dashboard.py
│
├── preprocessing.py
│
├── visualization.py
│
├── requirements.txt
│
└── README.md
```

---

# Required Python Libraries

```python
pip install pandas

pip install numpy

pip install plotly

pip install dash

pip install scikit-learn

pip install prophet
```

---

# Expected Output

* Interactive EV Dashboard
* Country-wise Analysis
* Government Policy Comparison
* World Map Visualization
* Future EV Market Prediction (2030–2040)
* Downloadable Reports

---

# Future Enhancements

* Live EV data updates through APIs
* Battery price forecasting
* Carbon emission reduction estimates
* EV charging station demand prediction
* AI-powered market insights
* Mobile-friendly dashboard


