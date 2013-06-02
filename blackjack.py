# Mini-project #6 - Blackjack
#Implementation at http://www.codeskulptor.org/#user15_4IVQitCqLW9f7s2.py
import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
#dealer_hand = []
#player_hand = []
#game_deck = Deck()

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.field_cards = []  # create Hand object
        
            
    def __str__(self):
        ans = ""
        for i in range(len(self.field_cards)):
            ans += str(self.field_cards[i]) + " "
        return "Hand contais " + ans
        

    # return a string representation of a hand

    def add_card(self, card):
        self.card = card
        self.field_cards.append(self.card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        sum_value = []
        hand_value = 0
#        flag = 0
        
        for card in self.field_cards:
            card_rank = card.get_rank()
            hand_value += VALUES[card_rank]  #compute the value of the hand, see Blackjack video

        if card_rank == 'A':
#            flag = 1
            hand_value += 10
        else:
            if hand_value + 10 <= 21:
                hand_value += 10
            
        return hand_value       
        
#        return total
    def draw(self, canvas, pos):
        for card in self.field_cards:	# draw a hand on the canvas, use the draw method for cards
            card.draw(canvas, pos)
            pos[0] +=80

            
player_hand = Hand()
dealer_hand = Hand()
# define deck class 
class Deck:
    def __init__(self):
        self.deck_list = []	# create a Deck object
        for i in SUITS:
            for j in RANKS:
                p = Card(i, j)
                self.deck_list.append(p)
        
    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.deck_list)	# use random.shuffle() to shuffle the deck

    def deal_card(self):
        p = random.choice(self.deck_list)	# deal a card object from the deck
        return p
    
    def __str__(self):
        ans = ""
        for i in range(len(self.deck_list)):
            ans += str(self.deck_list[i]) + " "
        return "Deck contais " + ans	# return a string representing the deck        

game_deck = Deck()
#define event handlers for buttons
def deal():
    global outcome, in_play,dealer_hand, player_hand, game_deck, score

    # your code goes here
    
    player_hand = Hand()
    dealer_hand = Hand()
    game_deck.shuffle()
    for i in range(2):
        player_hand.add_card(game_deck.deal_card())
        dealer_hand.add_card(game_deck.deal_card())
    
#    print "Player",player_hand, player_hand.get_value()
#    print "Dealer",dealer_hand, dealer_hand.get_value()
    
#    draw.canvas.draw_text("Hit or Stand or New Deal?", [150, 500], 30, "Black")
    if in_play:
        score -=1
        outcome = "You Loose"
    in_play = True
    outcome = "Hit or stand or New deal"
#deal()

def hit():
    # replace with your code below
    global player_hand, dealer_hand, outcome, score
    # if the hand is in play, hit the player
    outcome = ""
    game_deck.shuffle()
#    player_hand.add_card(game_deck.deal_card())
    if (player_hand.get_value())>=22:
        outcome = "Busted"
        score -=1
        in_play = False
    else:
        player_hand.add_card(game_deck.deal_card())
        in_play = True
#    print "Player",player_hand, player_hand.get_value(), outcome, score
    
    if outcome == "Busted":
        player_hand = []
        dealer_hand = []
    
    outcome = "Hit or Stand or New Deal?"
    # if busted, assign a message to outcome, update in_play and score
#hit()       
def stand():
    global in_play, dealer_hand, player_hand, score, outcome
    # replace with your code below
    if outcome == "Busted":
        return "Game is over"
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while dealer_hand.get_value() <= 17:
        dealer_hand.add_card(game_deck.deal_card())
    if dealer_hand.get_value() > 21:
        outcome = "Dealer has Busted, You Win"
        score +=1
    elif dealer_hand.get_value() >= player_hand.get_value():
        outcome = "You Loose"
        score -=1
    else:
        outcome = "You win"
        score+=1
        
    in_play = False
#    print outcome            
#    print "Dealer",dealer_hand, dealer_hand.get_value(), outcome, score
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player_hand, dealer_hand, outcome
#    card = Card("S", "A")
#    card.draw(canvas, [300, 300])
    pos1 = [100, 300]
    pos2 = [100, 100]
    canvas.draw_text("Dealer Hand", [100, 90], 30, "Yellow")
    player_hand.draw(canvas, pos1)
    canvas.draw_text("Player Hand", [100, 290], 30, "Yellow")
    dealer_hand.draw(canvas, pos2)
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [135, 149], CARD_BACK_SIZE)
    canvas.draw_text("BlackJack", [220, 50], 40, "White")
    canvas.draw_text(outcome, [150, 500], 30, "Black")
    canvas.draw_text("Score: "+ str(score), [400, 90], 30, "Red")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# remember to review the gradic rubric
