import unittest
import cetteAnnee as ca
class TestArbreBinaire(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.arbreDefault = "((((2 A) ((4 literate) (2 presentation))) ((2 that) (3 wonderfully))) ((((2 weaves) (((2 a) ((1 murderous) (2 event))) ((2 in) (2 1873)))) ((2 with) (((1 murderous) (1 rage)) ((2 in) (2 2002))))) (2 .)))"
    # DefaultStr = "((((2 A) ((4 literate) (2 presentation))) ((2 that) (3 wonderfully))) ((((2 weaves) (((2 a) ((1 murderous) (2 event))) ((2 in) (2 1873)))) ((2 with) (((1 murderous) (1 rage)) ((2 in) (2 2002))))) (2 .)))"
    def test_poids(self):
        arbre = ca.creer_arbre(self.arbreDefault)
        self.assertEqual(arbre.poids(), 17)

    def test_score(self):
        arbre = ca.creer_arbre(self.arbreDefault)
        self.assertEqual(arbre.score(), 2.0)

    def test_forme_correcte(self):
        self.assertTrue(ca.forme_correcte(self.arbreDefault)) 
        # forme_correcte() return True si il "(" a l'index 0 et ")" a l'index -1
        self.assertFalse(ca.forme_correcte("(1 2) 3 4"))

if __name__ == '__main__':
    unittest.main()