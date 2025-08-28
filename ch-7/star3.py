'''
***
* *
***

'''

n = int(input("Enter n: "))

for i in range(1,n+1):
    if (i==1 or i==n):
        print("*"*n, end="")
    else:
        print("*",end="")
        print(" "* (n-2),end="")
        print("*",end="")
    print("")

'''
Lets take n = 5

Loop: for i in range(1, 6) → i = 1,2,3,4,5

Iteration 1 → i = 1

Condition: i == 1 or i == 5 → ✅ True

Executes: print("*"*5, end="") → *****

Then print("") moves cursor to new line.
op: *****
-----------------------------------------------
Iteration 2 → i = 2

Condition: i == 1 or i == 5 →  False

Goes to else:

print("*", end="") → prints *

print(" " * (5-2), end="") → " " * 3 → prints (3 spaces)

print("*", end="") → prints *

Then print("") moves cursor to new line.
op : *   *
'''