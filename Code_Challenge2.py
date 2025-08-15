deposite = eval(input("Enter aomunt to deposite -->",))
print ("Here is a breakdown of the deposite amount:")

thousand = deposite // 1000
deposite = deposite % 1000 
fivehundred = deposite // 500
deposite = deposite % 500
twohundred = deposite // 200
deposite = deposite % 200 
onehundred = deposite // 100
deposite = deposite % 100
fifty = deposite // 50
deposite = deposite % 50
twenty = deposite // 20
deposite = deposite % 20
ten = deposite // 10
deposite = deposite % 10
five = deposite // 5
deposite = deposite % 5
one = deposite // 1
deposite = deposite % 1

print(thousand,"-1000")
print(fivehundred,"-500")
print(twohundred,"-200")
print(onehundred,"-100")
print(fifty,"-50")
print(twenty,"-20")
print(ten,"-10")
print(one,"-1")