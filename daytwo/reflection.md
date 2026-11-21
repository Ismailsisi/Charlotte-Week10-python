\# Week 10 – Class 2 Pandas Homework



\## Part A – Conceptual Questions



\### 1. Difference between a Series and a DataFrame



A Series is like one column of data. For example, it can contain the daily oil production values from one well. A DataFrame is like a table with different columns. For example, it can contain well ID, status, oil production and water production for several wells.



\### 2. Why does CSV data need dtype checks after import?



We need to check the data types after importing a CSV because some values may be read in the wrong format. For example, oil production values may be read as text instead of numbers. If this happens, calculations may not work correctly. Checking the data types helps us know that the data is ready for analysis.



\### 3. Difference between `.loc` and `.iloc`



`.loc` is used to select data using row and column labels, while `.iloc` is used to select data using their positions.



Example:



```python

df.loc\[0, "oil\_bpd"]

```



This selects the oil production value from the row labelled 0.



```python

df.iloc\[0, 2]

```



This selects the value in the first row and third column.



\### 4. Difference between missing oil volume and zero production



A missing oil volume means the production reading was not recorded or is not available. A zero value means the well was checked but did not produce oil at that time. They are not the same because replacing a missing value with zero can make it look like the well stopped producing when we actually do not know its production.



\### 5. What does .copy() help protect?



`.copy()` helps us make a separate copy of a DataFrame before making changes to it. This protects the original data from being changed accidentally when we add new columns or make other modifications.



\## Part C – Interpretation



\### Effect of Missing Measurements on Management Reports



Missing measurements can affect the accuracy of oil production reports. When some readings are not available, management may not have the correct information about how a well is performing. This can also affect production averages and decisions about well operations.



For example, imagine a well produced 1,000 barrels of oil per day, but the sensor failed to record the following day's production. If we replace the missing reading with zero, the report will show that production dropped from 1,000 to zero barrels per day. Management may think the well has stopped producing, even though the actual production is unknown.



A zero value and a missing value should therefore be treated differently. Zero means the well was measured and produced no oil, while a missing value means the reading is not available. It is better to identify missing readings and investigate why they are missing instead of automatically replacing them with zero. This will help management make decisions based on more reliable production data.



\## Measurement Units



\- `oil\_bpd`: bbl/day (barrels per day)

\- `water\_bpd`: bbl/day (barrels per day)

\- `total\_liquid\_bpd`: bbl/day (barrels per day)

