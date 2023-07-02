"""
This module contains unit tests for the time value of money calculations in
the quantitative_methods package.

It includes tests for the following functions:
- calculate_expected_annual_rate
- calculate_present_value
"""

import src_py.quantitative_methods.time_value_of_money as tvm


def test_calculate_expected_annual_rate():
    """
    Unit test for calculate_expected_annual_rate function.
    """
    assert round(tvm.calculate_expected_annual_rate(0.1524, 365), 4) == 0.1646
    assert round(tvm.calculate_expected_annual_rate(0.002 * 12, 12), 4) == 0.0243
    assert round(tvm.calculate_expected_annual_rate(0.06, 4), 4) == 0.0614


def test_calculate_present_value():
    """
    Unit test for calculate_present_value function.
    """
    assert round(tvm.calculate_present_value(1000, 3, 0.09), 2) == 772.18
    assert round(tvm.calculate_present_value(1350, 5, 0.09), 2) == 877.41
    assert round(tvm.calculate_present_value(1350, 5, 0.15), 2) == 671.19
