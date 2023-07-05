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
    present_value = future_payout / (1 + discount_rate) ** years
    return present_value
