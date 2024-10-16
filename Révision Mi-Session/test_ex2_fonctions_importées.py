import random

from ex2_fonctions_importées import *
from unittest import TestCase, main


class TestEx2FonctionsImportées(TestCase):

    def test_q1_random(self):
        random.seed(666)
        self.assertEqual(q1_random(1, 10), 8)
        self.assertEqual(q1_random(8, 12), 11)
        self.assertEqual(q1_random(55, 100), 82)

    def test_q2_somme_de_deux_dés(self):
        random.seed(42)
        self.assertEqual(q2_somme_de_deux_dés(), 7)
        self.assertEqual(q2_somme_de_deux_dés(), 7)
        self.assertEqual(q2_somme_de_deux_dés(), 5)
        self.assertEqual(q2_somme_de_deux_dés(), 4)

    def test_q3_roche_papier_ciseaux(self):
        random.seed(19)
        self.assertEqual(q3_roche_papier_ciseaux(), 'ciseaux')
        self.assertEqual(q3_roche_papier_ciseaux(), 'roche')
        self.assertEqual(q3_roche_papier_ciseaux(), 'ciseaux')

    def test_q4_sin_en_degrés(self):
        self.assertEqual(q4_sin_en_degrés(0), 0.0)
        self.assertEqual(q4_sin_en_degrés(30), 0.5)
        self.assertEqual(q4_sin_en_degrés(45), 0.7071067811865475)
        self.assertEqual(q4_sin_en_degrés(60), 0.8660254037844386)

    def test_q5_refraction(self):
        self.assertEqual(q5_refraction(1.0, 1.33, 60), 40.62813065148206)

    def test_q6_addition_binaire(self):
        self.assertEqual(q6_addition_binaire("8", "16"), "0b11000")
        self.assertEqual(q6_addition_binaire("42", "666"), "0b1011000100")


if __file__ == '__main__':
    main(verbosity=1)
