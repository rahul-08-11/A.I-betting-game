from string import capwords
import unittest


from poker.card import Card


class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card=Card(rank="Queen",suit="Hearts")
        self.assertEqual(card.rank,"Queen")

    def test_has_suit(self):
        card=Card(rank="2",suit="Clubs")
        self.assertEqual(card.suit,"Clubs") 

    def test_string_representation(self):
        card=Card(rank="Queen",suit="Diamonds")
        self.assertEqual(str(card),"Queen of Diamonds")

    def test_ambiguous_represntation(self):
        card=Card('3','Spades')
        self.assertEqual(repr(card),"Card('3','Spades')")


    def test_card_has_four_possible_suits(self):
        self.assertEqual(Card.suits,("Hearts","Clubs","Spades","Diamonds"))

    def test_card_has_thirteen_possible_ranks(self):
        self.assertEqual(Card.ranks,("2","3","4","5","6","7","8","9","10","Jake","Queen","King","Ace"))


    def test_card_has_the_valid_ranks(self):
        with self.assertRaises(ValueError):
            Card(rank="Three",suit="Hearts")

    def test_card_has_the_valid_ranks(self):
        with self.assertRaises(ValueError):
            Card(rank="3",suit="Queen")

    def test__create_52_standard_deck(self):
        cards=Card.create_52_standard_deck()
        self.assertEqual(len(cards),52)


    def test_first_card_of_deck(self):
        card=Card.create_52_standard_deck()
        
        self.assertEqual(card[0],Card("2","Hearts"))

    def test_last_card_of_deck(self):
        card=Card.create_52_standard_deck()
        self.assertEqual(card[-1],Card("Ace","Diamonds"))


    def test_two_cards_are_equal_if_same_rank_and_suit(self):
        self.assertEqual(
            Card("Ace","Clubs"),
            Card("Ace","Clubs")

        )

    def test_for_small_cards_sorting(self):
        queen_of_spades=Card(rank="Queen",suit="Spades")
        king_of_spades=Card(rank="King",suit="Spades")

        evalution = queen_of_spades < king_of_spades

        self.assertEqual(
            evalution,True,
            "The sort algorithm is not sorting lower card first"
            )

    def test_sorts_cards(self):
        two_of_spades=Card(rank="2",suit="Spades")
        five_of_diamonds=Card(rank="5",suit="Diamonds")
        five_Of_hearts=Card(rank="5",suit="Hearts")
        eight_of_hearts=Card(rank="8",suit="Hearts")
        ace_of_clubs=Card(rank="Ace",suit="Clubs")

        unsorted_cards=[
            two_of_spades,
            five_of_diamonds,
            five_Of_hearts,
            eight_of_hearts,
            ace_of_clubs
        ]
        unsorted_cards.sort()

        sorted_cards=[
            two_of_spades,
            five_of_diamonds,
            five_Of_hearts,
            eight_of_hearts,
            ace_of_clubs
        ]
    

        self.assertEqual(unsorted_cards,sorted_cards)




