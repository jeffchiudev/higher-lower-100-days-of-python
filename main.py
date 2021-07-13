from art import logo, vs
from game_data import data
import random

# format account data into printable format
def format_data(account):
  """format account data into printable format """
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_desc}, from {account_country}"


#display art
print(logo)

# generate random accounts from game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)
print(f"Against B: {format_data(account_b)}.")

# ask user to guess

# check if user is correct
## get follower count of each account
## Use if statement to check if correct

# give user feedback

# Score keeping

# make game repeatable.

# make account at position B become next account at position A

# game clears the screen