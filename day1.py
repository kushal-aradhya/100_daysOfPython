# Day-1: Welcome Message Generator

def get_user_details():
    """Collect user name and hobby from input."""
    name = input("What is your name? ")
    hobby = input("What is your hobby? ")
    return name, hobby

def generate_welcome_message(name, hobby):
    """Generate and print the personalized welcome message."""
    print("\n---Welcome Message---")
    print(f"Hello, {name}!")
    print("Welcome to the world of Python programming.")
    print(f"It's great to know that you love {hobby}.")
    print("Get ready to make some amazing projects.")

