from unittest import TestCase, main
from ex3_structures_conditionnelles import *


class TestEx3StructuresConditionnelles(TestCase):

    def test_q1_prix_zoo(self):
        self.assertEqual(q1_prix_zoo(1), 0)
        self.assertEqual(q1_prix_zoo(2), 0)
        self.assertEqual(q1_prix_zoo(3), 5.50)
        self.assertEqual(q1_prix_zoo(12), 5.50)
        self.assertEqual(q1_prix_zoo(13), 9.00)
        self.assertEqual(q1_prix_zoo(64), 9.00)
        self.assertEqual(q1_prix_zoo(65), 6.50)
        self.assertEqual(q1_prix_zoo(100), 6.50)

    def test_q2_upper_lower(self):
        self.assertEqual(q2_upper_lower("Bonjour"), "BONJOUR")
        self.assertEqual(q2_upper_lower("bonjour"), "bonjour")
        self.assertEqual(q2_upper_lower("Bonjour!"), "BONJOUR!")

    def test_q3_jeu_de_dés(self):
        random.seed(42)
        self.assertFalse(q3_jeu_de_dés())
        self.assertFalse(q3_jeu_de_dés())
        self.assertFalse(q3_jeu_de_dés())
        self.assertTrue(q3_jeu_de_dés())


if __name__ == '__main__':
    main(verbosity=1)
