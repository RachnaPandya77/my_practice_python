# Write a Python program to check if a number is prime using if_else.

num = int(input("Enter number: "))

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("not prime")
            break
    else:
        print('It is prime')
else:
    print("it is not prime")


