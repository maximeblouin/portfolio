import pandas as pd


def load_stock_prices():
    prices = pd.read_csv('../data/stock_prices.csv',
                         names=['ticker', 'date', 'open', 'high', 'low',
                                'close', 'volume', 'adj_close', 'adj_volume'])
    return prices

def load_price_volatility():
    """

    Data Model

    Columns | DataType | Description
    ------- | -------- | -----------
    price | decimal | .
    date | date | .
    ticker | string | .

    :return:
    """
    filename = '../data/prices_volatility.csv'

    return pd.read_csv(filename, parse_dates=['date'])


def load_stock_prices(symbol):
    data = pd.read_csv("../data/{}.csv".format(symbol))

    return data


def load_eod_quotemedia_value_filter(filename, values, symbols):
    data = load_eod_quotemedia_all(filename)
    data = data[data['ticker'].isin(symbols)]
    data = data.reset_index().pivot(index='date', columns='ticker', values=values)

    return data


def load_eod_quotemedia_value(filename, values):
    data = pd.read_csv("../data/{}.csv".format(filename), parse_dates=['date'], index_col=False)
    data = data.reset_index().pivot(index='date', columns='ticker', values=values)

    return data


def load_eod_quotemedia_all(filename):
    return pd.read_csv("../data/{}.csv".format(filename))


def csv_to_close(csv_filepath, field_names):
    """ It reads in data from a csv file and produces a DataFrame with close data.

    :param csv_filepath: The name of the csv file to read
    :type csv_filepath: str

    :param field_names: The field names of the field in the csv file
    :type field_names: list of str

    :return: Close prices for each ticker and date
    :rtype: DataFrame
    """

    return pd.read_csv(csv_filepath, names=field_names).pivot(index='date', columns='ticker', values='close')
