# 238 v1 - product of array except self
# no time comp optimization, n*2

nums = [1,2,3,4]

def prodExceptSelf(nums):
  answer = []

  for i in range(len(nums)):
    product = 1
    for j in range(len(nums)):
      if j != i:
        product *= nums[j]
    answer.append(product)

  return answer

print(prodExceptSelf(nums))
