import unittest

class TestTacos(unittest.TestCase):
    def test_frites_incluses(self):
        recette = open("tacos_ouledfayet.txt").read()
        self.assertIn("frites", recette)

if __name__ == "__main__":
    unittest.main()