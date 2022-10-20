import unittest


from poker.card import Card
from poker.validators import StraightValidator

class TestStraightValidator(unittest.TestCase):

    def setUp(self):
        two=Card(rank="2",suit="Spades")
        three=Card(rank="3",suit="Diamonds")
        self.four=Card(rank="4",suit="Diamonds")
        self.five=Card(rank="5",suit="Clubs")
        self.six=Card(rank="6",suit="Spades")
        self.seven=Card(rank="7",suit="Hearts")
        self.eight=Card(rank="8",suit="Clubs")   


        self.cards=[
            two,
            three,
            self.four,
            self.five,
            self.six,
            self.seven,
            self.eight
        ]

    def test_determine_have_five_cards_in_a_row(self):


        validator=StraightValidator(cards=self.cards)

        self.assertEqual(validator.is_valid(),True)



    def test_return_the_five_high_straight_cards(self):
 
        validator=StraightValidator(cards=self.cards)
        
        self.assertEqual(validator.valid_card(),
        [   self.four,
            self.five,
            self.six,
            self.seven,
            self.eight 
        ]
        )

