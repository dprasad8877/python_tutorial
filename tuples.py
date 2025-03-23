tea_tuple = ("chai", "tea", "pani", "water", "kutta", "dog", "billi", "cat", "gari", "car", "makan", "house")
print(tea_tuple) # ('chai', 'tea', 'pani', 'water', 'kutta', 'dog', 'billi', 'cat', 'gari', 'car', 'makan', 'house')
print(tea_tuple[0]) # chai
print(tea_tuple[-1]) # tea
print(tea_tuple[:2]) # pani
print(tea_tuple[::2]) # ('chai', 'pani', 'kutta', 'billi', 'gari', 'makan')

#tea_tuple[0] = "chaii" # TypeError: 'tuple' object does not support item assignment
#print(tea_tuple) # ('chai', 'tea', 'pani', 'water', 'kutta', 'dog', 'billi', 'cat', 'gari', 'car', 'makan', 'house')

more_tea = ("doodh", "milk", "shakar", "sugar")
print(more_tea) # ('doodh', 'milk', 'shakar', 'sugar')
All_tea = tea_tuple + more_tea
print(All_tea) # ('chai', 'tea', 'pani', 'water', 'kutta', 'dog', 'billi', 'cat', 'gari', 'car', 'makan', 'house', 'doodh', 'milk', 'shakar', 'sugar')

print("--------------------------------------------------")
# loop through tuple
for item in All_tea:
    print(item)
print("--------------------------------------------------")
for i in range(len(All_tea)):
    print(All_tea[i])
print("--------------------------------------------------")
i = 0
while i < len(All_tea):
    print(All_tea[i])
    i += 1 
print("--------------------------------------------------")
print(All_tea.index("gari")) # 8

#destructuring
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = All_tea
print(a) # chai


