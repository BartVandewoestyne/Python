import unittest


def transpose(m):
    """Transpose the given matrix."""
    """See also https://docs.python.org/2/tutorial/datastructures.html#nested-list-comprehensions"""
    return [[row[i] for row in m] for i in range(len(m[0]))]


class TestTranspose(unittest.TestCase):
    def test_transpose_square(self):
        m1 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
        m2 = [[1, 4, 7],
              [2, 5, 8],
              [3, 6, 9]]
        self.assertEqual(m2, transpose(m1))

    def test_transpose_non_square(self):
        m1 = [[1, 2, 3],
              [4, 5, 6]]
        m2 = [[1, 4],
              [2, 5],
              [3, 6]]
        self.assertEqual(m2, transpose(m1))


if __name__ == "__main__":
    unittest.main()
