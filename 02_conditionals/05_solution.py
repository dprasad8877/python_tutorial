weather = "sunny"

if weather == "rainy":
    activity = "watch a movie"
elif weather == "sunny":
    activity = "go for a walk"
elif weather == "snowy":
    activity = "build a snowman"
else:
    activity = "sit inside and read a book"

print(f"If the weather is {weather}, you should {activity}.")