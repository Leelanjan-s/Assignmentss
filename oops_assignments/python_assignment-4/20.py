# 10) Write a Python program to sort a given mixed list of integers and strings using lambda. 
# Numbers must be sorted before strings. 
# Original list: [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1] 
# Sort the said mixed list of integers and strings: [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']


# with lambda
mixed_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
sorted_list = sorted(mixed_list, key=lambda x: (isinstance(x, str), x))
print("Sorted mixed list:", sorted_list)

# without lambda
num=[]
string=[]
for i in mixed_list:
    if type(i)==int:
        num.append(i)
    else:
        string.append(i)
num.sort()
string.sort()
sorted_list=num+string
print("Sorted mixed list:",sorted_list)