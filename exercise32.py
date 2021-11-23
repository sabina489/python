# Loops and Lists   # a container of things that are organized in order from first to last.
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'mango']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too
for i in change:
    print(f"A fruit of type: {fruit}")

#We can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 5):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)  #it simply appends to the end of the list.

#Now we can print them out too
for i in elements:
    print(f"Element was: {i}")