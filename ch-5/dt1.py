marks = {
    'Rachna' : 75,
    'Harsh'  : 85,
    'Daxata' : 95
}

print(marks, type(marks))
print("length of dict. : ", len(marks))

print(marks.keys())
print(marks.values())

#update
marks.update({"Harsh" : 99, 'Jagruti': 100})
print(marks)

#get method
print(marks.get('Rachna'))