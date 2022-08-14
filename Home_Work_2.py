import math

# 1. Construct an integer from the string "123"
# 2. Construct a float from the integer 123
# 3. Construct an integer from the float 12.345

a = int('123')
b = float(a)
c = int(12.345)

print("Construct an integer from the string '123'", a, type(a), sep=" -> ")
print("Construct a float from the integer 123", b, type(b), sep=" -> ")
print("Construct an integer from the float 12.345", c, type(c), sep=" -> ")

# 4. Write a Python-script that detects the last 4 digits of a credit card
credit_card_number = "5486732058864471"

print()

print("Credit card number:", credit_card_number)
print("Last 4 digits of card number is", credit_card_number[12:], '\n')

# 5. Write a Python-script that calculates the sum of the digits of a three-digit number
a = str(input("Input 3 digit number: "))

sum = int(a[0]) + int(a[1]) + int(a[2])

print("Sum =", sum, '\n')

# 6. Write a program that calculates and displays the area of a triangle if its sides are known

print("Input three sides of triangle:")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

s = (a + b + c) / 2

S = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("S =", S, '\n')

# 7. *Write a Python-script that calculates the sum of the digits of a number
n = input("Input number: ")

l = len(n)
i = l - 1
sum = 0

while i >= 0:
    sum += int(n[i])
    i -= 1

print()

print("Sum of digits of the number is", sum, '\n')

# 8. *Determine the number of digits in a number
print("Number of digits in number is", l, '\n')

# 9. *Print the digits in reverse order
j = 0
k = l - 1
reverse_n = ""

while k >= 0:
    reverse_n += n[k]
    j += 1
    k -= 1

print("Digits in reverse oreder:", reverse_n)
