# 

# \# Week 10 Class 2 — Student Practical

# 

# \## Program Description

# 

# This program uses Pandas to read and analyse daily oil production data from four wells across two fields.

# 

# It checks the data for missing oil and pressure readings, selects producing observations, and adds two calculated columns to the production table.

# 

# The program keeps the original data unchanged and saves the enriched data in a new CSV file.

# 

# \## Setup

# 

# Open the practical folder in VS Code.

# 

# Install the required packages:

# 

# ```bash

# python -m pip install -r requirements.txt

# ```

# 

# \## How to Run

# 

# Run the program using:

# 

# ```bash

# python pandas\_production\_lab.py

# ```

# 

# \## Input and Output Files

# 

# Input file:

# 

# `daily\_production.csv`

# 

# Output file:

# 

# `outputs/production\_enriched.csv`

# 

# The output file contains the original seven columns and two additional columns:

# 

# \- `total\_liquid\_bpd`

# \- `pressure\_kpa`

# 

# \## Measurement Units

# 

# \- `oil\_bpd` — barrels per day (bbl/day)

# \- `water\_bpd` — barrels per day (bbl/day)

# \- `total\_liquid\_bpd` — barrels per day (bbl/day)

# \- `pressure\_psi` — pounds per square inch (psi)

# \- `pressure\_kpa` — kilopascals (kPa)

# 

# \## Key Findings

# 

# The dataset contains 16 records from 4 unique wells across 2 fields.

# 

# The program identified:

# \- 14 producing observations.

# \- 1 missing oil reading.

# \- 1 missing pressure reading.

# 

# The exported CSV contains 16 rows and 9 columns.

# 

# \## Operational Observation

# 

# On November 2, 2026, WELL-12 was marked as PRODUCING, but its oil production reading was missing. Its water production reading was 190 bpd.

# 

# This means the total liquid production for that observation could not be calculated. The missing oil reading should be checked before using the result in a production report.

# 

# \## Why Missing Values Should Not Be Replaced With Zero

# 

# A missing value means that a measurement was not available or was not recorded. Zero means that a measurement was recorded and its value was zero.

# 

# For example, replacing the missing oil reading for WELL-12 with zero would make it appear that the well produced no oil on that day.

# 

# This could give an incorrect production report. Missing values should therefore remain missing until the correct readings are available.



