nums = [1,1,1,2,2,3]
k = 2

def freq(nums, k):
  map = {}

  for number in nums: # same increment approach similar to last time
    if number in map:
        map[number] += 1
    else:
        map[number] = 1

  # turning hash table into list of tuples to sort by x[1]
  sorted_map = sorted(map.items(), key=lambda x: x[1], reverse=True) # using sorted and the two optional args
  # key= is the function used to tune the sorting, lambda is defining the throwaway function expecting x and returning x[1], reversing to see highest first (could slice end if you wanted ig)

  result = [] 
  for item in sorted_map[:k]: # return the 
    result.append(item[0])

  return result


print(freq(nums, k))
