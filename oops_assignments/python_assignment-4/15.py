# 5) Write a Python program to check whether a given string is number or not using Lambda.
string = "12345"
number = lambda s: s.isdigit()
if number(string):
    print("It is a number")
else:
    print("It is not a number")