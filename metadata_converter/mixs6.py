
"""
converts mixs6 spreadsheet

spreadsheet:
https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/edit#gid=567040283

Note: should also work for mixs5 xlsx files too, once exported to tsv
"""
import yaml
from dataclasses import dataclass, field
from typing import Optional, Set, List, Union, Dict, Any, Tuple
import pandas as pd
import logging
import re

CORE_PACKAGE_NAME = 'core'

# TODO: find source of metadata for each checklist
CHECKLISTS = ['migs_eu',
              'migs_ba',
              'migs_pl',
              'migs_vi',
              'migs_org',
              'me',
              'mimarks_s',
              'mimarks_c',
              'misag',
              'mimag',
              'miuvig']

datatype_schema = {
    'classes':
        {'quantity value':
             {'description': 'used to record a measurement',
              'attributes': {
                  'has unit': {
                      'description': 'Example "m"'
                  },
                  'has numeric value': {
                      'range': 'double'
                  },
                  'has raw value': {
                      'string_serialization': '{has numeric value} {has unit}'
                  }
              }
            }
        }
}

def safe(s: str) -> str:
    """
    render a string safe for use as a python variable

    :param s:
    :return:
    """
    if s[0].isdigit():
        s = f"x_{s}"
    if '/' in s:
        s = s.replace("/", "_")
    return s

def parse_value_syntax(s: str) -> Tuple[str,str]:
    pattern = s
    range = 'string'
    if s == '{float} {unit}':
        return None, 'quantity value'
    elif s == '{float}':
        return None, 'double'
    return pattern, range

