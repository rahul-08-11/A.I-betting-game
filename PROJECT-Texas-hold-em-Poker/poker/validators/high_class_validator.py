class HighClassValidator():
    def __init__(self,cards) -> None:
        self.cards=cards
        self.name="High Card"


    def is_valid(self):
        return len(self.cards)>=2

    def valid_card(self):
        return self.cards[-1:]




    