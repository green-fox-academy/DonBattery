import poker
import unittest

test_game = poker.Game()
test_hand = poker.Hand()

class MinTest(unittest.TestCase):


    def test_if_game_is_present(self):
        self.assertEqual(test_game.present, True, "init failed")

    def test_if_hands_are_present(self):
        self.assertEqual(test_hand.present, True, "init failed")
    
    def test_if_the_deck_is_52_card_long(self):
        self.assertEqual(len(test_game.cards), 42, "wrong number of cards")

    def test_if_cards_are_present(self):
        self.assertIn({'Symbol' : 'C', 'Value' : 14}, test_game.cards, "wrong deck")
    
    def test_random_shuffle(self):
        self.assertNotEqual(test_game.shuffle_the_cards, test_game.cards )

    def test_hand_if_have_pair(self):
        test_hand.hand = [{'Symbol': 'S', 'Value': 4},
                          {'Symbol': 'C', 'Value': 12},
                          {'Symbol': 'S', 'Value': 11},
                          {'Symbol': 'D', 'Value': 12},
                          {'Symbol': 'H', 'Value': 5}]
        self.assertEqual(test_hand.if_pair(), True)

    def test_highest_value(self):
        self.assertEqual(test_hand.get_highest(), 12, 'Wrong highest value')

    def test_hand_if_have__two_pairs(self):
        test_hand.hand = [{'Symbol': 'S', 'Value': 11},
                          {'Symbol': 'C', 'Value': 12},
                          {'Symbol': 'S', 'Value': 11},
                          {'Symbol': 'D', 'Value': 12},
                          {'Symbol': 'H', 'Value': 5}]
        self.assertEqual(test_hand.if_two_pairs(), True, 'Wrong two-pair detection')

    def test_hand_if_have_drill(self):
        test_hand.hand = [{'Symbol': 'S', 'Value': 11},
                          {'Symbol': 'C', 'Value': 11},
                          {'Symbol': 'S', 'Value': 12},
                          {'Symbol': 'D', 'Value': 13},
                          {'Symbol': 'H', 'Value': 5}]
        self.assertEqual(test_hand.if_drill(), True, 'Wrong drill detection')

    def test_hand_if_have_straight(self):
        test_hand.hand = [{'Symbol': 'S', 'Value': 2},
                          {'Symbol': 'C', 'Value': 3},
                          {'Symbol': 'S', 'Value': 3},
                          {'Symbol': 'D', 'Value': 5},
                          {'Symbol': 'H', 'Value': 6}]
        self.assertEqual(test_hand.if_straight(), True, 'Wrong straight detection')

if __name__ == '__main__':
    unittest.main()