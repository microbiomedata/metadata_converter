
"""
converts generic table definition DDL expressed as TSV
"""
import yaml
from dataclasses import dataclass, field
from typing import Optional, Set, List, Union, Dict, Any
import pandas as pd
import logging
import re

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
class DDLConverter:
    """
    converts DDL TSV
    """

    filename: Optional[str] = None

    def convert_and_save(self, fn: str) -> None:
        obj = self.convert()
        with open(fn, 'w') as stream:
            yaml.safe_dump(obj, stream, sort_keys=False)

    def convert(self, id: str='ddl', sep: str = '\t') -> Dict[str, Any]:
        ddl = pd.read_csv(self.filename, sep=sep, comment='#')
        slots = {}
        classes = {}
        subsets = {}
        obj = {
            'id': f'https://microbiomedata/schema/{id}',
            'description': 'Rendering of {id} schema',
            'imports': [
                'biolinkml:types'
            ],
            'prefixes': {
                'biolinkml': 'https://w3id.org/biolink/biolinkml/',
                id: f'https://microbiomedata/schema/{id}/'
            },
            'default_prefix': id,
            'slots': slots,
            'classes': classes,
            'subsets': subsets
        }

        logging.info(f'Parsing')
        for _,v in ddl.iterrows():
            c = v['table']
            s = v['field']
            sn = s.replace('_',' ').lower()
            sn = sn.replace(' id','')
            aliases = [sn]
            toks = sn.split(' ')
            if toks[0] in packages:
                aliases.append(' '.join(toks[1:]))
            if c not in classes:
                classes[c] = {
                    'slots': []
                }
            classes[c]['slots'].append(s)
            if s not in slots:
                slots[s] = {
                    'aliases': aliases,
                    'range': convert_range(v['type'], s)
                }
        return obj
