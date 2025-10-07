# Thingy

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
    
def option_selection(options, subject, multi = False):
    max = len(options)
    print("\n")
    if (multi):
        print("*"*5, f" {subject} SELECTIONS ", "*"*5)
    else:
        print("*"*5, f" {subject} SELECTIONS - Choose as many as you like", "*"*5)
    if multi:
        option_list = []
    while True:
        i = 0
        for option in options:
            print(f"{i+1}. {option}")
            i += 1
        print("*"*30, "\n")
        selected_option = force_number(f"Select an option to add (1-{max}): ", True, 1, max)
        print(f"You selected '{options[selected_option-1]}'")
        if multi:
            if selected_option == max:
                return option_list
            else:
                option_list.append(options[selected_option-1])
        else:
            return options[selected_option-1]
    
        
def force_phone(min, max):
    while True:
        unverified_number = str(input("Your mobile phone number: "))
        if len(unverified_number) < min or len(unverified_number) > max or not unverified_number.isnumeric():
            print(f"Your phone number must only have {min}-{max} numbers.")
        else:
            validated_number = unverified_number
            return validated_number
        
def print_order(order):
    file = open("sams_sandwich.txt", "a")
    file.write("\n****Customer order****\n")
    for item in order:
        if type(item) is list:
            for i in item:
                file.write(i+"\n")
                print(i)
        else:
            file.write(item+"\n")
            print(item)



bread_options = ["White", "Wholemeal", "Malted Rye", "Flatbread", "Italian", "No bread"]
meat_options = ["Pastrami", "Pepperoni", "Turkey", "Chicken", "Champaign Ham", "No meat"]
cheese_options = ["Cheddar", "Mozzarella", "Edam", "Camembert", "No cheese"]
salad_options = ["Caesars salad", "Small salad", "Large salad", "Blue salad", "Red Salad", "No salad"]
dressing_options = ["Sulfuric acid", "Balsamic vinegar", "Sam's Special Dressing", "No dressing"]

selected_bread = option_selection(bread_options, "BREAD")
selected_meat = option_selection(meat_options, "MEAT")
selected_cheese = option_selection(cheese_options, "CHEESE")
selected_salad = option_selection(salad_options, "SALAD", True)
selected_dressing = option_selection(dressing_options, "DRESSING")

first_name = force_name("Enter your first name: ", 3, 20)
last_name = force_name("Enter your last name: ", 3, 20)
phone_number = force_phone(9, 12)

sandwich_order = first_name, last_name, phone_number, selected_bread, selected_meat, selected_cheese, selected_salad, selected_dressing

print_order(sandwich_order)