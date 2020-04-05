import unittest
from rwalang import isKinyarwanda


class TestRwalang(unittest.TestCase):

    def test_kinsentence(self):
        self.assertEqual(isKinyarwanda("Mbifurije umunsi mwiza"), True)
        self.assertEqual(isKinyarwanda(
            "Ikinyarwanda kigizwe n'inyuguti"), True)
        self.assertEqual(isKinyarwanda("500"), True)
        words = ["500", "hello", "array", "holy", "murakoze"]
        self.assertEqual(isKinyarwanda(words[0]), True)
        self.assertEqual(isKinyarwanda(words[1]), False)
        self.assertEqual(isKinyarwanda(words[2]), False)
        self.assertEqual(isKinyarwanda(words[3]), False)
        self.assertEqual(isKinyarwanda(words[4]), True)

    def test_foreignwords(self):
        self.assertEqual(isKinyarwanda(
            "hello"), False)
        self.assertEqual(isKinyarwanda("should behave as expected"), False)

    def test_kinwithponctuations(self):
        self.assertEqual(isKinyarwanda(
            "Ubutinde:Ni uburyo ijambo ritinda"), True)
        self.assertEqual(isKinyarwanda("1) ryama kare "), True)

    def test_kinwithtonations(self):
      words = [
      "gihaânga",
      "Kanâama",
      "Kaanamâ",
      "Gateêra",
      "Mu myandikire ya gihaânga",
    ]
      
      self.assertEqual(isKinyarwanda(words[0]), True)
      self.assertEqual(isKinyarwanda(words[1]), True)
      self.assertEqual(isKinyarwanda(words[2]), True)
      self.assertEqual(isKinyarwanda(words[3]), True)
      self.assertEqual(isKinyarwanda(words[4]), True)
if __name__ == '__main__':
    unittest.main()
