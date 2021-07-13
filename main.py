# break down problem: import game data; randomly select an entry from game_data list of dictionary entries and compare to another item; get user to select which one has a higher follower count.  If user choses wrong, game ends, if correct, 2nd item becomes the first item and is comapred to a new list item.
# make a to do list: import game data, assign random list items to variables, display them in the correct manner, make fx that replaces first list item if user is correct, make fxn to score
# start with the easiest todo
# turn problem into comments
# start coding
# move to next task

import random
import os
from art import logo, vs
from game_data import data

# A = random.sample(data, 1)
# B = random.sample(data, 1)
# test_item_name = [x['description'] for x in A]
# print(A)
# print(B)
# print(test_item_name)

def assign(list):
  return random.sample(list, 1)


def high_low(data):
  winning = True
  score = 0
  print(logo)
  A = assign(data)
  B = assign(data)

  print(f"Compare A: {A[0]['name']}, a {A[0]['description']}, from {A[0]['country']}.")

  print(vs)

  print(f"Compare B: {B[0]['name']}, a {B[0]['description']}, from {B[0]['country']}.") 

  answer = input("Who has more followers? Type 'A' or 'B':")

  if answer == 'A' and A[0]['follower_count'] > B[0]['follower_count']:
    score += 1
    print(f"You're right! Current score: {score}")
  elif answer == 'B' and A[0]['follower_count'] < B[0]['follower_count']:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")

  # while winning == True: 
  #   print(f"{A[0]['name']}, a {A[0]['description']}, from {A[0]['country']}")
  #   print(f"{B[0]['name']}, a {B[0]['description']}, from {B[0]['country']}")
  #   winning = False

high_low(data)