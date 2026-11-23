
# Week 10 Class 3 — Operational Notes

## Dataset Overview

The production surveillance dataset contains 24 records from four wells across two fields: North and South.

There are 22 ACTIVE records and 2 SHUT_IN records.

## Operational Observations

1. WELL-B1 recorded the three highest valid ACTIVE oil observations: 226 bbl on October 4, 230 bbl on October 5, and 234 bbl on October 6, 2026.

2. WELL-B1 had the highest valid ACTIVE oil total, with 1,122 bbl across five observations. WELL-A1 followed with 1,104 bbl across six observations.

3. WELL-A1 had a missing water reading on October 2, 2026. Its oil reading was available at 178 bbl, so it can still be included in an oil-only analysis.

4. Two records, R010 and R023, were marked SHUT_IN. Although they contain oil values, they were excluded from the ACTIVE oil calculations.

5. The pivot table contains NaN values where a well does not belong to a particular field. These missing combinations were not replaced with zero.

## Inclusion and Exclusion Policy

The analysis includes records where:

- Status is ACTIVE.
- Oil reading is available.
- Oil reading is zero or greater.

The analysis excludes:

- SHUT_IN records.
- Records with missing oil readings.
- Records with negative oil readings.

A missing water reading does not exclude a record from oil-only calculations. However, it must be considered in calculations involving both oil and water.

Zero values are retained because zero is a valid measured value, not a missing reading.


# Week 10 Class 3 — Operational Notes

## Dataset Overview

The production surveillance dataset contains 24 records from four wells across two fields: North and South.

There are 22 ACTIVE records and 2 SHUT_IN records.

## Operational Observations

1. WELL-B1 recorded the three highest valid ACTIVE oil observations: 226 bbl on October 4, 230 bbl on October 5, and 234 bbl on October 6, 2026.

2. WELL-B1 had the highest valid ACTIVE oil total, with 1,122 bbl across five observations. WELL-A1 followed with 1,104 bbl across six observations.

3. WELL-A1 had a missing water reading on October 2, 2026. Its oil reading was available at 178 bbl, so it can still be included in an oil-only analysis.

4. Two records, R010 and R023, were marked SHUT_IN. Although they contain oil values, they were excluded from the ACTIVE oil calculations.

5. The pivot table contains NaN values where a well does not belong to a particular field. These missing combinations were not replaced with zero.

## Inclusion and Exclusion Policy

The analysis includes records where:

- Status is ACTIVE.
- Oil reading is available.
- Oil reading is zero or greater.

The analysis excludes:

- SHUT_IN records.
- Records with missing oil readings.
- Records with negative oil readings.

A missing water reading does not exclude a record from oil-only calculations. However, it must be considered in calculations involving both oil and water.

Zero values are retained because zero is a valid measured value, not a missing reading.

## Conclusion

The analysis identifies the highest oil observations, calculates each valid observation's contribution to its well's total oil, and compares oil totals across fields and wells.




## Conclusion

The analysis identifies the highest oil observations, calculates each valid observation's contribution to its well's total oil, and compares oil totals across fields and wells.
