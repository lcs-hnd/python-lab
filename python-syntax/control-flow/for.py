# dictonary rather than object
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'} # used to be an unordered list, python 3.7+ are not insertion-ordered
# still key-value pairs
# keys are explicit and strict aka hashable (contains a hash value that remains constant throughout its lifetime)
# you must quote strings
# js defaults to strings if unquoted

for user, status in users.copy().items(): # items() returns key-value pairs as tuples
    # this is a frozen snapshot of the dictionary to iterate through while mutating the original
    # the hash table layout changes if the mutation happens during iteration, this removes the map towards the dictionary
    # thus you need a copy
    if status == 'inactive':
        del users[user]

active_users = {} # empty dictionary
for user, status in users.items(): # fine to iterate directly since it is mutating a different dictionary
    if status == 'active':
        active_users[user] = status # bracket notation in js, not sure about the name here

# copy() is a method belonging to mutable objects
# items() belong specifically to dictionaries