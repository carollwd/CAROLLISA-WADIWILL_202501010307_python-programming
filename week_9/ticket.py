def create_ticket():
    print("=== IT Helpdesk Ticket ===")

    name = input("Student Name: ")
    student_id = input("Student ID: ")
    issue = input("Issue: ")
    location = input("Location: ")

    # Validate priority
    while True:
        priority = input("Priority (High/Medium/Low): ").strip().lower()

        if priority == "high":
            technician = "Ahmad"
            break
        elif priority == "medium":
            technician = "Siti"
            break
        elif priority == "low":
            technician = "Ali"
            break
        else:
            print("Invalid priority! Please enter High, Medium, or Low.")

    # Optional: Capitalize priority for display
    priority = priority.capitalize()

    status = "Pending"

    return (
        name,
        student_id,
        issue,
        location,
        priority,
        technician,
        status
    )