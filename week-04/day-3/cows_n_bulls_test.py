from cows_n_bulls import CNB
import unittest

test_CNB = CNB()

class MinTest(unittest.TestCase):
    def test_init(self):
        self.assertEqual(test_CNB.present, True)
    
    #def test_empty_list(self):
     #   self.assertEqual(summer([]), 0)

if __name__ == '__main__':
    unittest.main()