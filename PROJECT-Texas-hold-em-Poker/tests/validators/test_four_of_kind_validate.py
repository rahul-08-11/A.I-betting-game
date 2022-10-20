import unittest


from poker.card import Card
from poker.validators import FourOfKind

class TestFourOfKind(unittest.TestCase):
    def setUp(self) -> None:
        self.three_of_diamonds=Card(rank="3",suit="Diamonds")
        self.three_of_clubs=Card(rank="3",suit="Clubs")
        self.three_of_spades=Card(rank="3",suit="Spades")
        self.three_of_hearts=Card(rank="3",suit="Hearts")

        self.cards=[
            Card(rank="2",suit="Hearts"),
            self.three_of_clubs,
            self.three_of_diamonds,
            self.three_of_hearts,
            Card(rank="4",suit="Clubs"),
            self.three_of_spades ,    
            Card(rank="Queen",suit="Clubs")

        ]
    def test_have_four_kind_of_same_rank(self):

        validator=FourOfKind(cards=self.cards)

        self.assertEqual(validator.is_valid(),True)

    def test_return_four_kind_of_card(self):
        validator=FourOfKind(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
        [ 
            self.three_of_clubs,
            self.three_of_diamonds,
            self.three_of_hearts,
            self.three_of_spades

        ])
