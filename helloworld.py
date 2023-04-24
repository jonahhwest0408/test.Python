print("Please enter the following information:")

print()

# Ask for the basic questions
first = input("First name: ")
last = input("Last name: ")
email = input("Email: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID number: ")

# Ask for additional information
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month = input("Month: ")
training = input("Training complete, y/n: ")

# Print ID card
print()
print("---------------------------------")
print("\nThe ID Card is: ")
print(f"{last.upper()}, {first.capitalize()}")
print(f"{job_title.title()}")
print()
print(f"ID {id_number.lower()}")
print(f"Phone Number: {phone_number}")
print()

# Additional information
print(f"Hair: {hair_color.capitalize():12} Eyes: {eye_color.capitalize()}")
print(f"Month: {month.capitalize():11} Training: {training.capitalize()}")
print()
print("----------------------------------")
print()

print("Thank you for your information.")
print("----------------------------------")