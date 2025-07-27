# Write python program that swap two number with temp variable and without temp variable.

# with temp

a = 10
b = 20

temp = a
a = b
b = temp

print("a : ",a)
print("b : ",b)
print("\n")

# without temp

a = 30 
b = 40

a = a + b
b = a - b
a = a - b

