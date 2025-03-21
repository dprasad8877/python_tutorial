tea_list = ['Earl Grey', 'Green', 'Peppermint', 'Chamomile']
# print(tea_list)
# print(tea_list[0])
# print(tea_list[-1])
# print(tea_list[1:3])
# print(tea_list[:2])
# print(tea_list[2:])
# tea_list[1] = 'Lemon' 
# print(tea_list)
# tea_list.append('Green')
# print(tea_list)
# tea_list.insert(1, 'Green')
# print(tea_list)  
# tea_list[1:3] = ['Chai', 'Oolong']
# tea_list.insert(1, 'Green')
# print(tea_list)
# tea_list.remove('Green')
# print(tea_list)
# print(tea_list.pop(1))
# print(tea_list[1:1])
# tea_list[1:1] = ['Green', 'Peppermint']
# print(tea_list)
# print(tea_list.index('Green'))

for tea in tea_list:
    print(tea)
for tea in tea_list:
    print(tea, end='--')
print()
if 'Green' in tea_list:
    print('Green is in the list')
else:
    print('Green is not in the list')

tea_list_copy = tea_list
print(tea_list_copy)
tea_list_copy[1] = 'Green1'
print(tea_list)
tea_list_copy = tea_list.copy()
print(tea_list_copy)
tea_list_copy[1] = 'Green2'
print(tea_list)

squared_numbers = [x*x for x in range(10)]
print(squared_numbers)

squared_numbers = [x*x for x in range(10) if x % 2 == 0]
print(squared_numbers)

cube_numbers = [x**3 for x in range(10)]
print(cube_numbers)




