import unittest
from unittest.mock import MagicMock,call




from poker.card import Card
from poker.gameround import GameRound



class TestGameRound(unittest.TestCase):
    def setUp(self):
        self.first_two_card=[ 
            Card(rank="Ace",suit="Diamonds")
            ,Card(rank="4",suit="Spades")
        ]
        self.next_two_card=[ 
            Card(rank="5",suit="Hearts")
            ,Card(rank="9",suit="Spades")
        ]

        self.flop_cards=[ 
            Card(rank="2",suit="Spades"),
            Card(rank="3",suit="Diamonds"),
            Card(rank="6",suit="Clubs")
        ]

        self.turn_card=[ 
            Card(rank="King",suit="Diamonds")
        ]
        self.river_card=[ 
            Card(rank="10",suit="Hearts")
        ]
        

    def test_stores_deck_and_player(self):
        mock_deck=MagicMock()
        players=[
            MagicMock(),
            MagicMock()
        ]

        gameround=GameRound(deck=mock_deck,players=players)

        self.assertEqual(gameround.deck,mock_deck)
        self.assertEqual(gameround.players,players)


        gameround.play()
        mock_deck.shuffle.assert_called_once()

    def test_deals_two_initial_cards_from_deck_to_each_player(self):

        mock_deck=MagicMock()
        mock_deck.remove_cards.side_effect=[
            self.first_two_card,
            self.next_two_card,
            self.flop_cards,
            self.turn_card,
            self.river_card
            ]


        mock_player1=MagicMock()
        mock_player2=MagicMock()
        players=[mock_player1,mock_player2]
        gameround=GameRound(deck=mock_deck,players=players)


        gameround.play()
        
        mock_deck.remove_cards.assert_has_calls([
            call(2),call(2)
        ])
        mock_player1.add_card.assert_has_calls([
            call(self.first_two_card)
        ]
            )
        mock_player2.add_card.assert_has_calls([
            call(self.next_two_card)
            ])




    def test_remove_player_if_not_willing_to_bet(self):
        deck=MagicMock()

        player1=MagicMock()
        player2=MagicMock()

        player1.wants_to_fold.return_value=True
        player2.wants_to_fold.return_value=False


        players=[player1,player2]
        game_round=GameRound(deck=deck,players=players)
        game_round.play()

        self.assertEqual(game_round.players,[player2])




    def test_deal_same_three_flop_one_turn_one_river(self):

        mock_player1=MagicMock()
        mock_player1.wants_to_fold.return_value=False

        mock_player2=MagicMock()
        mock_player2.wants_to_fold.return_value=False

        players=[mock_player1,mock_player2]

        mock_deck=MagicMock()
        mock_deck.remove_cards.side_effect=[ 
            self.first_two_card,
            self.next_two_card,
            self.flop_cards,
            self.turn_card,
            self.river_card
        ]

        game_round=GameRound(deck=mock_deck,players=players)
        game_round.play()

        mock_deck.remove_cards.assert_has_calls(
            [call(3),call(1),call(1)]
            )

        calls=[ 
            call(self.flop_cards),
            call(self.turn_card),
            call(self.river_card)
        ]
        for player in players:
            player.add_card.assert_has_calls(calls)
        
