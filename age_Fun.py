import Validation

name = input("Please enter your name")

number = Validation.get_and_validate_number(120)

# It's your birthday!!
number += 1
print(f"Hello {name} you are now {number} years old!")