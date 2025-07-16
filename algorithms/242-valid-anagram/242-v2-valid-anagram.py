# 242 v2 - valid anagrams
str1 = "racecar"
str2 = "acecarr"

def isAnagram(str1, str2):
  string_map1 = {} 
  string_map2 = {}

  # get method allows to check for a key's existence/value and assignment at the same time
  # if a letter isn't found then get returns 0 as its value and receives 1 right after
  # if it's found then no assignment is performed and that key's value is increased by 1
  for letter in str1: 
    string_map1[letter] = string_map1.get(letter, 0) + 1
  
  for letter in str2: 
    string_map2[letter] = string_map2.get(letter, 0) + 1

  return string_map1 == string_map2 # returning the dictionary comparison

print(isAnagram(str1, str2))



