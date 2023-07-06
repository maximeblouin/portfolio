"""
This module provides functions for financial calculations.
"""


def calculate_expected_annual_rate(apr, compounding_periods_per_year):
    """
    Calculates the expected annual rate (EAR) given the APR and the compounding periods per year.

    :param apr: The Annual Percentage Rate (APR).
    :param compounding_periods_per_year: The number of compounding periods per year.

    :return: The expected annual rate (EAR).
    """
    return (1 + (apr / compounding_periods_per_year)) ** compounding_periods_per_year - 1


def calculate_present_value(future_payout, years, discount_rate):
    """
    Calculates the present value given the future payout, the year, and the discount rate.

    :param future_payout: The future payout or cash flow.
    :param years: The number of years.
    :param discount_rate: The discount rate.

    :return: The present value.
    """

    return future_payout / (1 + discount_rate) ** years


def find_best_investment(investments):
    """
    Calculates the present value of a list of investments based on their future payouts, years,
    and discount rates.

    :param investments: A list of investments. Each investment should be a dictionary with keys
                        'future_payout', 'years', and 'discount_rate'.

    :return: The investment with the highest present value.
    """
    max_present_value = -float('inf')
    best_investment = None

    for investment in investments:

        present_value = calculate_present_value(
            future_payout=investment['future_payout'],
            years=investment['years'],
            discount_rate=investment['discount_rate'])

        if present_value > max_present_value:
            max_present_value = present_value
            best_investment = investment

    return best_investment
