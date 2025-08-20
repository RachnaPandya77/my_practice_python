# prime number

n = int(input("Enter number: "))#7

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime Number")
            break
    else:
        print("Prime number")
else:
    print("Not Prime")

