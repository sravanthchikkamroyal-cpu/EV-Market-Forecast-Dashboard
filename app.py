import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
from sklearn.linear_model import LinearRegression
import numpy as np

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv("data/ev_data.csv")

# ----------------------------
# Initialize Dash App
# ----------------------------
app = Dash(__name__)
app.title = "EV Market Forecast Dashboard"

# ----------------------------
# Dropdown Values
# ----------------------------
countries = sorted(df["Country"].unique())

# ----------------------------
# Dashboard Layout
# ----------------------------
app.layout = html.Div([

    html.H1(
        "🚗 EV Market Forecast Dashboard",
        style={
            "textAlign": "center",
            "color": "#2E86C1"
        }
    ),

    html.Br(),

    html.Div([

        html.Label("Select Country"),

        dcc.Dropdown(
            id="country-dropdown",
            options=[
                {"label": c, "value": c}
                for c in countries
            ],
            value=countries[0],
            clearable=False
        )

    ], style={
        "width": "40%",
        "margin": "auto"
    }),

    html.Br(),

    html.Div([

        html.Div(id="sales-card", className="card"),
        html.Div(id="market-card", className="card"),
        html.Div(id="station-card", className="card"),

    ], style={
        "display": "flex",
        "justifyContent": "space-around"
    }),

    html.Br(),

    dcc.Graph(id="sales-chart"),

    dcc.Graph(id="market-chart"),

    dcc.Graph(id="forecast-chart")

])

# ----------------------------
# Callback
# ----------------------------
@app.callback(

    Output("sales-card", "children"),
    Output("market-card", "children"),
    Output("station-card", "children"),
    Output("sales-chart", "figure"),
    Output("market-chart", "figure"),
    Output("forecast-chart", "figure"),

    Input("country-dropdown", "value")

)

def update_dashboard(country):

    dff = df[df["Country"] == country]

    total_sales = int(dff["EV_Sales"].sum())

    avg_market = round(dff["Market_Share"].mean(), 2)

    stations = int(dff["Charging_Stations"].max())

    # ------------------------
    # Sales Trend
    # ------------------------
    sales_fig = px.line(
        dff,
        x="Year",
        y="EV_Sales",
        markers=True,
        title="EV Sales Trend"
    )

    # ------------------------
    # Market Share
    # ------------------------
    market_fig = px.bar(
        dff,
        x="Year",
        y="Market_Share",
        title="Market Share (%)"
    )

    # ------------------------
    # Forecast
    # ------------------------
    X = dff[["Year"]]
    y = dff["EV_Sales"]

    model = LinearRegression()
    model.fit(X, y)

    future = np.arange(
        dff["Year"].max() + 1,
        2036
    )

    future_df = pd.DataFrame({
        "Year": future
    })

    prediction = model.predict(future_df)

    forecast = pd.DataFrame({
        "Year": future,
        "Forecast": prediction
    })

    forecast_fig = px.line(
        forecast,
        x="Year",
        y="Forecast",
        markers=True,
        title="EV Sales Forecast"
    )

    return (

        html.Div([
            html.H3("Total EV Sales"),
            html.H2(f"{total_sales:,}")
        ]),

        html.Div([
            html.H3("Average Market Share"),
            html.H2(f"{avg_market}%")
        ]),

        html.Div([
            html.H3("Charging Stations"),
            html.H2(f"{stations:,}")
        ]),

        sales_fig,
        market_fig,
        forecast_fig

    )

# ----------------------------
# Run Server
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
