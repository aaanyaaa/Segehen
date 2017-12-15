# Sagehen Creek Field Station Climate Data and Web Scrapers
Includes files and Python scripts used to collect and clean the Sagehen Creek Field Station Climate Data from Apr 1997 - Dec 2017 

## Climate Data from APR 97 to DEC 17:
- Located in `SAGEHEN_1APR1997-14DEC2017.csv`
- `saved_terminal_output_OCT2002-DEC2017` includes notes on the missing dates from 2002 to 2017.

## Requirements:
To use any of the scripts in this repository you'll need to:
* Install all of the Python third party libraries listed in `requirements.txt`
* Have a version of Python 3 installed on your machine.
* Have Firefox installed.
* Place the `geckodriver` in your path (instructions below).

### Geckodriver Instructions
Run the following command while inside the directory with the `geckodriver`.
* `$ sudo mv geckodriver /usr/local/bin`

## `sagehen_scraper_<dates that it works with>.py`
Near the top of the files you'll find the following lines:
```python
# User Variables
start_year = 2002
start_month = "OCT"
end_year = 2017
end_month = "DEC"
```
You may adjust these accordingly to collect the data desired within the constraints of the scraper's date range.
