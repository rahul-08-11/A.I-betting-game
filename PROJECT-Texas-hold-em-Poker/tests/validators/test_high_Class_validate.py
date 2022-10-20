import unittest
from wsgiref.validate import validator

from poker.card import Card
from poker.validators import HighClassValidator


class TestHighClass(unittest.TestCase):
    def test_validate_hand_have_a_high_card(self):

        cards=[ 
            Card(rank="Ace",suit="Spades"),
            Card(rank="5",suit="Diamonds")

        ]

        validator=HighClassValidator(cards=cards)
     

        self.assertEqual(validator.is_valid(),True)

    def test_return_high_card_from_collection(self):
        ace_of_spade=Card(rank="Ace",suit="Spades")
        cards=[ 

            Card(rank="5",suit="Diamonds"),
            Card(rank="King",suit="Diamonds"),
            Card(rank="8",suit="Clubs"),
            Card(rank="9",suit="Spades"),
            ace_of_spade
        ]

        validator=HighClassValidator(cards=cards)

        self.assertEqual(
            validator.valid_card(),
            [ace_of_spade]
        )
