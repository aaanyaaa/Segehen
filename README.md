# Sagehen Creek Field Station Climate Data and Web Scrapers
Includes files and Python scripts used to collect and clean the Sagehen Creek Field Station Climate Data from Apr 1997 - Dec 2017 

## Requirements:
To use any of the scripts in this repository you'll need to:
* Install all of the Python third party libraries listed in `requirements.txt`
* Have a version of Python 3 installed on your machine.
* Have Firefox installed.
* Place the `geckodriver` in your path (instructions below).

### Geckodriver Instructions
Run the following command while inside the directory with the `geckodriver`.
* `$ sudo mv geckodriver /usr/local/bin`

## `sagehen_scraper.py`
Near the top of the file you'll find the following lines:
```python
# User Variables
beginning_year = 1997
end_year = 2017
```
You may adjust these accordingly to collect the data desired.
