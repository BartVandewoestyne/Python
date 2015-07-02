import unittest


def is_prime(n):
    """Check if the given number is a prime number."""
    n_prime = True
    for k in range(2, n/2+1):
        if n % k == 0:
            n_prime = False
            break
    return n_prime


def is_armstrong(n):
    """Check if the given number is an Armstrong number."""
    n_string = str(n)
    nb_digits = len(n_string)
    my_sum = 0
    for d in n_string:
        my_sum += int(d)**nb_digits
    return my_sum == n


def is_perfect_number(n):
    """Check if the given number is a perfect number"""
    my_sum = 0
    for k in range(1, n/2+1):
        if (n % k) == 0:
            my_sum += k
    return n == my_sum


class TestNumberTester(unittest.TestCase):
    def test_is_prime(self):
        for n in [1, 2, 3, 5, 7, 11, 13, 17, 19]:
            self.assertTrue(is_prime(n))
        for n in [4, 6, 8, 9, 12, 14, 15, 16]:
            self.assertFalse(is_prime(n))

    def test_is_armstrong(self):
        for n in [153, 370]:
            self.assertTrue(is_armstrong(n))
        for n in [100, 200]:
            self.assertFalse(is_armstrong(n))

    def test_is_perfect_number(self):
        perfects = [6, 28, 496, 8128]
        for n in perfects:
            self.assertTrue(is_perfect_number(n))
        for n in range(1, 10000):
            if n not in perfects:
                self.assertFalse(is_perfect_number(n), "{0:d} should not be perfect".format(n))

if __name__ == "__main__":
    unittest.main()
