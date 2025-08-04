# 42 v1 - trapping rain water

height=[4,2,3]

def water(height):
  left = 0
  lm = 0
  right = len(height) - 1
  rm = 0
  bucket = 0

  while left < right:
    lm = max(lm,height[left])
    rm = max(rm,height[right])
    mbar = min(lm,rm)
    if height[left] <= height[right]:
      bucket += max(0,mbar-height[left])
      left +=1
    elif height[left] > height[right]:
      bucket += max(0,mbar-height[right])
      right -=1 
  return bucket

print(water(height))