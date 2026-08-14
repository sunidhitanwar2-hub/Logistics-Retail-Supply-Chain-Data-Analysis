import pandas as pd
from sqlalchemy import create_engine

# ======================================================
# MySQL Connection
# ======================================================

username = "root"
password = "123"
host = "localhost"
port = "3306"
database = "RetailDB"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

print("Connected to MySQL Successfully!")

# ======================================================
# Read CSV Files
# ======================================================

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
sales = pd.read_csv("data/retail_sales.csv")

# ======================================================
# Load Customers
# ======================================================

customers.to_sql(
    "customers",
    con=engine,
    if_exists="append",
    index=False
)

print("Customers Loaded!")

# ======================================================
# Load Products
# ======================================================

products.to_sql(
    "products",
    con=engine,
    if_exists="append",
    index=False
)

print("Products Loaded!")

# ======================================================
# Load Sales
# ======================================================

sales.to_sql(
    "retail_sales",
    con=engine,
    if_exists="append",
    index=False
)

print("Sales Loaded!")

print("\nETL Load Completed Successfully!")