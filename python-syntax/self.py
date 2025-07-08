# self is a reference to the instance of the class itself
# similar to `this` in JS
# allows you to access instance variables and methods from within the class
# automatically passed to methods when you call them on an object

class Person:
    def __init__(self, name): # self refers to the instance (objectj) of the class
        self.name = name  

    def greet(self):
        print(f"Hello, my name is {self.name}") 

p = Person("Lucas")
p.greet() # calling greet of the given instance 'p', self is 'p' here

# you always define self in method signatures
# self in python is always explictly tied to the object and you never lose it like in JS