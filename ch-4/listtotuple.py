# list to tuple

l1 = ['one','two','three', 'two']
s1 = tuple(l1)
print(s1)

#multiple datatype

t1 = (1,'one',1.5)
print(t1)

#concate two tuple to one

t2 = ('Hello, there!.....')
t3 = ('How are you ?')

t4 = t2 + t3
print(t4)

# access first value

n = ('Apple','Mango','Orange')
firstvalue = n[0]
print("First index of tuple : ", firstvalue)
