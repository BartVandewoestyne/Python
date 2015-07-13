import unittest
from piglatin import to_piglatin
from piglatin import from_piglatin

class TestPigLatin(unittest.TestCase):
    def test_to_piglatin(self):
        self.assertEqual("appyhay", to_piglatin("happy"))
        self.assertEqual("uckday", to_piglatin("duck"))
        self.assertEqual("oveglay", to_piglatin("glove"))
        self.assertEqual("eggay", to_piglatin("egg"))
        self.assertEqual("inboxay", to_piglatin("inbox"))
        self.assertEqual("eightay", to_piglatin("eight"))

        self.assertEqual("appyHay", to_piglatin("Happy"))
        self.assertEqual("uckDay", to_piglatin("Duck"))
        self.assertEqual("oveGlay", to_piglatin("Glove"))
        self.assertEqual("Eggay", to_piglatin("Egg"))
        self.assertEqual("Inboxay", to_piglatin("Inbox"))
        self.assertEqual("Eightay", to_piglatin("Eight"))

        self.assertEqual("Eightay.", to_piglatin("Eight."))

    def test_to_piglatin_hyphened(self):
        self.assertEqual("appy-hay", to_piglatin("happy", True))
        self.assertEqual("uck-day", to_piglatin("duck", True))
        self.assertEqual("ove-glay", to_piglatin("glove", True))
        self.assertEqual("egg-ay", to_piglatin("egg", True))
        self.assertEqual("inbox-ay", to_piglatin("inbox", True))
        self.assertEqual("eight-ay", to_piglatin("eight", True))

        self.assertEqual("appy-Hay", to_piglatin("Happy", True))
        self.assertEqual("uck-Day", to_piglatin("Duck", True))
        self.assertEqual("ove-Glay", to_piglatin("Glove", True))
        self.assertEqual("Egg-ay", to_piglatin("Egg", True))
        self.assertEqual("Inbox-ay", to_piglatin("Inbox", True))
        self.assertEqual("Eight-ay", to_piglatin("Eight", True))

    def test_from_piglatin(self):
        self.assertEqual(from_piglatin("east-bay"), "beast")

if __name__ == "__main__":
    unittest.main()
