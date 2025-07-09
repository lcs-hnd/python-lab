# a set holds unique values only, no duplicated are allowed
# given instant lookups (checking for a key's existence)

seen = set()
seen.add(1)

print(1 in seen) # true
print(2 in seen) # false
