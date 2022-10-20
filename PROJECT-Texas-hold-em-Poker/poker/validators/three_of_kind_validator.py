from poker.validators import RankValidator
class ThreeOfKind(RankValidator):
    def __init__(self,cards) -> None:
        self.cards=cards
        self.name="Three of a Kind"

    def is_valid(self):
        card_of_three_kind=self._rank_with_count(3)
        return len(card_of_three_kind)==1

    def valid_card(self):
        card_of_three_kind=self._rank_with_count(3)
        return [card for card in self.cards if card.rank in card_of_three_kind]

        