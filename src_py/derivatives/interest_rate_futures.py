from datetime import datetime
import QuantLib as ql

def calculate_accrued_interest(settlement_date, issue_date, maturity_date, face_value, coupon_rate, is_corporate=False):
    """
    Calculate the accrued interest for a bond.

    :param settlement_date: The settlement date of the bond. (Datetime)
    :param issue_date: The issue date of the bond. (Datetime)
    :param maturity_date: The maturity date of the bond. (Datetime)
    :param face_value: The face value or principal amount of the bond. (float)
    :param coupon_rate: The coupon rate of the bond as a percentage. (float)
    :param is_corporate: Specifies if the bond is a corporate bond. Default is False. (bool)

    :return: The accrued interest of the bond as a percentage of the face value. (float)
    """

    # Convert settlement_date, issue_date, and maturity_date to ql.Date objects
    settlement_date = ql.Date(settlement_date.day, settlement_date.month, settlement_date.year)
    issue_date = ql.Date(issue_date.day, issue_date.month, issue_date.year)
    maturity_date = ql.Date(maturity_date.day, maturity_date.month, maturity_date.year)

    # Create a calendar and day-count convention based on the settlement date
    calendar = ql.UnitedStates(ql.UnitedStates.Settlement)
    day_count = ql.Thirty360(ql.UnitedStates.Settlement) if is_corporate else ql.ActualActual(ql.UnitedStates.Settlement)

    # Calculate the number of calendar days between issue date and settlement date
    days_issue_to_settlement = day_count.dayCount(issue_date, settlement_date)
    print(f"Calendar days between {issue_date} and {settlement_date}: {days_issue_to_settlement} days")

    # Calculate the number of calendar days between issue date and maturity date
    days_issue_to_maturity = day_count.dayCount(issue_date, maturity_date)
    print(f"Calendar days between {issue_date} and {maturity_date}: {days_issue_to_maturity} days")
    
    # Set up the bond schedule
    tenor = ql.Period(ql.Semiannual)
    schedule = ql.Schedule(issue_date, maturity_date, tenor, calendar,
                           ql.Unadjusted, ql.Unadjusted, ql.DateGeneration.Backward, False)

    # Create the bond with settlement days set to 0
    bond = ql.FixedRateBond(0, face_value, schedule, [coupon_rate / 100], day_count)

    # Calculate the accrued interest as a percentage of the face value
    accrued_interest = ql.BondFunctions.accruedAmount(bond, settlement_date) / face_value * 100

    return accrued_interest
