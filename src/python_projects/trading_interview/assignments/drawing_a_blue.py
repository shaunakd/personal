"""
Project 9: Drawing a Blue

You have 13 red cards and 13 blue cards, labeled from 1 to 13. You remove 7 blue cards at random.
What is the probability that the card drawn is blue given that the number on the card is 3? Please write a simulation that has the probability as an output.
"""

import random


def run_simulation(n_simulations: int, n_cards: int) -> float:
    # initialising counters
    n_3, n_blue_3 = 0, 0
    
    # simulation cannot run if there are no cards
    if n_cards > 0:
        for _ in range(n_simulations):
            # generating red and blue cards
            red_cards, blue_cards = list(range(1, n_cards + 1)), list(range(1, n_cards + 1))

            # removing (n_cards + 1)/2 cards
            n_cards_to_remove = n_cards // 2 if n_cards % 2 else n_cards // 2 + 1
            blue_cards_to_remove = random.sample(blue_cards, n_cards_to_remove)
            blue_cards = [card for card in blue_cards if card not in blue_cards_to_remove]

            # combining remaining cards
            cards = [("red", card) for card in red_cards] + [
                ("blue", card) for card in blue_cards
            ]

            # drawing a card and checking if it is a 3
            card: tuple[str, int] = random.choice(cards)
            if card[1] == 3:
                n_3 += 1
                if card[0] == "blue":
                    n_blue_3 += 1

    prob_blue_given_3 = (
        0 if n_3 == 0 else n_blue_3 / n_3
    )  # avoiding division by 0 if no 3s were drawn
    return prob_blue_given_3


n_simulations = 1000000
prob_blue_given_3 = run_simulation(n_simulations=n_simulations, n_cards=13)
print(f"Probability that the card is blue given it is a 3: {prob_blue_given_3:.4f}")
