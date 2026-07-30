OVERTIME_RATE = 25
BONUS = 500


def gross_salary(basic_salary, allowance, overtime_hours, years_service):
    overtime_pay = overtime_hours * OVERTIME_RATE

    reward = 0
    if years_service > 3:
        reward = BONUS

    gross = basic_salary + allowance + overtime_pay + reward
    return gross


def epf(gross):
    return gross * 0.11


def socso(gross):
    return gross * 0.005


def net_salary(gross):
    return gross - epf(gross) - socso(gross)