@dataclass
class MIxS6Converter:
    """
    converts TSV from MIxS spreadsheet into LinkML yaml
    """

    core_filename: Optional[str] = None
    packages_filename: Optional[str] = None

    def convert_and_save(self, fn: str) -> None:
        obj = self.convert()
        with open(fn, 'w') as stream:
            yaml.safe_dump(obj, stream, sort_keys=False)

    def create_slot(self, row, enums: dict = {}) -> (str, Dict):
        """
        turn a row from EITHER core tab OR packages tab into a slot definition

        :param row:
        :return: tuple of id and definition dictionary
        """
        s_id = row['Structured comment name']
        if s_id is None or s_id == '-':
            logging.error(f"Bad row: {row}")
            return None, None
        if ';' in s_id:
            logging.error(f'Bad ID / SCN: {s_id} in {row}')
            return None, None
        if 'Item' in row:
            s_name = row['Item']
        elif 'Package item' in row:
            s_name = row['Package item']
        else:
            s_name = row['Item (rdfs:label)']
        if s_name == '':
            logging.error(f'No name: {s_id}')
            return None, None
        if ';' in s_name:
            logging.error(f'Bad name: {s_name} in {row}')
            return None, None
        comments = []
        for k in ('Expected value', 'Preferred unit', 'Occurrence', 'Position'):
            if k in row:
                comments.append(f'{k}: {row[k]}')

        # the column header is not consistent between sheets here
        slot_uri = None
        if 'Unique MIXS ID' in row and row['Unique MIXS ID'] is not None:
            slot_uri = row['Unique MIXS ID']
        elif 'unique MIXS ID' in row and row['unique MIXS ID'] is not None:
            slot_uri = row['unique MIXS ID']
        elif 'MIXS ID' in row and row['MIXS ID'] is not None:
            slot_uri = row['MIXS ID']
        else:
            None
            #logging.error(f'No ID: {slot_uri}')

        section = row['Section'] if 'Section' in row else 'environment'
        if section == '':
            logging.warning(f'No section: {s_id}')
            section = 'core'
        is_a = f'{section} field'
        pattern, range = parse_value_syntax(row['Value syntax'])
        slot = {
            'is_a': is_a,
            'aliases': [s_name],
            'description': row['Definition'],
            'range': range,
            'examples': [
                {'value': row['Example']}
            ],
            'comments': comments
        }
        if pattern is not None:
            slot['pattern'] = pattern
        LINK = 'Link to GH issue'
        if LINK in row:
            url = row[LINK]
            if url is not None and url.startswith("http"):
                slot['see_also'] = url

        s_id = safe(s_id)
        if pattern is not None and '|' in pattern:
            vals = pattern.replace('[', '').replace(']','').split('|')
            vals = [v.strip() for v in vals]
            # remove entries like '[{PMID}|{DOI}|...]'
            vals = [v for v in vals if not v.startswith('{')]
            if len(vals) > 2:
                enum_name = f'{s_id}_enum'
                slot['range'] = enum_name
                enums[enum_name] = {
                    'permissible_values': {v: {} for v in vals}
                }
        if slot_uri is not None:
            slot['slot_uri'] = slot_uri
        if 'Expected value' in row:
            range = row['Expected value']

        if 'Section' in row:
            row['in_subset'] = [row['Section']]

        return (s_id, slot)

    def convert(self) -> Dict[str, Any]:
        """
        Converts set of inputs to a schema

        :return: link schema as a python Dictionary
        """
        core_df = pd.read_csv(self.core_filename, sep="\t").fillna("")
        pkg_df  = pd.read_csv(self.packages_filename, sep="\t").fillna("")
        slots = {
            'core field': {
                'description': "basic fields"
            },
            'investigation field': {
                'description': "field describing aspect of the investigation/study to which the sample belongs"
            },
            'nucleic acid sequence source field': {},
            'sequencing field': {},
            'mixs extension field': {},
            'environment field': {
                'description': "field describing environmental aspect of a sample"
            }
        }
        classes = {}
        subsets = {}
        enums = {}
        obj = {
            'id': f'http://w3id.org/mixs6',
            'description': 'MIxS 6 linkml rendering',
            'imports': [
                'biolinkml:types'
            ],
            'prefixes': {
                'biolinkml': 'https://w3id.org/biolink/biolinkml/',
                'mixs.vocab': 'https://w3id.org/mixs/vocab/',
                'MIXS': 'https://w3id.org/mixs/terms/',
            },
            'default_prefix': 'mixs.vocab',
            'slots': slots,
            'classes': classes,
            'subsets': subsets,
            'enums': enums
        }

        # TODO: make configurable whether this is in main schema or import
        for cid,c in datatype_schema['classes'].items():
            classes[cid] = c

        cls_slot_req = {}
        slot_cls_req = {}

        core_slots = []
        core_env_slots = []

        core_slot_dict = {}
        for _, row in core_df.iterrows():
            s_id, slot = self.create_slot(row, enums=enums)
            if s_id is None:
                continue
            slots[s_id] = slot
            core_slot_dict[s_id] = row
            core_slots.append(s_id)
            if row['Section'] == 'environment':
                core_env_slots.append(s_id)

        for checklist in CHECKLISTS:
            checklist_slot_usage = {}
            for s_id, s_row in core_slot_dict.items():
                cardinality = s_row[checklist]
                if cardinality != '-' and cardinality != 'E':
                    usage = {}
                    checklist_slot_usage[s_id] = usage
                    if cardinality == 'M':
                        usage['required'] = 'True'
                    elif cardinality == 'X':
                        usage['required'] = 'False'
                    elif cardinality == 'C':
                        usage['comments'] = ['conditional mandatory']
            classes[checklist] = {
                'mixin': True,
                'description': f'{checklist} Checklist',
                'todos': ['add details here'],
                'slots': list(checklist_slot_usage.keys()),
                'slot_usage': checklist_slot_usage
            }
        classes[CORE_PACKAGE_NAME] = {
            'description': 'Core package. Do not use this directly, this is used to build other packages',
            'slots': core_slots
        }
        env_packages = []
        for _, row in pkg_df.iterrows():
            p = row['Environmental package']
            req = row['Requirement']
            is_required = req == 'M'
            cn = safe(p.lower())
            if cn not in classes:
                env_packages.append(cn)
                cls_slot_req[cn] = {}
                classes[cn] = {
                    #'is_a': CORE_PACKAGE_NAME,
                    'description': p,
                    'mappings': [],
                    'slots': list(core_env_slots),
                    'slot_usage': {}
                }
            c = classes[cn]

            s_id, slot = self.create_slot(row, enums=enums)

            if s_id is not None:
                # TODO: this makes the documentation odd
                #c['slot_usage'][s_id] = {'required': is_required}
                cls_slot_req[cn][s_id] = req

                if s_id not in slots:
                    slots[s_id] = slot
                else:
                    None ## TODO: compare
                if s_id not in slot_cls_req:
                    slot_cls_req[s_id] = {}
                slot_cls_req[s_id][cn] = req
                if s_id not in core_slots:
                    c['slots'].append(s_id)

        n_cls = len(cls_slot_req.keys())
        inf_core_slots = []
        for s_id, s in slot_cls_req.items():
            packages_str = ', '.join(list(s.keys()))
            if len(s.keys()) == n_cls:
                inf_core_slots.append(s_id)
                cmt = "This field is used in all packages"
            elif len(s.keys()) == 1:
                cmt = f"This field is used uniquely in: {packages_str}"
            else:
                cmt = f"This field is used in: {len(s.keys())} packages: {packages_str}"
            slots[s_id]['comments'].append(cmt)


        for p in env_packages:
            for checklist in CHECKLISTS:
                combo = f'{p} {checklist}'
                classes[combo] = {
                    'is_a': p,
                    'mixins': [checklist],
                    'description': f'Combinatorial checklist for {p} with {checklist}'
                }
        return obj
