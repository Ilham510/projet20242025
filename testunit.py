import unittest



from main import calculer_pourcentages
class TestProjet(unittest.TestCase):
    def test_calculer_pourcentages(self):
        sequence = "AAACCCGGGUU"
        expected = {'A': 30.0, 'C': 30.0, 'G': 30.0, 'U': 10.0}
        self.assertEqual(calculer_pourcentages(sequence), expected)


if __name__ == '__main__':
    unittest.main()
