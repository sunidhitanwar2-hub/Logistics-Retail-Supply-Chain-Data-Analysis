import pandas as pd

# Read the dataset
df = pd.read_csv("data/superstore.csv")

print("Original Shape:", df.shape)

# -----------------------------
# Convert Date Columns
# -----------------------------
df["Order.Date"] = pd.to_datetime(df["Order.Date"])
df["Ship.Date"] = pd.to_datetime(df["Ship.Date"])

# -----------------------------
# Remove unnecessary column
# -----------------------------
df.drop(columns=["记录数"], inplace=True)

# -----------------------------
# Rename columns
# -----------------------------
df.columns = (
    df.columns
    .str.replace(".", "_", regex=False)
    .str.replace(" ", "_")
)

print("Cleaned Shape:", df.shape)

print("\nColumns after cleaning:\n")
print(df.columns)

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv("transformed/cleaned_superstore.csv", index=False)

print("\n✅ Cleaned dataset saved successfully!")