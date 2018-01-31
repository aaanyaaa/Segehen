import csv


missing_days = []

with open('../SAGEHEN_1APR1997-14DEC2017.csv') as CSVfile:
    readCSV = csv.reader(CSVfile, delimiter=",")
    set_day = 1
    set_month = 4
    set_year = 1997
    for row in readCSV:
        if row[0] != 'DATE':
            year, month, day = row[0].split('-')
            year = int(year)
            month = int(month)
            day = int(day)

            if set_day != day or set_month != month or set_year != year:
                if set_year+1 == year:
                    set_year += 1
                    set_month = 1
                    set_day = 1
                elif set_month+1 == month:
                    set_month += 1
                    set_day = 1
                else:
                    if set_day+1 != day:
                        # print(year, month, "day Change: {} --> {}".format(set_day, day))
                        missing_days.append([year, month, set_day+1, day]) 
                        set_day = day
                    else:
                        set_day += 1


            # if set_day != day and set_day+1 != day:
            #     if set_month+1 == month:
            #         set_month += 1
            #     elif set_year+1 == year:
            #         set_year += 1
            #     else:
            #         print(year, month, "day Change: {} --> {}".format(set_day, day))
            #         set_month = month
            #         set_year = year
            #     set_day = day
            # elif set_day+1 == day:
            #     set_day += 1
print(missing_days)