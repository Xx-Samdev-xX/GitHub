import random
import time
import winsound

while True:
    secret = random.randint(1, 20)
    nguess=0
    times = 1


    try:
        easy_hard = int(input("1.EASY(10 CHANCES)\n2.HARD(5 CHANCES)\n>>>"))

        if easy_hard ==1:
            nguess=10

        elif easy_hard ==2:
            nguess=5

        else:
            print("ENTER 1 / 2")
            continue

    except ValueError:
        print("WRONG INPUT")
        continue




    print("\nSTARTING A NEW GAME")
    print(f"YOU HAVE {nguess} CHANCES TO GUESS THE NUMBER\nGL 😁")


    while nguess > 0:
        try:
            guess = float(input("\nGUESS A WHOLE NUMBER (1 - 20): "))

            if guess.is_integer() is False:
                print("ENTER A WHOLE NUMBER")
                winsound.Beep(600, 150)
                continue

            guess = int(guess)

            if guess < 1 or guess > 20:
                print("❌ Not in range! Try again.")
                winsound.Beep(500, 200)
                continue

            if guess == secret:
                print("\n🎉 NICE, THAT IS CORRECT! 🎉")
                print("WANA TRY YOUR LUCK AGAIN??😃😃")
                winsound.Beep(1000, 200)
                winsound.Beep(1200, 200)
                print(f"You guessed in {times} chance{'s' if times > 1 else ''}.")
                break

            elif guess < secret:
                print("TOO LOW! Try again.")
                winsound.Beep(400, 150)

            else:
                print("TOO HIGH! Try again.")
                winsound.Beep(450, 150)


            nguess -= 1
            times += 1

            print(f"You have {nguess} guesses left.")

            if nguess == 0 and easy_hard == 1:
                print("GAME OVER 😢")
                time.sleep(1)
                print("YOU LOST WITH 10 CHANCES 💩💩")
                time.sleep(1)
                print("YOU'R SO TRAAASHHH HAHA😂😂💩")
                time.sleep(1)
                print("GET A FRICKING LIFE 😂🤣🤣")
                time.sleep(1)
                print("😹😹"*5)
                time.sleep(1)
                print("🤏🤏🧠🧠"*5)
                time.sleep(1)
                print("🤌🤌"*5)
                time.sleep(1)
                print("💩💩💩"*5)
                time.sleep(1)
                print("💩💩💩🤌🤌😹😹"*10)

                print("\nTRY AGAIN IF YOU DARE \nTRASH AAH NINGNING😏😏")
                print("." * 50)
                time.sleep(1)
                winsound.Beep(300, 250)
                winsound.Beep(200, 300)

                break

            elif nguess == 0 and easy_hard == 2:
                print("GAME OVER 😢{time.sleep(0.5)}\nYOU LOST 💩💩")
                print(f"\nThe secret number was {secret} 💁‍♂️💁‍♂️")
                print("\nTRY YOUR LUCK AGAIN IF YOU DARE😏😏")


        except ValueError:
            print("🚫 That’s not even a number! Try again.")
            winsound.Beep(400, 200)

    play_again = input("\nEnter 'y' to Play again? : ").lower()
    if play_again != "y":
        print("Bye! 👋")
        winsound.Beep(800, 200)
        winsound.Beep(600, 200)
        break
