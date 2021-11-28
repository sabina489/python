# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


# Creating a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Sabina", "Karki")
x.printname()

# Creating a Child Class
class Student(Person):
    pass  # pass keyword is used when we do not want to add any other properties or methods to the class.
x = Student("Sabina", "karki")
x.printname

#Adding the __init__() Function
#THe __init__() function is called automatically every time the class is being used to create a new object.
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
x = Student("Saru", "Karki")
x.printname()

