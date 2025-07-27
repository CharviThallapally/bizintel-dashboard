import pandas as pd

# Load CSV with proper encoding
df = pd.read_csv("superstore.csv", encoding='latin1')

# Show first 5 rows
print(df.head())

# Show column names
print("\nColumns:")
print(df.columns)
