import random

HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''']

word_List = ["aardvark", "baboon", "camel"]

lives = 6

chosen_Word = random.choice(word_List)
print(chosen_Word)

placeholder = ""

for blank in chosen_Word:
    placeholder += "_"

print(placeholder)

game_Over = False
correct_List = []

while not game_Over:
    print(f'********************************{lives}/6 LIVES LEFT**************'
          '*******************************')
    guess = input("Guess a letter: ").lower()

    if guess in correct_List:
        print(f'You\'ve already guessed {guess}')

    display_Letter = ""

    for letter in chosen_Word:
        if letter == guess:
            display_Letter += letter
            correct_List.append(letter)
        elif letter in correct_List:
            display_Letter += letter
        else:
            display_Letter += "_"

    print(display_Letter)

    if guess not in chosen_Word:
        print(f"You Guessed {guess}, that's not in the word. You losa a life.")
        lives -= 1
        print(HANGMANPICS[lives])
        if lives == 0:
            game_Over = True
            print('********************************YOU LOSE*****************'
                  '*****************************')

    if "_" not in display_Letter:
        game_Over = True
        print('********************************YOU WIN**********************'
              '************************')
