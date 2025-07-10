# method from dict
#' dict.get(key, default_value)

#* key is the argument representing the key whose value you are looking to retrieve
#* default_value is optional and specifies a value to be returned if the key is not found
  #> when omitted it returns none

dictionary = {"name": "Doug", "favorite_color": "Red"}

# retrieve a key
color = dictionary.get("favorite_color")
print(f"1. {color}") # None

city = dictionary.get("favorite_city")
print(f"2. {city}") # None

age = dictionary.get("age", "Missing?")
print(f"3. {age}") # Missing

