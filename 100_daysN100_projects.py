# 100_daysN100_projects.py (main runner)
 
 # if __name__ == "__main__": \\ Gatekeeper statement to control when to execute this code.
  # When you run this file directly: Python sets __name__ == "__main__". 
  # The condition is true, and the code on lines 8 and 9 (calling the functions) will execute.
  # If you were to import this file elsewhere: (e.g., if you wrote import 100_daysN100_projects inside a different script). 
  # The code on lines 8 and 9 would not run automatically.

if __name__ == "__main__":     
 day = int(input("Which Day's Project do you want to execute? "))

 if day == 1:
   from day1 import get_user_details, generate_welcome_message

   name, hobby = get_user_details()
   generate_welcome_message(name, hobby)

 elif day == 2:    
   from day2 import greet_user, greeting_message
 
   name, hobby, colour, yob = greet_user()
   greeting_message(name, hobby, colour, yob)

 else:
    print("Invalid day selected.")

# Pause to keep terminal open (remove if not needed)
    input("Press Enter to exit.")    