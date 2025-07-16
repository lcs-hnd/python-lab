# 1 v2 - two sum
# switching away from O(n*2) TC into O(n)
# making use of precomputed values

nums = [3, 2 ,4]
target = 6

def twoSum(nums, target):
  seen = {} # define hash table

  for i, num in enumerate(nums): # i as index and num as value
    tcomp = target - num # tcomp is the num to look for when returning the indices

    if tcomp in seen: # checks for the number in seen's keys
      return [seen[tcomp], i] # returns the the index of that number since
      # it's stored in the value and not the key
    
    seen[num] = i # if not found store it in the hash table as a key and the index as a value


