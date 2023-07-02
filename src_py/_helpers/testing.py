"""
Module providing color codes for terminal output.
"""

class BgColors:
    """
    Provides color codes for terminal output.

    Attributes:
        HEADER (str): Header color code.
        OKBLUE (str): Ok blue color code.
        OKCYAN (str): Ok cyan color code.
        OKGREEN (str): Ok green color code.
        WARNING (str): Warning color code.
        FAIL (str): Fail color code.
        ENDC (str): End color code.
        BOLD (str): Bold color code.
        UNDERLINE (str): Underline color code.
    """

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def get_all_colors():
        """
        Returns a list of all color codes available.

        :return: List of color codes.
        :rtype: List[str]
        """
        return [getattr(BgColors, attr) for attr in dir(BgColors) if not attr.startswith("__")]

    @classmethod
    def get_color_names(cls):
        """
        Returns a list of all color names available.

        :return: List of color names.
        :rtype: List[str]
        """
        return [attr for attr in dir(cls) if not attr.startswith("__")]

def assert_equals(actual, expected):
    """
    Asserts whether the actual value is equal to the expected value.

    :param actual: The actual value.
    :type actual: Any
    :param expected: The expected value.
    :type expected: Any

    :return: None
    """

    res = actual == expected
    if isinstance(res, bool):
        if not res:
            print(f"Error: {BgColors.FAIL} \"{actual}\" is not \"{expected}\" {BgColors.ENDC}")
            return
    else:
        if not res.all():
            print(f"Error: {BgColors.FAIL} \"{actual}\" is not \"{expected}\" {BgColors.ENDC}")
            return

    print(f"{BgColors.OKGREEN}Assert okay{BgColors.ENDC}")
