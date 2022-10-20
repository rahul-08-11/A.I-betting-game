
class StraightValidator():
    def __init__(self,cards) -> None:
        self.cards=cards
        self.name="The Straight Rank"

    def is_valid(self):
        if len(self.cards)<5:
            return False

        return len(self._filtering_out_cards_to_get_straights)>=1

    def valid_card(self):
        return self._filtering_out_cards_to_get_straights[-1]
        

    @property
    def _filtering_out_cards_to_get_straights(self):
        index=0
        final_index=len(self.cards)-1
        list_of_possible_straight_cards=[]

        while index+4 <= final_index:
            next_five_straight=self.cards[index:index+5]
            rank_indexes=[card.index_rank for card in next_five_straight]
            if self._every_element_increase_by1(rank_indexes):
                list_of_possible_straight_cards.append(next_five_straight)
  
            index+=1

            
        return list_of_possible_straight_cards

        
    def _every_element_increase_by1(self,rank_indexes):
        starting_rank_index=rank_indexes[0]
        last_rank_index=rank_indexes[-1]

        straight_consecutive_indexe=list(
            range(starting_rank_index,last_rank_index+1)
            )

        return rank_indexes==straight_consecutive_indexe
