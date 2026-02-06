# 10. Write a Python program to remove a key from a dictionary.
d = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
item = 'c'
if item in d:
    del d[item]
print("Dictionary after removing key:", d) 