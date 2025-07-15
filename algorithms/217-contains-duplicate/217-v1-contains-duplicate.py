# 217 v1 - contains duplicate

# given array of integers return true if any value appears at 
# least twice in the array, return false if all are distinct

nums = [1, 2, 3, 3] # true

# can't assume sorted
# python set is useful in this case

def hasDuplicate(nums):
  seen = set()

  for num in nums: # loop through once O(n)
    if num in seen: # checks if in set O(1)
      return True
    else:
      seen.add(num) # adds nubmer to the set O(1)
  return False # if loop finished with no duplicate

print(hasDuplicate(nums))

# total time complexity O(n)

# auxiliary space complexity O(n)
# > worst case no duplicates thus all n numbers are stored in set()

#' this could be optimized for memory with space complexity reduced to O(1)
#' the array is first sorted O(n log n) and adjacent elements scanned O(n)
#' time: O(n log n), space: O(1)

#$ we are trading space 

