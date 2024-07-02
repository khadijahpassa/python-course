number1 = 14
number2 = 6

print(number1==number2) # False
print(number1>number2) # True
print(number1<number2) 
print(number1>=number2)
print(number1<=number2)
print(number1!=number2)

print ("Logical Operator")
print (number1 == 14 and number2 > 10)
print (number1 == 14 or number2 > 10)
print (not number1 > 14)

print ("Identity Operator")
num1 = 15
num2 = 14
num3 = 14
num4 = "15"

print(num1 is num4)
print(num2 is num3)
print(num1 is not num4)

print ("Membership Operator")
letter = "a"
words = "Hello World"
print(letter in words)

number = 10
numbers = [1, 2, 3, 4]
print(number not in numbers)
