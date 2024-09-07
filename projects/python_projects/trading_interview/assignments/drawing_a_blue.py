"""Project 9"""

import random
from typing import Optional

def get_prob_blue_given_n(num_of_red_cards: int, num_of_blue_cards: int, n: Optional[int]) -> float:
  assert num_of_red_cards == num_of_blue_cards, "There must be as many reds as blues."
  red_cards = range(1, num_of_red_cards + 1)
  blue_cards = range(1, num_of_blue_cards + 1)
  assert n in red_cards and n in blue_cards, "The card number given must be within range."
  num_of_blue_cards = (num_of_blue_cards + 1)/2
  prob_blue_given_n = 0
  return prob_blue_given_n


def simulate(n_cards: int) -> None:
  total_3_count, blue_3_count = 0, 0
  
  # generating red and blue cards
  red_cards, blue_cards = list(range(1, n_cards + 1)), list(range(1, n_cards + 1))
  
  # removing (n_cards + 1)/2 cards
  blue_cards_to_remove = random
  