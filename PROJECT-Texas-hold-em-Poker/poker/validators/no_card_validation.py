class NoCardValidator():
    def __init__(self,cards) -> None:
        self.cards=cards
        self.name="No Card"

    def is_valid(self):
        return len(self.cards)==0

    def valid_card(self):
        return []