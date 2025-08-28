'''WAP to find student has passes or failed if it requires a total of 40% 
and at least 33%  in each subject to pass. Assume 3 subject and take marks as 
an input from the user '''

s1 = int(input("Enter Marks: "))
s2 = int(input("Enter Marks: "))
s3 = int(input("Enter Marks: "))
s4 = int(input("Enter Marks: "))

total = s1 + s2 + s3 + s4
print(total)

pr = total/4
print(pr)

if s1 < 33 or s2 < 33 or s3 < 33 or s4 < 33:
    print("Try Again(Bcoz less than 33 in one or more subject)")

elif pr < 40:
    print("Try Agian")

else :
    print("Pass")

