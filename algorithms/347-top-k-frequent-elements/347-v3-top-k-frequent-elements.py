import heapq
from collections import Counter

nums = [1,1,1,2,2,3]
k = 2 

def freq(nums, k):
  count = Counter(nums) # new class from collections, creating an instance

  heap = []
  for number, freq in count.items(): # unpacking the newly made tuple from the count object
    heapq.heappush(heap, (freq, number)) # pushing to the list now used as a heap where it's sorted by freq

    if len(heap) > k: # prioritize the larget frequencies
      heapq.heappop(heap) 
  
  return [number for freq, number in heap] # loops through heap where each item is a tuple but only number is returned