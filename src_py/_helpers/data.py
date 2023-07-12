"""
This module provides functions for loading and manipulating stock price data using pandas.

"""

import pandas as pd


def load_stock_prices(csv_path):
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

    header = ['ticker', 'date', 'open', 'high', 'low', 'close',
              'volume', 'adj_close', 'adj_volume']

    return pd.read_csv(
        filepath_or_buffer=csv_path,
        names=header)


def csv_to_close(data):
    """
    Reads data from a csv file and returns a DataFrame with close data.

    :param data: DataFrame with close data
    :type data: pd.DataFrame
    :return: Close prices for each ticker and date
    :rtype: pd.DataFrame
    """

    return data.pivot(index='date', columns='ticker', values='close')
