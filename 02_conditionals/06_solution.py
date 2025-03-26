distance = 100
if distance < 3:
    transport = "walk"
elif distance < 15:
    transport = "bike"
else:
    transport = "car"
print(f"Distance: {distance} km, Transport: {transport}")
