"""Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero."""

a = int(input("Enter num: "))
b = int(input("Enter num: "))
c = int(input("Enter num; "))

if a == b or b == c or c == b:
    print("Two num are equal")
    print("0")

else :
    sum = a + b + c
    print(sum)