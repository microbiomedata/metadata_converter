import os
import unittest
from metadata_converter import DDLConverter


class GoldTestCase(unittest.TestCase):
    def test_convert(self):
        cv = DDLConverter()
        cv.filename = './tests/gold/gold-schema.tsv'
        self.assertTrue(True)
        cv.convert_and_save('tests/gold/gold.yaml')

    def test_convert_biosample(self):
        cv = DDLConverter()
        cv.filename = './tests/gold/gold-BIOSAMPLE-schema.tsv'
        self.assertTrue(True)
        cv.convert_and_save('tests/gold/biosample.yaml')


if __name__ == '__main__':
    unittest.main()
