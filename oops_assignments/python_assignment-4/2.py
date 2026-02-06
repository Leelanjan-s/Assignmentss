# 2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These 
# brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" 
# and "{{{" are invalid. 
class ValidParentheses:
    def is_valid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch in ')}]':
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return len(stack) == 0
obj = ValidParentheses()
print(obj.is_valid("()"))
print(obj.is_valid("()[]{}"))
print(obj.is_valid("[)"))
print(obj.is_valid("({[)]"))
print(obj.is_valid("{{{"))  