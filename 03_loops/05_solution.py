# Find the First Non-Repeated Character

input_string = "minimum"

for char in input_string:
    if input_string.count(char) == 1:
        print('char is: ', char)
        break