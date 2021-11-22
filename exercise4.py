 #Variables and Names
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity  = cars_driven  *  space_in_a_car
average_passengers_per_car  = passengers  /  cars_driven

print("There are",  cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven,  "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")



#Another example
a = "sabina"
b = 30

#printing the varible
print(a)
print(b)

#Printing the type of variable
print(type(a))
print(type(b))

''' Rules for defining a variable:
A variable name can contain alphabets, digits and underscores.
A variable name can only start with an alphabet and underscore.
A variable name can not start with a digit.
No while space is allowed to be used inside a variable name. '''