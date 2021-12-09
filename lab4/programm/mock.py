from unittest import TestCase
from unittest.mock import patch
import main


class TestRoots(TestCase):
    @patch('main.get_roots', return_value=[])
    def test_no_roots(self, get_roots):
        self.assertEqual(main.get_roots(1, 2, 3), get_roots(1, 2, 3))

    @patch('main.get_roots', return_value=[0])
    def test_one_root(self, get_roots):
        expected_value = get_roots(1, 1, 0)

        cur_value = main.get_roots(1, 1, 0)
        self.assertEqual(len(cur_value), 1)
        self.assertEqual(expected_value[0] == cur_value[0], True)

    @patch('main.get_roots', return_value=[-2, 2])
    def test_two_roots(self, get_roots):
        expected_len = 2
        expected_value = get_roots(1, -2, -8)

        cur_value = main.get_roots(1, -2, -8)
        self.assertEqual(len(cur_value), expected_len)
        self.assertEqual(expected_value[0] in cur_value, True)
        self.assertEqual(expected_value[1] in cur_value, True)

    @patch('main.get_roots', return_value=[-1, 0, 1])
    def test_three_roots(self, get_roots):
        expected_len = 3
        expected_value = get_roots(1, -1, 0)

        cur_value = main.get_roots(1, -1, 0)
        self.assertEqual(len(cur_value), expected_len)
        self.assertEqual(expected_value[0] in cur_value, True)
        self.assertEqual(expected_value[1] in cur_value, True)
        self.assertEqual(expected_value[2] in cur_value, True)

    @patch('main.get_roots', return_value=[-1, 1, 0.5, -0.5])
    def test_four_roots(self, get_roots):
        expected_len = 4
        expected_value = get_roots(4, -5, 1)

        cur_value = main.get_roots(4, -5, 1)
        self.assertEqual(expected_value[0] in cur_value, True)
        self.assertEqual(expected_value[1] in cur_value, True)
        self.assertEqual(expected_value[2] in cur_value, True)
        self.assertEqual(expected_value[3] in cur_value, True)

# if __name__ == "__main__":
#     TestRoots.no_roots()
#     TestRoots.one_root()
#     TestRoots.two_roots()
#     TestRoots.three_roots()
#     TestRoots.four_roots()