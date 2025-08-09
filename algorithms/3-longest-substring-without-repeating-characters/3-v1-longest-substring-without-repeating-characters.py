# 3 v1 - longest substring without repeating characters
# Given a string s, find the length of the longest without duplicate characters.

s = "abcabcbb"
r = "bbbbbb"
t = "pwwkew"
x = "abcbcrdeb"
f = "atttttrsg"
v = "abcdde"

def algo(input):
  left = 0
  length = 0
  hash_map ={}

  for right in range(len(input)):
    if input[right] in hash_map:
      left = max(left, hash_map[input[right]] + 1)
    hash_map[input[right]] = right
    length = max(length, right - left + 1)
  return length