# 567 v1 - permutation in string 
# You are given two strings s1 and s2.
# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
# Both strings only contain lowercase letters.

s1 = "abc"
s2 = "lecabee"

def alg(s1, s2):
  max_length = len(s1)
  if max_length > len(s2):
    return False
  
  original = {}
  sub_string = {}
  left = 0

  for char in s1:
    original[char] = original.get(char, 0) + 1

  for right, char in enumerate(s2):
    sub_string[char] = sub_string.get(char, 0) + 1

    if right - left + 1 > max_length:
      sub_string[s2[left]] -= 1
      if sub_string[s2[left]] == 0:
        sub_string.pop(s2[left])
      left += 1

    if right - left + 1  == max_length and original == sub_string:
      return True
      
  return False

print(alg(s1, s2))
    