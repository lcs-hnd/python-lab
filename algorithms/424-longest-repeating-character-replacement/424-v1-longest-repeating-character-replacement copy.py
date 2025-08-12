#  424 v1 - longest repeating character replacement 
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
s = "XYYX"
k = 2

def algo(s, k):
  left = 0
  mlen = 0
  mfreq = 0
  count = {}

  for right, char in enumerate(s):
    count[char] = count.get(char, 0) + 1
    mfreq = max(mfreq, count[char])

    if ((right - left + 1) - mfreq) > k:
      count[s[left]] -= 1
      left += 1
    
    mlen = max(mlen, right - left + 1)
  
  return mlen

print(algo(s,k))

# i prefer this version but the other one might be considered more readable 