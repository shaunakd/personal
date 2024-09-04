from typing import Optional

def get_prob_blue_given_n(num_of_red_cards: int, num_of_blue_cards: int, n: Optional[int]) -> float:
  assert num_of_red_cards == num_of_blue_cards, "There must be as many reds as blues."
  red_cards = range(1, num_of_red_cards + 1)
  blue_cards = range(1, num_of_blue_cards + 1)
  assert n in red_cards and n in blue_cards, "The card number given must be within range."
  num_of_blue_cards = (num_of_blue_cards + 1)/2
  prob_blue_given_n = prob_
