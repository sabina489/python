# Functions can Return Something

def add(a, b):   #Here, function is called with two arguments: a and b
    print(f"Adding {a} + {b}")  # We print out what our function is doing, in this cse" adding"
    return a + b #Then we tell python to do something kind of backward: we return the addition of a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print("fMULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(4, 5)
height = subtract(9, 3)
weight = multiply(2, 4)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

