from art import logo, vs
from game_data import data
import random

#display art
print(logo)

# generate random accounts from game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)
# format account data into printable format

# ask user to guess

# check if user is correct
## get follower count of each account
## Use if statement to check if correct

# give user feedback

# Score keeping

# make game repeatable.

# make account at position B become next account at position A

# game clears the screen