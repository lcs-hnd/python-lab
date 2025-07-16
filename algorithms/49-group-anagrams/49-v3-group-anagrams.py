# 49 v3 - group anagrams
from collections import defaultdict

strs = ["act","pots","tops","cat","stop","hat"]

def groupAnagrams(strs):
  groups = defaultdict(list) # using default dict and passing list class as an arg
  # when a missing key is accessed, call list() to create a default value
  # passing classes in order to provide default values is unique to defaultdict 

  for word in strs:
    key = ''.join(sorted(word))
    groups[key].append(word)

  return list(groups.values()) # return a list of the values in the hash table

print(groupAnagrams(strs))