from food_order import calculate_total


def main():
    try:
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))

        total = calculate_total(price, quantity)

        if isinstance(total, (int, float)):
            print(f"Total Payment = RM {total:.2f}")
        else:
            print(f"Error: {total}")

    except ValueError:
        print("Invalid input! Please enter numerical values.")


if __name__ == "__main__":
    main()