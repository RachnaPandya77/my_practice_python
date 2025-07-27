# Write a Python program to count the occurrences of each word in a given sentence

txt = input("Enter string : ")

for ch in set(txt):
    print(ch, '=', txt.count(ch))


print("-----------------------------------")

