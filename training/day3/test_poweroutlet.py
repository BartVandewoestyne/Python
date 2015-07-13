import unittest
from poweroutlet import *


class TestPowerOutletBank(unittest.TestCase):
    def test_get_outlets(self):
        pass

    def test_set_outlet_state(self):
        pass


class TestPowerOutlet(unittest.TestCase):

    outlet = None

    def setUp(self):
        self.outlet = PowerOutlet(PowerOutletBank(), 1)

    def test_constructor(self):
        self.assertIsNotNone(self.outlet.bank)
        self.assertEqual(1, self.outlet.identifier)

    def test_set_state(self):
        self.assertRaises(NotImplementedError, self.outlet.set_state, PowerOn)
        self.assertRaises(NotImplementedError, self.outlet.set_state, PowerOff)

if __name__ == "__main__":
    unittest.main()
