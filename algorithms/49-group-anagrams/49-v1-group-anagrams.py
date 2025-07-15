# 49 v1 - group anagrams

strs = ["act","pots","tops","cat","stop","hat"]

def hasAnagram(strs):
  groups = {}

  for word in strs:
    count = [0] * 26 # create a 26 item list with all items as 0

    for char in word:
      # ord returns the unicode number for the given character
      # by doing - ord('a') you create an anchor point to map a-z into array indices (0-25)
      count[ord(char) - ord('a')] += 1 # adds 1 to the corresponding item in the list 

    key = tuple(count) # lists aren't hashable so they can't be dict keys, thus turning the list into a tuple

    if key in groups:
      groups[key].append(word)
    else:
      groups[key] = [word]

  return list(groups.values())

print(hasAnagram(strs))

