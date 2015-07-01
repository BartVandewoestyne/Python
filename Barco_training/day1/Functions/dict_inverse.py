import unittest

def dict_inverse(d):
    """This is my own solution, not the model solution."""
    new_d = {}
    for city, code in d.items():
        the_city = new_d.get(code, "unknown")
        if the_city != "unknown":
            new_d[code].append(city)
        else:
            new_d[code] = [city]
    return new_d

class TestDictInverse(unittest.TestCase):
    def test_dict_inverse(self):
        d = {
              "Oostende": 8400,
              "Zandvoorde": 8400,
              "Stene": 8400,
              "Brugge": 8000,
              "Gent": 9000
              }

        d2 = dict_inverse(d)

        self.assertEqual(len(d2), 3)

        self.assertEqual(len(d2[8400]), 3)
        for city in ("Oostende", "Zandvoorde", "Stene"):
            self.assertTrue(city in d2[8400])

        self.assertEqual(d2[8000], ["Brugge"])
        self.assertEqual(d2[9000], ["Gent"])

if __name__ == "__main__":
    unittest.main()