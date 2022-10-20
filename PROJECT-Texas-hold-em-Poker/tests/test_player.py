import unittest
from unittest.mock import MagicMock

from defer import return_value

from poker.card import Card
from poker.hand import Hand
from poker.player import Player

class TestPlayer(unittest.TestCase):

    def test_for_player_name_and_hand(self):
        hand=Hand()
        player=Player(name="Rahul",hand=hand)

        self.assertEqual(player.name,"Rahul")
        self.assertEqual(player.hand,hand)


    def test_player_best_rank(self):
        mock_hand=MagicMock()
        mock_hand.best_rank.return_value="Flush"
        player=Player(name="Rahul",hand=mock_hand)
        
        self.assertEqual(player.best_hand(),"Flush")
        mock_hand.best_rank.assert_called()

    def test_passes_new_cards_to_hands(self):
        mock_hand=MagicMock()
        
        cards=[
            Card(rank="Ace",suit="Spades"),
            Card(rank="8",suit="Diamonds")

        ]
        player=Player(name="Rahul",hand=mock_hand)
        player.add_card(cards)
        mock_hand.add_cards.assert_called_once_with(cards)
        
    def test_player_Decided_to_continue_or_droup_out_of_game(self):
        player=Player(name="Rahul",hand=Hand())
        self.assertEqual(
            player.wants_to_fold(),
            False
        )
 
    def  test_is_sorted_by_best_hand(self):
        mock_hand1=MagicMock()
        mock_hand1.best_rank.return_value=(0,"Royal Flush",[])

        mock_hand2=MagicMock()
        mock_hand2.best_rank.return_value=(2,"Pair",[])
 
        player1=Player(name="Rahul",hand=mock_hand1)
        player2=Player(name="Raj",hand=mock_hand2)

        players=[player1,player2]

        self.assertEqual(
            max(players),
            player1
        )
     


