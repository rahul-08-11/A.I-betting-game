from poker.validators import RankValidator

class FourOfKind(RankValidator):
    def __init__(self,cards) -> None:
        self.cards=cards 
        self.name="Four of a Rank"

    def is_valid(self):
        card_of_four_kind=self._rank_with_count(4)
        return len(card_of_four_kind)==1

    def valid_cards(self):
        return [card for card in self.cards if card.rank in self._rank_with_count(4)]
