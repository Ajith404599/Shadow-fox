# 5_for_loops.py

import random

# Task 1: Roll a six-sided die 20 times
rolls = []
for i in range(20):
    rolls.append(random.randint(1, 6))

print("Rolls:", rolls)

count_6 = rolls.count(6)
count_1 = rolls.count(1)

# Count two consecutive 6s
consecutive_6s = 0
for i in range(len(rolls)-1):
    if rolls[i] == 6 and rolls[i+1] == 6:
        consecutive_6s += 1

print(f"\nNumber of times rolled a 6: {count_6}")
print(f"Number of times rolled a 1: {count_1}")
print(f"Number of times rolled two 6s consecutively: {consecutive_6s}")

# ----------------------------------------

# Task 2: Jumping Jacks Workout
total_jumping_jacks = 100
completed = 0

while completed < total_jumping_jacks:
    completed += 10
    print(f"\nCompleted {completed} jumping jacks.")
    if completed >= total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break
    tired = input("Are you tired? (yes/y or no/n): ").lower()
    if tired in ['yes', 'y']:
        skip = input("Do you want to skip remaining sets? (yes/y or no/n): ").lower()
        if skip in ['yes', 'y']:
            print(f"\nYou completed a total of {completed} jumping jacks.")
            break
