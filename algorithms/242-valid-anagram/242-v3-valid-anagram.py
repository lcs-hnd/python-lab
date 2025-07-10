# Valid Anagram V3

str1 = "racecar"
str2 = "acecarr"

def isAnagram(str1, str2):
  if len(str1) != len(str2): # TC: O(1) early detection
    return False
  
  string_map = {} # single hash map now

  for letter in str1: 
    string_map[letter] = string_map.get(letter, 0) + 1

  for letter in str2: # decreasing counter from first hash map
    string_map[letter] = string_map.get(letter, 0) - 1 # if a new letter shows up its value goes 0 -> 1
    if string_map[letter] < 0: # loop exits in case a key has a value less than 0
      return False
  return True

print(isAnagram(str1, str2))

