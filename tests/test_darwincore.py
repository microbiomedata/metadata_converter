import unittest
from metadata_converter import DWCConverter


class DarwincoreTestCase(unittest.TestCase):
    def test_convert(self):
        cv = DWCConverter()
        cv.filename = 'tests/dwc/dwc.csv'
        self.assertTrue(True)
        cv.convert_and_save('tests/dwc/dwc.yaml')


if __name__ == '__main__':
    unittest.main()
