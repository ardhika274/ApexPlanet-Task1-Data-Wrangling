import pandas as pd 
df = pd.read_excel("dataset/ApexPlanet_DataAnalytics_Dataset.xlsx")
print(df.head())
print(df.head())
print("Dataset size:")
print(df.shape)
print("\ncolumn information:")
print(df.info(0))
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate values:")
print(df.duplicated().sum())
# Clean missing values

df["Age"] = df["Age"].fillna(df["Age"].median())

df["City"] = df["City"].fillna("Unknown")

print("\nMissing values after cleaning:")
print(df.isnull().sum())
# Convert Order_Date to proper date format

df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

print("\nOrder Date data type:")
print(df["Order_Date"].dtype)
print("\nData types of numerical columns:")
print(df[["Age", "Quantity", "Unit_Price", "Total_Sales"]].dtypes)
# Check Total Sales consistency

df["Calculated_Sales"] = df["Quantity"] * df["Unit_Price"]

df["Sales_Difference"] = (
    df["Total_Sales"] - df["Calculated_Sales"]
)

print("\nSales difference:")
print(df["Sales_Difference"].describe())

print("\nRows with inconsistent sales:")
print(
    df[df["Sales_Difference"].abs() > 0.01]
    [["Order_ID", "Quantity", "Unit_Price", "Total_Sales", "Calculated_Sales", "Sales_Difference"]]
    .head(10)
)
# Remove temporary checking columns

df.drop(columns=["Calculated_Sales", "Sales_Difference"], inplace=True)

print("\nFinal columns:")
print(df.columns)
# Save cleaned dataset

df.to_excel("dataset/cleaned_dataset.xlsx", index=False)

print("\nCleaned dataset saved successfully!")
print("\nTask 1 cleaning completed.")
print("Final dataset shape:", df.shape)
print("Remaining missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())