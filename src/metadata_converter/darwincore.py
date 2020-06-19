
"""
converts generic table definition DDL expressed as TSV
"""
import yaml
from dataclasses import dataclass, field
from typing import Optional, Set, List, Union, Dict, Any
import pandas as pd
import logging
import re

# https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
camel_pattern = re.compile(r'(?<!^)(?=[A-Z])')


def camel_case_to_label(s: str) -> str:
    return camel_pattern.sub(' ', s).lower()

def convert_range(s: str, slot: str) -> str:
    if s == 'number':
        if slot.lower().endswith('_id'):
            return 'integer' # TODO; FK
        else:
            return 'double'
    if s == 'time':
        return 'time'
    return 'string'

packages = ['soil', 'water', 'biogas']

@dataclass
class DWCConverter:
    """
    converts DDL TSV
    """

    filename: Optional[str] = None

    def convert_and_save(self, fn: str) -> None:
        obj = self.convert()
        with open(fn, 'w') as stream:
            yaml.safe_dump(obj, stream, sort_keys=False)

    def convert(self) -> Dict[str, Any]:
        df = pd.read_csv(self.filename)
        df = df.fillna("")
        slots = {}
        classes = {}
        subsets = {}
        obj = {
            'id': f'http://rs.tdwg.org/dwc/terms',
            'description': 'DarwinCore biolinkml rendering',
            'imports': [
                'biolinkml:types'
            ],
            'prefixes': {
                'biolinkml': 'https://w3id.org/biolink/biolinkml/',
                'dwc': 'http://rs.tdwg.org/dwc/terms/'
            },
            'default_prefix': 'dwc',
            'slots': slots,
            'classes': classes,
            'subsets': subsets
        }

        for _, v in df.iterrows():
            if v['rdf_type'] != 'http://www.w3.org/2000/01/rdf-schema#Class':
                continue
            id = v['label']
            classes[id] = {
                'aliases': [id],
                'description': v['definition'],
                'mappings': [],
                'slots': []
            }
            if v['replaces'] != "":
                classes[id]['mappings'] += v['replaces'].split('|')
        for _, v in df.iterrows():
            if v['rdf_type'] != 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property':
                continue
            id = v['label']
            slots[id] = {
                'aliases': [camel_case_to_label(id)],
                'description': v['definition'],
                'mappings': []
            }
            if v['replaces'] != "":
                slots[id]['mappings'] += v['replaces'].split('|')
            c = v['organized_in']
            c = c.replace('http://rs.tdwg.org/dwc/terms/', '')
            if c in classes:
                classes[c]['slots'].append(id)
            else:
                logging.error(f'Slot {id} organized_in non existent {c}')
        return obj
