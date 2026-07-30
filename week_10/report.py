def print_report(
    name,
    employee_id,
    basic_salary,
    allowance,
    overtime_hours,
    years_service,
    gross,
    epf_amount,
    socso_amount,
    net
):
    print("\n=========== SALARY REPORT ===========")

    print(f"Employee Name : {name}")
    print(f"Employee ID   : {employee_id}")

    print("------------------------------------")

    print(f"Basic Salary  : RM {basic_salary:.2f}")
    print(f"Allowance     : RM {allowance:.2f}")
    print(f"Overtime Pay  : RM {overtime_hours*25:.2f}")

    if years_service > 3:
        print("Service Reward: RM 500.00")
    else:
        print("Service Reward: RM 0.00")

    print("------------------------------------")

    print(f"Gross Salary  : RM {gross:.2f}")
    print(f"EPF (11%)     : RM {epf_amount:.2f}")
    print(f"SOCSO (0.5%)  : RM {socso_amount:.2f}")

    print("------------------------------------")

    print(f"Net Salary    : RM {net:.2f}")

    print("====================================")