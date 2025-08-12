'''Write a Python function that takes two lists and returns true if they have
at least one common member. '''

l1 = ['one','two','three']
l2 = ['four','one','five']

result = bool(set(l1) & set(l2))
print(result)