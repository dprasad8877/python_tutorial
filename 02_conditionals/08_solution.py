password = input("Enter your password: ")

if len(password) < 8:
    print("Password is too short")
elif len(password) > 12:
    print("Password is too long")
else:
    print("Password is just right")
    
    