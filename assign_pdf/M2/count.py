'''Write a Python program to count the number of characters (character
frequency) in a string'''

'''
count() is a string method that returns the number of times a 
specific character or substring appears in a string.
'''

a = 'collection'

print(a.count('o'))

print("-------------------------")

str1 = input("Enter a string: ")

for ch in set(str1):
    print(ch, "=",str1.count(ch))