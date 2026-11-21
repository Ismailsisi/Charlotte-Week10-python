# Engineering Reflection

Reliable handling of missing sensor readings is important in drilling analytics because sensors may sometimes fail to record measurements or produce incomplete data. If missing values are treated as zero, the analysis may produce misleading results and affect engineering decisions. Using `np.nan` to represent missing readings and functions such as `np.nanmean` allows calculations to use available valid measurements without treating missing data as real measurements.

Appropriate engineering units are equally important when analysing pressure, temperature, vibration and flow. Each measurement has a different unit and meaning. For example, pressure recorded in psi should not be confused with pressure in kPa, and temperature in Fahrenheit should be converted correctly when Celsius is required. Correct units make results easier to interpret and compare.

These practices are important when developing later data-quality pipelines because they help maintain accurate, consistent and reliable sensor data. They also support better identification of unusual readings and reduce the risk of incorrect conclusions during drilling operations.
