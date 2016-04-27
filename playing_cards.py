#Демонстрирует сочетание объектов
class Card(object):
    RANKS = ["A","2","3","4","5","6","7","8","9","10","10","J","Q","K"]
    SUITS = ["c","d","h","s"]
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep
class Hand(object):
    def __init__(self):
        self.cards=[]
    def __str__(self):
        if self.cards:
            rep =""
            for card in self.cards:
                rep +=str(card) + " "
        else:
            rep = "<пусто>"
        return rep
    def clear(self):
        self.cards=[]
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)
#основная часть
card1 = Card(rank = "A",suit ="C")
print("Вывожу на экран объект-карту:")
print(card1)
card2 = Card(rank="2",suit="c")
card3 = Card(rank="3",suit="c")
card4 = Card(rank="4",suit="c")
card5 = Card(rank="5",suit="c")
print("\nВывожу еще четыре карты:")
print(card2)
print(card3)
print(card4)
print(card5)
my_hand = Hand()
print("\nПечатаю карты, которые у меня на руках до раздачи:")
print(my_hand)
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card5)
print("\nПечатаю пять карт, которые появились у меня на руках:")
print(my_hand)
your_hand = Hand()
my_hand.give(card1,your_hand)
my_hand.give(card2,your_hand)
print("\nПервые две из моих карт я передал Вам")
print("Теперь у нас на руках:")
print(your_hand)
print(my_hand)

my_hand.clear()
print("\nУ меня на руках после того, как я сбросил все карты:")
print(my_hand)

