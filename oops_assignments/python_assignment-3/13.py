# 13. Write a Python program to remove duplicates from Dictionary.
d = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
new_dict = {}
for i, j in d.items():
    if j not in new_dict.values():
        new_dict[i] = j
print("Dictionary after removing duplicates:", new_dict)