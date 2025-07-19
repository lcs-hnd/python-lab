# calculates the product of all the elements in the inputted iterable
# default start value is 1

# 238 v2 - product of array except self
# still O(n*2) but with a different approach

import math
nums = [1,2,3,4]

def prodExceptSelf(nums):
  res = [0] * len(nums)
  for i in range(len(nums)):
    left = math.prod(nums[:i])
    right = math.prod(nums[i+1:])
    res[i] = left * right
    
  return res

print(prodExceptSelf(nums))