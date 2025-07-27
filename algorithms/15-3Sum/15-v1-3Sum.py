# 15 v1 - 3Sum

nums = [-1,0,1,2,-1,-4]

def solve(nums):
  sorted_nums = sorted(nums)
  res = []

  for i, a in enumerate(sorted_nums):
    if a > 0:
      break

    if i > 0 and a == sorted_nums[i - 1]:
      continue

    left = i + 1
    right = len(sorted_nums) - 1

    while left < right:
      current_sum = a + sorted_nums[left] + sorted_nums[right]
      if (current_sum == 0):
        res.append([a, sorted_nums[left], sorted_nums[right]])
        left += 1 
        while left < right and sorted_nums[left] == sorted_nums[left - 1]:
          left += 1
      elif (current_sum > 0):
        right -= 1
      elif (current_sum < 0):
        left += 1

  return res

print(solve(nums))