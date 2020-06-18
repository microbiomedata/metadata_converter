"""
Converts kbase sample service desription
"""
import yaml
from dataclasses import dataclass, field
from typing import Optional, Set, List, Union, Dict, Any
import logging

@dataclass
class KBaseConverter:
    """
    converts kbase sample service yaml to NMDC/blml representation
    """

    dirname: Optional[str] = None

    # https://github.com/kbaseIncubator/sample_service_validator_config/blob/master/metadata_validation.yml
    validators: Optional[Dict[str, Any]] = None

    # https://github.com/kbaseIncubator/sample_service_validator_config/blob/master/sample_uploader_mappings.yml
    spec_dict: Optional[Dict[str, Any]] = None

    def load(self) -> None:
        """
        loads from folder
        :return:
        """
        self.load_validators(f'{self.dirname}/metadata_validation.yml')
        self.load_spec(f'{self.dirname}/sample_uploader_mappings.yml')

    def load_validators(self, fn) -> None:
        """
        loads the metadata_validation.yml file
        :param fn:
        :return:
        """
        with open(fn, 'r') as stream:
            self.validators = yaml.safe_load(stream)['validators']

    def load_spec(self, fn) -> None:
        with open(fn, 'r') as stream:
            self.spec_dict = yaml.safe_load(stream)

    def convert_and_save(self, fn: str) -> None:
        obj = self.convert()
        with open(fn, 'w') as stream:
            yaml.safe_dump(obj, stream, sort_keys=False)

    def convert(self) -> Dict[str, Any]:
        slots = {}
        classes = {}
        obj = {
            'id': 'https://microbiomedata/schema/kbase',
            'description': 'NMDC rendering of KBase metadata schema',
            'imports': [
                'biolinkml:types'
            ],
            'prefixes': {
                'biolinkml': 'https://w3id.org/biolink/biolinkml/',
                'kbase': 'http://kbase.us/'
            },
            'default_prefix': 'kbase',
            'slots': slots,
            'classes': classes
        }
        for k,v in self.validators.items():
            meta = v['key_metadata']
            slot = {
                'aliases': [meta['display_name']]
            }
            if 'description' in meta:
                slot['description'] = meta['description']

            range = 'string'
            if 'validators' in v:
                for validator in v['validators']:
                    cb = validator['callable_builder']
                    if cb == 'number':
                        range = 'double'
            else:
                logging.error(f"no validator for {k}")
            slot['range'] = range
            slots[k] = slot

        shared_fields = self.spec_dict['shared_fields']
        for k,v in self.spec_dict.items():
            if k == 'shared_fields':
                continue
            cm = v['column_mapping']
            cslots = []
            for col in v['basic_columns'] + shared_fields:
                cslots.append(col)
                if col not in slots:
                    slots[col] = {
                        'description': 'Auto-populated'
                    }
            cls = {
                'description': 'TODO',
                'slots': cslots
            }
            classes[k] = cls
        return obj
