strs = ["act","pots","tops","cat","stop","hat"]

def groupAnagrams(strs):
  groups = {}

  for word in strs:
    key = ''.join(sorted(word)) # sort the incoming word and assign it to key

    if key in groups: # if the given key is in hash table append the word to that key
      groups[key].append(word)
    else:
      groups[key] = [word] # else create array at that key

  return list(groups.values()) # return a list of the values in the hash table

print(groupAnagrams(strs))