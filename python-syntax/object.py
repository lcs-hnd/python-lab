x = 42 # x is an instance of int, which inherits from object
print(x.__str__())  # 42 comes from int class

# every object is an instance of a class

# object is the base class from which all classes inherit from
# Object.prototype JS equivalent

class MyClass: # MyClass doesn't declare a parent but python makes it inherit from object
    pass

print(issubclass(MyClass, object))  # True
print(isinstance(MyClass(), object))  # True
