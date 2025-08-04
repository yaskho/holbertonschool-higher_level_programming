#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -5, -2]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-10, 2, 0, -3, 5]), 5)

    def test_all_equal(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_list_of_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 2.9]), 3.3)

    def test_mixed_ints_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3, 2]), 3)

    def test_string_as_list(self):
        self.assertEqual(max_integer("holberton"), "t")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["Holberton", "School", "Python"]), "School")

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 2])

    def test_non_list_argument(self):
        with self.assertRaises(TypeError):
            max_integer(123)


if __name__ == '__main__':
    unittest.main()
