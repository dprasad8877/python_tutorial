age = 16
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price - 2

print("Ticket price: {price}".format(price=price))


