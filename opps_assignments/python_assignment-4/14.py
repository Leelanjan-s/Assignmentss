# 4) Write a Python program to find if a given string starts with a given character using Lambda.
string = "Hello"
char = "H"
starts_with = lambda s, c: s.startswith(c)
if starts_with(string, char):
    print(f"The string starts with '{char}'")
else:
    print(f"The string does not start with '{char}'")
