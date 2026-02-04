# 10. Write a Python program to remove a key from a dictionary.
d = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
key_to_remove = 'c'
if key_to_remove in d:
    del d[key_to_remove]
print("Dictionary after removing key:", d) 