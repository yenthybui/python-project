import os

from game_data import data
import art
import random

def clear_screen():
    os.system("cls|clear")

clear_screen()

def random_dict():
    dict = random.choice(data)
    data.remove(dict)
    return dict

a = random_dict()
print(art.logo)
print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")

b = random_dict()
print(art.vs)
print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

def result(a,b):
    if a['follower_count'] > b['follower_count']:
        return (a,"A")
    else:
        return (b, "B")

score = 0
while True:
    response = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear_screen()

    correct_answer = result(a,b)
    if response == correct_answer[1]:
        score += 1
        print(f"You're right. Current score: {score}")
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        # game_over = True
        exit()

    a = correct_answer[0]
    print(art.logo)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")

    b = random_dict()
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")