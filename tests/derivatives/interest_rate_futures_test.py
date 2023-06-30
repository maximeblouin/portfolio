import pytest
from datetime import datetime
import src_py.derivatives.interest_rate_futures as bonds

def test_calculate_accrued_interest():
    """
    Unit test for calculate_accrued_interest function.
    """
    settlement_date = datetime(2017, 8, 8)
    issue_date = datetime(2017, 7, 7)
    maturity_date = datetime(2018, 1, 7)
    face_value = 100.0
    coupon_rate = 7.0

    # U.S. Treasury bond
    interest_accrued = bonds.calculate_accrued_interest(
        settlement_date = settlement_date,
        issue_date = issue_date,
        maturity_date = maturity_date,
        face_value = face_value,
        coupon_rate = coupon_rate,
        is_corporate = False)

    expected_accrued_interest = 0.6087  # Expected accrued interest

    assert pytest.approx(interest_accrued, abs=1e-4) == expected_accrued_interest

    # U.S. Corporate bond
    interest_accrued = bonds.calculate_accrued_interest(
        settlement_date = settlement_date,
        issue_date = issue_date,
        maturity_date = maturity_date,
        face_value = face_value,
        coupon_rate = coupon_rate,
        is_corporate = True)

    expected_accrued_interest = 0.6028  # Expected accrued interest

    assert pytest.approx(interest_accrued, abs=1e-4) == expected_accrued_interest
