# prioritizing space complexity

def hasDuplicates(nums):
  nums.sort()
  for index in range(len(nums) - 1): 
    if nums[index] == nums[index + 1]:
      return True
  return False