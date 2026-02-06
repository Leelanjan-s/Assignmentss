# 8) Write a python class which has 2 methods get_string and print_string. get_string takes a 
# string from the user and print_string prints the string in reverse order
class ReverseString:
    def get_string(self):
        self.s = input()
    def print_string(self):
        print(self.s[::-1])
obj = ReverseString()
obj.get_string()
obj.print_string()