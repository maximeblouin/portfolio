class bg_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def assert_equals(a, b):
    res = a == b
    if type(res) is bool:
        if not res:
            print(f"Error: {bg_colors.FAIL} \"{a}\" is not \"{b}\" {bg_colors.ENDC}")
            return
    else:
        if not res.all():
            print(f"Error: {bg_colors.FAIL} \"{a}\" is not \"{b}\" {bg_colors.ENDC}")
            return

    print(f"{bg_colors.OKGREEN}Assert okay{bg_colors.ENDC}")