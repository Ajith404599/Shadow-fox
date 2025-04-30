# 4_if_conditions.py

# Task 1: BMI Category
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("\nYour BMI is:", round(bmi, 2))

if bmi >= 30:
    print("Category: Obesity")
elif bmi >= 25:
    print("Category: Overweight")
elif bmi >= 18.5:
    print("Category: Normal")
else:
    print("Category: Underweight")

# ----------------------------------------

# Task 2: City to Country Mapping
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("\nEnter a city name: ")

if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"{city} is not listed.")

# ----------------------------------------

# Task 3: Check if two cities belong to the same country
city1 = input("\nEnter the first city: ")
city2 = input("Enter the second city: ")

def find_country(city_name):
    if city_name in Australia:
        return "Australia"
    elif city_name in UAE:
        return "UAE"
    elif city_name in India:
        return "India"
    else:
        return None

country1 = find_country(city1)
country2 = find_country(city2)

if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}.")
    else:
        print("They don't belong to the same country.")
else:
    print("One or both cities not listed.")
