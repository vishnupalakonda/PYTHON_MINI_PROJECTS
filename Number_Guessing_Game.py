import random
def start_game():
    print("\n+================================+")
    print("|       Number Guessing Game     |")
    print("+================================+")
    print("\nChoose Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    try:
        difficulty = int(input("Choose Difficulty: "))
        if difficulty == 1:
            max_number = 50
            attempts = 10
        elif difficulty == 2:
            max_number = 100
            attempts = 7
        elif difficulty == 3:
            max_number = 200
            attempts = 5
        else:
            print("Invalid Difficulty!")
            return
        secret_number = random.randint(1, max_number)
        score = 100
        print("\n+================================+")
        print("|          Game Started!         |")
        print("+================================+")
        print(f"Guess a number between 1 and {max_number}")
        print(f"You have {attempts} attempts.")
        for attempt in range(1, attempts + 1):
            try:
                guess = int(
                    input(f"\nAttempt {attempt}/{attempts}: ")
                )
                if guess < 1 or guess > max_number:
                    print(
                        f"Enter a number between 1 and {max_number}."
                    )
                    continue
                if guess == secret_number:
                    print("\n+================================+")
                    print("|       Correct Answer!          |")
                    print("+================================+")
                    print(
                        f"You guessed it in {attempt} attempts!"
                    )
                    print(f"Your Score: {score}")
                    return
                elif guess < secret_number:
                    print("Too Low!")
                else:
                    print("Too High!")
                score -= 10
            except ValueError:
                print("Please enter a valid number!")
        print("\n+================================+")
        print("|           Game Over!           |")
        print("+================================+")
        print(f"The correct number was: {secret_number}")
        print(f"Your Score: {score}")
    except ValueError:
        print("Please enter a valid difficulty!")
while True:
    print("\n+================================+")
    print("|       NUMBER GUESSING GAME     |")
    print("+================================+")
    print("|  1. Start Game                 |")
    print("|  2. Exit                       |")
    print("+================================+")
    try:
        choice = int(
            input("Choose an Option From 1 To 2: ")
        )
        if choice == 1:
            start_game()
        elif choice == 2:
            print("\n+================================+")
            print("|       Thanks For Playing!      |")
            print("+================================+")
            break
        else:
            print("Invalid Choice!")
    except ValueError:
        print("Please Enter a Valid Number!")