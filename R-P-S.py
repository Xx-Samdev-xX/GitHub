import random
import time

choice = ("rock", "paper", "scissors")

print("🎮 ---------ROCK PAPER SCISSORS---------🎮\n")
time.sleep(1.25)

while True:
    # Ask the user how long the match should be
    while True:
        try:
            rounds = int(input("Play best of (3, 5, or 7)? "))
            if rounds in (3, 5, 7):
                break
            else:
                print("Please choose 3, 5, or 7 only.\n")
        except ValueError:
            print("Enter a valid number.\n")

    # Calculate how many wins needed to win the match
    wins_needed = (rounds // 2) + 1

    user_score = 0
    computer_score = 0
    ties = 0

    print(f"\nStarting BEST OF {rounds} match! First to {wins_needed} wins.\n")
    time.sleep(1.25)


    while True:
        # Check if match is over
        if user_score == wins_needed or computer_score == wins_needed:
            print("GAME OVER!!")
            if user_score > computer_score:
                print("🏆 YOU WIN THE MATCH!! 🥳")
                time.sleep(1.25)

            else:
                print("💻 COMPUTER WINS THE MATCH 💩")
                time.sleep(1.25)


            again = input("Play again? (Y/N): ").lower()
            if again == 'y':
                print("\n...STARTING NEW MATCH...\n")
                time.sleep(1.25)

                break
            else:
                if user_score < computer_score:
                  print("Wow what a quiter goodbye trash ahh ning ning 💩💩🪠")
                elif  user_score > computer_score:
                    print("Goodbye thanks for playing👋")
                    time.sleep(1)
                    print("Congrats for winning👏👏")
                time.sleep(1.25)

                exit()

        # Get user input
        user = input("Enter your choice (rock, paper, scissors or 'quit'): ").lower()

        if user == "quit":
            print("You quit — computer wins by default 💀")
            time.sleep(1.25)

            exit()

        if user not in choice:
            print("Invalid choice!\n")
            time.sleep(1.25)

            continue

        # Computer choice
        computer = random.choice(choice)
        print(f"Computer chose: {computer}")
        time.sleep(1)


        # Determine result
        if user == computer:
            print("IT'S A TIE!\n")
            time.sleep(1)

            ties += 1
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'scissors' and computer == 'paper') or \
             (user == 'paper' and computer == 'rock'):
            print("YOU WIN THIS ROUND!\n")
            time.sleep(1)

            user_score += 1
        else:
            print("YOU LOSE THIS ROUND!\n")
            time.sleep(1)

            computer_score += 1

        # Show score
        time.sleep(1.25)

        print(f"Score -> You: {user_score} | Computer: {computer_score} | Ties: {ties}\n")
