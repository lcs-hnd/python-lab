# intro into heapq module from the 347 problem

# tree-based data structure
# min-heap: smallest element always at the top
# max-heap: largest element always at the top

# 347 v2 is sorting all n items O(n log n) and then slicing the top (k)
# this is fine for small array but if n is huge and k is small this is wasteful
# a heap based approach allows you to keep track of only the top k elements while processing the array
# time comp: O(n log k) is better than O(n log n)


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