def check_computers():
    computers = []

    for number in range(1, 6):
        while True:
            status = input(f"Computer {number} Status (A/U/M): ").strip().upper()

            if status in ["A", "U", "M"]:
                computers.append(status)
                break
            else:
                print("Please enter A, U or M.")

    return computers


def count_available(computers):
    available = 0

    for status in computers:
        if status == "A":
            available += 1

    return available


def display_status(computers, available):
    print("\n========== LAB STATUS ==========")

    for number in range(1, 6):
        print(f"Computer {number}: {computers[number - 1]}")

    print("-------------------------------")
    print(f"Available Computers: {available}")
    print("================================")


def main():
    while True:
        computers = check_computers()

        available = count_available(computers)

        display_status(computers, available)

        while True:
            again = input(
                "\nPerform another monitoring cycle? (Y/N): "
            ).strip().upper()

            if again == "Y":
                break
            elif again == "N":
                print("Monitoring ended.")
                return
            else:
                print("Please enter Y or N.")


if __name__ == "__main__":
    main()