"""Write a Python program to find a specific string in the list using a simple
for loop and if condition"""

alpha = ['a','b','c','d','e','f','g','h']
print(alpha)

search = input("Enter String to find : ")

for i in alpha:
    if i == search:
        print("Found")
        break

else:
    print("Not Found")
