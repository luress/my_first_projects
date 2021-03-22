import random

winning_cases = {
    'water': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
    'dragon': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
    'devil': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
    'lightning': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
    'gun': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
    'rock': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
    'fire': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
    'scissors': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
    'snake': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
    'human': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
    'tree': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
    'wolf': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
    'sponge': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
    'paper': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
    'air': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper']
}

losing_cases = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}


def olds_game(player_score:  int):
    while True:
        choices = input()
        if choices == "!exit":
            print("Bye!")
            exit(0)
        elif choices == "!rating":
            print(f"Your rating: {player_score}")
        elif choices in ["rock", 'paper', 'scissors']:
            player_score += who_win(choices)
        else:
            print("Invalid input")
            continue


def modern_game(options, score):
    while True:
        computer = random.choice(options)
        choices = input()
        if choices == computer:
            print(f"There is a draw ({computer})")
            score += 50
        elif choices in winning_cases and computer in winning_cases.get(choices):
            print(f"Well done. The computer chose {computer} and failed")
            score += 100
        elif choices in losing_cases and computer in losing_cases.get(choices):
            print(f"Sorry, but the computer chose {computer}")
        elif choices == "!rating":
            print(f'Your rating: {score}')
        elif choices == "!exit":
            print('Bye!')
            exit(0)
        else:
            print("Invalid input")
            continue


def who_win(wish):
    computer_choice = random.choice(["rock", 'paper', 'scissors'])
    anti_player_choice = 'scissors' if wish == "paper" else "rock" if wish == "scissors" else "paper"
    if computer_choice == anti_player_choice:
        print(f"Sorry, but the computer chose {computer_choice}")
        return 0
    elif computer_choice == wish:
        print(f"There is a draw ({computer_choice})")
        return 50
    else:
        print(f"Well done. The computer chose {computer_choice} and failed")
        return 100


def check_score(player_name:  str):
    score_file = open('rating.txt', 'r')
    score = 0
    for line in score_file:
        temp = line.split()
        if temp[0] == name:
            score = int(temp[1])
            break
    score_file.close()
    return score


def check_win(player_opinion):
    pass


def read_game_options(options: str):
    return options.split(',')


name = input("Enter your name:")
print(f"Hello,", name)
option = input()
print("Okay, let's start")
if option:
    game_options = read_game_options(option)
    modern_game(game_options, check_score(name))
else:
    olds_game(check_score(name))






