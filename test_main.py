from unittest import TestCase
import main


class Test(TestCase):
    def test_add(self):
        self.assertEqual(9, main.add(4, 5))

    def test_sub(self):
        self.assertEqual(5, main.sub(7, 2))

    def test_mul(self):
        self.assertEqual(9, main.mul(3, 3))

    def test_div(self):
        self.assertEqual(10, main.div(30, 3))
