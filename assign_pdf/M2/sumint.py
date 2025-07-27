'''Write a python program to sum of the first n positive integers.'''

n = int(input("Enter number : "))
total = 0

for i in range(1, n + 1):
    total += i


print(total)