from poker.validators import StraightValidator

class StraightFlushValidator(StraightValidator):
    def __init__(self,cards) -> None:
        self.cards=cards 
        self.name="Straight Flush"

    def is_valid(self):

        return len(self._checking_weather_a_straight_have_flush_or_not)>=1

  
    def valid_card(self):
        return self._checking_weather_a_straight_have_flush_or_not[-1]



    @property
    def _checking_weather_a_straight_have_flush_or_not(self):
        card_suit_count={} 
        storing_possible_straight_flush=[]
        for list_of_straight_cards in self._filtering_out_cards_to_get_straights:
            for card in list_of_straight_cards:
                card_suit_count.setdefault(card.suit,0)
                card_suit_count[card.suit]+=1
            card_suit_count.clear() if len(card_suit_count)>1 else storing_possible_straight_flush.append(list_of_straight_cards)
            
        return storing_possible_straight_flush

                



