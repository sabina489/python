# Doing Things to Lists

ten_things = "Apples Mango Crows Pen Light Dark"
print("There are not 10 things")

stuff = ten_things.split(' ')
more_stuff = ["Book", "Copy", "Dance", "Basketball", "Boy", "Girl", "Corn"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:4]))

