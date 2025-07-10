# Valid Anagram V1

# anagrams are strings with the same characters
# assuming lowercase in this scenario
str1 = "racecar"
str2 = "acecarr"

def isAnagram(str1, str2):
  string_map1 = {}
  string_map2 = {}

  for letter in str1: 
    if letter in string_map1:
      string_map1[letter] += 1 
    else:
      string_map1[letter] = 1
  
  for letter in str2:
    if letter in string_map2:
      string_map2[letter] += 1 
    else:
      string_map2[letter] = 1

  if string_map1 == string_map2:
    return True
  return False


