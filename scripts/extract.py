import pandas as pd

# Read the dataset
df = pd.read_csv("data/superstore.csv")

# Display first 5 rows
print(df.head())

print("\n" + "="*60)

# Shape of dataset
print("Dataset Shape:")
print(df.shape)

print("\n" + "="*60)

# Column Names
print("Column Names:")
print(df.columns)

print("\n" + "="*60)

# Data Types
print("Data Types:")
print(df.dtypes)
print("\n" + "="*60)

# Dataset Information
print("Dataset Information:")
df.info()

print("\n" + "="*60)

# Missing Values
print("Missing Values:")
print(df.isnull().sum())

print("\n" + "="*60)

# Duplicate Rows
print("Duplicate Rows:")
print(df.duplicated().sum())

print("\n" + "="*60)

# Statistical Summary
print("Statistical Summary:")
print(df.describe())