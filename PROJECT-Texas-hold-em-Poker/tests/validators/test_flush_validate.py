import unittest


from poker.card import Card
from poker.validators import FlushValidator

class TestFLushValidator(unittest.TestCase):
    def setUp(self):
        self.two_of_hearts=Card(rank="2",suit="Hearts")
        self.four_of_hearts=Card(rank="4",suit="Hearts")
        self.seven_of_hearts=Card(rank="7",suit="Hearts")
        self.ace_of_hearts=Card(rank="Ace",suit="Hearts")
        self.five_of_hearts=Card(rank="5",suit="Hearts")
        self.eight_of_hearts=Card(rank="8",suit="Hearts")
        self.nine_of_hearts=Card(rank="9",suit="Hearts")

        self.cards=[
            self.two_of_hearts,
            self.four_of_hearts,
            self.five_of_hearts,
            self.seven_of_hearts,
            self.eight_of_hearts,
            self.nine_of_hearts,
            self.ace_of_hearts
         
        ]
        
    def test_validate_that_5_same__suit_exist_in_collection(self):


        validator=FlushValidator(cards=self.cards)


        self.assertEqual(validator.is_valid(),True)

    def test_return_five_high_cards_of_same_suit(self):

        validator=FlushValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [ 
                self.five_of_hearts,
                self.seven_of_hearts,
                self.eight_of_hearts,
                self.nine_of_hearts,
                self.ace_of_hearts
            ]


        )
