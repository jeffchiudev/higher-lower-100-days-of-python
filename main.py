from art import logo, vs
from game_data import data
import random
import os

# format account data into printable format
def format_data(account):
  """format account data and returns into printable format """
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """use if statement to check answer and returns if correct"""
  if a_followers > b_followers:
    return guess == 'a'
  else: 
    return guess == 'b'


#display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


# make game repeatable.
while game_should_continue: 
  # generate random accounts from game data

  # make account at position B become next account at position A
  account_a = account_b 
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")

  # ask user to guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # check if user is correct
  ## get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

# game clears the screen
  os.system("clear")
  print(logo)
  # give user feedback
  # Score keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}.")





