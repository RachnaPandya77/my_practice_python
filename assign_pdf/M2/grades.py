# Write a Python program to calculate grades based on percentage using if-else ladder.

total = 0

for i in range(1,5):
    mark = int(input(f"Enter mark for sub {i}: "))
    total += mark

print("Total : ", total)

pr = total / 4
print("percentage: ",pr)

if pr >= 90:
    grade = 'A'

elif pr >=75:
    grade = 'B'

elif pr >= 65:
    grade = 'C'

else:
    grade = 'D'

print("Grade: ", grade)
