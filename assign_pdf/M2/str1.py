'''Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string'''

str1 = "ABCD"
str2 = "XYZ"

newstr1 = str1[:2] + str2[1:]
newstr2 = str1[1:] + str2[0:1]

new = newstr1 + " " + newstr2

print(new)