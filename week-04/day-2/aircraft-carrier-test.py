from aircraft_carrier import Aircraft, Aircraft_F16, Aircraft_F35
import unittest

test_aircraft = Aircraft()
test_aircraft_F16 = Aircraft_F16()
test_aircraft_F35 = Aircraft_F35()

class MinTest(unittest.TestCase):

    def test_aircraft_init(self):
        self.assertEqual(test_aircraft.alive(), True, "init failed")

    def test_aircraft_F16_init(self):
        self.assertEqual(test_aircraft_F16.alive(), True, "init failed")

    def test_aircraft_F35_init(self):
        self.assertEqual(test_aircraft_F35.alive(), True, "init failed")

if __name__ == '__main__':
    unittest.main()