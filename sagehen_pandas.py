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


def column_adder(cols_wanted):
    """A helper function that adds the list of columns passed to it
    into a string object, seperated by commas
    """
    if not cols_wanted:
        select_cols = "*"
    else:
        select_cols = 'id,date_time'
        for column in cols_wanted:
            select_cols += "," + column
    return select_cols


def year_search(start_yr, end_yr, cols_wanted=[]):
    """Returns a Pandas DataFrame with rows matching the specified
    year range
    """
    select_cols = column_adder(cols_wanted)
    sql_query = "SELECT {0} FROM hourdata WHERE date_time >= '{1}-01-01' AND date_time <= '{2}-12-31';".format(select_cols, start_yr, end_yr)
    results = pd.read_sql(
        sql_query,
        con=DATEBASE,
    )
    return config_df(results)


def date_search(start_date, end_date, cols_wanted=[]):
    """Returns a Pandas DataFrame with rows matching the specified date
    range
    """
    select_cols = column_adder(cols_wanted)
    sql_query = "SELECT {0} FROM hourdata WHERE date_time >= '{1}' AND date_time <= '{2}';".format(select_cols, start_date, end_date)
    results = pd.read_sql(
        sql_query,
        con=DATEBASE,
    )
    return config_df(results)


def value_search(col, start_val, end_val, cols_wanted=[]):
    """
    Returns a Pandas DataFrame with the rows matching the specified value
    range within the specified column
    """
    if cols_wanted:
        cols_wanted.append(col)
    select_cols = column_adder(cols_wanted)

    sql_query = "SELECT {3} FROM hourdata WHERE {0} >= {1} AND {0} <= {2} AND {0} IS NOT NULL;".format(col, start_val, end_val, select_cols)
    print(sql_query)
    results = pd.read_sql(
        sql_query,
        con=DATEBASE
    )
    return config_df(results)


def iplot_labeler(g_title, x_axis, y_axis):
    """
    Creates a dictionary objects structured for Plotly's
    iplot layout parameter
    """
    return dict(
        title=g_title,
        xaxis=dict(title=x_axis),
        yaxis=dict(title=y_axis),
        )
