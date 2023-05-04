#User Inputs
planet = input("planet: ")
animal = input("animal: ")
adjective_one = input("adjective: ")
noun_one = input("noun: ")
day_of_week = input("day of the week: ")
food_one = input("food: ")
verb_one = input("verb: ")
food_two = input("food: ")
emotion = input("emotion: ")
verb_two = input("verb: ")
adjective_three = input("adjective: ")
city = input("city: ")



#Print Mad Libs from User Choices
print()
print("Your MadLib is: ")
print()

print(f"Long past the stars of {planet.title()}, there once lived a {animal.lower()}.")
print(f"It was a very {adjective_one.lower()} creature with lots of {noun_one.lower()} on it's planet. ")
print(f"One bright {day_of_week.title()} there was an attack of living {food_one.upper()}! What else could the creature do but {verb_one.lower()}. ")
print(f"Before the creature knew it, from the ground came a bunch of {food_two.lower()}'s! The creature was {emotion.lower()} about all the food monsters. ")
print(f"In order to make things right, he had to {verb_two.lower()}. Once the smoke cleared, the creature was surrounded by all the {adjective_three.lower()} people of {city.title()}. ")
print()
print("THE END")