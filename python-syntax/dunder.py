# dunder method (short for double underscore)
# used to give special behavior to objects
# you almost never call them, they're 'python's magic hooks'

class Person:
    def __init__(self, name): # constructor like in JS
        self.name = name

    def __str__(self):  
        return f"Person({self.name})"

p = Person("Lucas")
print(p)  # Person(Lucas)
