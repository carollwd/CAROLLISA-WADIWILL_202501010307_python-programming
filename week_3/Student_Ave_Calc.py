choice = "y"

# loop for "y"
while choice == "y":

    # input section
    quiz_1 = int(input("Enter Quiz 1 mark: "))
    quiz_2 = int(input("Enter Quiz 2 mark: "))
    quiz_3 = int(input("Enter Quiz 3 mark: "))

    # calculate average
    average = (quiz_1 + quiz_2 + quiz_3) / 3

    # display average
    print("Average mark:", average)

    # decision (pass/fail)
    if average >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

    # ask user if they want to continue
    choice = input("Continue? Select Y/N: ").lower()

print("Program Ended")