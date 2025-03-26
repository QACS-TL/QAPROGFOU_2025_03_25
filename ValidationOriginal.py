def validate_age():
    age_as_string = input("Please enter your age")
    age = -1
    valid_flag = False
    while valid_flag == False:
        while not age_as_string.isnumeric():
            print(f"Invalid age: must be numeric")
            age_as_string = input("Please enter your age")
        age = int(age_as_string)
        if age >= 0 and age <= 120:
            valid_flag = True
        else:
            age_as_string = "X"

    return age

name = input("Please enter your name")

age = validate_age()

# It's your birthday!!
age += 1
print(f"Hello {name} you are now {age} years old!")