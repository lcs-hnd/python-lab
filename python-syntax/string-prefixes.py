# formatted string literal
# similar to JS template literals 
# console.log(`Hello ${name}`);

name = "Lucas"
print(f"Hello {name}!")  # Hello Lucas!

# raw string literal, backslashes won't be treated as escape characters
path = r"C:\Users\Lucas\Documents"

#. | pfix | Meaning                          |
#. | ---- | -------------------------------- |
#. | `f`  | Formatted string (f-string)      |
#. | `r`  | Raw string (no escaping)         |
#. | `u`  | Unicode string (Python 2 legacy) |
#. | `b`  | Bytes literal                    |
