# concise and efficient way to create new lists based on existing iterables
# this provides a more readable and faster alternative to traditional for loops for list construction


# list = [expression for item in iterable]
# expression is the opration performed on each item from the iterable (defining the value added to the list)
# item is the temp variable to represent each element from the iterable during iteration
# iterable is the source sequence

# 347 for example

nums = [1,1,1,2,2,3]
k = 2

def freq(nums, k):
  map = {}

  for number in nums: 
    if number in map:
        map[number] += 1
    else:
        map[number] = 1

  sorted_map = sorted(map.items(), key=lambda x: x[1], reverse=True) 
  return [item[0] for item in sorted_map[:k]] # concise format, as usual sorted_map[:k] slices the first k elements of sorted_map
  # item[0] defines the value added, in this case it's the first value of each tuple
  # item is the temp var
  # sorted_map is the sequence and we slice it with integer k, [:k], in order to only take the values from the first intended tuples 



