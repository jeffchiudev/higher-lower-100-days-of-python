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
  while winning == True: 
    A = assign(data)
    print(A[0]['name'])
    B = assign(data)
    print(B[0]['name'])
    winning = False

high_low(data)