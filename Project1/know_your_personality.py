import time

print("Let's discover who you really are with some fun data magic! ")
time.sleep(1)
print("Scanning colors,food, and animal energies...")
time.sleep(1)
print("Calculating your personality type using complex non-scientific logic...")
time.sleep(1)
name=input("Your Name").strip()
age=int(input("Your Age"))
city=input("City you live in ").strip()
food=input("Your Favourite Food").strip()
color=input("Your Favourite Color").strip()
animal=input("Your Spirit Animal").strip()
hobby=input("one thing you love doing".title()).strip()

print(f"Hey {name.title()} , here's your fun personality report!")

time.sleep(5)

print(f"You're from {city.title()}, a place of dreams!")
print(f"You love {food} and enjoy doing {hobby}")
print(f"You vibe the colour {color.upper()} and your spirit animal is the {animal}")
print(f"You've lived approximately {int(age)*12} months already ")

if age < 18:
    print("You belong to the 'Young Explorer' tribe ")
elif age <=30 and age >= 18:
    print("You belong to the 'Adventurer' tribe ")
else:
    print("You belong to the 'Wise Owl' tribe ")

print(f"Your Secret Personality Code is: {name[0:2].upper()+str(age//10)+animal[0]+color[0]}")

if len(hobby)>9:
    print("You seem deeply passionate — that hobby says a lot about your vibe!")
else:
    print(" Time to explore more hobbies? You’ve got hidden sparks waiting!")

print("You are officially certified as: FUNKY AND FABULOUS!" )