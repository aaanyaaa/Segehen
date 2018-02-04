import csv
import datetime
import peewee


DATABASE = peewee.SqliteDatabase('sagehen.db')


class HourData(peewee.Model):
    date_time = peewee.DateTimeField()
    solar_rad = peewee.CharField(
        verbose_name="TOTAL SOLAR RAD (K W-hr/m^2)",
        max_length=225,
    )
    wind_ave = peewee.CharField(
        verbose_name="AVE WIND SPEED (m/s)",
        max_length=225,
    )
    wind_dir = peewee.CharField(
        verbose_name="V. WIND DIR (Deg)",
        max_length=225,
    )
    wind_max = peewee.CharField(
        verbose_name="MAX WIND SPEED (m/s)",
        max_length=225,
    )
    temp_ave = peewee.CharField(
        verbose_name="AIR TEMP AVE (Deg C)",
        max_length=225,
    )
    temp_max = peewee.CharField(
        verbose_name="AIR TEMP MAX (Deg C)",
        max_length=225,
    )
    temp_min = peewee.CharField(
        verbose_name="AIR TEMP MIN (Deg C)",
        max_length=225,
    )
    soil_tave = peewee.CharField(
        verbose_name="SOIL TEMP AVE (Deg C)",
        max_length=225,
    )
    soil_tmax = peewee.CharField(
        verbose_name="SOIL TEMP MAX (Deg C)",
        max_length=225,
    )
    soil_tmin = peewee.CharField(
        verbose_name="SOIL TEMP MIN (Deg C)",
        max_length=225,
    )
    rh_ave = peewee.CharField(
        verbose_name="RELATIVE HUMIDITY AVE (%)",
        max_length=225,
    )
    rh_max = peewee.CharField(
        verbose_name="RELATIVE HUMIDITY MAX (%)",
        max_length=225,
    )
    rh_min = peewee.CharField(
        verbose_name="RELATIVE HUMIDITY MIN (%)",
        max_length=225,
    )
    dew_pt = peewee.CharField(
        verbose_name="DEW PT. (Deg C)",
        max_length=225,
    )
    wet_bulb = peewee.CharField(
        verbose_name="WET BULB (Deg C)",
        max_length=225,
    )
    pressure = peewee.CharField(
        verbose_name="BARO. PRESS. (mb)",
        max_length=225,
    )
    snow = peewee.CharField(
        verbose_name="SNOW DEPTH (mm)",
        max_length=225,
    )
    precip = peewee.CharField(
        verbose_name="TOTAL PRECIP (mm)",
        max_length=225,
    )

    class Meta:
        database = DATABASE
    
    def __str__(self):
        return self.date_time.strftime("%Y-%m-%d %H:%M")
    

def connect_and_create_tables():
    DATABASE.connect()
    DATABASE.create_tables([HourData], safe=True)
    DATABASE.close()


def build_db():
    with open('SAGEHEN_1APR1997-14DEC2017.csv') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            date_str = row['DATE'] + " " + row['HOUR OF DAY ENDING AT L.S.T']
            HourData.create(
                date_time=datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M"),
                solar_rad=row["TOTAL SOLAR RAD (K W-hr/m^2)"],
                wind_ave=row["AVE WIND SPEED (m/s)"],
                wind_dir=row["V. WIND DIR (Deg)"],
                wind_max=row["MAX WIND SPEED (m/s)"],
                temp_ave=row["AIR TEMP AVE (Deg C)"],
                temp_max=row["AIR TEMP MAX (Deg C)"],
                temp_min=row["AIR TEMP MIN (Deg C)"],
                soil_tave=row["SOIL TEMP AVE (Deg C)"],
                soil_tmax=row["SOIL TEMP MAX (Deg C)"],
                soil_tmin=row["SOIL TEMP MIN (Deg C)"],
                rh_ave=row["RELATIVE HUMIDITY AVE (%)"],
                rh_max=row["RELATIVE HUMIDITY MAX (%)"],
                rh_min=row["RELATIVE HUMIDITY MIN (%)"],
                dew_pt=row["DEW PT. (Deg C)"],
                wet_bulb=row["WET BULB (Deg C)"],
                pressure=row["BARO. PRESS. (mb)"],
                snow=row["SNOW DEPTH (mm)"],
                precip=row["TOTAL PRECIP (mm)"],
            )


if __name__ == "__main__":
    connect_and_create_tables()
    build_db()
