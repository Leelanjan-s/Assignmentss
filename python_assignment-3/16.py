# 16. Write a Python program to find the highest 3 values in a dictionary.
d = {'a': 10, 'b': 40, 'c': 30, 'd': 50}
print(sorted(d.values(), reverse=True)[:3])
