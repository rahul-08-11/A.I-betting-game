import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class TestStraightFlush(unittest.TestCase):
    def setUp(self) -> None:
        self.three_of_diamonds=Card(rank="3",suit="Diamonds")
        self.four_of_diamonds=Card(rank="4",suit="Diamonds")
        self.five_of_diamonds=Card(rank="5",suit="Diamonds")
        self.six_of_diamonds=Card(rank="6",suit="Diamonds")
        self.seven_of_diamonds=Card(rank="7",suit="Diamonds")

        self.cards=[ 
            Card(rank="2",suit="Clubs"),
            self.three_of_diamonds,
            self.four_of_diamonds,
            self.five_of_diamonds,
            self.six_of_diamonds,
            self.seven_of_diamonds,
            Card(rank="Queen",suit="Diamonds")
        ]

    def test_to_determine_it_consist_of_straight_and_flush(self):

        validator=StraightFlushValidator(cards=self.cards)

        self.assertEqual(validator.is_valid(),True)

    def test_return_valid_cards(self):
        validator=StraightFlushValidator(cards=self.cards)

        self.assertEqual(validator.valid_card(),
        [ 
            self.three_of_diamonds,
            self.four_of_diamonds,
            self.five_of_diamonds,
            self.six_of_diamonds,
            self.seven_of_diamonds

        ])
