name = input("input your name here --> ")
print("++++++++++++++++++++++++")
print("ODD NUMBER SUMMATION, PRESS 0 TO STOP")

variable = True
sum = 0
odd = ""

while variable == True:
    num = eval(input("enter a number here --> "))

    if num % 2 == 1:   
        print("your number is odd, continue")
        sum += num
        odd += str(num) + " "
        continue

    elif num % 2 == 0:
        if num == 0:
            print("code stopped") 
            break
        else:
            print("your number is even, continue")  
    else:
        print("invalid input")
        continue

print(f"Hi {name}, the sum of all ODD numbers is {sum}")
print(f"Odd numbers detected included the ff: {odd}")
