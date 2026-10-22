
import pandas as pd

# Read the CSV file
df = pd.read_csv("Auto.csv")

# 1. Clean and update the CSV file
df.columns = df.columns.str.strip().str.lower().str.replace("-", "_")

# Remove extra spaces and replace missing values
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str).str.strip().replace(
        {"?": pd.NA, "": pd.NA}
    )

# Convert horsepower into numeric data
df["horsepower"] = pd.to_numeric(df["horsepower"], errors="coerce")

# Remove rows containing missing values
df.dropna(inplace=True)

# Extract company name from the car name
df["company"] = df["name"].str.split().str[0].str.title()

# Save the cleaned data
df.to_csv("Auto_cleaned.csv", index=False)

print("CSV file cleaned and updated successfully.")

# 2. Print total cars of all companies
print("\nTotal cars manufactured by each company:")
print(df["company"].value_counts().sort_index())

# 3. Find average mileage of all companies
print("\nAverage mileage of each company:")
print(df.groupby("company")["mpg"].mean().round(2).sort_index())
