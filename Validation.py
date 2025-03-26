def get_and_validate_number(upperlimit, lowerlimit = 0):
    number_as_string = input("Please enter the number")
    number = -1
    valid_flag = False
    while valid_flag == False:
        while not number_as_string.isnumeric():
            print(f"Invalid number: must be numeric")
            number_as_string = input("Please enter the number")
        number = int(number_as_string)
        if number >= lowerlimit and number <= upperlimit:
            valid_flag = True
        else:
            number_as_string = "X"

    return number

