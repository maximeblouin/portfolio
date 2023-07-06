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

    Source: CFA Institute Investment Foundations - Chapter 8 - Example 1

    A credit card charges interest at an APR of 15.24%, compounded daily.
    A bank pays 0.2% monthly on the average amount on deposit over the month.
    A loan is made with a 6.0% annual rate, compounded quarterly.
    Calculate EAR.
    """

    # Test a credit card which charges interest at an APR of 15.24%, compounded daily.
    expected_apr = tvm.calculate_expected_annual_rate(
        apr=0.1524,
        compounding_periods_per_year=365)
    assert round(expected_apr, 4) == 0.1646

    # Test a bank pays 0.2% monthly on the average amount on deposit over the month.
    expected_apr = tvm.calculate_expected_annual_rate(
        apr=0.002 * 12,
        compounding_periods_per_year=12)
    assert round(expected_apr, 4) == 0.0243

    # Test a loan made with a 6.0% annual rate, compounded quarterly.
    expected_apr = tvm.calculate_expected_annual_rate(
        apr=0.06,
        compounding_periods_per_year=4)
    assert round(expected_apr, 4) == 0.0614


def test_calculate_present_value():
    """
    Unit test for calculate_present_value function.

    Source: CFA Institute Investment Foundations - Chapter 8 - Example 2

    Part 1
    You are choosing between two investments of equal risk. You believe that given the risk,
    the appropriate discount rate to use is 9%. Your initial investment (outflow) for each is
    £500. One investment is expected to pay out £1,000 three years from now; the other investment
    is expected to pay out £1,350 five years from now. To choose between the two investments,
    you must compare the value of each investment at the same point in time.

    Part 2
    You are choosing between the same two investments, but you have reassessed their risks. You
    now consider the five-year investment to be more risky than the first and estimate that a 15%
    return is required to justify making this investment.

    """

    # Test the present value of £1,000 in three years discounted at 9%
    expected_pv = tvm.calculate_present_value(
        future_payout=1000,
        years=3,
        discount_rate=0.09)

    assert round(expected_pv, 2) == 772.18

    # Test the present value of £1,350 in five years discounted at 9%
    expected_pv = tvm.calculate_present_value(
        future_payout=1350,
        years=5,
        discount_rate=0.09)

    assert round(expected_pv, 2) == 877.41

    # Test the present value of £1,350 in five years discounted at 15%
    expected_pv = tvm.calculate_present_value(
        future_payout=1350,
        years=5,
        discount_rate=0.15)

    assert round(expected_pv, 2) == 671.19


def test_find_best_investment():
    """
    Unit test for calculate_present_value function.

    Source: CFA Institute Investment Foundations - Chapter 8 - Example 2

    Part 1
    You are choosing between two investments of equal risk. You believe that given the risk,
    the appropriate discount rate to use is 9%. Your initial investment (outflow) for each is
    £500. One investment is expected to pay out £1,000 three years from now; the other investment
    is expected to pay out £1,350 five years from now. To choose between the two investments,
    you must compare the value of each investment at the same point in time.

    Part 2
    You are choosing between the same two investments, but you have reassessed their risks. You
    now consider the five-year investment to be more risky than the first and estimate that a 15%
    return is required to justify making this investment.

    """

    investments = [
        {
            'future_payout': 1000,
            'years': 3,
            'discount_rate': 0.09
        },
        {
            'future_payout': 1350,
            'years': 5,
            'discount_rate': 0.09
        }
    ]

    # Call the function to get the best investment
    best_investment = tvm.find_best_investment(investments)

    # Assert that the best investment matches the expected result
    assert best_investment == {
        'future_payout': 1350,
        'years': 5,
        'discount_rate': 0.09
    }

    investments = [
        {
            'future_payout': 1000,
            'years': 3,
            'discount_rate': 0.09
        },
        {
            'future_payout': 1350,
            'years': 5,
            'discount_rate': 0.15
        }
    ]

    # Call the function to get the best investment
    best_investment = tvm.find_best_investment(investments)

    # Assert that the best investment matches the expected result
    assert best_investment == {
        'future_payout': 1000,
        'years': 3,
        'discount_rate': 0.09
    }
