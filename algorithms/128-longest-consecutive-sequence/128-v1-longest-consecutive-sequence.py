# 128 v1 - longest consecutive sequence

nums = [100,4,200,1,3,2] # unsorted array of integers

def long(nums):
  num_set = set(nums)
  longest_streak = 0

  for n in num_set:
    if ((n - 1) not in num_set):
      current_num = n
      count = 1
      while (current_num + 1) in num_set:
        count += 1
        current_num += 1

      longest_streak = max(longest_streak, count)

  return longest_streak

print(long(nums))



