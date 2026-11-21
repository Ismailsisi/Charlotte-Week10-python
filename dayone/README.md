# NumPy Sensor Laboratory

## Setup

Install the required package:

    python -m pip install -r requirements.txt

## Run the Script

Run the following command from the dayone folder:

    python numpy_sensor_lab.py

## Sensor Channels and Units

The sensor dataset contains four measurement channels:

- Pressure: psi
- Temperature: Fahrenheit (°F)
- Vibration: mm/s
- Flow: barrels per day (bpd)

Pressure is converted from psi to kPa, and temperature is converted from Fahrenheit to Celsius during processing.

## Missing-Value Policy

Blank numeric CSV fields are represented using `np.nan`.

Functions such as `np.nanmean` and `np.nanmax` ignore missing values during calculations. Missing readings are not treated as zero.

## Results and Interpretation

- Total observations: 12
- High-pressure readings: 4
- High-vibration readings: 4
- Missing pressure readings: 1
- Missing flow readings: 1
- Average pressure: 3363.64 psi
- Maximum pressure: 3900.00 psi
- Average flow: 442.73 bpd

WELL-13 has the highest average pressure, while WELL-12 has the lowest average pressure.

The results show why handling missing sensor readings correctly is important when analysing drilling measurements.
