import random

data = [
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 615,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 485,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 429,
        'description': 'Singer, Actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 400,
        'description': 'Model, Entrepreneur',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 397,
        'description': 'Actor, Former Wrestler',
        'country': 'United States'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 380,
        'description': 'Singer, Actress',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 364,
        'description': 'Media Personality, Businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 318,
        'description': 'Singer, Actress',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 310,
        'description': 'Media Personality, Businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 291,
        'description': 'Singer',
        'country': 'Canada'
    }
]

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/      
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def highGame(first_Player,  second_Player):

    if first_Player['follower_count'] > second_Player['follower_count']:
        return 'A'
    elif first_Player['follower_count'] < second_Player['follower_count']:
        return 'B'
    elif first_Player['follower_count'] == second_Player['follower_count']:
        return 'A'
    else:
        return


score = 0
game_Over = False
second_Player = random.choice(data)


while not game_Over:
    print(logo)
    first_Player = second_Player
    second_Player = random.choice(data)

    print(f"Compare A: {first_Player['name']}, a {first_Player['description']}, from {first_Player['country']}")
    print(vs)
    print(f"Aganist B: {second_Player['name']}, a {second_Player['description']}, from {second_Player['country']}")
    choosen_Option = input("Who has more followers? Type 'A' or 'B': ").capitalize()

    ans = highGame(first_Player, second_Player)

    if choosen_Option == ans:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_Over = True
