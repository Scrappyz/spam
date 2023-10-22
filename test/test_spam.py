import sys, pathlib, unittest

sys.path.append(str(pathlib.Path(__file__).parents[1].joinpath("project").resolve()))

import spam

class TestSpam(unittest.TestCase):
    def test_convertInterval(self):
        self.assertEqual(spam.convertInterval("100sec"), 100)
        self.assertEqual(spam.convertInterval("100"), 100)
        self.assertEqual(spam.convertInterval("1hour"), 3600)
        self.assertEqual(spam.convertInterval("100ms"), 100/1000)
        self.assertEqual(spam.convertInterval("1m"), 60)
        
if __name__ == "__main__":
    unittest.main()