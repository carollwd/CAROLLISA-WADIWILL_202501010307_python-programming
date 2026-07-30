def get_employee():
    print("=== Employee Information ===")

    name = input("Employee Name : ")
    employee_id = input("Employee ID : ")

    basic_salary = float(input("Basic Salary (RM): "))
    allowance = float(input("Allowance (RM): "))

    overtime_hours = float(input("Overtime Hours : "))
    years_service = int(input("Years of Service : "))

    return (
        name,
        employee_id,
        basic_salary,
        allowance,
        overtime_hours,
        years_service
    )