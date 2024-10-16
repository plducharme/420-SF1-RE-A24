from ex4_structures_répétitives import *
from unittest import TestCase, main


class TestStructuresRépétitives(TestCase):

    def test_q1_somme_liste(self):
        self.assertEqual(q1_somme_liste([1, 2, 3, 4, 5]), 15)
        self.assertEqual(q1_somme_liste([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)
        self.assertEqual(q1_somme_liste([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 120)

    def test_q2_somme_pairs(self):
        self.assertEqual(q2_somme_pairs(), 2550)

    def test_q3_somme_fibonacci(self):
        self.assertEqual(q3_somme_fibonacci(100), 232)
        self.assertEqual(q3_somme_fibonacci(666), 1596)
        self.assertEqual(q3_somme_fibonacci(4), 7)


if __file__ == '__main__':
    main(verbosity=1)
