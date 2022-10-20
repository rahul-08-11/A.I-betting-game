import unittest


from poker.card import Card
from poker.validators import RoyalFlushValidator


class TestRoyalFLushValidator(unittest.TestCase):

    def setUp(self):
        self.ten_of_diamonds=Card(rank="10",suit="Diamonds")
        self.jake_of_diamonds=Card(rank="Jake",suit="Diamonds")
        self.queen_of_diamonds=Card(rank="Queen",suit="Diamonds")
        self.king_of_diamonds=Card(rank="King",suit="Diamonds")
        self.ace_of_diamonds=Card(rank="Ace",suit="Diamonds")
 
        self.cards= [ 
            Card(rank="5",suit="Spades"),
            Card(rank="8",suit="Clubs"),
            self.ten_of_diamonds,
            self.jake_of_diamonds,
            self.queen_of_diamonds,
            self.king_of_diamonds,
            self.ace_of_diamonds
        ]

    def test_hand_have_flush_and_straight_with_last_five_high_rank(self):
        validator=RoyalFlushValidator(cards=self.cards)

        self.assertEqual(validator.is_valid(),True)

    def test_return_royal_flush_cards(self):
        validator=RoyalFlushValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_card(),
            [ 
            self.ten_of_diamonds,
            self.jake_of_diamonds,
            self.queen_of_diamonds,
            self.king_of_diamonds,
            self.ace_of_diamonds

            ]
        )

