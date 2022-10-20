from poker.validators import RankValidator

class PairCardValidator(RankValidator):
    def __init__(self,cards) -> None:
        self.cards=cards
        self.name="Pair"

    def is_valid(self) -> bool:       
        card_of_pair=self._rank_with_count(2)
        return len(card_of_pair)==1 

    def valid_card(self):
        card_of_pair=self._rank_with_count(2) #{"8":2}
        return [card for card in self.cards if card.rank in card_of_pair.keys()]

