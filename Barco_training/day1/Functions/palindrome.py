import unittest

def is_palindrome(s):
    s_lower = s.lower()
    return s_lower == s_lower[::-1]

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("ABBA"))
        self.assertTrue(is_palindrome("SOS"))
        self.assertTrue(is_palindrome("SOs"))
        self.assertTrue(is_palindrome("Kayak"))
        self.assertTrue(is_palindrome("Satanoscillatemymetallicsonatas"))

if __name__ == "__main__":
    unittest.main()