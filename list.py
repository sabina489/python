# List: Python list are containers to store a set of values of any data type.
a = [1, 3, 5 ,4] #creating the listing using []
print(a)

#printing the list using print() function.
a[0] = 10
print(a)  #index start with 0

#Access using index a[0], a[1], a[2]
print(a[2])
print(a[3])

#We can create a list with items of different types
b = [45, "saru", False, 4.3]
print(b)

#List slicing
fruits = ["apple", "mango"]
print(fruits)
print(fruits[0:1])

#list methods
l1 = [1, 2, 3, 3 ,4, 5, 6]
l1.sort
print(l1)
l1.reverse()  #reverse the list
print(l1)

l1.append(20)  # adds 20 at the end of the list
l1.insert(1,30)  #insert 30 at the index 1
l1.pop(2)  #delete element at index 2
l1.remove(4)  #remove 4 from the list
print(l1)