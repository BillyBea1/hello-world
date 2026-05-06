#A simple rugby score tracker
tries = 5
conversions = 3
penalties= 1
bonus_points = 0

#Logic: If the team scored 4 or more tries, they get a bonus point 
if tries >= 4
    bonus_point = 1
    print("Bonus point earned for 4+ tries!")

#Calculations
total_points = (tries * 5) + (conversions * 3) + (penalties * 3) + bonus_point

print("Match Performance Report:")
print("Final Score with Bonus:", total_points)
