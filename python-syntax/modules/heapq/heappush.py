# a heap is a special kinf of list where python keeps the smallest element at the top (index 0)
# when heappush"ing" python will automatically reorder the list to keep the smallest on top

# heaps can have anything pushed to them as long as python can compare them
# if you want to push objects then you have to define how they're to be compared in the respective classes

# full sig: heapq.heappush(heap, item)
  # heap is the list you want to use as a heap (heap stays as heap bc the list was defined as heap = [])
  # item is the element you want to insert, in this case it's (freq, number) 

import heapq
from collections import Counter 

nums = [1,1,1,2,2,3]
k = 2

def freq(nums, k):
  count = Counter(nums) # defining the map as before, now with Counter

  heap = []
  for number, freq in count.items(): # tuple of count for sorting
    heapq.heappush(heap, (freq, number)) # push as (frequency, number)
    if len(heap) > k:
      heapq.heappop(heap) # pop the smallest freq if size > k

  return [number for freq, number in heap]
  

print(freq(nums, k))