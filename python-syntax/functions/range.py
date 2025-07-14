# built in type (class)
# when range() is used the constructor is called to create an object
# produces each number on demand as you iterate unlike a list
# frequently used with len(), range(len(item))

sequence = range(5)

for n in sequence:
  print(n)

print(type(sequence)) # <class 'range'>
print(sequence) # range (0, 5), does include 5, it's simply a sequence of
# 5 numbers starting at 0

# 0
# 1
# 2
# 3
# 4