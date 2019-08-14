import unittest
from src.adder import add
from unittest import TestCase


class AdderTestCase(TestCase):
    add_params = (
        (2, 2, 4),
        (2, 3, 5),
        (10, 100, 110)
    )

    def test_add_works_as_expected(self):
        for a, b, res in self.add_params:
            with self.subTest():
                self.assertEqual(add(a, b), res)


if __name__ == '__main__':
    unittest.main()
