# enumerate() creates an enumerate object
# the object is an iterator (this means it doesn't generate all the index and value pairs up front) which is better for sc
# uses O(1) extra space

x = enumerate(["a", "b", "c"])
print(type(x))  # <class 'enumerate'>

# they can be converted into lists
print(list(x))  # [(0, 'a'), (1, 'b'), (2, 'c')]

# yields (index, value) tuples

