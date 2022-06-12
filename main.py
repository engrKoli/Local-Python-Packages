import random


possible_options = ["R", "P", "S"]

while True:
    user_action = input("Enter a choice (R, P, S):  ").upper()
    if user_action not in possible_options:
       continue
    computer_action = random.choice(possible_options)

     
    print(f"Player {user_action}, CPU {computer_action}")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R" and computer_action == "S":
        print("Rock smashes scissors! You won!")

    elif user_action == "P" and computer_action == "R":
        print("paper covers rock! You won!")    

    elif user_action == "S" and computer_action == "P":
        print("Scissors cuts paper! You won!")        
    
    else:
        print("You lost!")
    