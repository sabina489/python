# Is-A, Has-A, Objects and Classes
# We use a Is-A when we talk about objects and classes being related to each other by a class relationship.
# We use a Has-A when we talk about objects and classes that are related only because they reference each other.

# Animal is-a object
class Animal(object):
    pass
 #Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        # Dog is-a ANimal
        self.name = name

#Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        # Cat is-a Animal
        self.name = name

# Person is-a object
class Person(object):
    def __init__(self, name):
        # person is-a object
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

#Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        #call __init__ of person
        super(Employee, self).__init__(name)
        #emoloyee has-a salary
        self.salary = salary  

# Fish  is-a Fish
class Fish(object):
    pass
    # Salmon is-a Fish
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

#Satan is-a Cat
satan = Cat("Satan")

# Mary is-a Person
mary = Person("Mary")

# mary has-a pet
mary.pet = satan

# Frank is-a Employee
frank = Employee("Frank", 1000)

#Frank has-a Pet
frank.pet = rover

#flipper is-a fish
flipper = Fish()

#crouse is-a fish
crouse = Salmon()

#harry is-a Person
harry = Halibut()

