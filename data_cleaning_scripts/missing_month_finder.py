import csv


with open('../SAGEHEN_1APR1997-14DEC2017.csv') as CSVfile:
    readCSV = csv.reader(CSVfile, delimiter=",")
    set_year = 1997
    set_month = 4
    missing_year = []
    missing_month = []
    for row in readCSV:
        if row[0] != 'DATE':
            year, month, day = row[0].split('-')
            year = int(year)
            month = int(month)

            if set_month != month and set_month+1 != month:
                if set_month-11 == month:
                    set_month -= 11
                else:
                    print(year, "Month Change: {} --> {}".format(set_month, month))
                    set_month = month 
            elif set_month+1 == month:
                set_month += 1
