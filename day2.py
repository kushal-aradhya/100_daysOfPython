# Day-2 : Personalised greeting program

def greet_user():
    name = input("What's your name? ")
    hobby = input("What's your favourite hobby? ")
    colour = input("What's your favourite colour? ")
    yob = input("When is your year of birth? (YYYY) ")
    return name, hobby, colour, yob
    
def greeting_message(name, hobby, colour, yob):    
    print("\n---Personalised Greeting---")
    age = 2024 - int(yob)
    print(f"Hello {name}! It's great that you enjoy {hobby} at the age of {age}. By the way, {colour} is a beautiful colour!")  
