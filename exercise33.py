# While Loops
# A while loop will keep executing the code block under it as long as a boolean expression is True.

i = 0
numbers = []

while i < 4:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1

    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")

print("The numbers:")
for num in numbers:
    print(num)

# A for-looop can only iterate(loop) over collectioins of things. A while-loop can do any kind of iteration(looping) we want.