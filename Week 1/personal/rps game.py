import random
c_moves = ["Rock", "Paper", "scissor"]
computer = c_moves[random.randint(0,2)]
player = False
while player == False:
    player = input("Enter your move:")
    if computer == player:
        print("its a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("you loose, computer wins!")
        else:
            print("You win!")
    elif player == "Paper":
        if computer == "Scissor":
            print("you loose, computer wins!")
        else:
                print("You win!")
    elif player == "Scissor":
        if computer == "Rock":
            print("you loose, computer wins!")
        else:
                print("You win!")
    new_game = input("do you want to play another round? (y/n")
    if new_game == "y":
        player = False
    else:
        print("thanks for playing!!!")
        break;