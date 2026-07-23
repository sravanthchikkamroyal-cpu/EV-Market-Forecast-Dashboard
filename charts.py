import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------
# Load Data
# -----------------------------------
df = pd.read_csv("data/cleaned_ev_data.csv")


# -----------------------------------
# 1. EV Sales Trend
# -----------------------------------
def sales_trend(country):

    data = df[df["Country"] == country]

    fig = px.line(
        data,
        x="Year",
        y="EV_Sales",
        markers=True,
        title=f"EV Sales Trend - {country}",
        template="plotly_white"
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="EV Sales"
    )

    return fig


# -----------------------------------
# 2. Market Share
# -----------------------------------
def market_share(country):

    data = df[df["Country"] == country]

    fig = px.bar(
        data,
        x="Year",
        y="Market_Share",
        color="Market_Share",
        title=f"Market Share - {country}",
        template="plotly_white"
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Market Share (%)"
    )

    return fig


# -----------------------------------
# 3. Charging Stations
# -----------------------------------
def charging_station_chart(country):

    data = df[df["Country"] == country]

    fig = px.bar(
        data,
        x="Year",
        y="Charging_Stations",
        color="Charging_Stations",
        title=f"Charging Stations - {country}",
        template="plotly_white"
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Charging Stations"
    )

    return fig


# -----------------------------------
# 4. Country Comparison
# -----------------------------------
def compare_countries():

    latest_year = df["Year"].max()

    data = df[df["Year"] == latest_year]

    fig = px.bar(
        data,
        x="Country",
        y="EV_Sales",
        color="Country",
        title=f"EV Sales Comparison ({latest_year})",
        template="plotly_white"
    )

    return fig


# -----------------------------------
# 5. Pie Chart
# -----------------------------------
def sales_distribution():

    latest_year = df["Year"].max()

    data = df[df["Year"] == latest_year]

    fig = px.pie(
        data,
        names="Country",
        values="EV_Sales",
        title="Global EV Sales Distribution"
    )

    return fig


# -----------------------------------
# 6. Scatter Plot
# -----------------------------------
def charging_vs_sales():

    latest_year = df["Year"].max()

    data = df[df["Year"] == latest_year]

    fig = px.scatter(
        data,
        x="Charging_Stations",
        y="EV_Sales",
        size="Market_Share",
        color="Country",
        hover_name="Country",
        title="Charging Stations vs EV Sales",
        template="plotly_white"
    )

    return fig


# -----------------------------------
# 7. Growth Rate
# -----------------------------------
def growth_chart(country):

    data = df[df["Country"] == country]

    fig = px.line(
        data,
        x="Year",
        y="Growth_Rate",
        markers=True,
        title=f"EV Growth Rate - {country}",
        template="plotly_white"
    )

    fig.update_layout(
        yaxis_title="Growth Rate (%)"
    )

    return fig


# -----------------------------------
# 8. Forecast Chart
# -----------------------------------
def forecast_chart(country):

    history = df[df["Country"] == country]

    forecast = pd.read_csv("data/forecast.csv")
    forecast = forecast[forecast["Country"] == country]

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(
            x=history["Year"],
            y=history["EV_Sales"],
            mode="lines+markers",
            name="Historical"
        )

    )

    fig.add_trace(

        go.Scatter(
            x=forecast["Year"],
            y=forecast["Forecast_EV_Sales"],
            mode="lines+markers",
            name="Forecast"
        )

    )

    fig.update_layout(

        title=f"EV Sales Forecast - {country}",
        xaxis_title="Year",
        yaxis_title="EV Sales",
        template="plotly_white"

    )

    return fig


# -----------------------------------
# 9. KPI Cards
# -----------------------------------
def dashboard_metrics(country):

    data = df[df["Country"] == country]

    metrics = {

        "Total Sales": int(data["EV_Sales"].sum()),

        "Average Market Share": round(
            data["Market_Share"].mean(), 2
        ),

        "Charging Stations": int(
            data["Charging_Stations"].max()
        ),

        "Growth Rate": round(
            data["Growth_Rate"].mean(), 2
        )

    }

    return metrics
