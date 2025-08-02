# 11 v1 - container with most water

height = [1,8,6,2,5,4,8,3,7]

def water(input):
  left = 0
  right = len(height) - 1
  max_area = 0

  while left < right:
    width = right - left
    area = width * min(height[left], height[right])
    max_area = max(max_area, area)

    if height[left] >= height[right]:
      right -=1
    else:
      left +=1

  return max_area

print(water(height))
      