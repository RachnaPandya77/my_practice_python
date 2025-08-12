# largee , small , sum

n = [55,1,85,77,98,34,52,44,32,56]

#initialize

large = n[0]
small = n[0]

for num in n:
    if num > large:
        large = num
    if num < small:
        small = num

print("Largest num : ", large)
print("Smallest num : ", small)

print(sum(n))