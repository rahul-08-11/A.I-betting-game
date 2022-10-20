class RankValidator():

    def _rank_with_count(self,count):
        return {
            rank:rank_count
            for rank,rank_count in self._card_rank_count.items()
            if rank_count==count
        }

    @property
    def _card_rank_count(self):
        card_rank_count={}
        for card in self.cards:
            card_rank_count.setdefault(card.rank,0)
            card_rank_count[card.rank]+=1
        return card_rank_count
    