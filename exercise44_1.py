# Composition
#Another way to do the inheritance exact same thing is just to use other classes and modules, rather than rely on implicit inheritance.

class Parent(object):
    def override(self):
        print("OTHER override()")
    
    def implicit(self):
        print("PARENT implicit()")
    
    def altered(self):
        print("PARENT altered()")

#Creating the Child Class
class Child(Parent):
    def override(self):
        print("CHILD IS override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).alteed()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()