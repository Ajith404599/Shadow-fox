# Justice League Superheroes List
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# 1. Calculate number of members
print("\nNumber of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\nAfter adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\nAfter making Wonder Woman the leader:", justice_league)

# 4. Separate Aquaman and Flash by moving Green Lantern between them
justice_league.remove("Green Lantern")
index_flash = justice_league.index("Flash")
justice_league.insert(index_flash, "Green Lantern")
print("\nAfter placing Green Lantern between Aquaman and Flash:", justice_league)

# 5. Replace the existing list with a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nNew Justice League team:", justice_league)

# 6. Sort the list alphabetically
justice_league.sort()
print("\nJustice League after sorting alphabetically:", justice_league)

# BONUS: Who is the new leader (0th index)?
print("\nNew leader of the Justice League:", justice_league[0])
