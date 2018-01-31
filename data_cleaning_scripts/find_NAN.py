import csv

COLUMNS = [
    'TOTAL SOLAR RAD (K W-hr/m^2)',
    'AVE WIND SPEED (m/s)',
    'V. WIND DIR (Deg)',
    'MAX WIND SPEED (m/s)',
    'AIR TEMP AVE (Deg C)',
    'AIR TEMP MAX (Deg C)',
    'AIR TEMP MIN (Deg C)',
    'SOIL TEMP AVE (Deg C)',
    'SOIL TEMP MAX (Deg C)',
    'SOIL TEMP MIN (Deg C)',
    'RELATIVE HUMIDITY AVE (%)',
    'RELATIVE HUMIDITY MAX (%)',
    'RELATIVE HUMIDITY MIN (%)',
    'DEW PT. (Deg C)',
    'WET BULB (Deg C)',
    'BARO. PRESS. (mb)',
    'SNOW DEPTH (mm)',
    'TOTAL PRECIP (mm)',
]


def write_missing_data(line):
    with open('sagehen_missing_max_wind_speed.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(line)


with open('SAGEHEN_1APR1997-14DEC2017.csv') as CSVfile:
    readCSV = csv.DictReader(CSVfile, delimiter=",")
    missing_data = []
    for row in readCSV:
        if 'NAN' in row[COLUMNS[3]]:
            missing_data.append(row['DATE'])
    write_missing_data(sorted(set(missing_data)))
