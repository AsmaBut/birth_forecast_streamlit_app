import pandas as pd

# -------------------------
# 1. Load unemployment Excel file
# -------------------------
df = pd.read_csv("unemployment-rate.csv")

# -------------------------
# 2. Ensure first column contains the year/quarter
# -------------------------
# Rename columns if needed
df.columns = ["Period", "UnemploymentRate"]

# -------------------------
# 3. Keep only annual values (remove quarters like '1971 Q1')
# -------------------------
annual_df = df[df["Period"].astype(str).str.match(r"^\d{4}$")]

# Convert Period to integer
annual_df["Year"] = annual_df["Period"].astype(int)

# -------------------------
# 4. Final cleaned dataset
# -------------------------
annual_df = annual_df[["Year", "UnemploymentRate"]].reset_index(drop=True)

# Save cleaned file
annual_df.to_csv("unemployment_rate_clean.csv", index=False)

print("✅ Cleaned annual unemployment data saved as unemployment_rate_clean.xlsx")
