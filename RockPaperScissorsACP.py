import random

moves = ["rock", "paper", "scissors"]

def checkWin(userChoice, aiChoice):
    if aiChoice == userChoice:
        print("Its a tie!")
    elif userChoice == "rock" and aiChoice == "scissors":
            print("Rock smashes scissors, you win!")
    elif userChoice == "paper" and aiChoice == "rock":
        print("Paper covers rock, you win!")
    elif userChoice == "scissors" and aiChoice == "paper":
        print("Scissors cuts paper, you win!")
    else:
        print("You lose! Try again next time.")

def playGame():
    userChoice = input("Enter your move: Rock, Paper, or Scissors. ").lower()
    if userChoice not in moves:
        print("Invalid input. Try again.")
        return

    aiChoice = random.choice(moves)
    print(f"You chose: {userChoice}")
    print(f"The AI chose: {aiChoice}")
    
    checkWin(userChoice, aiChoice)



while True:
    playGame()
    playAgain = input("Do you want to play again? Yes/No? ").lower()
    if playAgain != "yes":
        print("Thanks for playing! See you next time!")
        break