import unittest
from main import get_roots


class TestGetRoots(unittest.TestCase):
    # x^4+2x^2+3 = 0
    def test_no_roots(self):
        self.assertEqual(get_roots(1, 2, 3), [])

    def test_four_roots(self):
        expected_len = 4
        expected_value = [-1, 1, 0.5, -0.5]

        cur_value = get_roots(4, -5, 1)
        self.assertEqual(len(cur_value), expected_len)
        self.assertEqual(expected_value[0] in cur_value, True)
        self.assertEqual(expected_value[1] in cur_value, True)
        self.assertEqual(expected_value[2] in cur_value, True)
        self.assertEqual(expected_value[3] in cur_value, True)

    def test_three_roots(self):
        expected_len = 3
        expected_value = [-1, 0, 1]

        cur_value = get_roots(1, -1, 0)
        self.assertEqual(len(cur_value), expected_len)
        self.assertEqual(expected_value[0] in cur_value, True)
        self.assertEqual(expected_value[1] in cur_value, True)
        self.assertEqual(expected_value[2] in cur_value, True)

    def test_two_roots(self):
        expected_len = 2
        expected_value = [-2, 2]

        cur_value = get_roots(1, -2, -8)
        self.assertEqual(len(cur_value), expected_len)
        self.assertEqual(expected_value[0] in cur_value, True)
        self.assertEqual(expected_value[1] in cur_value, True)

    def test_one_root(self):
        expected_value = [0]

        cur_value = get_roots(1, 1, 0)
        self.assertEqual(len(cur_value), 1)
        self.assertEqual(expected_value[0], cur_value[0], True)


if __name__ == "__main__":
    unittest.main()

