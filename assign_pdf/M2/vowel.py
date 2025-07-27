# Write a Python program to test whether a passed letter is a vowel or not.

ch = input("Enter Alphabet: ").lower()

if ch in 'aeiou':
    print(f"{ch} is vowel")

else :
    print(f"{ch} NOT VOWEL")