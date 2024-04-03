import os
import art
os.system('cls||clear')

print(art.logo)

new_record = {}
name_list = []

def name_check():
    name_check = True
    while name_check:
        name = input('What is your name? ')
        if name in name_list:
            print('Please choose another name. This name has already taken.')
        else:
            name_list.append(name)
            new_record['name'] = name
            name_check = False

def bid_check():
    bid_check = True
    while bid_check:
        bid = input('What is your bid? $')
        if not bid.isdigit():
            print('Please input a number.')
        else:
            bid = int(bid)
            new_record['bid'] = bid
            bid_check = False


bid_continue = True
all_bidding = []
while bid_continue:
    name_check()
    bid_check()
    all_bidding.append(new_record)
    new_record = {}

    replay = input("Are there any other bidder? Type 'yes' or 'no'\n")
    os.system('cls||clear')
    if replay == 'no':
        bid_continue = False

highest_bid = 0
winner = ''
for i in all_bidding:
    if i['bid'] > highest_bid:
        highest_bid = i['bid']
        winner = i['name']
print(f'The winner is {winner} with a bid of ${highest_bid}.')