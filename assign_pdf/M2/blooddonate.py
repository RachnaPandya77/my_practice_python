# Write a Python program to check if a person is eligible to donate blood using a nested if.

age = int(input("Enter age :  "))

if age >=18:
    weight = int(input("Enter weight :  "))

    if weight >= 50:
        print("You are eligible to donate blood")
    else:
        print("You are not eligible to donate blood because your weight is less than 50 kg.")

else:
    print("You are not eligible to donate blood because your age is below 18.")
