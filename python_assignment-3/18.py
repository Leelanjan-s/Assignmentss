# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
sample_list1 = [{}, {}, {}]
sample_list2 = [{1, 2}, {}, {}]
def sample(dicts):
    return all(not i for i in dicts)
print(sample(sample_list1))  
print(sample(sample_list2))  