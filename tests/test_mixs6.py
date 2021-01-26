import unittest
from metadata_converter import MIxS6Converter
from biolinkml.generators.pythongen import PythonGenerator
import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))

TGT = f'{TEST_DIR}/mixs6/mixs.yaml'
class MIxS6TestCase(unittest.TestCase):
    def test_convert(self):
        print(f'TEST DIR = {TEST_DIR}')

        cv = MIxS6Converter()
        cv.core_filename = f'{TEST_DIR}/mixs6/mixs6_core.tsv'
        cv.packages_filename = f'{TEST_DIR}/mixs6/mixs6.tsv'
        self.assertTrue(True)
        cv.convert_and_save(TGT)
        print(f'Yaml written to {TGT}')
        g = PythonGenerator(TGT)
        print(g.serialize()[0:3000])





if __name__ == '__main__':
    unittest.main()
