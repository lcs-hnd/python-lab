# 238 v2 - product of array except self
# still O(n*2) but with a different approach

import math
nums = [1,2,3,4]

def prodExceptSelf(nums):
  res = [0] * len(nums)
  for num in nums:
     res[nums.index(num)] = (math.prod(nums[0:nums.index(num)])) * (math.prod(nums[nums.index(num)+1:]))

  return res

print(prodExceptSelf(nums))