# 271 v1 - encode & decode strings
strs = ["random", "string", "gotta#test#it", "", "#", "#is this working?"]
new_string = "6#random6#string13#gotta#test#it0#1##17##is this working?"

def encode(strs):
  encoded = ""
  for string in strs:
    encoded += f"{len(string)}#{string}"
  
  return encoded

def decode(s):
  decoded = [] # define the list
  i = 0 # starting character

  while i < len(s): # loop while the starting character isn't at the end of the payload
    j = i # redefine the separator to the new start

    while s[j] != "#": # increment the separator's position until its value is equal to the expected delimiter
      j += 1

    length = int(s[i:j]) # pull the metadata (string's length) kept from the starting character until the separator index (delimiter # `j`)
    decoded.append(s[j+1:j+length+1]) # append a slice from the string's beggining (1 position past the separator index (delimiter) (j + 1))
    # until the start of the next section's metadata (string_length_integer`delimiter`)
    i = j + 1 + length # redefine the start of the section as the first chacter of the next metadata
    
  return decoded

print(encode(strs))
print(decode(new_string))