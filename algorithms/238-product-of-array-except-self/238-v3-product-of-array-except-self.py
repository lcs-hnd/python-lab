# 238 v3 - product of array except self
# O(n) time complexity
# O(1) extra space

def prodExceptSelf(nums):
  n = len(nums)
  # initialize the result array with 1s
  # res[i] will store the final product except self, and 1 is neutral in multiplication
  res = [0] * n

  # initialize prefix as 1
  # there are no elements to the left, so the prefix should be neutral to start with
  prefix = 1
  
  # a left to right pass to build the prefix products
  for i in range(n):
    res[i] = prefix
    # res 3 = prefix 
    prefix *= nums[i]

  suffix = 1
  for i in reversed(range(n)):
    res[i] *= suffix
    suffix *= nums[i]

  return res

print(prodExceptSelf([1, 2, 3, 4]))