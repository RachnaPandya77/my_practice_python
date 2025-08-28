"""
  *
 ***
*****
"""

n = int(input("Enter n : "))
for i in range(1, n + 1):
    print(" " * (n - i), end='')  # print space
    print("*" * (2*i-1), end='')
    print("")

"""
2*i-1
2*1-1 = 1
2*2-1 = 3
2*3-1 = 4
"""