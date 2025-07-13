#function
def create_greeting(name):
    message = (
        f"Hello {name}, welcome to the GDG Web Development Team! "
        "You're doing great, and I truly believe that someday you'll be an amazing developer. "
        "Life may feel challenging right now, and programming can be overwhelming at times, "
        "but remember, all your hard work will pay off in the end. "
        "Keep pushing forward, you're on the right path!"
    )
    return message

#main
try:
    user_name = input("Please enter your name: ")
    
    greeting = create_greeting(user_name)
    print("\nThe greeting message is:")
    print(greeting)

except ValueError:
    print("Invalid input: Please enter a valid name.")
