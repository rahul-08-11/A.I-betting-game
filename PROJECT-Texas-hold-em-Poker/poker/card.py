class Card():
  suits=("Hearts","Clubs","Spades","Diamonds")
  ranks=("2","3","4","5","6","7","8","9","10","Jake","Queen","King","Ace")
   

  def __init__(self,rank,suit) -> None:
    if rank not in self.ranks:
      raise ValueError(f"Please input a valid rank,It should in this tuple range:{self.ranks}")
    if suit not in self.suits:
      raise ValueError(f"Please input a valid suit,It should in this tuple range:{self.suits}")
    self.rank=rank
    self.index_rank=self.ranks.index(rank)
    self.suit=suit

  @classmethod
  def create_52_standard_deck(cls):
    cards=[]
    for rank in cls.ranks:
      for suit in cls.suits:
        cards.append(cls(rank,suit))
  
    return cards
    
    
      
  def __str__(self):
    return f"{self.rank} of {self.suit}"

  def __repr__(self) -> str:
     return f"Card('{self.rank}','{self.suit}')"

  def __eq__(self,other) -> bool:
    return self.rank==other.rank and self.suit==other.suit

  def __lt__(self,other):
    if self.rank==other.rank:
      return self.suit < other.suit
    return self.index_rank<other.index_rank

  

  

    


  
