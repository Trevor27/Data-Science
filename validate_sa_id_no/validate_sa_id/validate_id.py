from datetime import datetime


def length(id_no):
    return len(str(id_no)) == 13


def check_if_digits(id_no):
    return id_no.isdigit()


def constant(id_no):
    return id_no[-2] == "8"


def check_date_of_birth(id_no):
    year = id_no[0:2]
    month = id_no[2:4]
    day = id_no[4:6]

    date_one = f"19{year}/{month}/{day}"
    date_two = f"20{year}/{month}/{day}"
    format_date = "%Y/%m/%d"
    try:
        if datetime.strptime(date_one, format_date) or datetime.strptime(
            date_two, format_date
        ):
            return True
    except:
        return False


def gender(id_no):
    gender = id_no[6:10]
    if 0 < int(gender) <= 9999:
        return True
    return False


def citizenship(id_no):
    citizenship = id_no[10:11]
    if int(citizenship) <= 1:
        return True
    return False


def checksum(id_no):
    id_length = len(id_no)
    digit_sum = 0
    second_number = False

    for number in range(id_length - 1, -1, -1):
        digits = ord(id_no[number]) - ord("0")

        if second_number == True:
            digits = digits * 2
        digit_sum += digits // 10
        digit_sum += digits % 10
        second_number = not second_number

    if digit_sum % 10 == 0:
        return True
    return False

def validation(id_no):
    if (
        length(id_no) == True
        and check_if_digits(id_no) == True
        and check_date_of_birth(id_no) == True
        and gender(id_no) == True
        and constant(id_no) == True
        and citizenship(id_no) == True
        and checksum(id_no) == True
    ):
        return True
    return False
