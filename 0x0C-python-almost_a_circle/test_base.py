import unittest
from models.base import Base
from models.square import Square
import json

class TestBase(unittest.TestCase):

    def setUp(self):
        pass

    def test_id_is_zero(self):
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_value_passed(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_with_list(self):
        b = Base([1, 5, 8])
        self.assertEqual(b.id, [1, 5, 8])
    
    def test_id_with_tuple(self):
        b = Base({'idd': 11})
        self.assertEqual(b.id, {'idd': 11})

if __name__ == '__main__':
    unittest.main()
