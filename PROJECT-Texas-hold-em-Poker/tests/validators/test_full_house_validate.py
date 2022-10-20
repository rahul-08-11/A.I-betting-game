

import unittest


from poker.card import Card
from poker.validators import FullHouseValidator

class TestFullHouse(unittest.TestCase):
    def setUp(self) -> None:

        self.three_of_diamonds=Card(rank="3",suit="Diamonds")
        self.three_of_clubs=Card(rank="3",suit="Clubs")
        self.three_of_spades=Card(rank="3",suit="Spades")
        self.five_of_hearts=Card(rank="5",suit="Hearts")
        self.five_of_clubs=Card(rank="5",suit="Clubs")

        self.cards=[
            Card(rank="2",suit="Diamonds"),
            self.three_of_clubs,
            self.three_of_diamonds,
            self.three_of_spades,
            self.five_of_clubs,
            self.five_of_hearts,
            Card(rank="Queen",suit="Hearts")

        ]



    def test_to_determine_if_one_pair_and_three_kind_exist_in_collection(self):
        validator=FullHouseValidator(cards=self.cards)
        self.assertEqual(validator.is_valid(),True)
    
    def test_return_five_cards_of_three_kind_and_pair(self):

        validator=FullHouseValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [ 
                self.three_of_clubs,
                self.three_of_diamonds,
                self.three_of_spades,
                self.five_of_clubs,
                self.five_of_hearts
            ]
        )