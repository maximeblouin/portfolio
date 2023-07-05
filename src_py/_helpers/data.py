"""
This module provides functions for loading and manipulating stock price data using pandas.
"""

import pandas as pd


def load_stock_prices():
    """
    Reads data from a CSV file and produces a DataFrame with close data.

    column names:
        ticker
        date
        open
        high
        low
        close
        volume
        adj_close
        adj_volume
    """

    return pd.read_csv(
        filepath_or_buffer='../../data/stock_prices.csv',
        names=['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'adj_close', 'adj_volume'])


def load_price_volatility():
    """
    Loads data from a CSV file and returns a DataFrame.

    Data Model:

    Columns | DataType | Description
    ------- | -------- | -----------
    price   | decimal  | -
    date    | date     | -
    ticker  | string   | -

    :return: DataFrame with price volatility data
    :rtype: pd.DataFrame
    """
    filename = '../data/prices_volatility.csv'

    return pd.read_csv(filename, parse_dates=['date'])


def load_eod_quotemedia_value_filter(filename, values, symbols):
    """
    Loads data from a CSV file, filters it by ticker symbols, and pivots the data.

    :param filename: The name of the CSV file to load
    :type filename: str
    :param values: The values to pivot the data on
    :type values: str
    :param symbols: The ticker symbols to filter the data on
    :type symbols: list of str
    :return: Pivoted data with filtered ticker symbols
    :rtype: pd.DataFrame
    """
    data = load_eod_quotemedia_all(filename)
    data = data[data['ticker'].isin(symbols)]
    data = data.reset_index().pivot(index='date', columns='ticker', values=values)

    return data


def load_eod_quotemedia_value(filename, values):
    """
    Loads data from a CSV file, pivots it based on ticker symbols and values, and
    returns a DataFrame.

    :param filename: The name of the CSV file to load
    :type filename: str
    :param values: The values to pivot the data on
    :type values: str
    :return: Pivoted data based on ticker symbols and values
    :rtype: pd.DataFrame
    """
    data = pd.read_csv(f"../data/{filename}.csv", parse_dates=['date'], index_col=False)
    data = data.reset_index().pivot(index='date', columns='ticker', values=values)

    return data


def load_eod_quotemedia_all(filename):
    """
    Loads data from a CSV file and returns a DataFrame.

    :param filename: The name of the CSV file to load
    :type filename: str
    :return: DataFrame with loaded data
    :rtype: pd.DataFrame
    """
    return pd.read_csv(f"../data/{filename}.csv")


def csv_to_close(csv_filepath, field_names):
    """
    Reads data from a csv file and returns a DataFrame with close data.

    :param csv_filepath: The name of the csv file to read
    :type csv_filepath: str
    :param field_names: The field names of the fields in the csv file
    :type field_names: list of str
    :return: Close prices for each ticker and date
    :rtype: pd.DataFrame
    """

    data = pd.read_csv(csv_filepath, names=field_names)

    return data.pivot(index='date', columns='ticker', values='close')
