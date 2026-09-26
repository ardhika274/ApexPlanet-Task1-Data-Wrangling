# ApexPlanet Data Analytics Internship – Task 1

## Task 1: Data Immersion & Wrangling

### Objective
The objective of this task was to understand, inspect, clean, and prepare the provided dataset for further analysis.

## Dataset

The dataset contains 1000 records and 12 columns related to customer orders and sales.

### Columns

- Order_ID
- Order_Date
- Customer_ID
- Customer_Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit_Price
- Total_Sales

## Data Quality Assessment

The dataset was checked for:

- Missing values
- Duplicate records
- Data types
- Date formatting
- Sales calculation consistency

### Findings

- 20 missing values were found in the Age column.
- 13 missing values were found in the City column.
- No duplicate rows were found.
- Order_Date was converted to a proper date format.
- Total_Sales was checked against Quantity × Unit_Price.
- No meaningful inconsistencies were found in Total_Sales.

## Data Cleaning

- Missing Age values were replaced using the median age.
- Missing City values were replaced with "Unknown".
- Order_Date was converted to datetime format.
- Temporary calculation columns were removed after validation.

## Tools Used

- Python
- Pandas
- NumPy
- Excel
- Visual Studio Code

## Deliverables

- Python data-cleaning script
- Cleaned dataset
- Data dictionary
- README documentation
