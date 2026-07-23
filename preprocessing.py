import pandas as pd

# --------------------------------------
# Load Dataset
# --------------------------------------
INPUT_FILE = "data/ev_data.csv"
OUTPUT_FILE = "data/cleaned_ev_data.csv"

df = pd.read_csv(INPUT_FILE)

print("Original Dataset Shape:", df.shape)

# --------------------------------------
# Remove Duplicate Rows
# --------------------------------------
df.drop_duplicates(inplace=True)

# --------------------------------------
# Handle Missing Values
# --------------------------------------
numeric_columns = [
    "EV_Sales",
    "Market_Share",
    "Charging_Stations"
]

for column in numeric_columns:
    if column in df.columns:
        df[column].fillna(df[column].median(), inplace=True)

categorical_columns = ["Country"]

for column in categorical_columns:
    if column in df.columns:
        df[column].fillna("Unknown", inplace=True)

# --------------------------------------
# Convert Data Types
# --------------------------------------
df["Year"] = df["Year"].astype(int)
df["EV_Sales"] = df["EV_Sales"].astype(int)
df["Market_Share"] = df["Market_Share"].astype(float)
df["Charging_Stations"] = df["Charging_Stations"].astype(int)

# --------------------------------------
# Sort Data
# --------------------------------------
df.sort_values(
    by=["Country", "Year"],
    inplace=True
)

df.reset_index(drop=True, inplace=True)

# --------------------------------------
# Feature Engineering
# --------------------------------------

# Previous Year's Sales
df["Previous_Year_Sales"] = (
    df.groupby("Country")["EV_Sales"].shift(1)
)

# Year-over-Year Growth (%)
df["Growth_Rate"] = (
    (df["EV_Sales"] - df["Previous_Year_Sales"])
    / df["Previous_Year_Sales"]
) * 100

df["Growth_Rate"] = df["Growth_Rate"].fillna(0)

# Cumulative EV Sales
df["Cumulative_Sales"] = (
    df.groupby("Country")["EV_Sales"].cumsum()
)

# --------------------------------------
# Save Clean Dataset
# --------------------------------------
df.to_csv(OUTPUT_FILE, index=False)

print("Cleaned Dataset Saved Successfully!")
print("Saved File:", OUTPUT_FILE)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())
