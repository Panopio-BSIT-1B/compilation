# the factorial program
number = eval(input("PLACE ANY NUMBER HERE: "))
sum = 1
for f in range(number, 0, -1):
    sum *= f
print("The factorial of", number, "is", sum)
