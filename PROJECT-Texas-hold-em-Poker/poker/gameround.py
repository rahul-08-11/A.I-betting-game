class   GameRound():
    
    def __init__(self,deck,players) -> None:
        self.deck=deck
        self.players=players
    
    def play(self):
        self._shuffle_deck()
        self._deal_two_cards_to_each_player()
        self._make_bets()

        self._deal_flop_cards()  
        self._make_bets()
 
        self._deal_turn_cards()
        self._make_bets()


        self._deal_river_cards()
        self._make_bets()


    def _shuffle_deck(self):
        self.deck.shuffle()
        

    def _deal_two_cards_to_each_player(self):
        for player in self.players:
            two_card=self.deck.remove_cards(2)
            player.add_card(two_card)

    def _make_bets(self):
        for player in self.players:
            if player.wants_to_fold():
                self.players.remove(player)

    def _deal_community_cards(self,number):
        community_card=self.deck.remove_cards(number)
        for player in self.players:
            player.add_card(community_card)

    def _deal_flop_cards(self):
        self._deal_community_cards(3)

    def _deal_turn_cards(self):
        self._deal_community_cards(1)


    def _deal_river_cards(self):
        self._deal_community_cards(1)







 

