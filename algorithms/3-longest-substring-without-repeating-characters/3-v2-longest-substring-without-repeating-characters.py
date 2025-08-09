# 3 v2 - longest substring without repeating characters
# Given a string s, find the length of the longest without duplicate characters.

s = "abcabcbb"
r = "bbbbbb"
t = "pwwkew"
x = "abcbcrdeb"
f = "atttttrsg"
v = "abcdde"

def algo(s):
  left = max_length = 0
  char_index = {}

  for right, char in enumerate(s):
    if char in char_index:
      left = max(left, char_index[char] + 1)
    char_index[char] = right
    max_length = max(max_length, right - left + 1)
  return max_length
