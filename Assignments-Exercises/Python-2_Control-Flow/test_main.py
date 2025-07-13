try: # try catch
    age_input = input("Please enter your age: ") # get input
    age = int(age_input) #convert string into integer
    
    # conditional statements
    
    if age < 0:
        print("Invalid input: Age cannot be negative.")
    elif age < 13:
        print("You are categorized as: Child")
    elif age <= 19:
        print("You are categorized as: Teenager")
    elif age <= 59:
        print("You are categorized as: Adult")
    else:
        print("You are categorized as: Senior")

except ValueError:
    print(f"Invalid input: invalid literal for int() with base 10: '{age_input}'")