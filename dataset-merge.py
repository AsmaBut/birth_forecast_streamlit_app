import pandas as pd

# -------------------------
# 1. Read Monthly Birth Data
# -------------------------
birth_df = pd.read_csv("monthly-birth-registrations.csv", encoding="latin1")

# Convert wide monthly columns into long format
birth_long = birth_df.melt(
    id_vars=["Year"], 
    value_vars=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"],
    var_name="Month", 
    value_name="Births"
)

# Ensure months are ordered correctly
month_order = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
birth_long["Month"] = pd.Categorical(birth_long["Month"], categories=month_order, ordered=True)


cpi_df = pd.read_excel("cpi-dataset.xlsx", engine="openpyxl")

# Month mapping to match Birth dataset format
month_map = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
    5: "May", 6: "June", 7: "July", 8: "Aug",
    9: "Sept", 10: "Oct", 11: "Nov", 12: "Dec"
}

# Handle if Excel read as datetime
if pd.api.types.is_datetime64_any_dtype(cpi_df["year"]):
    cpi_df["Year"] = cpi_df["year"].dt.year
    cpi_df["Month"] = cpi_df["year"].dt.month.map(month_map)
else:
    # Handle if Excel kept as text
    cpi_df["Month"] = cpi_df["year"].str[:3]
    cpi_df["Year"] = cpi_df["year"].str[-2:].astype(int)
    cpi_df["Year"] = cpi_df["Year"].apply(lambda x: 1900+x if x > 50 else 2000+x)

print(cpi_df.head(12))
# -------------------------
# 2. Read Annual Datasets
# -------------------------

unemployment_df = pd.read_csv("unemployment_rate_clean.csv")  # Year, UnemploymentRate
maternal_df = pd.read_excel("maternal-health-indicator.xlsx")  # Year, BMI, Diabetes, Induction, etc.
education_df = pd.read_excel("female-tertiary-enrollment.xlsx")  # Year, FemaleEnrollment

# Extract 4-digit year safely
birth_long["Year"] = (
    birth_long["Year"]
    .astype(str)
    .str.extract(r"(\d{4})")
)

# Drop rows with no valid year
birth_long = birth_long.dropna(subset=["Year"])

# Convert to integer
birth_long["Year"] = birth_long["Year"].astype(int)

# Ensure CPI Year is also int
cpi_df["Year"] = cpi_df["Year"].astype(int)

# -------------------------
# Merge again
# -------------------------
merged_df = birth_long.merge(
    cpi_df[["Year", "Month", "cpi index"]],
    on=["Year", "Month"], how="left"
)
# -------------------------
# 5. Merge Annual Data with Monthly Data
# -------------------------
merged_df = merged_df.merge(unemployment_df, on="Year", how="left")
merged_df = merged_df.merge(maternal_df, on="Year", how="left")
merged_df = merged_df.merge(education_df, on="Year", how="left")

# -------------------------
# 6. Save Final Merged File
# -------------------------
merged_df.to_csv("final_merged_dataset.csv", index=False)

print("✅ Final merged dataset saved as 'final_merged_dataset.csv'")
