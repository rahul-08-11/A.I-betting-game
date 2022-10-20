import unittest

from poker.validators import  TwoPairValidator
from poker.card import Card


class TestTwoPairValidator(unittest.TestCase):
    def test_hand_have_two_pair_card(self):
            three_of_diamonds=Card(rank="3",suit="Diamonds")
            three_of_clubs=Card(rank="3",suit="Clubs")
            ace_of_hearts=Card(rank="Ace",suit="Hearts")
            ace_of_clubs=Card(rank="Ace",suit="Clubs")

            cards=[ 
            three_of_clubs,
            three_of_diamonds,
            Card(rank="5",suit="Spades"),
            ace_of_clubs,
            ace_of_hearts
        ]
            validator=TwoPairValidator(cards=cards)

            self.assertEqual(validator.is_valid(),True)

    def test_return_two_pair_of_cards(self):
            three_of_diamonds=Card(rank="3",suit="Diamonds")
            three_of_clubs=Card(rank="3",suit="Clubs")
            ace_of_hearts=Card(rank="Ace",suit="Hearts")
            ace_of_clubs=Card(rank="Ace",suit="Clubs")

            cards=[ 
            three_of_clubs,
            three_of_diamonds,
            Card(rank="5",suit="Spades"),
            ace_of_clubs,
            ace_of_hearts
        ]
            validator=TwoPairValidator(cards=cards)

            self.assertEqual(
                validator.valid_cards(),
                [three_of_clubs,three_of_diamonds,ace_of_clubs,ace_of_hearts]
            )
        




