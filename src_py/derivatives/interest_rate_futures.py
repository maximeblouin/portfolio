"""
This module provides function to calculate the accrued interest for a
U.S. bond using the QuantLib library.
"""

import QuantLib as ql


def calculate_accrued_interest_us_corporate_bond(settlement_date, issue_date, maturity_date,
                                                 face_value, coupon_rate):
    """
    Calculate the accrued interest for a U.S. corporate bond.

    :param settlement_date: The settlement date of the bond. (Datetime)
    :param issue_date: The issue date of the bond. (Datetime)
    :param maturity_date: The maturity date of the bond. (Datetime)
    :param face_value: The face value or principal amount of the bond. (float)
    :param coupon_rate: The coupon rate of the bond as a percentage. (float)

    :return: The accrued interest of the U.S. corporate bond as a percentage
    of the face value. (float)
    """

    # Convert settlement_date, issue_date, and maturity_date to ql.Date objects
    settlement_date = ql.Date(settlement_date.day, settlement_date.month, settlement_date.year)
    issue_date = ql.Date(issue_date.day, issue_date.month, issue_date.year)
    maturity_date = ql.Date(maturity_date.day, maturity_date.month, maturity_date.year)

    # Create a calendar and day-count convention based on the settlement date
    calendar = ql.UnitedStates(ql.UnitedStates.Settlement)

    day_count = ql.Thirty360(ql.UnitedStates.Settlement)

    # Set up the bond schedule
    tenor = ql.Period(ql.Semiannual)

    schedule = ql.Schedule(
        issue_date,
        maturity_date,
        tenor,
        calendar,
        ql.Unadjusted,
        ql.Unadjusted,
        ql.DateGeneration.Backward,
        False)

    # Create the bond with settlement days set to 0
    bond = ql.FixedRateBond(0, face_value, schedule, [coupon_rate / 100], day_count)

    # Calculate the accrued interest as a percentage of the face value
    accrued_interest = ql.BondFunctions.accruedAmount(bond, settlement_date) / face_value * 100

    return accrued_interest


def calculate_accrued_interest_us_treasury_bond(settlement_date, issue_date, maturity_date,
                                                face_value, coupon_rate):
    """
    Calculate the accrued interest for a U.S. Treasury bond.

    :param settlement_date: The settlement date of the bond. (Datetime)
    :param issue_date: The issue date of the bond. (Datetime)
    :param maturity_date: The maturity date of the bond. (Datetime)
    :param face_value: The face value or principal amount of the bond. (float)
    :param coupon_rate: The coupon rate of the bond as a percentage. (float)

    :return: The accrued interest of the bond as a percentage of the face value. (float)
    """

    # Convert settlement_date, issue_date, and maturity_date to ql.Date objects
    settlement_date = ql.Date(settlement_date.day, settlement_date.month, settlement_date.year)
    issue_date = ql.Date(issue_date.day, issue_date.month, issue_date.year)
    maturity_date = ql.Date(maturity_date.day, maturity_date.month, maturity_date.year)

    # Create a calendar and day-count convention based on the settlement date
    calendar = ql.UnitedStates(ql.UnitedStates.Settlement)

    day_count = ql.ActualActual(ql.UnitedStates.Settlement)

    # Set up the bond schedule
    tenor = ql.Period(ql.Semiannual)

    schedule = ql.Schedule(
        issue_date,
        maturity_date,
        tenor,
        calendar,
        ql.Unadjusted,
        ql.Unadjusted,
        ql.DateGeneration.Backward,
        False)

    # Create the bond with settlement days set to 0
    bond = ql.FixedRateBond(0, face_value, schedule, [coupon_rate / 100], day_count)

    # Calculate the accrued interest as a percentage of the face value
    accrued_interest = ql.BondFunctions.accruedAmount(bond, settlement_date) / face_value * 100

    return accrued_interest
