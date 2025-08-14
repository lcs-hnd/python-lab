# 567 v2 - permutation in string 
# You are given two strings s1 and s2.
# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
# Both strings only contain lowercase letters.

s1 = "abc"
s2 = "lecabee"

def alg(s1, s2):
  from collections import Counter

  len_s1 = len(s1)
  len_s2 = len(s2)
  if len_s1 > len_s2:
    return False
  
  count_s1 = Counter(s1)
  window_count = Counter()

  matches = 0

  for i, char in enumerate(s2):
    window_count[char] += 1

    if char in count_s1 and window_count[char] == count_s1[char]:
      matches += 1
    elif char in count_s1 and window_count[char] == count_s1[char] + 1:
      matches -= 1

    if i >= len_s1:
      left_char = s2[i - len_s1]
      if left_char in count_s1 and window_count[left_char] == count_s1[left_char]:
        matches -= 1
      elif left_char in count_s1 and window_count[left_char] == count_s1[left_char] + 1:
        matches += 1
      window_count[left_char] -= 1

    if matches == len(count_s1):
      return True
  
  return False

print(alg(s1, s2))