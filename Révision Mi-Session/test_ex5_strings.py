from ex5_strings import *
from unittest import TestCase, main

class TestStrings(TestCase):

    def test_q1_str_nieme(self):
        self.assertEqual(q1_str_nieme("Bonjour", 3), "n")
        self.assertEqual(q1_str_nieme("Bonjour", 6), "u")
        self.assertEqual(q1_str_nieme("Bonjour", 1), "B")
        self.assertEqual(q1_str_nieme("Bonjour", 7), "r")
        self.assertEqual(q1_str_nieme("Bonjour", 20), "")

    def test_q2_str_milieu(self):
        self.assertEqual(q2_str_milieu("Bonjour"), "j")
        self.assertEqual(q2_str_milieu("Bonsoir"), "s")
        self.assertEqual(q2_str_milieu("Amie"), "")
        self.assertEqual(q2_str_milieu("Bonne"), "n")

    def test_q3_str_split(self):
        self.assertEqual(q3_str_split("B\to\tn\tj\to\tu\tr"), ["B", "o", "n", "j", "o", "u", "r"])
        self.assertEqual(q3_str_split("Vive la liberté,\tvive l'indépendance!"), ["Vive la liberté,",
                                                                                  "vive l'indépendance!"])

    def test_q4_str_slice(self):
        self.assertEqual(q4_str_slice("Bonjour"), "jour")
        self.assertEqual(q4_str_slice("Allo à tous"), "à tous")
        self.assertEqual(q4_str_slice("Tranchons"), "chons")

    def test_q5_str_replace(self):
        self.assertEqual(q5_str_replace("Bonjour", "jour", "soir"), "Bonsoir")
        self.assertEqual(q5_str_replace("Allo à tous", "Allo", "Bonjour"), "Bonjour à tous")
        self.assertEqual(q5_str_replace("La patience est amère, mais son fruit est doux.", "a",
                                        "@"), "L@ p@tience est @mère, m@is son fruit est doux.")

    def test_q6_str_replace_fin(self):
        self.assertEqual(q6_str_replace_fin("Bonjour les amis", "jour", "soir"), "Bonjour les amis")
        self.assertEqual(q6_str_replace_fin("Que le grand crique me croque!", "croque", "craque"),
                         "Que le grand crique me craque!")
        self.assertEqual(q6_str_replace_fin("La patience est amère, mais son fruit est doux.", "a",
                                            "@"), "La patience est amère, mais son fruit est doux.")