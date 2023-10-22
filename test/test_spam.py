import sys, pathlib, unittest

sys.path.append(str(pathlib.Path(__file__).parents[1].joinpath("project").resolve()))

import spam

class TestSpam(unittest.TestCase):
    def test_convertFrequency(self):
        self.assertEqual(spam.convertFrequency("100sec"), 100)
        self.assertEqual(spam.convertFrequency("100"), 100)
        self.assertEqual(spam.convertFrequency("1hour"), 3600)
        
if __name__ == "__main__":
    unittest.main()