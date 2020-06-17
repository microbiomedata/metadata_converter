import os
import unittest
from metadata_converter import KBaseConverter


class KBaseTestCase(unittest.TestCase):
    def test_convert(self):
        cv = KBaseConverter()
        cv.dirname = 'tests/kbase'
        cv.load()
        self.assertTrue(True)
        obj = cv.convert()
        print(obj)
        cv.convert_and_save('tests/kbase/kbase.yaml')



if __name__ == '__main__':
    unittest.main()
