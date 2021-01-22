import grade


# WEIGHTED GRADE ____________________________________
def weighted():
    weightedGrade = 0
    partition = []
    worth = []
    received = []
    gradeInput = 0.00
    valid = False

    while True:
        if not valid:
            partitionInput = input("Enter an assignment grouping (eg. 'Homework', 'Exams'...): ")
            partition.append(partitionInput)
        inputC = input("(E)nter another assignment grouping OR (C)ontinue: ")
        if inputC == 'c' or inputC == 'C':
            valid = True
            break
        if inputC == 'e' or inputC == 'E':
            valid = False
        else:
            print("That is an invalid option. Try again.")
            valid = True

    print("\n")

    for i in range(0, len(partition)):
        valid = False
        while not valid:
            gradeInput = input("Enter percentage worth for '" + partition[i] + "': ")
            try:
                gradeInput = float(gradeInput)
            except:
                print("Please enter a numerical percentage value.")
                continue

            if 0.01 > gradeInput > 100:
                print(partition[i] + " cannot be worth " + gradeInput + "%. Try again.")
                valid = False
            else:
                valid = True
                worth.append(gradeInput / 100)

    print("\n")

    for i in range(0, len(partition)):
        valid = False
        while not valid:
            gradeInput = input("Enter percentage received for '" + partition[i] + "': ")
            try:
                gradeInput = float(gradeInput)
            except:
                print("Please enter a numerical percentage value.")
                continue

            if 0.00 > gradeInput:
                print("We sure hope you didn't get a negative worth. Try again.")
                valid = False
            else:
                valid = True
                received.append(gradeInput)

    for i in range(0, len(partition)):
        weightedGrade += (received[i] * worth[i])

    print("\nYour final grade is: " + str(weightedGrade) + "%")
    print("Letter Grade: " + grade.letterGrade(weightedGrade))
    # ____________________________________________________________________________

    # GPA CALCULATOR _____________________________________________________________


# noinspection PyBroadException
def cumulative():
    units = []
    received = []

    while True:
        num = input("Enter number of classes to compare to previous GPA: ")
        try:
            num = int(num)
        except:
            print("That is not a valid input. Try again")
            continue
        break

    for i in range(1, num + 1):
        while True:
            value = input("Enter number of units of class " + str(i) + ": ")
            try:
                value = float(value)
            except:
                print("That is not a valid input. Try again.")
                continue
            break

        units.append(value)

        while True:
            value = input("Enter letter grade received for class " + str(i) + ": ")
            value = value.upper()
            if value == 'A+':
                received.append(4.0)
            elif value == 'A':
                received.append(4.0)
            elif value == 'A-':
                received.append(3.7)
            elif value == 'B+':
                received.append(3.3)
            elif value == 'B':
                received.append(3.0)
            elif value == 'B-':
                received.append(2.7)
            elif value == 'C+':
                received.append(2.3)
            elif value == 'C':
                received.append(2.0)
            elif value == 'C-':
                received.append(1.7)
            elif value == 'D+':
                received.append(1.3)
            elif value == 'D':
                received.append(1.0)
            elif value == 'D-':
                received.append(0.7)
            elif value == 'F':
                received.append(0)
            else:
                print("Invalid input, try again.")
                continue
            break
    while True:
        previous_units = input("Enter previous total units: ")
        try:
            previous_units = float(previous_units)
        except:
            print("Invalid input. Try again.")
            continue
        break

    while True:
        previous_gpa = input("Enter previous GPA: ")
        try:
            previous_gpa = float(previous_gpa)
        except:
            print("Invalid input. Try again.")
            continue
        break


def gpa():
    print("\nOPTIONS:")
    print("1. Enter this semester's GPA versus cumulative.")
    print("2. Enter individual classes")

    while True:
        choice = input("Enter an option: ")
        try:
            choice = int(choice)
        except:
            print("That is not a valid option. Try again.")
            continue

        if choice == 1:
            cumulative()
            break
        elif choice == 2:
            print("Choice 2 selected")
            break
        else:
            print("That is not a valid option. Try again.")
