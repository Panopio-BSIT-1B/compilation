isDirty = True
count = 0

while isDirty:
    confirm = input("Do you want to keep washing? (yes/no): ").lower()
    count += 1

    if confirm == 'yes':
        print("Continue washing.....")
        continue
    elif confirm == 'no':
        print("Washing stops....")
        isDirty = False
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

print(f"You've washed {count} times.")
