# subclass of the built in dict class, a dict with enhacements
# "It overrides one method and adds one writable instance variable."

# 49 group anagram solution as an eg

from collections import defaultdict

strs = ["act","pots","tops","cat","stop","hat"]

def groupAnagrams(strs):
  groups = defaultdict(list) # 

  for word in strs:
    key = ''.join(sorted(word))

    groups[key].append(word)

  return list(groups.values())

print(groupAnagrams(strs))