import random

class Deck(object):
  def __init__(self, name = 'deck_1',):
    self.active = True
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

  def addPlayer(self, player,):
    self.players.append(player)
    player.addDeck(self)
    return self
  def displayPlayers(self):
    for player in self.players:
      print player.name, player.total
    return self

class Player(object):
  def __init__(self, name,):
    self.name = name.capitalize()
    self.total = 0
    self.deck = ''
    self.set = []
    self.selectedCards = []
  def addDeck(self, deck):
    self.deck = deck
  def info(self):
    pass
    # print info

<<<<<<< HEAD
  def selectSet(self, a, b, c):
    self.selectedCards = []
    self.selectedCards.append(self.deck.activeCards[a-1])
    self.selectedCards.append(self.deck.activeCards[b-1])
    self.selectedCards.append(self.deck.activeCards[c-1])
    self.activeCards.remove(a-1)
    self.activeCards.remove(b-1)
    self.activeCards.remove(c-1)
=======
  def selectSet(self, three_cards):
    three_cards = list(three_cards)
    three_cards.remove(')')
    three_cards.remove(',')
    three_cards.remove(',')
    three_cards.remove('(')
    three_cards = map(int, three_cards)
    print three_cards
    self.selectedCards.append(self.deck.activeCards[three_cards[0] - 1])
    self.selectedCards.append(self.deck.activeCards[three_cards[1] - 1])
    self.selectedCards.append(self.deck.activeCards[three_cards[2] - 1])
    self.deck.activeCards.remove(self.deck.activeCards[three_cards[2] - 1])
    self.deck.activeCards.remove(self.deck.activeCards[three_cards[1] - 1])
    self.deck.activeCards.remove(self.deck.activeCards[three_cards[0] - 1])
>>>>>>> 2f65d4b5070c52e00d56d4e996074ac3fcb52795
    return self


  def displaySet(self):
    i = 0
    for card in self.selectedCards:
      i += 1
      print "This is card",i,":", card["number"], card["shape"], card["color"], card["fill"]
    print '\n'

deck1 = Deck('deck1')

def startgame():
  val = raw_input('How many players? ')
  for i in range(0, int(val)):
    name = raw_input('Enter name of Player ' + str(i + 1) + " ")
    deck1.addPlayer(Player(name))
    print deck1.players[i].name

# startgame()
# deck1.displayActive()
# while deck1.active:
#   val = raw_input('>>> ')
#   if val.lower() == 'quit':
#     deck1.active = False

deck1.displayPlayers()
player1 = Player('sfkl')
deck1.displayActive()
player1.selectSet(2,4,5).displaySet()
deck1.displayActive()
<<<<<<< HEAD
=======
while deck1.active:
  val = raw_input('>>> ')
  if val.lower() == 'quit':
    deck1.active = False
  elif val.lower() == 'check':
    who = raw_input('Which player do you want to check? ')
  elif val.lower() == 'grab':
    who = raw_input('Which player is grabbing? ')
    three_cards = raw_input('Which cards? ( , , ) ')
    deck1.players[int(who) - 1].selectSet(three_cards)
    deck1.players[int(who) - 1].displaySet()
    deck1.displayActive()
  elif val.lower() == 'scores':
    deck1.displayPlayers
>>>>>>> 2f65d4b5070c52e00d56d4e996074ac3fcb52795


