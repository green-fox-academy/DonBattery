import random

card_values = [14, 2, 3, 4,
               5, 6, 7, 8, 
               9, 10, 11, 12, 
               13]

card_symbols = ['C', 'D', 'H', 'S']

class Game(object):

    def __init__(self):
        self.hand_a = Hand()
        self.hand_b = Hand()
        self.present = True
        self.cards = [{'Symbol' : '', 'Value' : 0} for i in range(52)]
        for i in range(52):
            self.cards[i]['Symbol'] = card_symbols[i % 4]
            self.cards[i]['Value'] = card_values[i % 13]

        self.cards = self.shuffle_the_cards()

        for i in range(0,5):
            self.hand_a.hand.append(self.cards[0])
            del(self.cards[0])
            self.hand_b.hand.append(self.cards[0])
            del(self.cards[0])

    def shuffle_the_cards(self):
        random.shuffle(self.cards)
        return self.cards
            
class Hand(object):
    def __init__(self):
        self.present = True
        self.hand = []

    def get_strength(self):
        return self.if_pair()
    
    def get_highest(self):
        highest = {'Value' : 0}
        for card in self.hand:
            if card['Value'] > highest['Value']:
                highest = card
        return highest['Value']  

    def if_pair(self):
        state = False
        for c in range(0,4):
            for next_c in range(c + 1,5):
                if self.hand[c]['Value'] == self.hand[next_c]['Value']:
                    state = True
        return state

    def if_two_pairs(self):
        state = 0
        for i in range(0, 4):
            for j in range(i + 1, 5):
                if self.hand[i]['Value'] == self.hand[j]['Value']:
                    state += 1
        if state == 2:
            return True
        else:
            return False

    def if_drill(self):
        for i in range(0, 3):
            for j in range(i + 1, 4):
                for k in range(j + 1, 5):                
                    if self.hand[i]['Value'] == self.hand[j]['Value'] and self.hand[j]['Value'] == self.hand[k]['Value']:
                        return True
        return False

    def if_straight(self):
        test_list = self.hand
        test_list.sort(key = lambda x: x['Value'], reverse = False)
        for i in range(1, 5):
            if test_list[i - 1]['Value'] != test_list[i]['Value'] - 1:
                return False
        return True

if __name__ == '__main__':
    test_game = Game()
    test_hand = Hand()