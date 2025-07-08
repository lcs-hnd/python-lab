a, b = 0, 1 # multiple assigment
while a < 10: 
  print(a) # indented body, this is how python groups statements
  a, b = b, a+b 
  # blank line to indicate completion
