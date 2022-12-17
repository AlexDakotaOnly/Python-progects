import random

exit = False
user_points = 0
computer_points = 0


while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Your score: " + str(user_points) + ". Computer score: " + str(computer_points))
        print("Game ended.")

        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("A tie!")
        elif computer_input == "paper":
            print("Paper covers your rock. You loose!")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your rock broke scissors. You win!")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "paper":
            print("A tie!")
        elif computer_input == "rock":
            print("Your paper covers rock. You win!")
            user_points += 1
        elif computer_input == "scissors":
            print("Scissors cut your paper. You loose!")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "scissors":
            print("A tie!")
        elif computer_input == "paper":
            print("Your scissors cut paper. You win!")
            user_points += 1
        elif computer_input == "rock":
            print("Rock broke your scissors. You loose!")
            computer_points += 1

    elif user_input != "rock" and user_input != "paper" and user_input != "scissors" and user_input != "exit":
        print("I don't understand!")





