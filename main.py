W_LOOP = True

prompt1 = "Please provide a the date in the format (yyyy,mm,dd): "
prompt2 = "Please provide another date in the format (yyyy, mm, dd): "
INTRO_PROMPT = "This program will prompt 2 messages that require actions. " \
               "You will need to give 2 dates in the (yyyy,mm,dd) format"
ERROR_MSG = "!INVALID INPUT! Please try again."
MONTH_ERROR_MSG = "Invalid input! You have given an invalid month."
DAY_ERROR_MSG = "Invalid input! You have given an invalid day"

print(INTRO_PROMPT)


# Asking for user for a valid input, if invalid keep asking
def INPUT_CHECKER(x):
    try:
        LIST: list[str] = x.split(",")
        YEAR_FL = int(LIST[0])
        MONTH_FL = int(LIST[1])
        DAY_FL = int(LIST[2])
        assert type(YEAR_FL) == int
        assert type(MONTH_FL) == int
        assert type(DAY_FL) == int
    except ValueError:
        print(ERROR_MSG)
        return False
    except IndexError:
        print(ERROR_MSG)
        return False
    if 0 < MONTH_FL <= 12:
        if MONTH_FL <= 7:
            if (MONTH_FL == 2 and 0 < DAY_FL <= 28) or (MONTH_FL % 2 == 0 and 0 < DAY_FL <= 30 and MONTH_FL != 2) \
                    or (not MONTH_FL % 2 == 0 and 0 < DAY_FL <= 31 and MONTH_FL != 2):
                return True
            else:
                print(DAY_ERROR_MSG)
                return False
        elif 7 < MONTH_FL <= 12:
            if (MONTH_FL % 2 == 0 and 0 < DAY_FL <= 31) or (MONTH_FL % 2 != 0 and 0 < DAY_FL <= 30):
                return True
            else:
                print(DAY_ERROR_MSG)
                return False
        else:
            print(MONTH_ERROR_MSG)
            return False
    else:
        print(MONTH_ERROR_MSG)
        return False


def month_to_day(lst):
    days = 0
    range_list = range(0, int(lst[1]))
    for x in range_list:
        if x == 2:
            days += 28
        elif x % 2 == 0:
            days += 30
        else:
            days += 31
    return days


def in_year_diff(lst1, lst2):
    # Find the difference of years from 2 given dates than
    year_diff_in_years = int(lst2[0]) - int(lst1[0])

    # Coverts year_diff_in_years into year_diff_in_days
    year_diff_in_days = year_diff_in_years * 365

    # Converts months, list[1], into days

    # Find the difference between 2 months in days
    day_diff_in_days = month_to_day(lst2) - month_to_day(lst1)

    # Adds difference between days to day_diff_in_days
    day_diff_in_days += int(lst2[2]) - int(lst1[2])

    # Adds year_diff_in_days to day_diff_in_days
    ANSWER = day_diff_in_days + year_diff_in_days

    return str(ANSWER) + " days"


while W_LOOP:
    while True:
        INPUT_1 = input(prompt1)
        if INPUT_CHECKER(INPUT_1):
            LIST_1 = INPUT_1.split(",")
            break

    while True:
        INPUT_2 = input(prompt2)
        if INPUT_CHECKER(INPUT_2):
            LIST_2 = INPUT_2.split(",")
            break

    print(in_year_diff(LIST_1, LIST_2) + ". Try some more dates!")
