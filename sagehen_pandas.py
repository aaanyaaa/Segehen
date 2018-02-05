import pandas as pd
import sqlite3


DATEBASE = sqlite3.connect("sagehen.db")


def config_df(dataframe_obj):
    """
    Configures a Pandas DataFrame to a set of specifications
    """
    dataframe_obj.drop('id', axis=1, inplace=True)
    dataframe_obj['date_time'] = pd.to_datetime(
        dataframe_obj['date_time'],
        errors="coerce",
    )
    dataframe_obj.set_index(['date_time'], inplace=True)
    dataframe_obj = dataframe_obj.apply(pd.to_numeric, args=('coerce',))
    return dataframe_obj


def year_search(start_yr, end_yr):
    """
    Returns a Pandas DataFrame with rows matching the specified year range
    """
    results = pd.read_sql(
        "SELECT * FROM hourdata WHERE date_time >= '{}-01-01' AND date_time <= '{}-12-31';".format(start_yr, end_yr),
        con=DATEBASE
    )
    return config_df(results)


def date_search(start_date, end_date):
    """
    Returns a Pandas DataFrame with rows matching the specified date range
    """
    results = pd.read_sql(
        "SELECT * FROM hourdata WHERE date_time >= '{}' AND date_time <= '{}';".format(start_date, end_date),
        con=DATEBASE
    )
    return config_df(results)


def value_search(col, start_val, end_val):
    """
    Returns a Pandas DataFrame with the rows matching the specified value
    range within the specified column
    """
    results = pd.read_sql(
        "SELECT * FROM hourdata WHERE {} >= {} AND {} <= {} AND {} IS NOT NULL;".format(col, start_val, col, end_val, col),
        con=DATEBASE
    )
    return config_df(results)

