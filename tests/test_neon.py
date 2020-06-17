import os
import unittest
from metadata_converter import NeonConverter


class NeonTestCase(unittest.TestCase):
    def test_convert(self):
        cv = NeonConverter()
        cv.dirname = 'tests/neon'
        cv.load()
        self.assertTrue(True)
        obj = cv.convert()
        print(obj)
        cv.convert_and_save('tests/neon/neon.yaml')



if __name__ == '__main__':
    unittest.main()
