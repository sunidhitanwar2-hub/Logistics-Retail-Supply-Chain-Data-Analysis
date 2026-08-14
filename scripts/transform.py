import pandas as pd
import numpy as np
# Read cleaned dataset
df = pd.read_csv("transformed/cleaned_superstore.csv")

print("Original Shape:", df.shape)

# -----------------------------
# Convert Date Columns
# -----------------------------
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])

# -----------------------------
# Feature Engineering
# -----------------------------

# Order Month
df["Order_Month"] = df["Order_Date"].dt.month_name()

# Order Quarter
df["Order_Quarter"] = df["Order_Date"].dt.quarter

# Order Day
df["Order_Day"] = df["Order_Date"].dt.day_name()

# Shipping Days
df["Shipping_Days"] = (
    df["Ship_Date"] - df["Order_Date"]
).dt.days

# Profit Margin
df["Profit_Margin"] = np.where(
    df["Sales"] != 0,
    (df["Profit"] / df["Sales"]) * 100,
    0
)

df["Profit_Margin"] = df["Profit_Margin"].round(2)
# Round to 2 decimal places
df["Profit_Margin"] = df["Profit_Margin"].round(2)

print("\nNew Columns Added:\n")

print(df[[
    "Order_Month",
    "Order_Quarter",
    "Order_Day",
    "Shipping_Days",
    "Profit_Margin"
]].head())

# Save transformed dataset
df.to_csv(
    "transformed/transformed_superstore.csv",
    index=False
)

print("\n✅ Transformation Completed Successfully!")