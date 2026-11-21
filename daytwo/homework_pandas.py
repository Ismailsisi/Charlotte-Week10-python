
import pandas as pd

# Create well production data
data = {
    "well_id": ["WELL-001", "WELL-002", "WELL-003", "WELL-004", "WELL-005", "WELL-006"],
    "status": ["Producing", "Producing", "Shut-in", "Producing", "Producing", "Producing"],
    "oil_bpd": [1200, 950, 0, None, 1100, 850],
    "water_bpd": [200, 150, 0, 180, 250, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Well Production Data:")
print(df)

# Display shape and data types
print("\nDataFrame Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

# Select producing wells
producing_df = df[df["status"] == "Producing"]

print("\nProducing Wells:")
print(producing_df)

# Calculate total liquid production
df["total_liquid_bpd"] = df["oil_bpd"] + df["water_bpd"]

print("\nTotal Liquid Production:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isna().sum())

# Measurement units:
# oil_bpd = barrels per day
# water_bpd = barrels per day
# total_liquid_bpd = barrels per day
