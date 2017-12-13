from summer import summer
import unittest

class MinTest(unittest.TestCase):
    def test_0_1(self):
        self.assertEqual(summer([0,1]), 1)
    
    def test_empty_list(self):
        self.assertEqual(summer([]), 0)

if __name__ == '__main__':
    unittest.main() 
    