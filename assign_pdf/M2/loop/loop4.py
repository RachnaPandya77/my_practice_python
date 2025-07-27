# Calculate the sum of all numbers from 1 to a given number (e.g., 10) 
# using a for loop. 


n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("The sum of numbers: ", total)

