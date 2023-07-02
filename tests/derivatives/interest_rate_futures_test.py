"""
Module: interest_rate_futures_tests

This module contains unit tests for the interest_rate_futures module in the derivatives package.
It includes tests for calculating accrued interest for U.S. Treasury bonds and
U.S. Corporate bonds.

"""
from datetime import datetime
import pytest
import src_py.derivatives.interest_rate_futures as bonds

def test_calculate_accrued_interest_us_treasury_bond():
    """
    Unit test for calculate_accrued_interest_us_treasory_bond function.
    """

    # U.S. Treasury bond
    interest_accrued = bonds.calculate_accrued_interest_us_treasury_bond(
        settlement_date = datetime(2017, 8, 8),
        issue_date = datetime(2017, 7, 7),
        maturity_date = datetime(2018, 1, 7),
        face_value = 100.0,
        coupon_rate = 7.0)

    expected_accrued_interest = 0.6087  # Expected accrued interest

    assert pytest.approx(interest_accrued, abs=1e-4) == expected_accrued_interest

def test_calculate_accrued_interest_us_corporate_bond():
    """
    Unit test for calculate_accrued_interest_us_corporate_bond function.
    """

    # U.S. Corporate bond
    interest_accrued = bonds.calculate_accrued_interest_us_corporate_bond(
        settlement_date = datetime(2017, 8, 8),
        issue_date = datetime(2017, 7, 7),
        maturity_date = datetime(2018, 1, 7),
        face_value = 100.0,
        coupon_rate = 7.0)

    expected_accrued_interest = 0.6028  # Expected accrued interest

    assert pytest.approx(interest_accrued, abs=1e-4) == expected_accrued_interest
