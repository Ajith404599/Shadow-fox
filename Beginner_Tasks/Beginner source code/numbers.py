# Task 1: Format function example
def format_example():
    value = 145
    format_type = 'o'  # Octal representation
    formatted = format(value, format_type)
    print(f"Formatted value of {value} in octal is: {formatted}")

format_example()

# Task 2: Area of a circular pond
radius = 84
pi = 3.14
pond_area = pi * (radius ** 2)
print(f"\nArea of the pond is: {pond_area} square meters")

# Bonus: Total water amount (1.4 liters per square meter)
water_per_sqm = 1.4
total_water = pond_area * water_per_sqm
print(f"Total water (without decimal): {int(total_water)} liters")

# Task 3: Speed calculation
distance_meters = 490
time_minutes = 7
time_seconds = time_minutes * 60
speed_mps = distance_meters / time_seconds
print(f"\nSpeed without decimal: {int(speed_mps)} meters/second")
