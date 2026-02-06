# 3) Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6] 
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]] 
class Subsets:
    def get_subsets(self, nums):
        result = []
        self.backtrack(nums, [], result)
        return result

    def backtrack(self, nums, path, result):
        result.append(path)
        for i in range(len(nums)):
            self.backtrack(nums[i + 1:], path + [nums[i]], result)
obj = Subsets()
print(obj.get_subsets([4, 5, 6]))