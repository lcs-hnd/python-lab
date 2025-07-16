# 271 v1 - encode & decode strings
strs = ["random", "string", "gotta#test#it", "", "#", "#is this working?"]
new_string = "6#random6#string13#gotta#test#it0#1##17##is this working?"

def encode(strs):
  encoded = ""
  for string in strs:
    encoded += f"{len(string)}#{string}"
  
  return encoded

def decode(str):
  decoded = []

  i = 0
  while i < len(str):
    j = i

    while str[j] != "#": # if the character at this index isn't # add 1 to j every loop
      j += 1

    length = int(str[i:j]) # string length is the integer of the this slice? still confusing at this point
    decoded.append(str[j+1:j+1+length]) # unsure of how this string extraction is performed, i get that it's a slice but this is complicated to me
    i = j + 1 + length # couldn't you define this before the previous line in order to use i in the place of j + 1 + length?
    
  return decoded

print(encode(strs))
print(decode(new_string))