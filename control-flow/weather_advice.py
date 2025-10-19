# Create a file named weather_advice.py
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

if weather=="sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    # This block runs if the user enters "cold".
    print("Make sure to wear a warm coat and a scarf.")
else:
    # This block runs if the input does not match any of the above conditions.
    print("Sorry, I don't have recommendations for this weather.")
