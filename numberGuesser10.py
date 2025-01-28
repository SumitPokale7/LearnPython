import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

number = random.randint(1, 100)


def check_Ans(user_Guess, actual_Ans, turns):
    if user_Guess > actual_Ans:
        print("Too High.")
        return turns - 1
    elif user_Guess < actual_Ans:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_Ans}.")


def set_Difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 & 100.")
    answer = random.randint(1, 100)

    turns = set_Difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        turns = check_Ans(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"Pssst, the correct answer is {answer}")
            return
        elif guess != answer:
            print("Guess again.")


game()
