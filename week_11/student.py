def get_student():
    print("===== Computer Lab Access =====")

    while True:
        name = input("Student Name : ").strip()

        if name == "":
            print("Please enter your name.")
        elif not all(char.isalpha() or char.isspace() for char in name):
            print("Please enter a valid name.")
        else:
            break


    while True:
        student_id = input("Student ID   : ").strip()

        if student_id == "":
            print("Please enter your student ID.")
        elif not student_id.isdigit():
            print("Please enter a valid student ID.")
        else:
            break


    while True:
        registered = input("Registered for today's lab? (Y/N): ").strip().upper()

        if registered == "":
            print("Please enter Y or N.")
        elif registered not in ["Y", "N"]:
            print("Please enter Y or N.")
        else:
            break

    while True:
        lab_open = input("Is the lab open? (Y/N): ").strip().upper()

        if lab_open == "":
            print("Please enter Y or N.")
        elif lab_open not in ["Y", "N"]:
            print("Please enter Y or N.")
        else:
            break

    while True:
        computer_available = input("Computer Available? (Y/N): ").strip().upper()

        if computer_available == "":
            print("Please enter Y or N.")
        elif computer_available not in ["Y", "N"]:
            print("Please enter Y or N.")
        else:
            break

    return name, student_id, registered, lab_open, computer_available