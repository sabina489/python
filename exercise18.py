# Names, Variables, Code, Functions
'''They name pieces of code the way variables name strings and numbers.
2. They take arguments the way your scripts take argv.
3. Using 1 and 2, they let you make your own ”mini-scripts” or ”tiny commands.”'''

# We can create a function by using the word def in python.
#This function is like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#That *args is actually pointless, we can do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#This one takes no arguments
def print_none():
    print("I got something.")

print_two("Sabina","Saru")
print_two_again("Sabina","Saru")
print_one("First!")
print_none()
