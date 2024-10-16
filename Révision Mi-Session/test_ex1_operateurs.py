from unittest import TestCase, main
from ex1_operateurs import *


class TestOperateurs(TestCase):

    def test_q1_rest_division(self):
        self.assertEqual(q1_reste_division(10, 3), 1)
        self.assertEqual(q1_reste_division(10, 2), 0)
        self.assertEqual(q1_reste_division(10, 5), 0)
        self.assertEqual(q1_reste_division(10, 4), 2)

    def test_q2_hypotenuse(self):
        self.assertEqual(q2_hypotenuse(3, 4), 5.0)
        self.assertEqual(q2_hypotenuse(5, 12), 13.0)
        self.assertEqual(q2_hypotenuse(7, 24), 25.0)
        self.assertEqual(q2_hypotenuse(8, 15), 17.0)

    def test_q3_priorite(self):
        self.assertEqual(q3_priorite(2, 3, 4), 625)
        self.assertEqual(q3_priorite(3, 4, 2), 81)
        self.assertEqual(q3_priorite(4, 2, 3), 4096)
        self.assertEqual(q3_priorite(2, 4, 3), 64)

    def test_q4_moyenne(self):
        self.assertEqual(q4_moyenne(2.5, 3.5, 4.5), 3.5)
        self.assertEqual(q4_moyenne(3.5, 4.5, 5.5), 4.5)
        self.assertEqual(q4_moyenne(4.5, 5.5, 6.5), 5.5)
        self.assertEqual(q4_moyenne(5.5, 6.5, 7.5), 6.5)


if __name__ == '__main__':
    main(verbosity=1)





