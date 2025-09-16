

sum = 0
for Value in range(8):
    love_value = eval(input("Place any value here: "))
    if love_value % 2 != 0:
        sum = sum + love_value
print("The sum of the odd number is:", sum)