number = int(input("enter a number: "))

print("multiplication table for:", number)

for table in range(1, 11):
    product = number * table
    print(number, "x", table, "=", product)
