import unittest
from models.base import Base
from models.square import Square
import json

class TestBase(unittest.TestCase):

    def test_id_is_zero(self):
        self.assertEqual(base.id, None)


if __name__ == '__main__':
    unittest.main()
