# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "mango"]

unitue_items = set()

for item in items:
    if item in unitue_items:
        print("Duplicate found:", item)
        break
    unitue_items.add(item)