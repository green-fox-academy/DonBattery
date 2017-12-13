from apples import Apple
import unittest

test_apple = Apple()

class MinTest(unittest.TestCase):
    def test_apple(self):
        self.assertEqual(test_apple.get_apple(), "eggf", 'Ejnye')

if __name__ == '__main__':
    unittest.main() 
    