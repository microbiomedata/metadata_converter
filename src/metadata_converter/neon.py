
"""
converts NEON data definition csvs to yaml
"""
import yaml
from dataclasses import dataclass, field
from typing import Optional, Set, List, Union, Dict, Any
import pandas as pd
import logging
import re

# https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
camel_pattern = re.compile(r'(?<!^)(?=[A-Z])')

xref_pattern = re.compile(r'^[a-zA-Z0-9_-]+:\S+$')

def camel_case_to_label(s: str) -> str:
    return camel_pattern.sub(' ', s).lower()

def convert_range(s: str) -> str:
    if s == 'real':
        return 'double'
    if s == 'signed integer':
        return 'integer'
    if s == 'dateTime':
        return 'time'
    if s == 'integer':
        return 'integer'
    return 'string'

def normalize_xref(x: str) -> str:
    toks = x.split(":")
    if len(toks) == 2:
        [prefix,local_id] = toks
        if prefix.startswith('DWC'):
            prefix = 'dwc'
        return f'{prefix}:{local_id}'

@dataclass
class NeonConverter:
    """
    converts neon sample service yaml to NMDC/blml representation
    """

    dirname: Optional[str] = None

    neon_terms: pd.DataFrame = None
    neon_term_usage: pd.DataFrame = None

    def load(self) -> None:
        """
        loads from folder
        :return:
        """
        self.neon_terms = pd.read_csv(f'{self.dirname}/neon_terms.csv')
        self.neon_term_usage = pd.read_csv(f'{self.dirname}/neon_term_usage.csv')

    def convert_and_save(self, fn: str) -> None:
        obj = self.convert()
        with open(fn, 'w') as stream:
            yaml.safe_dump(obj, stream, sort_keys=False)

    def convert(self) -> Dict[str, Any]:
        slots = {}
        classes = {}
        subsets = {}
        obj = {
            'id': 'https://microbiomedata/schema/neon',
            'description': 'NEON rendering of KBase metadata schema',
            'imports': [
                'biolinkml:types'
            ],
            'prefixes': {
                'biolinkml': 'https://w3id.org/biolink/biolinkml/',
                'neon': 'https://data.neonscience.org/',
                'dwc': 'http://rs.tdwg.org/dwc/terms/',
                'mixs': 'https://microbiomedata/schema/mixs#'
            },
            'default_prefix': 'neon',
            'slots': slots,
            'classes': classes,
            'subsets': subsets
        }

        logging.info(f'Parsing slots')
        for _,v in self.neon_terms.iterrows():
            k = v['termName']
            n = camel_case_to_label(k)
            xrefstr = v['relatedTerms']
            if isinstance(xrefstr, str):
                xrefs = xrefstr.split(" ")
            else:
                xrefs = []
            xrefs = [normalize_xref(x) for x in xrefs if xref_pattern.match(x)]
            slot = {'slot_uri': f'neon:{k}',
                    'description': v['termDesc'],
                    'range': convert_range(v['dataType']),
                    'aliases': [n],
                    'mappings': xrefs}
            slots[k] = slot
            # TODO units https://github.com/biolink/biolinkml/issues/159

        logging.info(f'Parsing classes')
        for _,v in self.neon_term_usage.iterrows():
            c = v['tableName']
            if c not in classes:
                classes[c] = {
                    'class_uri': f'neon:{c}',
                    'slots':[],
                    'in_subset': []}
            cls = classes[c]
            cslots = cls['slots']
            tn = v['termName']
            if tn not in cslots:
                cslots.append(tn)
            if tn not in slots:
                slots[tn] = {
                    'description': 'Auto-added'
                }
            pid = v['productID']
            if pid not in subsets:
                subsets[pid] = {
                    'description': v['productName']
                }
                cls['in_subset'].append(pid)
        return obj
