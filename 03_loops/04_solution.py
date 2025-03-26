# reverse the string using for loop
input_string = "Hello World"
output_string = ""
for i in range(len(input_string)-1, -1, -1):
    output_string += input_string[i]
print(output_string)

reverse_string = ""
for i in input_string:
    reverse_string = i + reverse_string
print(reverse_string)

