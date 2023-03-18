# To run the code
# python -m pytest test.py --html=report.html --self-contained-html


import unittest
import pytest


class TestSum(unittest.TestCase):

    def test_wil_pass(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_will_fail(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()