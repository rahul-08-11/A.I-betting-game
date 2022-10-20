import unittest

from poker.validators import PairCardValidator 
from poker.card import Card

class TestPairCardValidator(unittest.TestCase):
    def test_hand_have_a_pair_card(self):

        cards=[ 
            Card(rank="8",suit="Spades"),
            Card(rank="8",suit="Diamonds")
        ]

        validator=PairCardValidator(cards=cards)

        self.assertEqual(validator.is_valid(),True)

    def test_return_pair_of_cards(self):
        eight_of_spades=Card(rank="8",suit="Spades")
        eight_of_diamonds=Card(rank="8",suit="Diamonds")

        cards=[ 
            Card(rank="3",suit="Spades"),
            eight_of_diamonds,
            eight_of_spades,
            Card(rank="6",suit="Diamonds"),
            Card(rank="Ace",suit="Clubs")

        ]

        validator=PairCardValidator(cards=cards)

        self.assertEqual(
            validator.valid_card(),
            [ eight_of_diamonds,eight_of_spades]
            )


    
    



