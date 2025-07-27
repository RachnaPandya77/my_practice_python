# Write a Python program to get the Factorial number of given number.

a = int(input("Enter number: "))
fact = 1

for i in range(1, a+1):
    fact*=i

print(fact)