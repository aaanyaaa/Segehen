# Sagehen Creek Field Station Climate Data and Web Scrapers

Includes files and Python scripts used to collect and clean the Sagehen Creek Field Station Climate Data from Apr 1997 - Dec 2017

## Climate Data from APR 97 to DEC 17

- Located in `SAGEHEN_1APR1997-14DEC2017.csv`

***

## Running the Scripts

### Requirements

To use any of the scripts in this repository you'll need to:

- Install all of the Python third party libraries listed in `requirements.txt`
- Have a version of Python 3 installed on your machine.
- Have Firefox installed.
- Place the `geckodriver` in your path (instructions below).

### Geckodriver Instructions

Run the following command while inside the directory with the `geckodriver`.

- `$ sudo mv geckodriver /usr/local/bin`

### `sagehen_scraper_<dates that it works with>.py`

Near the top of the files you'll find the following lines:

```python
# User Variables
start_year = 2002
start_month = "OCT"
end_year = 2017
end_month = "DEC"
```

You may adjust these accordingly to collect the data desired within the constraints of the scraper's date range.

***

## Sagehen Data Column Changes

- Earliest available data: April 1997.
- Latest available data: December 2017.
- Months included, but w/o data(Used NAN for missing data): NOV 97, APR 05, MAY 05
- Numerous days with missing days throughout the data set (Used NAN for missing data)

### APR 1, 1997 Column Format

- Hour of Day Ending at L.S.T.
- Total Solar Rad. ºKW-hr/m^2
- Wind Ave. m/s
- Wind V.Dir. Deg.
- Air Temperature Mean Deg. C.
- Relative Humidity Mean Percent
- Dew Point Deg. C.
- Wet Bulb Deg. C.
- Baro. Press. mb.*

### Addition of Columns on July 1, 2000

- Addition of Wind Max. m/s
- Addition of Air Temperature Max Deg. C.
- Addition of Air Temperature Min Deg. C.
- Addition of Relative Humdity Max Percent
- Addition of Relative Humidity Min Percent

### Addition of Columns on Sept 1, 2001

- Addition of Snow Depth mm.

### Addition of Columns on Oct 1, 2002

- Soil Temperature Mean Deg. C.
- Soil Temperature Max Deg. C.
- Soil Temperature Min Deg. C.