# 9. Write a Python program to multiply all the items in a dictionary.
d = {'a': 10, 'b': 20, 'c': 30}
result = 1
for i in d.values():
    result *= i
print(result)