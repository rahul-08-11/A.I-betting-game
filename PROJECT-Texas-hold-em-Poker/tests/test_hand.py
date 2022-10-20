
import  unittest

from numpy import rank


from poker.card import Card
from poker.hand import Hand
from poker.validators import PairCardValidator

class HandTest(unittest.TestCase):

    def test_hand_start_with_no_cards(self):
        hand=Hand()
        self.assertEqual(hand.cards,[])

    def test_show_all_cards_its_technocal_rep(self):
        cards=[ 
            Card(rank="Ace",suit="Diamonds"),
            Card(rank="7",suit="Clubs")
        ]

        hand=Hand()
        hand.add_cards(cards)
        self.assertEqual(repr(hand),"7 of Clubs,Ace of Diamonds")

    def test_hand_have_cards(self):
        cards=[
            Card(rank="Ace",suit="Spades"),
            Card(rank="6",suit="Clubs")
        ]
        sorted_cards=[
        Card(rank="6",suit="Clubs"),
        Card(rank="Ace",suit="Spades")


        ]
        hand=Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.cards,sorted_cards)





    def test_for_the_index_of_rank(self):
        card=Card(rank="Jake",suit="Spades")

        self.assertEqual(card.index_rank,9)


    def test_interact_with_validator_to_get_winning_hand(self):
        class HandWithOneValidator(Hand):
            VALIDATOR=(PairCardValidator,)

        ace_of_hearts=Card(rank="Ace",suit="Hearts")
        ace_of_spades=Card(rank="Ace",suit="Spades")

        card=[ace_of_hearts,ace_of_spades]

        hand=HandWithOneValidator()
        hand.add_cards(cards=card)

        self.assertEqual(
            hand.best_rank(),
            (0,"Pair",[ace_of_hearts,ace_of_spades])
        )
    
