# 76 v1 - minimum window 

# Given two strings s and t of lengths m and n respectively, 
# return the minimum window of s such that every character in t 
# (including duplicates) 
# is included in the window. 

# If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

s = "ADOBECODEBANC", t = "ABC"

def alg(s, t):
  left = 0
  target = dict()
  current_window = dict()

  for letter in t:
    target[letter] = target.get(letter, 0) + 1

  for right, char in enumerate(s):
    if char in target:
      current_window[right]




  
