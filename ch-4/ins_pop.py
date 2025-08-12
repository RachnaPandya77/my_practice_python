#insert() pop()

data = ['First', 'second', 'Third', 'Forth', 'Fifth']

data.insert(2, 'sixth')
print(data)

data.pop(1)
print(data)

data.append('Red')
print(data)

'''data.extend('white')
print(data)'''

data.remove('Red')
print(data)

data.sort()
print(data)



d1 = [55, 4, 62, 11, 85, 46, 23, 78, 94, 1]

d1.reverse() 
print(d1)

d1.pop() # remove last
print(d1)

d1.extend(99)
print(d1)
