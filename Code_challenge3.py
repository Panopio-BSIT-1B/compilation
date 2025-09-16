print("GOOD DAY!")
name = input("What is your name?: ")
fee = eval(input("what is your fare fee?: "))
if_student = input("Are you a student?: (yes/no) ")

if if_student == 'yes':
    discount = fee * 0.20
    discounted = fee - discount
    print("\nHello",name, "You have a discount")
    print("Your discounted fare fee is:",discounted)
else:
    print("\nHello",name)
    print("Your fare fee is:",fee)