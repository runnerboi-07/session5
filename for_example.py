# sum first 10 numbers
sum = 0
for num in range(1,101): # last one is excluded, so it goes from 1 to 100
    sum = sum + num
print(sum)

# print multiplication table
for i in range(1,11): # last one is excluded, so it goes from 1 to 100
    for j in range (1,11):
        print(f"{i} x {j} = {i*j}")
    print("") # new line b/w blocks

# rewrite using while loop
sum = 0
num = 0
while num < 10: # because we start from zero
    num = num + 1
    sum += num # same as sum = sum + num
print(sum)
