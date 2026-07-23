import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

# ------------------------------------
# Load Cleaned Dataset
# ------------------------------------
df = pd.read_csv("data/cleaned_ev_data.csv")

# ------------------------------------
# Store Forecast Results
# ------------------------------------
forecast_list = []

# ------------------------------------
# Train Model for Each Country
# ------------------------------------
countries = df["Country"].unique()

for country in countries:

    country_df = df[df["Country"] == country]

    X = country_df[["Year"]]
    y = country_df["EV_Sales"]

    model = LinearRegression()
    model.fit(X, y)

    # Prediction on Training Data
    train_pred = model.predict(X)

    # Evaluation Metrics
    r2 = r2_score(y, train_pred)
    mae = mean_absolute_error(y, train_pred)

    print("=" * 50)
    print("Country :", country)
    print("R² Score :", round(r2, 4))
    print("MAE :", round(mae, 2))

    # Save Model
    joblib.dump(model, f"models/{country}_model.pkl")

    # Forecast Future Years
    future_years = np.arange(
        country_df["Year"].max() + 1,
        2036
    )

    future_df = pd.DataFrame({
        "Year": future_years
    })

    predictions = model.predict(future_df)

    for year, sales in zip(future_years, predictions):

        forecast_list.append({

            "Country": country,
            "Year": year,
            "Forecast_EV_Sales": int(max(0, sales))

        })

# ------------------------------------
# Save Forecast
# ------------------------------------
forecast_df = pd.DataFrame(forecast_list)

forecast_df.to_csv(
    "data/forecast.csv",
    index=False
)

print("\nForecast saved successfully!")
print(forecast_df.head())
