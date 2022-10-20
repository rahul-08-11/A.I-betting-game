from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfKind,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfKind,
    TwoPairValidator,
    PairCardValidator,
    HighClassValidator,
    NoCardValidator

)
class Hand():

    def __init__(self) -> None:
        self.cards=[]
    
    def __repr__(self) -> str:
        cards_as_string=[str(card) for card in self.cards]
        return ",".join(cards_as_string)

    def add_cards(self,cards):
        copy=self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards=copy

    VALIDATOR= (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfKind,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfKind,
    TwoPairValidator,
    PairCardValidator,
    HighClassValidator,
    NoCardValidator

    )
    
    def best_rank(self):
        for index,validator_class in enumerate(self.VALIDATOR):
            validator=validator_class(cards=self.cards)
            if validator.is_valid():
                return (index,validator.name,validator.valid_card())

        

