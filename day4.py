import random

# Rock
Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
images = [Rock, Paper, Scissors]

user_Input = int(input('What do you choose? Type 0 for Rock,'
                       '1 for Paper or 2 for Scissors.\n'))

if user_Input >= 0 and user_Input <= 2:
    print(images[user_Input])

print("Computer chose")
computer_Input = random.randint(0, 2)
print(images[computer_Input])

if user_Input >= 3 or user_Input < 0:
    print("You typed an invalid number. You lose!")
elif user_Input == 0 and computer_Input == 2:
    print("You Win!")
elif computer_Input == 0 and user_Input == 2:
    print("You lose!")
elif computer_Input > user_Input:
    print("You lose!")
elif computer_Input < user_Input:
    print("You Win!")
elif user_Input == computer_Input:
    print("It's a Draw!")
