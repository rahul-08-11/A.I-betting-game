class FlushValidator():
    def __init__(self,cards) -> None:
        self.cards=cards
        self.name="Flush"

    def is_valid(self):
        return len(self._dictionary_of_same_suit_and_count)==1

    def valid_card(self):

        cards=[card for card in self.cards if card.suit in self._dictionary_of_same_suit_and_count.keys()]
        return cards[-5:]
    @property
    def _dictionary_of_same_suit_and_count(self):
        return {
            suit:suit_count for suit,suit_count in self._card_suit_count.items()
            if suit_count>=5
        }



    @property
    def _card_suit_count(self):
        card_suit_count={}
        for card in self.cards:
            card_suit_count.setdefault(card.suit,0)
            card_suit_count[card.suit]+=1
        return card_suit_count