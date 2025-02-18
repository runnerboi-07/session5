# Q1 - What does the code print

# (a)
divisor = 3
for num in range(0, 12, 3): # Start at 0, go till 12 (excluding 12) and step/skip by 3
    print(num/divisor)
# Outputs are floats: 0.0, 1.0, 2.0, 3.0
# This means num values were: 0, 3, 6, 9

# (b)
for letter in 'Ahola':
    print(letter)
# Prints each letter of 'Ahola' individually in separate lines
# Iterates over the string

# (c)
num = 0
while num <= 5:
    print(num)
    num += 2
print("Out")
print(num)
# Prints 0, 2, 4 then 'Out' and 6
# This means that even though the while stops when num is no longer <= 5, it still adds 2 in the last iteration

# (d)
num = 0
count = 0
while num <= 19:
    if num % 3 == 0:
        count += 1
    num = num + 1
print("Numbers divisible by 3:", count)
# 7 numbers less than or equal to 19 are divisible by 3

# Q2 - Print the multiplication table 1-10 without duplicates (if a*b=c appears, then b*a=c should not)
mult = [] # Empty list that I can add each combination to
for i in range(1, 11):
    for j in range(1, 11):
        if f"{i}*{j}" and f"{j}*{i}" not in mult: # If to check list to see if combination has already been used
            print(f"{i} x {j} = {i * j}")
        mult.extend([f"{i}*{j}", f"{j}*{i}"]) # Add combination and reverse combination as well since they are equivalent
    print("\n")

# Q3 - Suppose you can only do additions. Write a program that reads two positive, integer numbers a and b. It computes a**b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

answer = a
for i in range(1,b):
    if b != 0:
     answer *= a
    else:
        answer = 1
print(answer)

# Q4 - Read an int number. Check if the number is a palindrome. (A palindrome number read backwards has the same value. Example of palindrome numbers: 123454321, 999, 1598951)
number = str(input('Enter a number: '))

if number == number[::-1]:
    print("This number is a palindrome")
else:
    print("Sorry, this number is not a palindrome")