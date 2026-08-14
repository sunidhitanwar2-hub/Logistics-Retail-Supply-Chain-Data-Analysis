import pandas as pd

# ======================================================
# Read Transformed Dataset
# ======================================================

df = pd.read_csv("transformed/transformed_superstore.csv")

print("=" * 60)
print("RETAIL DATA ENGINEERING PIPELINE")
print("=" * 60)

print("\nOriginal Dataset Shape:", df.shape)

# ======================================================
# Create Customers Table
# ======================================================

customers = (
    df[
        [
            "Customer_ID",
            "Customer_Name",
            "Segment",
            "City",
            "State",
            "Country",
            "Region",
            "Market"
        ]
    ]
    .drop_duplicates(subset=["Customer_ID"])
)

print("\nCustomers Table Shape:", customers.shape)

# ======================================================
# Create Products Table
# ======================================================

products = (
    df[
        [
            "Product_ID",
            "Product_Name",
            "Category",
            "Sub_Category"
        ]
    ]
    .drop_duplicates(subset=["Product_ID"])
)

print("Products Table Shape:", products.shape)

# ======================================================
# Create Sales Table
# ======================================================

sales = df[
    [
        "Order_ID",
        "Order_Date",
        "Ship_Date",
        "Customer_ID",
        "Product_ID",
        "Sales",
        "Quantity",
        "Discount",
        "Profit",
        "Shipping_Cost",
        "Ship_Mode",
        "Order_Priority",
        "Year",
        "Order_Month",
        "Order_Quarter",
        "Order_Day",
        "Shipping_Days",
        "Profit_Margin"
    ]
]

print("Sales Table Shape:", sales.shape)

# ======================================================
# Validation Report
# ======================================================

print("\n" + "=" * 60)
print("VALIDATION REPORT")
print("=" * 60)

print("\nCustomers")
print("------------------------------")
print("Rows               :", len(customers))
print("Unique Customer IDs:", customers["Customer_ID"].nunique())

print("\nProducts")
print("------------------------------")
print("Rows              :", len(products))
print("Unique Product IDs:", products["Product_ID"].nunique())

print("\nSales")
print("------------------------------")
print("Rows:", len(sales))

# ======================================================
# Save CSV Files
# ======================================================

customers.to_csv(
    "data/customers.csv",
    index=False
)

products.to_csv(
    "data/products.csv",
    index=False
)

sales.to_csv(
    "data/retail_sales.csv",
    index=False
)

# ======================================================
# Success Message
# ======================================================

print("\n" + "=" * 60)
print("TABLES CREATED SUCCESSFULLY")
print("=" * 60)

print("\nFiles Saved Successfully")

print("✔ data/customers.csv")
print("✔ data/products.csv")
print("✔ data/retail_sales.csv")

print("\nETL Split Process Completed Successfully!")