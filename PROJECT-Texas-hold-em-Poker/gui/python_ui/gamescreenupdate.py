
from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player
from poker.gameround import GameRound
import random

class GameScreenOperation():

    def _finding_winner(self):
        dic_of_bit_with_wins=self._return_winner_and_their_win_counts()
        list_of_win_counts=list(dic_of_bit_with_wins.values())
        max_wins_a_bot_have=max(list_of_win_counts)
        index_of_max_wins=list_of_win_counts.index(max_wins_a_bot_have)
        list_of_bots=list(dic_of_bit_with_wins.keys())
        winner_bot=list_of_bots[index_of_max_wins]
        return winner_bot

    def _return_winner_and_their_win_counts(self):
        print(self.list_of_winner_in_each_round())
        winner_and_their_win_count={}
        for winner in self.list_of_winner_in_each_round():
            print(winner)
            winner_and_their_win_count.setdefault(winner,0)
            winner_and_their_win_count[winner]+=1
        print(winner_and_their_win_count)
        return winner_and_their_win_count

    def list_of_winner_in_each_round(self):
        list_of_winner_during_10_round=[]

        for round_number in range(10):
            deck,bots=self._deck_and_hand_distribution()
            gameround=GameRound(deck=deck,players=bots)
            gameround.play()
            for bot in bots:
                index,hand_name,hand_cards=bot.best_hand()
            winner_bot=max(bots)
            list_of_winner_during_10_round.append(winner_bot.name)

        return list_of_winner_during_10_round



    def _deck_and_hand_distribution(self):
        card=Card.create_52_standard_deck()
        deck=Deck()
        deck.add_card_into_collection(card)
 
        hand1=Hand()
        hand2=Hand()
        hand3=Hand()
        hand4=Hand()

        Ai_1=Player(name="A.I 1",hand=hand1)
        Ai_2=Player(name="A.I 2",hand=hand2)
        Ai_3=Player(name="A.I 3",hand=hand3)
        Ai_4=Player(name="A.I 4",hand=hand4)
        bots=[Ai_1,Ai_2,Ai_3,Ai_4]
        random.shuffle(bots)
        return [deck,bots]

       





    













