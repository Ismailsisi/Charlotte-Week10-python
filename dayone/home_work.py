from pathlib import Path
import csv
import numpy as np


DATA_FILE = Path(__file__).parent / 'data' / 'multiwell_sensor_readings.csv'


sample_ids = []
well_ids = []
pressure_values = []
vibration_values = []
flow_values = []


with open(DATA_FILE, 'r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        sample_ids.append(row['sample_id'])
        well_ids.append(row['well_id'])

        if row['pressure_psi'] == '':
            pressure_values.append(np.nan)
        else:
            pressure_values.append(float(row['pressure_psi']))

        if row['vibration_mm_s'] == '':
            vibration_values.append(np.nan)
        else:
            vibration_values.append(float(row['vibration_mm_s']))

        if row['flow_bpd'] == '':
            flow_values.append(np.nan)
        else:
            flow_values.append(float(row['flow_bpd']))


sample_ids = np.array(sample_ids)
well_ids = np.array(well_ids)

pressure = np.array(pressure_values)
vibration = np.array(vibration_values)
flow = np.array(flow_values)


# Question 5
flow_mask = flow > 400
vibration_mask = vibration > 6.0

combined_mask = flow_mask & vibration_mask

print('Question 5')
print('Sample IDs where flow exceeds 400 bpd and vibration exceeds 6.0 mm/s:')
print(sample_ids[combined_mask])


# Question 6
print('Question 6')
print('Pressure range per well (psi):')

pressure_ranges = {}

for well in np.unique(well_ids):
    well_mask = well_ids == well
    well_pressure = pressure[well_mask]

    pressure_range = np.nanmax(well_pressure) - np.nanmin(well_pressure)

    pressure_ranges[well] = pressure_range

    print(well, round(pressure_range, 2))


most_variable_well = max(pressure_ranges, key=pressure_ranges.get)
least_variable_well = min(pressure_ranges, key=pressure_ranges.get)

print(
    'Observation:',
    most_variable_well,
    'has the largest pressure range, while',
    least_variable_well,
    'has the smallest pressure range.'
)


# Question 7
pressure_ratios = pressure / 3500

ratios_above_one = pressure_ratios[pressure_ratios > 1]

print('Question 7')
print('Pressure ratios relative to 3500 psi:')
print(pressure_ratios)

print('Pressure ratios above 1:')
print(ratios_above_one)