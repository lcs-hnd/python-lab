#  424 v2 - longest repeating character replacement 
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
s = "XYYX"
k = 2

def algo(string, k):
  left = 0
  max_freq = 0
  max_len = 0
  char_count = {}

  for right, char in enumerate(string):
    char_count[char] = char_count.get(char, 0) + 1
    max_freq = max(max_freq, char_count[char])
    window_len = right - left + 1

    if (window_len - max_freq) > k:
      left_char = string[left]
      char_count[left_char] -= 1
      left += 1
      
    max_len = max(max_len, right - left + 1)

  return max_len

print(algo(s, k))