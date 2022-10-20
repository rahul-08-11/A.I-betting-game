from parser import suite
import unittest
from unittest.mock import patch


from poker.deck import Deck
from poker.card import Card

class DeckTest(unittest.TestCase):
    def test_length_of_deck_equal_to_number_of_Card(self):
        cards=[
            Card(rank="Ace",suit="Spades"),
            Card(rank="8",suit="Diamonds")
            ]
        deck=Deck()
        deck.add_card_into_collection(cards)
        self.assertEqual(len(deck),2)

        


    def test_deck_has_no_cards(self):
        deck=Deck()
        self.assertEqual(len(deck.cards),0)

    def test_add_cards_into_collection(self):
        card=Card(rank="Ace",suit="Hearts")
        deck=Deck()
        deck.add_card_into_collection([card])
        self.assertEqual(deck.cards,[card])


    @patch("random.shuffle")
    def test_shuffle_cards_in_random_order(self,mock_shuffle):
        deck=Deck()

        cards=[
            Card(rank="Ace",suit="Spades"),
            Card(rank="8",suit="Diamonds")
            ]
    
        deck.add_card_into_collection(cards)

        deck.shuffle()
        mock_shuffle.assert_called_once_with(cards)

    def test_remove_specified_number_of_cards_from_deck(self):

        
        ace= Card(rank="Ace",suit="Spades"),
        eight= Card(rank="8",suit="Diamonds")
            
        cards=[ace,
        eight
        ]
        deck=Deck()
        deck.add_card_into_collection(cards)

        self.assertEqual(
            deck.remove_cards(1),
            [ace]
        )

        self.assertEqual(
            deck.cards,
            [eight]
        )

