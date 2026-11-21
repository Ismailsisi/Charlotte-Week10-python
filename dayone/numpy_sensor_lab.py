
"""Charlotte Project Week 10 Class 1 — NumPy Sensor Arrays."""

from pathlib import Path
import csv
import numpy as np


DATA_FILE = Path(__file__).parent / 'data' / 'multiwell_sensor_readings.csv'

COLUMNS = (
    'pressure_psi',
    'temperature_f',
    'vibration_mm_s',
    'flow_bpd'
)


def load_numeric_sensor_matrix(csv_path=DATA_FILE):
    """Load identifiers and numeric sensor readings from CSV."""

    sample_ids = []
    well_ids = []
    numeric_rows = []

    with open(csv_path, 'r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            sample_ids.append(row['sample_id'])
            well_ids.append(row['well_id'])

            numeric_row = []

            for column in COLUMNS:
                value = row[column]

                if value == '':
                    numeric_row.append(np.nan)
                else:
                    numeric_row.append(float(value))

            numeric_rows.append(numeric_row)

    matrix = np.array(numeric_rows, dtype=float)

    return sample_ids, well_ids, matrix


def convert_units(matrix):
    """Convert pressure to kPa and temperature to Celsius."""

    pressure_kpa = matrix[:, 0] * 6.8947572932
    temperature_c = (matrix[:, 1] - 32) * 5 / 9

    processed_matrix = np.column_stack((
        pressure_kpa,
        temperature_c,
        matrix[:, 2],
        matrix[:, 3]
    ))

    return processed_matrix


def analyze_sensor_matrix(sample_ids, well_ids, matrix):
    """Filter and summarize sensor readings."""

    pressure = matrix[:, 0]
    vibration = matrix[:, 2]
    flow = matrix[:, 3]

    high_pressure_mask = pressure > 3500
    high_vibration_mask = vibration > 6.0

    high_pressure_count = np.count_nonzero(high_pressure_mask)
    high_vibration_count = np.count_nonzero(high_vibration_mask)

    high_pressure_samples = np.array(sample_ids)[high_pressure_mask]

    missing_pressure_count = np.count_nonzero(np.isnan(pressure))
    missing_flow_count = np.count_nonzero(np.isnan(flow))

    average_pressure = np.nanmean(pressure)
    maximum_pressure = np.nanmax(pressure)
    average_flow = np.nanmean(flow)

    well_pressure_averages = {}

    for well in np.unique(well_ids):
        well_mask = np.array(well_ids) == well
        well_pressure = pressure[well_mask]

        well_pressure_averages[well] = np.nanmean(well_pressure)

    report = {
        'high_pressure_count': high_pressure_count,
        'high_vibration_count': high_vibration_count,
        'high_pressure_samples': high_pressure_samples,
        'missing_pressure_count': missing_pressure_count,
        'missing_flow_count': missing_flow_count,
        'average_pressure_psi': average_pressure,
        'maximum_pressure_psi': maximum_pressure,
        'average_flow_bpd': average_flow,
        'well_pressure_averages': well_pressure_averages
    }

    return report


def main():
    sample_ids, well_ids, matrix = load_numeric_sensor_matrix()

    print('Matrix shape:', matrix.shape)
    print('Matrix ndim:', matrix.ndim)
    print('Matrix dtype:', matrix.dtype)
    print('Total elements:', matrix.size)

    print('First three rows:')
    print(matrix[:3])

    print('Pressure column (psi):')
    print(matrix[:, 0])

    processed_matrix = convert_units(matrix)

    print('Processed matrix:')
    print(processed_matrix)

    report = analyze_sensor_matrix(sample_ids, well_ids, matrix)

    print('High-pressure readings:', report['high_pressure_count'])
    print('High-vibration readings:', report['high_vibration_count'])

    print('High-pressure sample IDs:')
    print(report['high_pressure_samples'])

    print('Missing pressure entries:', report['missing_pressure_count'])
    print('Missing flow entries:', report['missing_flow_count'])

    print('Average pressure (psi):', f"{report['average_pressure_psi']:.2f}")
    print('Maximum pressure (psi):', f"{report['maximum_pressure_psi']:.2f}")
    print('Average flow (bpd):', f"{report['average_flow_bpd']:.2f}")

    print('Average pressure per well (psi):')

    for well, average in report['well_pressure_averages'].items():
        print(well, f"{average:.2f}")


if __name__ == '__main__':
    main()
