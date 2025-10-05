

def force_name(message, min_length=2, max_length=20):
    # loop until a valid name is entered
    while(True):
        unverified_name = input(message)

        if len(unverified_name) > max_length:
            print(f"Invalid name: too many letters, please enter no more than {max_length}.")
            continue

        if len(unverified_name) < min_length:
            print(f"Invalid name: too few letters, please enter no less than than {min_length}.")
            continue

        if not unverified_name.isalpha():
            print("Invalid name: please use letters only.")
            continue

        # name passed all checks so return it
        return unverified_name.title()
    
def force_number(message, is_int, min=0, max=120):
    # loop until a valid number is entered
    while(True):
        if is_int:
            try:
                unverified_num = int(input(message))
            except:
                print("please enter a whole number with the characters 0-9 only")
                continue
        else:
            try:
                unverified_num = float(input(message))
            except:
                print("please enter a number with the characters 0-9 and . only")
                continue

        if unverified_num > max:
            print(f"Invalid number: your number is too long, please enter a number {max} or less.")
            continue

        if unverified_num < min:
            print(f"Invalid number: your number is too short, please enter a number {min} or more.")
            continue

        # number passed all checks so return it
        return unverified_num