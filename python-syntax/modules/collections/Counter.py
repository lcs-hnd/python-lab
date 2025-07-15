# dict subclass from collections module
# counts how many times each element appears in an iterable

from collections import Counter

nums = [1,1,1,2,2,3]
Counter(nums)  # {1: 3, 2: 2, 3: 1}
