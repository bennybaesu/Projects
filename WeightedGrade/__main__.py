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
        gradeInput = float(input("Enter percentage worth for '" + partition[i] + "': "))
        if 0.01 > gradeInput > 100:
            print(partition[i] + " cannot be worth " + gradeInput + "%. Try again.")
            valid = False
        else:
            valid = True
            worth.append(gradeInput / 100)


for i in range(0, len(partition)):
    valid = False
    while not valid:
        gradeInput = float(input("Enter percentage received for '" + partition[i] + "': "))
        if 0.00 > gradeInput:
            print("We sure hope you didn't get a negative worth. Try again.")
            valid = False
        else:
            valid = True
            received.append(gradeInput)


for i in range(0, len(partition)):
    weightedGrade += (received[i] * worth[i])


print("Your final grade is: " + str(weightedGrade) + "%\n")
