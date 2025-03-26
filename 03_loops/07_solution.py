# Keep asking the user for input until they enter a number between 1 and 10.
# Once they do, print "Thanks!" and exit the loop.

# while True:
#     number = int(input("Enter a number between 1 and 10: "))
#     if 1 <= number <= 10:
#         print("Thanks!")
#         break
#     else:
#         print("Invalid input. Try again.")

while True:
    number = int(input("Enter a number between 1 and 10: "))
    if 1 <= number <=10:
        print("Thanks!")
        break
    else:
        print("Invalid input. Try again.")
        