import random

class Deck(object):
  def __init__(self, name = 'deck_1',):
    self.name = name
    self.cards = []
    self.activeCards = []
    self.players = []
    self.gen()
    self.shuffle()
    self.deal(4)
  def gen(self):
    for color in range(0,3):
      for shape in range(0,3):
        for number in range(0,3):
          for fill in range(0,3):
            card = {}
            if shape == 0:
              card['shape'] = 'oval'
            elif shape == 1:
              card['shape'] = 'rectangle'
            elif shape == 2:
              card['shape'] = 'diamond'
            if number == 0:
              card['number'] = 'one'
            elif number == 1:
              card['number'] = 'three'
            elif number == 2:
              card['number'] = 'two'
            if color == 0:
              card['color'] = 'red'
            elif color == 1:
              card['color'] = 'blue'
            elif color == 2:
              card['color'] = 'green'
            if fill == 0:
              card['fill'] = 'solid'
            elif fill == 1:
              card['fill'] = 'dashed'
            elif fill == 2:
              card['fill'] = 'open'
            self.cards.append(card)

  def shuffle(self):
    for i in range(0, len(self.cards)):
      indx = random.randint(0, len(self.cards) - 1 - i)
      self.cards.append(self.cards[indx])
      self.cards.remove(self.cards[indx])
 master
    return self.cards

  def deal(self, n = 1):
    for i in range(0, n):
      for card in range(0,3):
        self.activeCards.append(self.cards[0])
        del self.cards[0]
    return self

  def displayActive(self):
    i = 0
    for card in self.activeCards:
      i += 1
      print "This is card",i,":", card["number"], card["shape"], card["color"], card["fill"] 
    return self

# print Deck().suffle()

class Player(object):
  def __init__(self, name,):
    self.name = name.capitalize()
    self.total = 0
  
  def info(self):
    pass
    # print info




deck1 = Deck('deck1')

# deck1.deal()
deck1.displayActive()
# print deck1.cards

