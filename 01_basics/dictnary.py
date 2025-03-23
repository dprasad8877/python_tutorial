english_dict = {
    "chai": "tea",
    "pani": "water",
    "kutta": "dog",
    "billi": "cat",
    "gari": "car",
    "makan": "house"
    }
print(english_dict) # {'chai': 'tea', 'pani': 'water', 'kutta': 'dog', 'billi': 'cat', 'gari': 'car', 'makan': 'house'}
print(english_dict["chai"]) # tea
print(english_dict["pani"]) # water

print(english_dict.get("kutta")) # dog

# If key is not present in dictionary
print(english_dict.get("kutti")) # None

# assign new value to key
english_dict["kutta"] = "doggy"
print(english_dict) # {'chai': 'tea', 'pani': 'water', 'kutta': 'doggy', 'billi': 'cat', 'gari': 'car', 'makan': 'house'}

#loop through dictionary
for key in english_dict:
    print(key)

for key in english_dict:
    print(key, english_dict[key])
print("--------------------------------------------------")
print(english_dict.keys()) # dict_keys(['chai', 'pani', 'kutta', 'billi', 'gari', 'makan'])
print(english_dict.values()) # dict_values(['tea', 'water', 'doggy', 'cat', 'car', 'house'])
print(english_dict.items()) # dict_items([('chai', 'tea'), ('pani', 'water'), ('kutta', 'doggy'), ('billi', 'cat'), ('gari', 'car'), ('makan', 'house')])

for key, value in english_dict.items():
    print(key, value)

print("--------------------------------------------------")
#if key is not present in dictionary
if "kutti" in english_dict:
    print(english_dict["kutti"])    
else:
    print("Key not present")
print(english_dict.get("kutti")) # None

# add new key value pair
english_dict["kutti"] = "female dog"
print(english_dict) # {'chai': 'tea', 'pani': 'water', 'kutta': 'doggy', 'billi': 'cat', 'gari': 'car', 'makan': 'house

# remove key value pair
del english_dict["kutti"]
print(english_dict) # {'chai': 'tea', 'pani': 'water', 'kutta': 'doggy', 'billi': 'cat', 'gari': 'car', 'makan': 'house'}

poped_value = english_dict.pop("kutta")
print(poped_value) # doggy
print(english_dict) # {'chai': 'tea', 'pani': 'water', 'billi': 'cat', 'gari': 'car', 'makan': 'house'}
print(english_dict.popitem()) # ('makan', 'house')
print(english_dict) # {'chai': 'tea', 'pani': 'water', 'billi': 'cat', 'gari': 'car'}

# clear dictionary
english_dict.clear()
print(english_dict) # {}

#recreate dictionary
english_dict = {
    "chai": "tea",
    "pani": "water",
    "kutta": "dog",
    "billi": "cat",
    "gari": "car",
    "makan": "house"
    }
print(english_dict) # {'chai': 'tea', 'pani': 'water', 'kutta': 'dog', 'billi': 'cat', 'gari': 'car', 'makan': 'house'}

# #delete dictionary
# del english_dict
# print(english_dict) # NameError: name 'english_dict' is not defined

#nested dictionary
student = {
    "name": "Ali",
    "age": 20,
    "courses": ["Math", "Science"],
    "marks": {
        "Math": 90,
        "Science": 80
        }
    }
print(student) # {'name': 'Ali', 'age': 20, 'courses': ['Math', 'Science'], 'marks': {'Math': 90, 'Science': 80}}
print(student["name"]) # Ali
print(student["courses"]) # ['Math', 'Science']
print(student["courses"][0]) # Math
print(student["marks"]) # {'Math': 90, 'Science': 80}
print(student["marks"]["Math"]) # 90
print(student["marks"]["Science"]) #

print("--------------------------------------------------")
squared_number_dict = {x: x*x for x in range(1, 6)}
print(squared_number_dict) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squared_number_dict .clear()
print(squared_number_dict) # {}

print("--------------------------------------------------")
keys = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]
zip_dict = dict(zip(keys, values))
print(zip_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("--------------------------------------------------")
keys = ["a", "b", "c", "d"]
default_value = 0
default_dict = dict.fromkeys(keys, default_value)
print(default_dict) # {'a': 0, 'b': 0, 'c': 0, 'd': 0}
