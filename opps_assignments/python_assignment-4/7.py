# 7) Write a Python class to reverse a string word by word. 
# Input string : 'hello .py' Expected Output : '.py hello' 
class ReverseWords:
    def reverse_words(self, s):
        words = s.split()
        return " ".join(words[::-1])
obj = ReverseWords()
print(obj.reverse_words("hello .py"))
