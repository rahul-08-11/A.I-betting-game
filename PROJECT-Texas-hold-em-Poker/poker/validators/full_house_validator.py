from poker.validators import ThreeOfKind ,PairCardValidator

class FullHouseValidator():
    def __init__(self,cards) -> None:
        self.cards=cards 
        self.name="The Full House"

    def is_valid(self):
        return ThreeOfKind(cards=self.cards).is_valid() and PairCardValidator(cards=self.cards).is_valid()
        

    def valid_card(self):
        three_of_kind_list=ThreeOfKind(cards=self.cards).valid_card()
        pair_card=PairCardValidator(cards=self.cards).valid_card()

        full_house_cards=three_of_kind_list+pair_card
        full_house_cards.sort()

        return full_house_cards