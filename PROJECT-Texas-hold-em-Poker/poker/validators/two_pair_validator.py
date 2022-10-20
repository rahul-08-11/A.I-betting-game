from poker.validators import RankValidator


class TwoPairValidator(RankValidator):
    def __init__(self,cards) -> None:
        self.cards=cards
        self.name="Two Pair"
        
    def is_valid(self):
        card_of_pair=self._rank_with_count(2)   #{"3":2 , "Ace":2}
        return len(card_of_pair)==2

    def valid_card(self):
        card_of_pair=self._rank_with_count(2)
        return [card for card in self.cards if card.rank in card_of_pair]
