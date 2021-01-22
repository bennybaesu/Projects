import functions

while True:
    print("----------------------------")
    print("WELCOME TO GRADE MANAGER")
    print("----------------------------")
    print("\t------")
    print("\t MENU")
    print("\t------")
    print("(1) - Weighted Grade Calculator")
    print("(2) - GPA Calculator")
    print("(3) - Final Grade Calculator")
    print("(4) - Quit")

    while True:
        try:
            choice = int(input("Enter menu option: "))
            if choice < 1 or choice > 4:
                raise ValueError
            break
        except ValueError:
            print("That menu choice is not an option. Please try again.")

    if choice == 1:
        functions.weighted()
    elif choice == 2:
        print("That function doesn't exist yet. Coming soon.")
    elif choice == 3:
        print("That function doesn't exist yet. Coming soon.")
    elif choice == 4:
        break
