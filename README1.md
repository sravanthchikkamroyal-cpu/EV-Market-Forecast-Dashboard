# 🚗 EV Market Forecast Dashboard

## Overview

The **EV Market Forecast Dashboard** is an interactive data analytics and forecasting application that analyzes Electric Vehicle (EV) market trends across multiple countries. The dashboard provides insights into EV sales, market share, charging infrastructure, and future market growth using machine learning.

Built with **Python, Pandas, Plotly, Dash, and Scikit-learn**, the project helps users visualize historical data and forecast future EV sales, making it useful for researchers, students, policymakers, and business analysts.

---

## Features

* 📈 Interactive EV sales trend visualization
* 🌍 Country-wise market comparison
* 🔋 Charging infrastructure analysis
* 📊 Market share dashboard
* 🤖 EV sales forecasting using Linear Regression
* 📉 Growth rate analysis
* 🎨 Responsive and modern dashboard UI
* 📋 KPI cards for quick insights
* 📱 Mobile-friendly dashboard layout

---

## Tech Stack

* **Programming Language:** Python
* **Framework:** Dash
* **Data Analysis:** Pandas, NumPy
* **Visualization:** Plotly
* **Machine Learning:** Scikit-learn
* **Model Storage:** Joblib

---

## Project Structure

```text
EV-Market-Forecast-Dashboard/
│
├── app.py
├── preprocessing.py
├── forecast.py
├── charts.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── ev_data.csv
│   ├── cleaned_ev_data.csv
│   └── forecast.csv
│
├── models/
│
├── assets/
│   └── style.css
```

---

## Dataset

The dataset contains EV market information for multiple countries.

### Columns

| Column            | Description                 |
| ----------------- | --------------------------- |
| Country           | Country name                |
| Year              | Year of record              |
| EV_Sales          | Number of EVs sold          |
| Market_Share      | EV market share (%)         |
| Charging_Stations | Number of charging stations |

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/EV-Market-Forecast-Dashboard.git
```

### Navigate to the Project Folder

```bash
cd EV-Market-Forecast-Dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

### Step 1: Clean the Dataset

```bash
python preprocessing.py
```

### Step 2: Train the Forecast Model

```bash
python forecast.py
```

### Step 3: Launch the Dashboard

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:8050
```

---

## Dashboard Modules

* Home Dashboard
* KPI Cards
* EV Sales Trend
* Market Share Analysis
* Charging Infrastructure
* Country Comparison
* Growth Rate Analysis
* Future EV Sales Forecast

---

## Machine Learning

The dashboard uses **Linear Regression** to learn historical EV sales patterns and predict future EV sales for each country until **2035**.

### Workflow

1. Load historical data
2. Clean and preprocess data
3. Train the regression model
4. Generate future predictions
5. Display forecasts in interactive charts

---

## Key Libraries

* Dash
* Plotly
* Pandas
* NumPy
* Scikit-learn
* Joblib

---

## Future Enhancements

* Use Prophet, XGBoost, or LSTM for improved forecasting
* Add real-time EV market data integration
* Include government policy analysis
* Display charging station maps
* Add downloadable PDF and Excel reports
* User authentication and personalized dashboards
* Deploy to Render, Railway, or Heroku

---

## Screenshots

Add screenshots after running the dashboard.

```text
screenshots/
│
├── dashboard.png
├── forecast.png
├── market_share.png
└── comparison.png
```

---

## Author

**Sravanth Chikkam Royal**

B.Tech Student | Aspiring Software Engineer

Skills:

* Python
* Java
* Data Structures & Algorithms
* Machine Learning
* Data Analytics
* Dash & Plotly
* SQL

---

## License

This project is released under the **MIT License**.

---

## Acknowledgements

* Dash
* Plotly
* Pandas
* NumPy
* Scikit-learn
* Open-source EV datasets and the data science community

