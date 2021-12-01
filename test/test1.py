import unittest
import sys
import os
sys.path.append(os.path.abspath("C:/git/serializer/"))
from xmlcreator import xml_tester

class MyTestCase(unittest.TestCase):
    def test_args_len(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
