pet_name = "Dog"
pet_age = 3

if pet_name == "Dog":
    if pet_age < 2:
        food = "puppy food"
    else:
        food = "dog food"
elif pet_name == "Cat":
    if pet_age < 5:
        food = "kitten food"
    else:
        food = "cat food"
else:
    food = "generic pet food"

print(f"{pet_name} should eat {food}.")
