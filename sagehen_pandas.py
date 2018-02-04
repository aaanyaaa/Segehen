import pandas as pd
import sqlite3


DATEBASE = sqlite3.connect("sagehen.db")


def year_search(start_yr, end_yr):
    """
    Returns a Pandas DataFrame with rows matching the specified year range
    """
    return pd.read_sql(
        "SELECT * FROM hourdata WHERE date_time >= '{}-01-01' AND date_time <= '{}-12-31';".format(start_yr, end_yr),
        con=DATEBASE
    )


def date_search(start_date, end_date):
    """
    Returns a Pandas DataFrame with rows matching the specified date range
    """
    return pd.read_sql(
        "SELECT * FROM hourdata WHERE date_time >= '{}' AND date_time <= '{}';".format(start_date, end_date),
        con=DATEBASE
    )
