import unittest

from poker.card import Card
from poker.validators import ThreeOfKind

class TestThreeOfKind(unittest.TestCase):

    def test_hand_have_three_of_kind(self):
        three_of_diamonds=Card(rank="3",suit="Diamonds")
        three_of_clubs=Card(rank="3",suit="Clubs")
        three_of_spades=Card(rank="3",suit="Spades")
        cards=[
            three_of_clubs,
            three_of_diamonds,
            three_of_spades,
            Card(rank="Ace",suit="Hearts"),
            Card(rank="5",suit="Clubs")
        ]

        validator=ThreeOfKind(cards=cards)
        self.assertEqual(validator.is_valid(),True)


    def test_return_three_of_kind_of_card(self):
        three_of_diamonds=Card(rank="3",suit="Diamonds")
        three_of_clubs=Card(rank="3",suit="Clubs")
        three_of_spades=Card(rank="3",suit="Spades")
        cards=[
            three_of_clubs,
            three_of_diamonds,
            three_of_spades,
            Card(rank="Ace",suit="Hearts"),
            Card(rank="5",suit="Clubs")
        ]


        validator=ThreeOfKind(cards=cards)
        self.assertEqual(
            validator.valid_cards(),
            [ three_of_clubs,three_of_diamonds,three_of_spades]
        
        )

