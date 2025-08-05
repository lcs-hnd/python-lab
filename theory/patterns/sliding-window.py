# sliding window pattern
#' imagine a dark library where you can only see a limited amount of books at a time with your flashlight
#' you scan the shelf from left to right
#' as you move forward the beam shifts, revealing new books ahead and hiding the ones behind
#' you're always seeing the same number of books, but which books are visible change as you slide the beam

#- this pattern is used to reduce nested loops in an algorithm

#$ using two markers, both start at the beggining
#$ 2nd marker moves to the right until a set condition
#$ 1st marker moves along after an item at a time checking each one
#| this allows for data to be managed in segments instead of all at once
#| it's a dynamic subset of a sequence, it traverses the sequence in fixed-size incremenets
