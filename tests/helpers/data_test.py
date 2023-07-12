"""
This module contains unit tests for the `load_stock_prices` function in the stock prices module.

"""

import pandas as pd
import pytest
from src_py._helpers import data


@pytest.mark.parametrize('expected_columns', [['ticker', 'date', 'open', 'high', 'low', 'close',
                                               'volume', 'adj_close', 'adj_volume']])
def test_load_stock_prices(expected_columns):
    """
    Test the `load_stock_prices` function.

    This test ensures that the function correctly loads the stock price data and returns a DataFrame
    with the expected column names.

    :param expected_columns: The expected column names in the DataFrame.
    """
    # Call the load_stock_prices function
    result = data.load_stock_prices(csv_path='data/stock_prices.csv')

    # Check if the loaded DataFrame has the expected column names
    assert list(result.columns) == expected_columns


def test_csv_to_close(stock_prices_fixture):
    """
    Test the `csv_to_close` function.

    This function compares the output of the `csv_to_close` function with the
    expected output DataFrame.

    The expected output DataFrame has the following structure:
    - Index: 'date'
    - Columns: 'ABC', 'EFG', 'XYZ'
    - Values: Close prices for respective stocks on different dates.

    Steps:
    1. Creates the expected output DataFrame.
    2. Sets the 'date' column as the index.
    3. Calls `csv_to_close` function with the sample input.
    4. Compares the output DataFrame with the expected output DataFrame.

    Raises an AssertionError if the output DataFrame doesn't match the expected output DataFrame.
    """

    # Create the data as a dictionary
    expected_output = {
        'date': ['2017-09-05', '2017-09-06', '2017-09-07', '2017-09-08',
                 '2017-09-11', '2017-09-12', '2017-09-13'],
        'ABC': [162.63, 161.13, 161.26, 158.05, 161.29, 161.09, 159.29],
        'EFG': [154.52, 154.45, 155.68, 155.86, 157.17, 156.71, 155.54],
        'XYZ': [63.95, 62.23, 60.46, 59.35, 58.24, 58.71, 60.33]
    }

    # Create the DataFrame
    expected_output = pd.DataFrame(expected_output)
    expected_output.set_index('date', inplace=True)
    expected_output.columns.name = 'ticker'

    # Call the function with the sample input
    output = data.csv_to_close(stock_prices_fixture)

    # Assert the output matches the expected output
    pd.testing.assert_frame_equal(output, expected_output)
