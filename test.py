import unittest
from example import addition

class TestAddition(unittest.TestCase):
    def test_addition(self):
        result = addition(8, 2)
        self.assertEqual(result, 10)
        

if __name__ == '__main__':
    unittest.main()

    