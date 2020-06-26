# Auto generated from gold.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-06-26 16:36
# Schema: ddl
#
# id: https://microbiomedata/schema/ddl
# description: Rendering of {id} schema
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import XSDTime
from includes.types import Double, Integer, String, Time

metamodel_version = "1.4.4"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DDL = CurieNamespace('ddl', 'https://microbiomedata/schema/ddl/')
DEFAULT_ = DDL


# Types

# Class references



@dataclass
class ANALYSISPROJECT(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ANALYSISPROJECT
    class_class_curie: ClassVar[str] = "ddl:ANALYSISPROJECT"
    class_name: ClassVar[str] = "ANALYSIS_PROJECT"
    class_model_uri: ClassVar[URIRef] = DDL.ANALYSISPROJECT

    ITS_ANALYSIS_PROJECT_ID: Optional[int] = None
    ANALYSIS_PROJECT_NAME: Optional[str] = None
    REFERENCE_AP_ID: Optional[int] = None
    IMG_TAXON_ID: Optional[int] = None
    ANALYSIS_PROJECT_TYPE: Optional[str] = None
    STATUS_ID: Optional[int] = None
    NCBI_TAX_ID: Optional[int] = None
    ADDED_BY: Optional[float] = None
    SUBMISSION_ID: Optional[int] = None
    GENE_COUNT: Optional[float] = None
    BINNING_METHOD: Optional[str] = None
    GENE_CALLING_METHOD: Optional[str] = None
    ITS_ANALYSIS_PROJECT_NAME: Optional[str] = None
    ITS_PRODUCT_NAME: Optional[str] = None
    GENBANK_LOW_QUALITY_ANNOTATION: Optional[str] = None
    IMG_ANALYSIS_COMPLETE: Optional[str] = None
    IS_GENE_PRIMP: Optional[str] = None
    IS_DECONTAMINATION: Optional[str] = None
    IS_IMG_ANNOTATION: Optional[str] = None
    ITS_ANNOTATION_AT_ID: Optional[int] = None
    IS_ASSEMBLED_DELETED: Optional[str] = None
    STUDY_ID: Optional[int] = None
    ITS_ASSEMBLY_AT_TYPE: Optional[str] = None
    APPENDED_AP_NAME: Optional[str] = None
    PI_NAME: Optional[str] = None
    ANALYSIS_PROJECT_NAME_FULL: Optional[str] = None
    IS_PRIMARY: Optional[str] = None
    PHYLOGENY_SUGGESTION: Optional[str] = None
    REPLACES_AP_ID: Optional[int] = None
    SCREENING_METHOD: Optional[str] = None
    DECONTAMINATION_METHOD: Optional[str] = None
    COMPLETION: Optional[str] = None
    REVIEW_STATUS: Optional[str] = None
    REJECTION_REASONS: Optional[str] = None
    PIPELINE_ANNOTATION_METHOD: Optional[str] = None
    CULTURE_COLLECTION: Optional[str] = None
    SEQUENCING_DEPTH: Optional[str] = None
    IMG_USE: Optional[str] = None
    AP_FOR_NONOWNER: Optional[str] = None
    ITS_NCBI_TAX_ID: Optional[int] = None
    ITS_VERSION_NUMBER: Optional[float] = None
    IMG_RNASEQ_ID: Optional[int] = None
    SUBMISSION_STATUS_ID: Optional[int] = None
    SUBMISSION_STATUS_NAME: Optional[str] = None
    SUBMISSION_COMMENTS: Optional[str] = None
    IMG_SUBMISSION_PRORITY: Optional[str] = None
    CONTAMINATION_PERCENTAGE: Optional[float] = None
    COMPLETENESS_PERCENTAGE: Optional[float] = None

@dataclass
class ANALYSISPROJECTSRARUNV2(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ANALYSISPROJECTSRARUNV2
    class_class_curie: ClassVar[str] = "ddl:ANALYSISPROJECTSRARUNV2"
    class_name: ClassVar[str] = "ANALYSIS_PROJECT_SRA_RUN_V2"
    class_model_uri: ClassVar[URIRef] = DDL.ANALYSISPROJECTSRARUNV2

    SRA_RUN_ID: Optional[str] = None

@dataclass
class BIOSAMPLE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.BIOSAMPLE
    class_class_curie: ClassVar[str] = "ddl:BIOSAMPLE"
    class_name: ClassVar[str] = "BIOSAMPLE"
    class_model_uri: ClassVar[URIRef] = DDL.BIOSAMPLE

    BIOSAMPLE_NAME: Optional[str] = None
    HABITAT: Optional[str] = None
    COMMUNITY: Optional[str] = None
    LOCATION: Optional[str] = None
    IDENTIFIER: Optional[str] = None
    JPA_ENTITY: Optional[str] = None
    BIOGAS_FED_SUBSTRATES: Optional[str] = None
    BIOGAS_RETENTION_TIME: Optional[str] = None
    BIOGAS_TEMPERATURE: Optional[str] = None
    BIOGAS_YIELD: Optional[str] = None
    BIOGAS_VOLATILE_ORGANIC_ACIDS: Optional[str] = None
    BIOGAS_TOTAL_INORGANIC_CARBON: Optional[str] = None
    BIOGAS_VOA_TIC: Optional[str] = None
    BIOGAS_AMMONIUM_NH4: Optional[str] = None
    BIOGAS_BUTANOL: Optional[str] = None
    BIOGAS_ETHANOL: Optional[str] = None
    BIOGAS_PROPANOL: Optional[str] = None
    BIOGAS_METHANOL: Optional[str] = None
    BIOGAS_ACETIC_ACID: Optional[str] = None
    BIOGAS_BUTYL_ACID: Optional[str] = None
    BIOGAS_ISO_BUTYL_ACID: Optional[str] = None
    BIOGAS_VALERIC_ACID: Optional[str] = None
    BIOGAS_ISO_VALERIC_ACID: Optional[str] = None
    BIOGAS_PROPIONIC_ACID: Optional[str] = None
    BIOGAS_METHANE_PCT: Optional[float] = None
    OXYGEN_PRESENCE: Optional[str] = None
    TEST_PACKAGE_ID: Optional[int] = None
    GLOBAL_PACKAGE_ID: Optional[int] = None

@dataclass
class CONTACT(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CONTACT
    class_class_curie: ClassVar[str] = "ddl:CONTACT"
    class_name: ClassVar[str] = "CONTACT"
    class_model_uri: ClassVar[URIRef] = DDL.CONTACT

    USERNAME: Optional[str] = None
    PASSWORD: Optional[str] = None
    EMAIL: Optional[str] = None
    PHONE: Optional[str] = None
    ADDRESS: Optional[str] = None
    CITY: Optional[str] = None
    STATE: Optional[str] = None
    X_SUPER_USER: Optional[str] = None
    X_IMG_EDITOR: Optional[str] = None
    X_IMG_GROUP: Optional[float] = None
    JGI_USER: Optional[str] = None
    X_IMG_EDITING_LEVEL: Optional[str] = None
    CALIBAN_ID: Optional[int] = None
    CALIBAN_USER_NAME: Optional[str] = None
    X_IMG_CONTACT_ID: Optional[int] = None
    MASTER_CONTACT_ID: Optional[int] = None
    ORACLE_USER_NAME: Optional[str] = None
    USER_ROLE: Optional[str] = None
    GEBA_ORGANISM_AVAIL_COUNT: Optional[float] = None
    GEBA_REVIEWER: Optional[str] = None

class CVAPCOMPLETION(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVAPCOMPLETION
    class_class_curie: ClassVar[str] = "ddl:CVAPCOMPLETION"
    class_name: ClassVar[str] = "CVAP_COMPLETION"
    class_model_uri: ClassVar[URIRef] = DDL.CVAPCOMPLETION


class CVAPREVIEWSTATUS(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVAPREVIEWSTATUS
    class_class_curie: ClassVar[str] = "ddl:CVAPREVIEWSTATUS"
    class_name: ClassVar[str] = "CVAP_REVIEW_STATUS"
    class_model_uri: ClassVar[URIRef] = DDL.CVAPREVIEWSTATUS


class CVAPSTATUS(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVAPSTATUS
    class_class_curie: ClassVar[str] = "ddl:CVAPSTATUS"
    class_name: ClassVar[str] = "CVAP_STATUS"
    class_model_uri: ClassVar[URIRef] = DDL.CVAPSTATUS


class CVAPTYPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVAPTYPE
    class_class_curie: ClassVar[str] = "ddl:CVAPTYPE"
    class_name: ClassVar[str] = "CVAP_TYPE"
    class_model_uri: ClassVar[URIRef] = DDL.CVAPTYPE


class CVAVAILABILITY(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVAVAILABILITY
    class_class_curie: ClassVar[str] = "ddl:CVAVAILABILITY"
    class_name: ClassVar[str] = "CVAVAILABILITY"
    class_model_uri: ClassVar[URIRef] = DDL.CVAVAILABILITY


class CVBIOME(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVBIOME
    class_class_curie: ClassVar[str] = "ddl:CVBIOME"
    class_name: ClassVar[str] = "CVBIOME"
    class_model_uri: ClassVar[URIRef] = DDL.CVBIOME


class CVBIOSAFETY(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVBIOSAFETY
    class_class_curie: ClassVar[str] = "ddl:CVBIOSAFETY"
    class_name: ClassVar[str] = "CVBIOSAFETY"
    class_model_uri: ClassVar[URIRef] = DDL.CVBIOSAFETY


class CVBIOTICRELATIONSHIP(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVBIOTICRELATIONSHIP
    class_class_curie: ClassVar[str] = "ddl:CVBIOTICRELATIONSHIP"
    class_name: ClassVar[str] = "CVBIOTIC_RELATIONSHIP"
    class_model_uri: ClassVar[URIRef] = DDL.CVBIOTICRELATIONSHIP


class CVBODYPRODUCT(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVBODYPRODUCT
    class_class_curie: ClassVar[str] = "ddl:CVBODYPRODUCT"
    class_name: ClassVar[str] = "CVBODY_PRODUCT"
    class_model_uri: ClassVar[URIRef] = DDL.CVBODYPRODUCT


class CVBODYSITE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVBODYSITE
    class_class_curie: ClassVar[str] = "ddl:CVBODYSITE"
    class_name: ClassVar[str] = "CVBODY_SITE"
    class_model_uri: ClassVar[URIRef] = DDL.CVBODYSITE


class CVBODYSUBSITE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVBODYSUBSITE
    class_class_curie: ClassVar[str] = "ddl:CVBODYSUBSITE"
    class_name: ClassVar[str] = "CVBODY_SUBSITE"
    class_model_uri: ClassVar[URIRef] = DDL.CVBODYSUBSITE


class CVCELLARRANGEMENT(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVCELLARRANGEMENT
    class_class_curie: ClassVar[str] = "ddl:CVCELLARRANGEMENT"
    class_name: ClassVar[str] = "CVCELL_ARRANGEMENT"
    class_model_uri: ClassVar[URIRef] = DDL.CVCELLARRANGEMENT


class CVCELLSHAPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVCELLSHAPE
    class_class_curie: ClassVar[str] = "ddl:CVCELLSHAPE"
    class_name: ClassVar[str] = "CVCELL_SHAPE"
    class_model_uri: ClassVar[URIRef] = DDL.CVCELLSHAPE


class CVCOLOR(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVCOLOR
    class_class_curie: ClassVar[str] = "ddl:CVCOLOR"
    class_name: ClassVar[str] = "CVCOLOR"
    class_model_uri: ClassVar[URIRef] = DDL.CVCOLOR


class CVCOUNTRY(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVCOUNTRY
    class_class_curie: ClassVar[str] = "ddl:CVCOUNTRY"
    class_name: ClassVar[str] = "CVCOUNTRY"
    class_model_uri: ClassVar[URIRef] = DDL.CVCOUNTRY


class CVCULTURETYPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVCULTURETYPE
    class_class_curie: ClassVar[str] = "ddl:CVCULTURETYPE"
    class_name: ClassVar[str] = "CVCULTURE_TYPE"
    class_model_uri: ClassVar[URIRef] = DDL.CVCULTURETYPE


class CVCURRENTLANDUSE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVCURRENTLANDUSE
    class_class_curie: ClassVar[str] = "ddl:CVCURRENTLANDUSE"
    class_name: ClassVar[str] = "CVCURRENT_LAND_USE"
    class_model_uri: ClassVar[URIRef] = DDL.CVCURRENTLANDUSE


class CVDATAVALIDITYTYPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVDATAVALIDITYTYPE
    class_class_curie: ClassVar[str] = "ddl:CVDATAVALIDITYTYPE"
    class_name: ClassVar[str] = "CVDATA_VALIDITY_TYPE"
    class_model_uri: ClassVar[URIRef] = DDL.CVDATAVALIDITYTYPE


class CVDISEASE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVDISEASE
    class_class_curie: ClassVar[str] = "ddl:CVDISEASE"
    class_name: ClassVar[str] = "CVDISEASE"
    class_model_uri: ClassVar[URIRef] = DDL.CVDISEASE


class CVDOMAIN(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVDOMAIN
    class_class_curie: ClassVar[str] = "ddl:CVDOMAIN"
    class_name: ClassVar[str] = "CVDOMAIN"
    class_model_uri: ClassVar[URIRef] = DDL.CVDOMAIN


class CVDRAINAGECLASS(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVDRAINAGECLASS
    class_class_curie: ClassVar[str] = "ddl:CVDRAINAGECLASS"
    class_name: ClassVar[str] = "CVDRAINAGE_CLASS"
    class_model_uri: ClassVar[URIRef] = DDL.CVDRAINAGECLASS


class CVENERGYSOURCE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVENERGYSOURCE
    class_class_curie: ClassVar[str] = "ddl:CVENERGYSOURCE"
    class_name: ClassVar[str] = "CVENERGY_SOURCE"
    class_model_uri: ClassVar[URIRef] = DDL.CVENERGYSOURCE


class CVENVPACKAGE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVENVPACKAGE
    class_class_curie: ClassVar[str] = "ddl:CVENVPACKAGE"
    class_name: ClassVar[str] = "CVENVPACKAGE"
    class_model_uri: ClassVar[URIRef] = DDL.CVENVPACKAGE


class CVFASTADOWNLOADSTATUS(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVFASTADOWNLOADSTATUS
    class_class_curie: ClassVar[str] = "ddl:CVFASTADOWNLOADSTATUS"
    class_name: ClassVar[str] = "CVFASTADOWNLOADSTATUS"
    class_model_uri: ClassVar[URIRef] = DDL.CVFASTADOWNLOADSTATUS


class CVFINISHINGGOAL(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVFINISHINGGOAL
    class_class_curie: ClassVar[str] = "ddl:CVFINISHINGGOAL"
    class_name: ClassVar[str] = "CVFINISHING_GOAL"
    class_model_uri: ClassVar[URIRef] = DDL.CVFINISHINGGOAL


class CVGEBAPRIORITYSTATUS(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVGEBAPRIORITYSTATUS
    class_class_curie: ClassVar[str] = "ddl:CVGEBAPRIORITYSTATUS"
    class_name: ClassVar[str] = "CVGEBA_PRIORITY_STATUS"
    class_model_uri: ClassVar[URIRef] = DDL.CVGEBAPRIORITYSTATUS


class CVGEBAREVIEWSTATUS(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVGEBAREVIEWSTATUS
    class_class_curie: ClassVar[str] = "ddl:CVGEBAREVIEWSTATUS"
    class_name: ClassVar[str] = "CVGEBA_REVIEW_STATUS"
    class_model_uri: ClassVar[URIRef] = DDL.CVGEBAREVIEWSTATUS


class CVGEBASAMPLETYPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVGEBASAMPLETYPE
    class_class_curie: ClassVar[str] = "ddl:CVGEBASAMPLETYPE"
    class_name: ClassVar[str] = "CVGEBA_SAMPLE_TYPE"
    class_model_uri: ClassVar[URIRef] = DDL.CVGEBASAMPLETYPE


class CVGEBATYPES(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVGEBATYPES
    class_class_curie: ClassVar[str] = "ddl:CVGEBATYPES"
    class_name: ClassVar[str] = "CVGEBA_TYPES"
    class_model_uri: ClassVar[URIRef] = DDL.CVGEBATYPES


class CVGRAMSTAIN(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVGRAMSTAIN
    class_class_curie: ClassVar[str] = "ddl:CVGRAMSTAIN"
    class_name: ClassVar[str] = "CVGRAM_STAIN"
    class_model_uri: ClassVar[URIRef] = DDL.CVGRAMSTAIN


class CVHABITAT(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVHABITAT
    class_class_curie: ClassVar[str] = "ddl:CVHABITAT"
    class_name: ClassVar[str] = "CVHABITAT"
    class_model_uri: ClassVar[URIRef] = DDL.CVHABITAT


class CVHORIZON(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVHORIZON
    class_class_curie: ClassVar[str] = "ddl:CVHORIZON"
    class_name: ClassVar[str] = "CVHORIZON"
    class_model_uri: ClassVar[URIRef] = DDL.CVHORIZON


class CVHOSTGENDER(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVHOSTGENDER
    class_class_curie: ClassVar[str] = "ddl:CVHOSTGENDER"
    class_name: ClassVar[str] = "CVHOST_GENDER"
    class_model_uri: ClassVar[URIRef] = DDL.CVHOSTGENDER


class CVIMGUSE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVIMGUSE
    class_class_curie: ClassVar[str] = "ddl:CVIMGUSE"
    class_name: ClassVar[str] = "CVIMGUSE"
    class_model_uri: ClassVar[URIRef] = DDL.CVIMGUSE


class CVIRRADIANCE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVIRRADIANCE
    class_class_curie: ClassVar[str] = "ddl:CVIRRADIANCE"
    class_name: ClassVar[str] = "CVIRRADIANCE"
    class_model_uri: ClassVar[URIRef] = DDL.CVIRRADIANCE


class CVLATLONG(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVLATLONG
    class_class_curie: ClassVar[str] = "ddl:CVLATLONG"
    class_name: ClassVar[str] = "CVLATLONG"
    class_model_uri: ClassVar[URIRef] = DDL.CVLATLONG


class CVMETABOLISM(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVMETABOLISM
    class_class_curie: ClassVar[str] = "ddl:CVMETABOLISM"
    class_name: ClassVar[str] = "CVMETABOLISM"
    class_model_uri: ClassVar[URIRef] = DDL.CVMETABOLISM


class CVMODEL(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVMODEL
    class_class_curie: ClassVar[str] = "ddl:CVMODEL"
    class_name: ClassVar[str] = "CVMODEL"
    class_model_uri: ClassVar[URIRef] = DDL.CVMODEL


class CVMONTH(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVMONTH
    class_class_curie: ClassVar[str] = "ddl:CVMONTH"
    class_name: ClassVar[str] = "CVMONTH"
    class_model_uri: ClassVar[URIRef] = DDL.CVMONTH


class CVMOTILITY(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVMOTILITY
    class_class_curie: ClassVar[str] = "ddl:CVMOTILITY"
    class_name: ClassVar[str] = "CVMOTILITY"
    class_model_uri: ClassVar[URIRef] = DDL.CVMOTILITY


class CVNUCLEICACID(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVNUCLEICACID
    class_class_curie: ClassVar[str] = "ddl:CVNUCLEICACID"
    class_name: ClassVar[str] = "CVNUCLEIC_ACID"
    class_model_uri: ClassVar[URIRef] = DDL.CVNUCLEICACID


class CVORGANISMTYPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVORGANISMTYPE
    class_class_curie: ClassVar[str] = "ddl:CVORGANISMTYPE"
    class_name: ClassVar[str] = "CVORGANISM_TYPE"
    class_model_uri: ClassVar[URIRef] = DDL.CVORGANISMTYPE


class CVOXYGEN(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVOXYGEN
    class_class_curie: ClassVar[str] = "ddl:CVOXYGEN"
    class_name: ClassVar[str] = "CVOXYGEN"
    class_model_uri: ClassVar[URIRef] = DDL.CVOXYGEN


class CVOXYGENPRESENCE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVOXYGENPRESENCE
    class_class_curie: ClassVar[str] = "ddl:CVOXYGENPRESENCE"
    class_name: ClassVar[str] = "CVOXYGEN_PRESENCE"
    class_model_uri: ClassVar[URIRef] = DDL.CVOXYGENPRESENCE


class CVOXYGENSTATSAMPLE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVOXYGENSTATSAMPLE
    class_class_curie: ClassVar[str] = "ddl:CVOXYGENSTATSAMPLE"
    class_name: ClassVar[str] = "CVOXYGEN_STAT_SAMPLE"
    class_model_uri: ClassVar[URIRef] = DDL.CVOXYGENSTATSAMPLE


class CVPACKAGES(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVPACKAGES
    class_class_curie: ClassVar[str] = "ddl:CVPACKAGES"
    class_name: ClassVar[str] = "CVPACKAGES"
    class_model_uri: ClassVar[URIRef] = DDL.CVPACKAGES


class CVPHENOTYPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVPHENOTYPE
    class_class_curie: ClassVar[str] = "ddl:CVPHENOTYPE"
    class_name: ClassVar[str] = "CVPHENOTYPE"
    class_model_uri: ClassVar[URIRef] = DDL.CVPHENOTYPE


class CVPHYLOGENY(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVPHYLOGENY
    class_class_curie: ClassVar[str] = "ddl:CVPHYLOGENY"
    class_name: ClassVar[str] = "CVPHYLOGENY"
    class_model_uri: ClassVar[URIRef] = DDL.CVPHYLOGENY


class CVPROFILEPOSITION(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVPROFILEPOSITION
    class_class_curie: ClassVar[str] = "ddl:CVPROFILEPOSITION"
    class_name: ClassVar[str] = "CVPROFILE_POSITION"
    class_model_uri: ClassVar[URIRef] = DDL.CVPROFILEPOSITION


class CVPROJECTSTATUS(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVPROJECTSTATUS
    class_class_curie: ClassVar[str] = "ddl:CVPROJECTSTATUS"
    class_name: ClassVar[str] = "CVPROJECT_STATUS"
    class_model_uri: ClassVar[URIRef] = DDL.CVPROJECTSTATUS


class CVPROJECTSUBTYPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVPROJECTSUBTYPE
    class_class_curie: ClassVar[str] = "ddl:CVPROJECTSUBTYPE"
    class_name: ClassVar[str] = "CVPROJECT_SUBTYPE"
    class_model_uri: ClassVar[URIRef] = DDL.CVPROJECTSUBTYPE


class CVPROJECTTYPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVPROJECTTYPE
    class_class_curie: ClassVar[str] = "ddl:CVPROJECTTYPE"
    class_name: ClassVar[str] = "CVPROJECT_TYPE"
    class_model_uri: ClassVar[URIRef] = DDL.CVPROJECTTYPE


class CVRELEVANCE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVRELEVANCE
    class_class_curie: ClassVar[str] = "ddl:CVRELEVANCE"
    class_name: ClassVar[str] = "CVRELEVANCE"
    class_model_uri: ClassVar[URIRef] = DDL.CVRELEVANCE


class CVROLES(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVROLES
    class_class_curie: ClassVar[str] = "ddl:CVROLES"
    class_name: ClassVar[str] = "CVROLES"
    class_model_uri: ClassVar[URIRef] = DDL.CVROLES


class CVSALINITY(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVSALINITY
    class_class_curie: ClassVar[str] = "ddl:CVSALINITY"
    class_name: ClassVar[str] = "CVSALINITY"
    class_model_uri: ClassVar[URIRef] = DDL.CVSALINITY


class CVSEQQUALITY(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVSEQQUALITY
    class_class_curie: ClassVar[str] = "ddl:CVSEQQUALITY"
    class_name: ClassVar[str] = "CVSEQ_QUALITY"
    class_model_uri: ClassVar[URIRef] = DDL.CVSEQQUALITY


class CVSEQSTATUS(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVSEQSTATUS
    class_class_curie: ClassVar[str] = "ddl:CVSEQSTATUS"
    class_name: ClassVar[str] = "CVSEQ_STATUS"
    class_model_uri: ClassVar[URIRef] = DDL.CVSEQSTATUS


class CVSOILFAOCLASS(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVSOILFAOCLASS
    class_class_curie: ClassVar[str] = "ddl:CVSOILFAOCLASS"
    class_name: ClassVar[str] = "CVSOILFAOCLASS"
    class_model_uri: ClassVar[URIRef] = DDL.CVSOILFAOCLASS


class CVSPECIMEN(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVSPECIMEN
    class_class_curie: ClassVar[str] = "ddl:CVSPECIMEN"
    class_name: ClassVar[str] = "CVSPECIMEN"
    class_model_uri: ClassVar[URIRef] = DDL.CVSPECIMEN


class CVSPORULATION(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVSPORULATION
    class_class_curie: ClassVar[str] = "ddl:CVSPORULATION"
    class_name: ClassVar[str] = "CVSPORULATION"
    class_model_uri: ClassVar[URIRef] = DDL.CVSPORULATION


class CVSTUDYTYPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVSTUDYTYPE
    class_class_curie: ClassVar[str] = "ddl:CVSTUDYTYPE"
    class_name: ClassVar[str] = "CVSTUDY_TYPE"
    class_model_uri: ClassVar[URIRef] = DDL.CVSTUDYTYPE


class CVTEMPRANGE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVTEMPRANGE
    class_class_curie: ClassVar[str] = "ddl:CVTEMPRANGE"
    class_name: ClassVar[str] = "CVTEMP_RANGE"
    class_model_uri: ClassVar[URIRef] = DDL.CVTEMPRANGE


class CVTIDALSTAGE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVTIDALSTAGE
    class_class_curie: ClassVar[str] = "ddl:CVTIDALSTAGE"
    class_name: ClassVar[str] = "CVTIDAL_STAGE"
    class_model_uri: ClassVar[URIRef] = DDL.CVTIDALSTAGE


class CVTILLAGE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVTILLAGE
    class_class_curie: ClassVar[str] = "ddl:CVTILLAGE"
    class_name: ClassVar[str] = "CVTILLAGE"
    class_model_uri: ClassVar[URIRef] = DDL.CVTILLAGE


class CVUNCULTUREDTYPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVUNCULTUREDTYPE
    class_class_curie: ClassVar[str] = "ddl:CVUNCULTUREDTYPE"
    class_name: ClassVar[str] = "CVUNCULTURED_TYPE"
    class_model_uri: ClassVar[URIRef] = DDL.CVUNCULTUREDTYPE


class CVYESNO(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVYESNO
    class_class_curie: ClassVar[str] = "ddl:CVYESNO"
    class_name: ClassVar[str] = "CVYES_NO"
    class_model_uri: ClassVar[URIRef] = DDL.CVYESNO


@dataclass
class CVYESNOONLY(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CVYESNOONLY
    class_class_curie: ClassVar[str] = "ddl:CVYESNOONLY"
    class_name: ClassVar[str] = "CVYES_NO_ONLY"
    class_model_uri: ClassVar[URIRef] = DDL.CVYESNOONLY

    TERM: Optional[str] = None
    SEQUENCE: Optional[float] = None

@dataclass
class ENVOLABELS(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ENVOLABELS
    class_class_curie: ClassVar[str] = "ddl:ENVOLABELS"
    class_name: ClassVar[str] = "ENVO_LABELS"
    class_model_uri: ClassVar[URIRef] = DDL.ENVOLABELS

    ENVO_LABEL: Optional[str] = None

@dataclass
class INSTITUTION(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.INSTITUTION
    class_class_curie: ClassVar[str] = "ddl:INSTITUTION"
    class_name: ClassVar[str] = "INSTITUTION"
    class_model_uri: ClassVar[URIRef] = DDL.INSTITUTION

    NAME: Optional[str] = None
    URL: Optional[str] = None
    COUNTRY: Optional[str] = None
    ORGANIZATION: Optional[str] = None
    DEPARTMENT: Optional[str] = None
    LABORATORY: Optional[str] = None
    IS_CURATED: Optional[str] = None

@dataclass
class ORGANISMBIOTICREL(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ORGANISMBIOTICREL
    class_class_curie: ClassVar[str] = "ddl:ORGANISMBIOTICREL"
    class_name: ClassVar[str] = "ORGANISM_BIOTIC_REL"
    class_model_uri: ClassVar[URIRef] = DDL.ORGANISMBIOTICREL

    BIOTIC_RELATIONSHIP_ID: Optional[int] = None

@dataclass
class ORGANISMBODYPRODUCT(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ORGANISMBODYPRODUCT
    class_class_curie: ClassVar[str] = "ddl:ORGANISMBODYPRODUCT"
    class_name: ClassVar[str] = "ORGANISM_BODY_PRODUCT"
    class_model_uri: ClassVar[URIRef] = DDL.ORGANISMBODYPRODUCT

    BODY_PRODUCT_ID: Optional[int] = None

@dataclass
class ORGANISMCELLARRANGEMENT(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ORGANISMCELLARRANGEMENT
    class_class_curie: ClassVar[str] = "ddl:ORGANISMCELLARRANGEMENT"
    class_name: ClassVar[str] = "ORGANISM_CELL_ARRANGEMENT"
    class_model_uri: ClassVar[URIRef] = DDL.ORGANISMCELLARRANGEMENT

    CELL_ARRANGEMENT_ID: Optional[int] = None

@dataclass
class ORGANISMDISEASE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ORGANISMDISEASE
    class_class_curie: ClassVar[str] = "ddl:ORGANISMDISEASE"
    class_name: ClassVar[str] = "ORGANISM_DISEASE"
    class_model_uri: ClassVar[URIRef] = DDL.ORGANISMDISEASE

    DISEASE_ID: Optional[int] = None

@dataclass
class ORGANISMENERGYSOURCE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ORGANISMENERGYSOURCE
    class_class_curie: ClassVar[str] = "ddl:ORGANISMENERGYSOURCE"
    class_name: ClassVar[str] = "ORGANISM_ENERGY_SOURCE"
    class_model_uri: ClassVar[URIRef] = DDL.ORGANISMENERGYSOURCE

    ENERGY_SOURCE_ID: Optional[int] = None

@dataclass
class ORGANISMHABITAT(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ORGANISMHABITAT
    class_class_curie: ClassVar[str] = "ddl:ORGANISMHABITAT"
    class_name: ClassVar[str] = "ORGANISM_HABITAT"
    class_model_uri: ClassVar[URIRef] = DDL.ORGANISMHABITAT

    HABITAT_ID: Optional[int] = None

@dataclass
class ORGANISMMETABOLISM(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ORGANISMMETABOLISM
    class_class_curie: ClassVar[str] = "ddl:ORGANISMMETABOLISM"
    class_name: ClassVar[str] = "ORGANISM_METABOLISM"
    class_model_uri: ClassVar[URIRef] = DDL.ORGANISMMETABOLISM

    METABOLISM_ID: Optional[int] = None

@dataclass
class ORGANISMPHENOTYPE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ORGANISMPHENOTYPE
    class_class_curie: ClassVar[str] = "ddl:ORGANISMPHENOTYPE"
    class_name: ClassVar[str] = "ORGANISM_PHENOTYPE"
    class_model_uri: ClassVar[URIRef] = DDL.ORGANISMPHENOTYPE

    PHENOTYPE_ID: Optional[int] = None

@dataclass
class ORGANISMV2(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ORGANISMV2
    class_class_curie: ClassVar[str] = "ddl:ORGANISMV2"
    class_name: ClassVar[str] = "ORGANISM_V2"
    class_model_uri: ClassVar[URIRef] = DDL.ORGANISMV2

    EXEMPLAR_DOI: Optional[str] = None
    EXEMPLAR_NAME: Optional[str] = None
    TAXON_DOI: Optional[str] = None
    CULTURE_COLLECTION_ID: Optional[str] = None
    TYPE_STRAIN: Optional[str] = None
    BIOSAFETY_LEVEL: Optional[str] = None
    NCBI_TAXONOMY_ID: Optional[int] = None
    NCBI_KINGDOM: Optional[str] = None
    NCBI_PHYLUM: Optional[str] = None
    NCBI_CLASS: Optional[str] = None
    NCBI_ORDER: Optional[str] = None
    NCBI_FAMILY: Optional[str] = None
    NCBI_GENUS: Optional[str] = None
    DOMAIN: Optional[str] = None
    STRAIN_INFO_ID: Optional[int] = None
    GENBANK_16S_ID: Optional[str] = None
    OXYGEN_REQUIREMENT: Optional[str] = None
    CELL_SHAPE: Optional[str] = None
    MOTILITY: Optional[str] = None
    SPORULATION: Optional[str] = None
    TEMPERATURE_RANGE: Optional[str] = None
    COLOR: Optional[str] = None
    GRAM_STAIN: Optional[str] = None
    COMMON_NAME: Optional[str] = None
    SYMBIOTIC_RELATIONSHIP: Optional[str] = None
    SYMBIOTIC_PHYSICAL_INTERACTION: Optional[str] = None
    SYMBIONT_NAME: Optional[str] = None
    SYMBIONT_TAXON_ID: Optional[int] = None
    CELL_LENGTH: Optional[str] = None
    SUBSPECIES: Optional[str] = None
    COMMERCIAL: Optional[str] = None
    COMMERCIAL_COMMENTS: Optional[str] = None
    OTHER_NAMES: Optional[str] = None
    SYNONYM_GROUP_ID: Optional[int] = None
    VIRAL_GROUP: Optional[str] = None
    VIRAL_SUBGROUP: Optional[str] = None
    GOLD_PHYLOGENY: Optional[str] = None
    CULTURE_TYPE: Optional[str] = None
    UNCULTURED_TYPE: Optional[str] = None
    CULTURED: Optional[str] = None
    CLADE: Optional[str] = None
    MASTER_GROUP_ID: Optional[int] = None
    ECOTYPE: Optional[str] = None
    CARBON_SOURCE: Optional[str] = None
    IMAGE_ID: Optional[int] = None
    NCBI_BIOSAMPLE_ID: Optional[str] = None
    OTHER_ECOSYSTEM: Optional[str] = None
    SAMPLE_COLLECTION_SITE: Optional[str] = None
    SAMPLE_ISOLATION_COMMENTS: Optional[str] = None
    SAMPLING_STRATEGY: Optional[str] = None
    REPLICATE_NUMBER: Optional[float] = None
    SAMPLE_VOLUME: Optional[str] = None
    SAMPLE_BIOMASS: Optional[str] = None
    SAMPLE_CONTACT_NAME: Optional[str] = None
    SAMPLE_CONTACT_EMAIL: Optional[str] = None
    GEOGRAPHIC_LOCATION: Optional[str] = None
    LAT_LONG_INFERRED: Optional[str] = None
    HOST_NAME: Optional[str] = None
    HOST_TAXONOMY_ID: Optional[int] = None
    HOST_GENDER: Optional[str] = None
    HOST_RACE: Optional[str] = None
    HOST_AGE: Optional[str] = None
    HOST_HEALTH_CONDITION: Optional[str] = None
    PATIENT_VISIT_NUMBER: Optional[float] = None
    HOST_MEDICATION: Optional[str] = None
    MRN: Optional[str] = None
    HOST_BODY_SITE: Optional[str] = None
    HOST_BODY_SUBSITE: Optional[str] = None
    HOST_BODY_PRODUCT: Optional[str] = None
    HOST_SPECIFICITY: Optional[str] = None
    HOST_COMMENTS: Optional[str] = None
    SPECIMEN: Optional[str] = None
    SUBMIT_BIOSAMPLE_NAME: Optional[str] = None
    ENV_PACKAGE: Optional[str] = None
    SAMPLE_COLLECTION_DAY: Optional[float] = None
    SAMPLE_COLLECTION_MONTH: Optional[float] = None
    SAMPLE_COLLECTION_YEAR: Optional[float] = None
    SAMPLE_COLLECTION_HOUR: Optional[float] = None
    SAMPLE_COLLECTION_MINUTE: Optional[float] = None
    GROWTH_CONDITIONS: Optional[str] = None
    OTHER_HOSTS: Optional[str] = None
    KNOWN_NON_HOSTS: Optional[str] = None
    ISOLATION_PUBMED_ID: Optional[int] = None
    HOST_BODY_SITE_ID: Optional[int] = None
    HOST_BODY_SUBSITE_ID: Optional[int] = None
    HOST_BODY_PRODUCT_ID: Optional[int] = None
    SAMPLE_ISOLATION_COUNTRY_ID: Optional[int] = None
    LONGHURST_CODE: Optional[str] = None
    CHLOROPHYLL_CONCENTRATION: Optional[str] = None
    NITRATE_CONCENTRATION: Optional[str] = None
    OXYGEN_CONCENTRATION: Optional[str] = None
    SALINITY_CONCENTRATION: Optional[str] = None
    CRUISE_LINE_NAME: Optional[str] = None
    PROPORT_OCEAN: Optional[str] = None
    PROPORT_ISOLATION: Optional[str] = None
    PROPORT_STATION: Optional[str] = None
    PROPORT_WOA_TEMPERATURE: Optional[float] = None
    PROPORT_WOA_SALINITY: Optional[float] = None
    PROPORT_WOA_DISSOLVED_OXYGEN: Optional[float] = None
    PROPORT_WOA_SILICATE: Optional[float] = None
    PROPORT_WOA_PHOSPHATE: Optional[float] = None
    PROPORT_WOA_NITRATE: Optional[float] = None
    ITS_GROWTH_CONDITIONS: Optional[str] = None
    ORGANISM_NAME: Optional[str] = None
    SUBMIT_ORGANISM_NAME: Optional[str] = None
    NCBI_TAXONOMY_NAME: Optional[str] = None
    GENUS: Optional[str] = None
    GENUS_SYNONYMS: Optional[str] = None
    SPECIES: Optional[str] = None
    SPECIES_SYNONYMS: Optional[str] = None
    STRAIN: Optional[str] = None
    SEROVAR: Optional[str] = None
    COMMENTS: Optional[str] = None
    NCBI_SPECIES: Optional[str] = None
    SALINITY: Optional[str] = None
    PRESSURE: Optional[str] = None
    PH: Optional[str] = None
    CELL_DIAMETER: Optional[str] = None
    IS_VIROCELL: Optional[str] = None
    STRAININFO_GROUP_ID: Optional[int] = None
    SOURCE: Optional[str] = None
    GOLD_CLASS: Optional[str] = None
    GOLD_ORDER: Optional[str] = None
    GOLD_FAMILY: Optional[str] = None
    NCBI_SUPERKINGDOM: Optional[str] = None
    TAXONOMY_STATUS: Optional[str] = None
    GROWTH_TEMPERATURE: Optional[float] = None
    SUBSURFACE_DEPTH: Optional[float] = None
    LEGACY_DEPTH_DATA: Optional[str] = None
    LATITUDE_TEST: Optional[float] = None
    LONGITUDE_TEST: Optional[float] = None
    ELEVATION: Optional[float] = None
    ELEVATION2: Optional[float] = None
    SOIL_CURR_LAND_USE: Optional[str] = None
    SOIL_CURR_VEGETATION: Optional[str] = None
    SOIL_CURR_VEGETATION_METHOD: Optional[str] = None
    SOIL_PREV_LAND_USE: Optional[str] = None
    SOIL_PREV_LAND_USE_METH: Optional[str] = None
    SOIL_CROP_ROTATION: Optional[str] = None
    SOIL_AGROCHEM_ADDITION: Optional[str] = None
    SOIL_TILLAGE: Optional[str] = None
    SOIL_FIRE: Optional[str] = None
    SOIL_FLOODING: Optional[str] = None
    SOIL_EXTREME_EVENT: Optional[str] = None
    SOIL_HORIZON: Optional[str] = None
    SOIL_HORIZON_METHOD: Optional[str] = None
    SOIL_SIEVING: Optional[str] = None
    SOIL_WATER_CONTENT: Optional[str] = None
    SOIL_WATER_CONTENT_SOIL_METH: Optional[str] = None
    SAMPLE_WEIGHT_DNA_EXT: Optional[str] = None
    SOIL_POOL_DNA_EXTRACTS: Optional[str] = None
    SOIL_STORAGE_CONDITION: Optional[str] = None
    SOIL_LINK_CLIMATE_INFO: Optional[str] = None
    SOIL_LINK_CLASS_INFO: Optional[str] = None
    SOIL_FAO_CLASS: Optional[str] = None
    SOIL_LOCAL_CLASS: Optional[str] = None
    SOIL_LOCAL_CLASS_METHOD: Optional[str] = None
    SOIL_TYPE: Optional[str] = None
    SOIL_TYPE_METHOD: Optional[str] = None
    SOIL_SLOPE_GRADIENT: Optional[float] = None
    SOIL_SLOPE_ASPECT: Optional[float] = None
    SOIL_PROFILE_POSITION: Optional[str] = None
    SOIL_DRAINAGE_CLASS: Optional[str] = None
    SOIL_TEXTURE: Optional[str] = None
    SOIL_TEXTURE_METHOD: Optional[str] = None
    SOIL_PH_METHOD: Optional[str] = None
    TOT_ORG_CARBON: Optional[float] = None
    SOIL_TOT_ORG_C_METHOD: Optional[str] = None
    TOT_NITROGEN: Optional[str] = None
    SOIL_TOT_N_METHOD: Optional[str] = None
    SOIL_MICROBIAL_BIOMASS: Optional[str] = None
    SOIL_MICROBIAL_BIOMASS_METHOD: Optional[str] = None
    SOIL_LINK_ADDIT_ANALYS: Optional[str] = None
    SOIL_SALINITY_METHOD: Optional[str] = None
    SOIL_HEAVY_METALS: Optional[float] = None
    SOIL_HEAVY_METALS_METHOD: Optional[str] = None
    SOIL_ALUMINIUM_SAT: Optional[float] = None
    SOIL_ALUMINIUM_SAT_METHOD: Optional[str] = None
    SOIL_MISC_PARAM: Optional[str] = None
    WATER_ALKALINITY: Optional[float] = None
    WATER_ALKYL_DIETHERS: Optional[float] = None
    WATER_AMINOPEPT_ACT: Optional[float] = None
    WATER_AMMONIUM: Optional[float] = None
    WATER_ATMOSPHERIC_DATA: Optional[str] = None
    WATER_BACTERIAL_PROD: Optional[float] = None
    WATER_BACTERIAL_RESP: Optional[float] = None
    WATER_BACTERIAL_CARBON_PROD: Optional[float] = None
    WATER_BISHOMOHOPANOL: Optional[str] = None
    WATER_BROMIDE: Optional[float] = None
    WATER_CALCIUM: Optional[str] = None
    WATER_CARBON_NITROG_RATIO: Optional[str] = None
    WATER_CHEM_ADMINISTRATION: Optional[str] = None
    WATER_CHLORIDE: Optional[float] = None
    WATER_DENSITY: Optional[float] = None
    WATER_DIETHER_LIPIDS: Optional[float] = None
    WATER_DISS_CARBON_DIOXIDE: Optional[float] = None
    WATER_DISS_HYDROGEN: Optional[float] = None
    WATER_DISS_INORG_CARBON: Optional[float] = None
    WATER_DISS_INORG_NITRO: Optional[float] = None
    WATER_DISS_INORG_PHOSPHORUS: Optional[float] = None
    WATER_DISS_ORG_CARBON: Optional[float] = None
    WATER_DISS_ORG_NITROGEN: Optional[float] = None
    WATER_DOWNWARD_PAR: Optional[float] = None
    WATER_FLUORESCENCE: Optional[float] = None
    WATER_GLUCOSIDASE_ACTIVITY: Optional[float] = None
    WATER_LIGHT_INTENSITY: Optional[float] = None
    WATER_MAGNESIUM: Optional[str] = None
    WATER_MEAN_FRICT_VEL: Optional[float] = None
    WATER_MEAN_PEAK_FRICT_VEL: Optional[float] = None
    WATER_MISC_PARAMETER: Optional[str] = None
    WATER_N_ALKANES: Optional[float] = None
    WATER_NITRITE: Optional[float] = None
    WATER_ORG_MATTER: Optional[float] = None
    WATER_ORG_NITROGEN: Optional[float] = None
    WATER_ORGANISM_COUNT: Optional[float] = None
    WATER_OXY_STAT_SAMPLE: Optional[str] = None
    WATER_PART_ORG_CARBON: Optional[float] = None
    WATER_PART_ORG_NITROGEN: Optional[float] = None
    WATER_PERTURBATION: Optional[str] = None
    WATER_PETROLEUM_HYDROCARBON: Optional[float] = None
    WATER_PHAEOPIGMENTS: Optional[float] = None
    WATER_PHOSPLIPID_FATT_ACID: Optional[str] = None
    WATER_PHOTON_FLUX: Optional[float] = None
    WATER_POTASSIUM: Optional[float] = None
    WATER_PRIMARY_PROD: Optional[float] = None
    WATER_REDOX_POTENTIAL: Optional[float] = None
    WATER_SAMP_STORE_DUR: Optional[str] = None
    WATER_SAMP_STORE_LOC: Optional[str] = None
    WATER_SAMP_STORE_TEMP: Optional[float] = None
    WATER_SODIUM: Optional[float] = None
    WATER_SOLUBLE_REACT_PHOSP: Optional[float] = None
    WATER_SULFATE: Optional[str] = None
    WATER_SULFIDE: Optional[str] = None
    WATER_SUSPEND_PART_MATTER: Optional[float] = None
    WATER_TIDAL_STAGE: Optional[str] = None
    WATER_TOT_DEPTH_WATER_COL: Optional[float] = None
    WATER_TOT_DISS_NITRO: Optional[float] = None
    WATER_TOT_INORG_NITRO: Optional[float] = None
    WATER_TOT_PART_CARBON: Optional[str] = None
    WATER_TOT_PHOSPHORUS: Optional[float] = None
    WATER_CURRENT: Optional[str] = None
    ALTITUDE: Optional[float] = None
    ALTITUDE2: Optional[float] = None
    DEPTH: Optional[float] = None
    DEPTH2: Optional[float] = None
    LONGITUDE: Optional[float] = None
    LATITUDE: Optional[float] = None
    BICARBONATE_MILLIMOL: Optional[float] = None
    SOLUBLE_IRON_MICROMOL: Optional[float] = None
    H2S_MILLIMOL: Optional[float] = None
    H2S_PRESENT: Optional[str] = None
    IRRADIANCE: Optional[str] = None
    METHANE_CONC_MILLIMOL: Optional[float] = None
    SAMPLE_CONDUCTIVITY: Optional[str] = None
    SOIL_SAMPLE_BIOMASS: Optional[float] = None
    SOIL_SAMPLE_VOLUME: Optional[float] = None
    IMG_BREADTH_CALC: Optional[float] = None
    GROWTH_TEMPERATURE2: Optional[float] = None
    SAMPLE_COLLECTION_TEMPERATURE: Optional[float] = None
    SAMPLE_COLLECTION_TEMPERATURE2: Optional[float] = None
    SUBSURFACE_DEPTH1: Optional[float] = None
    SUBSURFACE_DEPTH2: Optional[float] = None
    PH1: Optional[float] = None
    PH2: Optional[float] = None
    PH_OLD: Optional[str] = None
    WATER_ALKALINITY_METHOD: Optional[str] = None
    WATER_TURBIDITY: Optional[str] = None
    WATER_SIZE_FRAC_LOW: Optional[float] = None
    WATER_SIZE_FRAC_UP: Optional[float] = None
    SOIL_MEAN_ANNUAL_TEMP: Optional[float] = None
    SOIL_MEAN_SEASONAL_TEMP: Optional[float] = None
    SOIL_MEAN_ANNUAL_PRECPT: Optional[float] = None
    SOIL_MEAN_SEASONAL_PRECPT: Optional[float] = None
    SOIL_PACKAGE_ID: Optional[int] = None
    WATER_PACKAGE_ID: Optional[int] = None
    ENVO_BIOME_ID: Optional[str] = None
    ENVO_FEATURE_ID: Optional[str] = None
    ENVO_MATERIAL_ID: Optional[str] = None

@dataclass
class PROJECT(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.PROJECT
    class_class_curie: ClassVar[str] = "ddl:PROJECT"
    class_name: ClassVar[str] = "PROJECT"
    class_model_uri: ClassVar[URIRef] = DDL.PROJECT

    PROJECT_NAME: Optional[str] = None
    NCBI_BIOPROJECT_ID: Optional[int] = None
    MOD_BY: Optional[float] = None
    SPECIMEN_ID: Optional[int] = None
    ORGANISM_TYPE: Optional[str] = None
    NUCLEIC_ACID: Optional[str] = None
    SUBMITTER_PROJECT_NAME: Optional[str] = None
    NCBI_PROJECT_NAME: Optional[str] = None
    ISOLATION_PUBLICATION_ID: Optional[int] = None
    COMPLETION_DATE: Optional[Union[str, XSDTime]] = None
    PMO_PROJECT_ID: Optional[int] = None
    ITS_SPID: Optional[float] = None
    SAMPLE_OID: Optional[float] = None
    OLD_LEGACY_GOLD_ID: Optional[str] = None
    ORGANISM_ID: Optional[int] = None
    SEQUENCING_STATUS_ID: Optional[int] = None
    SEQUENCING_QUALITY_ID: Optional[int] = None
    FINISHING_GOAL_ID: Optional[int] = None
    SEQUENCING_COMMENTS: Optional[str] = None
    GC_PERCENT: Optional[float] = None
    CONTIG_COUNT: Optional[float] = None
    EST_SIZE: Optional[float] = None
    CHROMOSOME_COUNT: Optional[float] = None
    PLASMID_COUNT: Optional[float] = None
    SCAFFOLD_COUNT: Optional[float] = None
    EST_COUNT: Optional[float] = None
    SUBMITTER_ID: Optional[int] = None
    NCBI_BIOPROJECT_ACCESSION: Optional[str] = None
    PROJECT_COMMENTS: Optional[str] = None
    ANNOTATOR_COMMENTS: Optional[str] = None
    NCBI_SRA_ID: Optional[str] = None
    LIBRARY_METHOD: Optional[str] = None
    READ_COUNT: Optional[str] = None
    VECTOR: Optional[str] = None
    READ_SIZE: Optional[str] = None
    NCBI_LOCUS_TAG: Optional[str] = None
    ASSEMBLY_ACCESSION: Optional[str] = None
    NUCLEIC_ACID_ID: Optional[int] = None
    PI_ID: Optional[int] = None
    PROJECT_STATUS: Optional[str] = None
    MASTER_STUDY_ID: Optional[int] = None
    OTHER_PROJECT_NAMES: Optional[str] = None
    ITS_PROJECT_NAME: Optional[str] = None
    IS_SINGLE_CELL_MATERIAL: Optional[str] = None
    ITS_SEQUENCING_PRODUCT_NAME: Optional[str] = None
    PROJECT_MANAGER_ID: Optional[int] = None
    NCBI_BIOSAMPLE_ACCESSION: Optional[str] = None
    LOW_QUALITY_GENOME: Optional[str] = None
    SEQUENCING_STRATEGY: Optional[str] = None
    IS_JGI: Optional[str] = None
    SRA_SRS_ACCESSION: Optional[str] = None
    SRA_SRX_ACCESSION: Optional[str] = None
    FUNDING_PROGRAM: Optional[str] = None
    FUNDING_YEAR: Optional[float] = None
    ITS_SAMPLE_ID: Optional[int] = None
    ITS_SAMPLE_GROUP_NAME: Optional[str] = None
    EXPERIMENTAL_CONDITIONS: Optional[str] = None
    SAMPLE_GROUP_NAME: Optional[str] = None
    ITS_SAMPLE_NAME: Optional[str] = None
    PROJECT_SUBTYPE: Optional[str] = None
    SEQUENCING_STRATEGY_FULL: Optional[str] = None
    IS_APPROVED: Optional[str] = None
    IS_LOCKED: Optional[str] = None
    GPTS_SAMPLE_ID: Optional[int] = None
    GPTS_DISAMBIGUATOR: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.COMPLETION_DATE is not None and not isinstance(self.COMPLETION_DATE, XSDTime):
            self.COMPLETION_DATE = XSDTime(self.COMPLETION_DATE)
        super().__post_init__(**kwargs)


@dataclass
class PROJECTANALYSISPROJECT(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.PROJECTANALYSISPROJECT
    class_class_curie: ClassVar[str] = "ddl:PROJECTANALYSISPROJECT"
    class_name: ClassVar[str] = "PROJECT_ANALYSIS_PROJECT"
    class_model_uri: ClassVar[URIRef] = DDL.PROJECTANALYSISPROJECT

    ANALYSIS_PROJECT_ID: Optional[int] = None

@dataclass
class PROJECTBIOSAMPLE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.PROJECTBIOSAMPLE
    class_class_curie: ClassVar[str] = "ddl:PROJECTBIOSAMPLE"
    class_name: ClassVar[str] = "PROJECT_BIOSAMPLE"
    class_model_uri: ClassVar[URIRef] = DDL.PROJECTBIOSAMPLE

    BIOSAMPLE_ID: Optional[int] = None

class PROJECTCOLLABORATOR(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.PROJECTCOLLABORATOR
    class_class_curie: ClassVar[str] = "ddl:PROJECTCOLLABORATOR"
    class_name: ClassVar[str] = "PROJECT_COLLABORATOR"
    class_model_uri: ClassVar[URIRef] = DDL.PROJECTCOLLABORATOR


class PROJECTFUNDINGAGENCY(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.PROJECTFUNDINGAGENCY
    class_class_curie: ClassVar[str] = "ddl:PROJECTFUNDINGAGENCY"
    class_name: ClassVar[str] = "PROJECT_FUNDING_AGENCY"
    class_model_uri: ClassVar[URIRef] = DDL.PROJECTFUNDINGAGENCY


class PROJECTGENOMEPUBLICATION(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.PROJECTGENOMEPUBLICATION
    class_class_curie: ClassVar[str] = "ddl:PROJECTGENOMEPUBLICATION"
    class_name: ClassVar[str] = "PROJECT_GENOME_PUBLICATION"
    class_model_uri: ClassVar[URIRef] = DDL.PROJECTGENOMEPUBLICATION


@dataclass
class PROJECTOTHERPUBLICATION(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.PROJECTOTHERPUBLICATION
    class_class_curie: ClassVar[str] = "ddl:PROJECTOTHERPUBLICATION"
    class_name: ClassVar[str] = "PROJECT_OTHER_PUBLICATION"
    class_model_uri: ClassVar[URIRef] = DDL.PROJECTOTHERPUBLICATION

    PUBLICATION_ID: Optional[int] = None

@dataclass
class PROJECTRELEVANCE(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.PROJECTRELEVANCE
    class_class_curie: ClassVar[str] = "ddl:PROJECTRELEVANCE"
    class_name: ClassVar[str] = "PROJECT_RELEVANCE"
    class_model_uri: ClassVar[URIRef] = DDL.PROJECTRELEVANCE

    RELEVANCE_ID: Optional[int] = None

@dataclass
class PROJECTSEQUENCINGCENTER(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.PROJECTSEQUENCINGCENTER
    class_class_curie: ClassVar[str] = "ddl:PROJECTSEQUENCINGCENTER"
    class_name: ClassVar[str] = "PROJECT_SEQUENCING_CENTER"
    class_model_uri: ClassVar[URIRef] = DDL.PROJECTSEQUENCINGCENTER

    INSTITUTION_ID: Optional[int] = None

@dataclass
class PROJECTSEQUENCINGMETHOD(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.PROJECTSEQUENCINGMETHOD
    class_class_curie: ClassVar[str] = "ddl:PROJECTSEQUENCINGMETHOD"
    class_name: ClassVar[str] = "PROJECT_SEQUENCING_METHOD"
    class_model_uri: ClassVar[URIRef] = DDL.PROJECTSEQUENCINGMETHOD

    SEQUENCING_METHOD_ID: Optional[int] = None

@dataclass
class PUBLICATION(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.PUBLICATION
    class_class_curie: ClassVar[str] = "ddl:PUBLICATION"
    class_name: ClassVar[str] = "PUBLICATION"
    class_model_uri: ClassVar[URIRef] = DDL.PUBLICATION

    DOI: Optional[str] = None
    PUBMED_ID: Optional[int] = None
    JOURNAL_ID: Optional[int] = None
    PUBMODEL: Optional[str] = None
    VOLUME: Optional[str] = None
    ISSUE: Optional[str] = None
    PAGE: Optional[str] = None
    PUBLICATION_DATE: Optional[str] = None
    ABSTRACT: Optional[str] = None
    AFFILIATION: Optional[str] = None
    TITLE: Optional[str] = None
    LAST_AUTHOR_ID: Optional[int] = None
    FIRST_AUTHOR_ID: Optional[int] = None

@dataclass
class STUDY(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.STUDY
    class_class_curie: ClassVar[str] = "ddl:STUDY"
    class_name: ClassVar[str] = "STUDY"
    class_model_uri: ClassVar[URIRef] = DDL.STUDY

    STUDY_NAME: Optional[str] = None
    ITS_PROPOSAL_ID: Optional[int] = None
    NCBI_PROJECT_ID: Optional[int] = None
    ADD_DATE: Optional[Union[str, XSDTime]] = None
    MOD_DATE: Optional[Union[str, XSDTime]] = None
    CONTACT_ID: Optional[int] = None
    LAST_MOD_BY: Optional[float] = None
    IS_PUBLIC: Optional[str] = None
    GPTS_PROPOSAL_ID: Optional[int] = None
    PROJECT_OID: Optional[float] = None
    ACTIVE: Optional[str] = None
    LEGACY_GOLD_ID: Optional[str] = None
    BIOPROJECT_NAME: Optional[str] = None
    GOLD_STUDY_NAME: Optional[str] = None
    DESCRIPTION: Optional[str] = None
    GOLD_ID: Optional[str] = None
    METAGENOMIC: Optional[str] = None
    STUDY_TYPE_ID: Optional[int] = None
    ECOSYSTEM: Optional[str] = None
    ECOSYSTEM_CATEGORY: Optional[str] = None
    ECOSYSTEM_TYPE: Optional[str] = None
    ECOSYSTEM_SUBTYPE: Optional[str] = None
    SPECIFIC_ECOSYSTEM: Optional[str] = None
    OWNER_ID: Optional[int] = None
    IS_DRAFT: Optional[str] = None
    PUBLIC_SP_COUNT: Optional[float] = None
    ADMIN_SP_COUNT: Optional[float] = None
    PUBLIC_AP_COUNT: Optional[float] = None
    ADMIN_AP_COUNT: Optional[float] = None
    PUBLIC_DAP_COUNT: Optional[float] = None
    ADMIN_DAP_COUNT: Optional[float] = None
    PUBLIC_BIOSAMPLE_COUNT: Optional[float] = None
    ADMIN_BIOSAMPLE_COUNT: Optional[float] = None
    IS_GEBA: Optional[str] = None
    IS_HMP: Optional[str] = None
    ECOSYSTEM_PATH_ID: Optional[int] = None
    IS_TEST: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.ADD_DATE is not None and not isinstance(self.ADD_DATE, XSDTime):
            self.ADD_DATE = XSDTime(self.ADD_DATE)
        if self.MOD_DATE is not None and not isinstance(self.MOD_DATE, XSDTime):
            self.MOD_DATE = XSDTime(self.MOD_DATE)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.ITS_ANALYSIS_PROJECT_ID = Slot(uri=DDL.ITS_ANALYSIS_PROJECT_ID, name="ITS_ANALYSIS_PROJECT_ID", curie=DDL.curie('ITS_ANALYSIS_PROJECT_ID'),
                      model_uri=DDL.ITS_ANALYSIS_PROJECT_ID, domain=None, range=Optional[int])

slots.ANALYSIS_PROJECT_NAME = Slot(uri=DDL.ANALYSIS_PROJECT_NAME, name="ANALYSIS_PROJECT_NAME", curie=DDL.curie('ANALYSIS_PROJECT_NAME'),
                      model_uri=DDL.ANALYSIS_PROJECT_NAME, domain=None, range=Optional[str])

slots.GOLD_ID = Slot(uri=DDL.GOLD_ID, name="GOLD_ID", curie=DDL.curie('GOLD_ID'),
                      model_uri=DDL.GOLD_ID, domain=None, range=Optional[str])

slots.REFERENCE_AP_ID = Slot(uri=DDL.REFERENCE_AP_ID, name="REFERENCE_AP_ID", curie=DDL.curie('REFERENCE_AP_ID'),
                      model_uri=DDL.REFERENCE_AP_ID, domain=None, range=Optional[int])

slots.IMG_TAXON_ID = Slot(uri=DDL.IMG_TAXON_ID, name="IMG_TAXON_ID", curie=DDL.curie('IMG_TAXON_ID'),
                      model_uri=DDL.IMG_TAXON_ID, domain=None, range=Optional[int])

slots.ANALYSIS_PROJECT_TYPE = Slot(uri=DDL.ANALYSIS_PROJECT_TYPE, name="ANALYSIS_PROJECT_TYPE", curie=DDL.curie('ANALYSIS_PROJECT_TYPE'),
                      model_uri=DDL.ANALYSIS_PROJECT_TYPE, domain=None, range=Optional[str])

slots.STATUS_ID = Slot(uri=DDL.STATUS_ID, name="STATUS_ID", curie=DDL.curie('STATUS_ID'),
                      model_uri=DDL.STATUS_ID, domain=None, range=Optional[int])

slots.COMMENTS = Slot(uri=DDL.COMMENTS, name="COMMENTS", curie=DDL.curie('COMMENTS'),
                      model_uri=DDL.COMMENTS, domain=None, range=Optional[str])

slots.NCBI_TAX_ID = Slot(uri=DDL.NCBI_TAX_ID, name="NCBI_TAX_ID", curie=DDL.curie('NCBI_TAX_ID'),
                      model_uri=DDL.NCBI_TAX_ID, domain=None, range=Optional[int])

slots.IS_PUBLIC = Slot(uri=DDL.IS_PUBLIC, name="IS_PUBLIC", curie=DDL.curie('IS_PUBLIC'),
                      model_uri=DDL.IS_PUBLIC, domain=None, range=Optional[str])

slots.ADDED_BY = Slot(uri=DDL.ADDED_BY, name="ADDED_BY", curie=DDL.curie('ADDED_BY'),
                      model_uri=DDL.ADDED_BY, domain=None, range=Optional[float])

slots.ADD_DATE = Slot(uri=DDL.ADD_DATE, name="ADD_DATE", curie=DDL.curie('ADD_DATE'),
                      model_uri=DDL.ADD_DATE, domain=None, range=Optional[Union[str, XSDTime]])

slots.PI_ID = Slot(uri=DDL.PI_ID, name="PI_ID", curie=DDL.curie('PI_ID'),
                      model_uri=DDL.PI_ID, domain=None, range=Optional[int])

slots.SUBMISSION_ID = Slot(uri=DDL.SUBMISSION_ID, name="SUBMISSION_ID", curie=DDL.curie('SUBMISSION_ID'),
                      model_uri=DDL.SUBMISSION_ID, domain=None, range=Optional[int])

slots.SCAFFOLD_COUNT = Slot(uri=DDL.SCAFFOLD_COUNT, name="SCAFFOLD_COUNT", curie=DDL.curie('SCAFFOLD_COUNT'),
                      model_uri=DDL.SCAFFOLD_COUNT, domain=None, range=Optional[float])

slots.CONTIG_COUNT = Slot(uri=DDL.CONTIG_COUNT, name="CONTIG_COUNT", curie=DDL.curie('CONTIG_COUNT'),
                      model_uri=DDL.CONTIG_COUNT, domain=None, range=Optional[float])

slots.GENE_COUNT = Slot(uri=DDL.GENE_COUNT, name="GENE_COUNT", curie=DDL.curie('GENE_COUNT'),
                      model_uri=DDL.GENE_COUNT, domain=None, range=Optional[float])

slots.BINNING_METHOD = Slot(uri=DDL.BINNING_METHOD, name="BINNING_METHOD", curie=DDL.curie('BINNING_METHOD'),
                      model_uri=DDL.BINNING_METHOD, domain=None, range=Optional[str])

slots.GENE_CALLING_METHOD = Slot(uri=DDL.GENE_CALLING_METHOD, name="GENE_CALLING_METHOD", curie=DDL.curie('GENE_CALLING_METHOD'),
                      model_uri=DDL.GENE_CALLING_METHOD, domain=None, range=Optional[str])

slots.ITS_ANALYSIS_PROJECT_NAME = Slot(uri=DDL.ITS_ANALYSIS_PROJECT_NAME, name="ITS_ANALYSIS_PROJECT_NAME", curie=DDL.curie('ITS_ANALYSIS_PROJECT_NAME'),
                      model_uri=DDL.ITS_ANALYSIS_PROJECT_NAME, domain=None, range=Optional[str])

slots.ITS_PRODUCT_NAME = Slot(uri=DDL.ITS_PRODUCT_NAME, name="ITS_PRODUCT_NAME", curie=DDL.curie('ITS_PRODUCT_NAME'),
                      model_uri=DDL.ITS_PRODUCT_NAME, domain=None, range=Optional[str])

slots.COMPLETION_DATE = Slot(uri=DDL.COMPLETION_DATE, name="COMPLETION_DATE", curie=DDL.curie('COMPLETION_DATE'),
                      model_uri=DDL.COMPLETION_DATE, domain=None, range=Optional[Union[str, XSDTime]])

slots.EST_SIZE = Slot(uri=DDL.EST_SIZE, name="EST_SIZE", curie=DDL.curie('EST_SIZE'),
                      model_uri=DDL.EST_SIZE, domain=None, range=Optional[float])

slots.GENBANK_LOW_QUALITY_ANNOTATION = Slot(uri=DDL.GENBANK_LOW_QUALITY_ANNOTATION, name="GENBANK_LOW_QUALITY_ANNOTATION", curie=DDL.curie('GENBANK_LOW_QUALITY_ANNOTATION'),
                      model_uri=DDL.GENBANK_LOW_QUALITY_ANNOTATION, domain=None, range=Optional[str])

slots.ECOSYSTEM = Slot(uri=DDL.ECOSYSTEM, name="ECOSYSTEM", curie=DDL.curie('ECOSYSTEM'),
                      model_uri=DDL.ECOSYSTEM, domain=None, range=Optional[str])

slots.ECOSYSTEM_CATEGORY = Slot(uri=DDL.ECOSYSTEM_CATEGORY, name="ECOSYSTEM_CATEGORY", curie=DDL.curie('ECOSYSTEM_CATEGORY'),
                      model_uri=DDL.ECOSYSTEM_CATEGORY, domain=None, range=Optional[str])

slots.ECOSYSTEM_TYPE = Slot(uri=DDL.ECOSYSTEM_TYPE, name="ECOSYSTEM_TYPE", curie=DDL.curie('ECOSYSTEM_TYPE'),
                      model_uri=DDL.ECOSYSTEM_TYPE, domain=None, range=Optional[str])

slots.ECOSYSTEM_SUBTYPE = Slot(uri=DDL.ECOSYSTEM_SUBTYPE, name="ECOSYSTEM_SUBTYPE", curie=DDL.curie('ECOSYSTEM_SUBTYPE'),
                      model_uri=DDL.ECOSYSTEM_SUBTYPE, domain=None, range=Optional[str])

slots.SPECIFIC_ECOSYSTEM = Slot(uri=DDL.SPECIFIC_ECOSYSTEM, name="SPECIFIC_ECOSYSTEM", curie=DDL.curie('SPECIFIC_ECOSYSTEM'),
                      model_uri=DDL.SPECIFIC_ECOSYSTEM, domain=None, range=Optional[str])

slots.IMG_ANALYSIS_COMPLETE = Slot(uri=DDL.IMG_ANALYSIS_COMPLETE, name="IMG_ANALYSIS_COMPLETE", curie=DDL.curie('IMG_ANALYSIS_COMPLETE'),
                      model_uri=DDL.IMG_ANALYSIS_COMPLETE, domain=None, range=Optional[str])

slots.IS_GENE_PRIMP = Slot(uri=DDL.IS_GENE_PRIMP, name="IS_GENE_PRIMP", curie=DDL.curie('IS_GENE_PRIMP'),
                      model_uri=DDL.IS_GENE_PRIMP, domain=None, range=Optional[str])

slots.IS_DECONTAMINATION = Slot(uri=DDL.IS_DECONTAMINATION, name="IS_DECONTAMINATION", curie=DDL.curie('IS_DECONTAMINATION'),
                      model_uri=DDL.IS_DECONTAMINATION, domain=None, range=Optional[str])

slots.IS_IMG_ANNOTATION = Slot(uri=DDL.IS_IMG_ANNOTATION, name="IS_IMG_ANNOTATION", curie=DDL.curie('IS_IMG_ANNOTATION'),
                      model_uri=DDL.IS_IMG_ANNOTATION, domain=None, range=Optional[str])

slots.ITS_ANNOTATION_AT_ID = Slot(uri=DDL.ITS_ANNOTATION_AT_ID, name="ITS_ANNOTATION_AT_ID", curie=DDL.curie('ITS_ANNOTATION_AT_ID'),
                      model_uri=DDL.ITS_ANNOTATION_AT_ID, domain=None, range=Optional[int])

slots.IS_ASSEMBLED_DELETED = Slot(uri=DDL.IS_ASSEMBLED_DELETED, name="IS_ASSEMBLED_DELETED", curie=DDL.curie('IS_ASSEMBLED_DELETED'),
                      model_uri=DDL.IS_ASSEMBLED_DELETED, domain=None, range=Optional[str])

slots.STUDY_ID = Slot(uri=DDL.STUDY_ID, name="STUDY_ID", curie=DDL.curie('STUDY_ID'),
                      model_uri=DDL.STUDY_ID, domain=None, range=Optional[int])

slots.SPECIMEN = Slot(uri=DDL.SPECIMEN, name="SPECIMEN", curie=DDL.curie('SPECIMEN'),
                      model_uri=DDL.SPECIMEN, domain=None, range=Optional[str])

slots.ITS_ASSEMBLY_AT_TYPE = Slot(uri=DDL.ITS_ASSEMBLY_AT_TYPE, name="ITS_ASSEMBLY_AT_TYPE", curie=DDL.curie('ITS_ASSEMBLY_AT_TYPE'),
                      model_uri=DDL.ITS_ASSEMBLY_AT_TYPE, domain=None, range=Optional[str])

slots.DOMAIN = Slot(uri=DDL.DOMAIN, name="DOMAIN", curie=DDL.curie('DOMAIN'),
                      model_uri=DDL.DOMAIN, domain=None, range=Optional[str])

slots.NCBI_PHYLUM = Slot(uri=DDL.NCBI_PHYLUM, name="NCBI_PHYLUM", curie=DDL.curie('NCBI_PHYLUM'),
                      model_uri=DDL.NCBI_PHYLUM, domain=None, range=Optional[str])

slots.NCBI_CLASS = Slot(uri=DDL.NCBI_CLASS, name="NCBI_CLASS", curie=DDL.curie('NCBI_CLASS'),
                      model_uri=DDL.NCBI_CLASS, domain=None, range=Optional[str])

slots.NCBI_ORDER = Slot(uri=DDL.NCBI_ORDER, name="NCBI_ORDER", curie=DDL.curie('NCBI_ORDER'),
                      model_uri=DDL.NCBI_ORDER, domain=None, range=Optional[str])

slots.NCBI_FAMILY = Slot(uri=DDL.NCBI_FAMILY, name="NCBI_FAMILY", curie=DDL.curie('NCBI_FAMILY'),
                      model_uri=DDL.NCBI_FAMILY, domain=None, range=Optional[str])

slots.NCBI_GENUS = Slot(uri=DDL.NCBI_GENUS, name="NCBI_GENUS", curie=DDL.curie('NCBI_GENUS'),
                      model_uri=DDL.NCBI_GENUS, domain=None, range=Optional[str])

slots.NCBI_SPECIES = Slot(uri=DDL.NCBI_SPECIES, name="NCBI_SPECIES", curie=DDL.curie('NCBI_SPECIES'),
                      model_uri=DDL.NCBI_SPECIES, domain=None, range=Optional[str])

slots.APPENDED_AP_NAME = Slot(uri=DDL.APPENDED_AP_NAME, name="APPENDED_AP_NAME", curie=DDL.curie('APPENDED_AP_NAME'),
                      model_uri=DDL.APPENDED_AP_NAME, domain=None, range=Optional[str])

slots.MOD_BY = Slot(uri=DDL.MOD_BY, name="MOD_BY", curie=DDL.curie('MOD_BY'),
                      model_uri=DDL.MOD_BY, domain=None, range=Optional[float])

slots.MOD_DATE = Slot(uri=DDL.MOD_DATE, name="MOD_DATE", curie=DDL.curie('MOD_DATE'),
                      model_uri=DDL.MOD_DATE, domain=None, range=Optional[Union[str, XSDTime]])

slots.PI_NAME = Slot(uri=DDL.PI_NAME, name="PI_NAME", curie=DDL.curie('PI_NAME'),
                      model_uri=DDL.PI_NAME, domain=None, range=Optional[str])

slots.ANALYSIS_PROJECT_NAME_FULL = Slot(uri=DDL.ANALYSIS_PROJECT_NAME_FULL, name="ANALYSIS_PROJECT_NAME_FULL", curie=DDL.curie('ANALYSIS_PROJECT_NAME_FULL'),
                      model_uri=DDL.ANALYSIS_PROJECT_NAME_FULL, domain=None, range=Optional[str])

slots.IS_PRIMARY = Slot(uri=DDL.IS_PRIMARY, name="IS_PRIMARY", curie=DDL.curie('IS_PRIMARY'),
                      model_uri=DDL.IS_PRIMARY, domain=None, range=Optional[str])

slots.GOLD_PHYLOGENY = Slot(uri=DDL.GOLD_PHYLOGENY, name="GOLD_PHYLOGENY", curie=DDL.curie('GOLD_PHYLOGENY'),
                      model_uri=DDL.GOLD_PHYLOGENY, domain=None, range=Optional[str])

slots.PHYLOGENY_SUGGESTION = Slot(uri=DDL.PHYLOGENY_SUGGESTION, name="PHYLOGENY_SUGGESTION", curie=DDL.curie('PHYLOGENY_SUGGESTION'),
                      model_uri=DDL.PHYLOGENY_SUGGESTION, domain=None, range=Optional[str])

slots.REPLACES_AP_ID = Slot(uri=DDL.REPLACES_AP_ID, name="REPLACES_AP_ID", curie=DDL.curie('REPLACES_AP_ID'),
                      model_uri=DDL.REPLACES_AP_ID, domain=None, range=Optional[int])

slots.NCBI_BIOPROJECT_ID = Slot(uri=DDL.NCBI_BIOPROJECT_ID, name="NCBI_BIOPROJECT_ID", curie=DDL.curie('NCBI_BIOPROJECT_ID'),
                      model_uri=DDL.NCBI_BIOPROJECT_ID, domain=None, range=Optional[int])

slots.SCREENING_METHOD = Slot(uri=DDL.SCREENING_METHOD, name="SCREENING_METHOD", curie=DDL.curie('SCREENING_METHOD'),
                      model_uri=DDL.SCREENING_METHOD, domain=None, range=Optional[str])

slots.DECONTAMINATION_METHOD = Slot(uri=DDL.DECONTAMINATION_METHOD, name="DECONTAMINATION_METHOD", curie=DDL.curie('DECONTAMINATION_METHOD'),
                      model_uri=DDL.DECONTAMINATION_METHOD, domain=None, range=Optional[str])

slots.NCBI_BIOSAMPLE_ACCESSION = Slot(uri=DDL.NCBI_BIOSAMPLE_ACCESSION, name="NCBI_BIOSAMPLE_ACCESSION", curie=DDL.curie('NCBI_BIOSAMPLE_ACCESSION'),
                      model_uri=DDL.NCBI_BIOSAMPLE_ACCESSION, domain=None, range=Optional[str])

slots.NCBI_BIOPROJECT_ACCESSION = Slot(uri=DDL.NCBI_BIOPROJECT_ACCESSION, name="NCBI_BIOPROJECT_ACCESSION", curie=DDL.curie('NCBI_BIOPROJECT_ACCESSION'),
                      model_uri=DDL.NCBI_BIOPROJECT_ACCESSION, domain=None, range=Optional[str])

slots.COMPLETION = Slot(uri=DDL.COMPLETION, name="COMPLETION", curie=DDL.curie('COMPLETION'),
                      model_uri=DDL.COMPLETION, domain=None, range=Optional[str])

slots.NCBI_KINGDOM = Slot(uri=DDL.NCBI_KINGDOM, name="NCBI_KINGDOM", curie=DDL.curie('NCBI_KINGDOM'),
                      model_uri=DDL.NCBI_KINGDOM, domain=None, range=Optional[str])

slots.REVIEW_STATUS = Slot(uri=DDL.REVIEW_STATUS, name="REVIEW_STATUS", curie=DDL.curie('REVIEW_STATUS'),
                      model_uri=DDL.REVIEW_STATUS, domain=None, range=Optional[str])

slots.REJECTION_REASONS = Slot(uri=DDL.REJECTION_REASONS, name="REJECTION_REASONS", curie=DDL.curie('REJECTION_REASONS'),
                      model_uri=DDL.REJECTION_REASONS, domain=None, range=Optional[str])

slots.ORGANISM_ID = Slot(uri=DDL.ORGANISM_ID, name="ORGANISM_ID", curie=DDL.curie('ORGANISM_ID'),
                      model_uri=DDL.ORGANISM_ID, domain=None, range=Optional[int])

slots.PIPELINE_ANNOTATION_METHOD = Slot(uri=DDL.PIPELINE_ANNOTATION_METHOD, name="PIPELINE_ANNOTATION_METHOD", curie=DDL.curie('PIPELINE_ANNOTATION_METHOD'),
                      model_uri=DDL.PIPELINE_ANNOTATION_METHOD, domain=None, range=Optional[str])

slots.GENUS = Slot(uri=DDL.GENUS, name="GENUS", curie=DDL.curie('GENUS'),
                      model_uri=DDL.GENUS, domain=None, range=Optional[str])

slots.SPECIES = Slot(uri=DDL.SPECIES, name="SPECIES", curie=DDL.curie('SPECIES'),
                      model_uri=DDL.SPECIES, domain=None, range=Optional[str])

slots.SUBSPECIES = Slot(uri=DDL.SUBSPECIES, name="SUBSPECIES", curie=DDL.curie('SUBSPECIES'),
                      model_uri=DDL.SUBSPECIES, domain=None, range=Optional[str])

slots.CULTURE_COLLECTION = Slot(uri=DDL.CULTURE_COLLECTION, name="CULTURE_COLLECTION", curie=DDL.curie('CULTURE_COLLECTION'),
                      model_uri=DDL.CULTURE_COLLECTION, domain=None, range=Optional[str])

slots.SEROVAR = Slot(uri=DDL.SEROVAR, name="SEROVAR", curie=DDL.curie('SEROVAR'),
                      model_uri=DDL.SEROVAR, domain=None, range=Optional[str])

slots.STRAIN = Slot(uri=DDL.STRAIN, name="STRAIN", curie=DDL.curie('STRAIN'),
                      model_uri=DDL.STRAIN, domain=None, range=Optional[str])

slots.ECOSYSTEM_PATH_ID = Slot(uri=DDL.ECOSYSTEM_PATH_ID, name="ECOSYSTEM_PATH_ID", curie=DDL.curie('ECOSYSTEM_PATH_ID'),
                      model_uri=DDL.ECOSYSTEM_PATH_ID, domain=None, range=Optional[int])

slots.SEQUENCING_DEPTH = Slot(uri=DDL.SEQUENCING_DEPTH, name="SEQUENCING_DEPTH", curie=DDL.curie('SEQUENCING_DEPTH'),
                      model_uri=DDL.SEQUENCING_DEPTH, domain=None, range=Optional[str])

slots.IMG_USE = Slot(uri=DDL.IMG_USE, name="IMG_USE", curie=DDL.curie('IMG_USE'),
                      model_uri=DDL.IMG_USE, domain=None, range=Optional[str])

slots.ANNOTATOR_COMMENTS = Slot(uri=DDL.ANNOTATOR_COMMENTS, name="ANNOTATOR_COMMENTS", curie=DDL.curie('ANNOTATOR_COMMENTS'),
                      model_uri=DDL.ANNOTATOR_COMMENTS, domain=None, range=Optional[str])

slots.AP_FOR_NONOWNER = Slot(uri=DDL.AP_FOR_NONOWNER, name="AP_FOR_NONOWNER", curie=DDL.curie('AP_FOR_NONOWNER'),
                      model_uri=DDL.AP_FOR_NONOWNER, domain=None, range=Optional[str])

slots.NCBI_SUPERKINGDOM = Slot(uri=DDL.NCBI_SUPERKINGDOM, name="NCBI_SUPERKINGDOM", curie=DDL.curie('NCBI_SUPERKINGDOM'),
                      model_uri=DDL.NCBI_SUPERKINGDOM, domain=None, range=Optional[str])

slots.IS_TEST = Slot(uri=DDL.IS_TEST, name="IS_TEST", curie=DDL.curie('IS_TEST'),
                      model_uri=DDL.IS_TEST, domain=None, range=Optional[str])

slots.ITS_NCBI_TAX_ID = Slot(uri=DDL.ITS_NCBI_TAX_ID, name="ITS_NCBI_TAX_ID", curie=DDL.curie('ITS_NCBI_TAX_ID'),
                      model_uri=DDL.ITS_NCBI_TAX_ID, domain=None, range=Optional[int])

slots.ITS_VERSION_NUMBER = Slot(uri=DDL.ITS_VERSION_NUMBER, name="ITS_VERSION_NUMBER", curie=DDL.curie('ITS_VERSION_NUMBER'),
                      model_uri=DDL.ITS_VERSION_NUMBER, domain=None, range=Optional[float])

slots.IMG_RNASEQ_ID = Slot(uri=DDL.IMG_RNASEQ_ID, name="IMG_RNASEQ_ID", curie=DDL.curie('IMG_RNASEQ_ID'),
                      model_uri=DDL.IMG_RNASEQ_ID, domain=None, range=Optional[int])

slots.SUBMISSION_STATUS_ID = Slot(uri=DDL.SUBMISSION_STATUS_ID, name="SUBMISSION_STATUS_ID", curie=DDL.curie('SUBMISSION_STATUS_ID'),
                      model_uri=DDL.SUBMISSION_STATUS_ID, domain=None, range=Optional[int])

slots.SUBMISSION_STATUS_NAME = Slot(uri=DDL.SUBMISSION_STATUS_NAME, name="SUBMISSION_STATUS_NAME", curie=DDL.curie('SUBMISSION_STATUS_NAME'),
                      model_uri=DDL.SUBMISSION_STATUS_NAME, domain=None, range=Optional[str])

slots.SUBMISSION_COMMENTS = Slot(uri=DDL.SUBMISSION_COMMENTS, name="SUBMISSION_COMMENTS", curie=DDL.curie('SUBMISSION_COMMENTS'),
                      model_uri=DDL.SUBMISSION_COMMENTS, domain=None, range=Optional[str])

slots.IMG_SUBMISSION_PRORITY = Slot(uri=DDL.IMG_SUBMISSION_PRORITY, name="IMG_SUBMISSION_PRORITY", curie=DDL.curie('IMG_SUBMISSION_PRORITY'),
                      model_uri=DDL.IMG_SUBMISSION_PRORITY, domain=None, range=Optional[str])

slots.CONTAMINATION_PERCENTAGE = Slot(uri=DDL.CONTAMINATION_PERCENTAGE, name="CONTAMINATION_PERCENTAGE", curie=DDL.curie('CONTAMINATION_PERCENTAGE'),
                      model_uri=DDL.CONTAMINATION_PERCENTAGE, domain=None, range=Optional[float])

slots.COMPLETENESS_PERCENTAGE = Slot(uri=DDL.COMPLETENESS_PERCENTAGE, name="COMPLETENESS_PERCENTAGE", curie=DDL.curie('COMPLETENESS_PERCENTAGE'),
                      model_uri=DDL.COMPLETENESS_PERCENTAGE, domain=None, range=Optional[float])

slots.SRA_RUN_ID = Slot(uri=DDL.SRA_RUN_ID, name="SRA_RUN_ID", curie=DDL.curie('SRA_RUN_ID'),
                      model_uri=DDL.SRA_RUN_ID, domain=None, range=Optional[str])

slots.BIOSAMPLE_NAME = Slot(uri=DDL.BIOSAMPLE_NAME, name="BIOSAMPLE_NAME", curie=DDL.curie('BIOSAMPLE_NAME'),
                      model_uri=DDL.BIOSAMPLE_NAME, domain=None, range=Optional[str])

slots.DESCRIPTION = Slot(uri=DDL.DESCRIPTION, name="DESCRIPTION", curie=DDL.curie('DESCRIPTION'),
                      model_uri=DDL.DESCRIPTION, domain=None, range=Optional[str])

slots.SAMPLE_COLLECTION_SITE = Slot(uri=DDL.SAMPLE_COLLECTION_SITE, name="SAMPLE_COLLECTION_SITE", curie=DDL.curie('SAMPLE_COLLECTION_SITE'),
                      model_uri=DDL.SAMPLE_COLLECTION_SITE, domain=None, range=Optional[str])

slots.ISOLATION_PUBLICATION_ID = Slot(uri=DDL.ISOLATION_PUBLICATION_ID, name="ISOLATION_PUBLICATION_ID", curie=DDL.curie('ISOLATION_PUBLICATION_ID'),
                      model_uri=DDL.ISOLATION_PUBLICATION_ID, domain=None, range=Optional[int])

slots.SAMPLE_ISOLATION_COMMENTS = Slot(uri=DDL.SAMPLE_ISOLATION_COMMENTS, name="SAMPLE_ISOLATION_COMMENTS", curie=DDL.curie('SAMPLE_ISOLATION_COMMENTS'),
                      model_uri=DDL.SAMPLE_ISOLATION_COMMENTS, domain=None, range=Optional[str])

slots.SAMPLING_STRATEGY = Slot(uri=DDL.SAMPLING_STRATEGY, name="SAMPLING_STRATEGY", curie=DDL.curie('SAMPLING_STRATEGY'),
                      model_uri=DDL.SAMPLING_STRATEGY, domain=None, range=Optional[str])

slots.REPLICATE_NUMBER = Slot(uri=DDL.REPLICATE_NUMBER, name="REPLICATE_NUMBER", curie=DDL.curie('REPLICATE_NUMBER'),
                      model_uri=DDL.REPLICATE_NUMBER, domain=None, range=Optional[float])

slots.SAMPLE_VOLUME = Slot(uri=DDL.SAMPLE_VOLUME, name="SAMPLE_VOLUME", curie=DDL.curie('SAMPLE_VOLUME'),
                      model_uri=DDL.SAMPLE_VOLUME, domain=None, range=Optional[str])

slots.SAMPLE_BIOMASS = Slot(uri=DDL.SAMPLE_BIOMASS, name="SAMPLE_BIOMASS", curie=DDL.curie('SAMPLE_BIOMASS'),
                      model_uri=DDL.SAMPLE_BIOMASS, domain=None, range=Optional[str])

slots.SAMPLE_CONTACT_NAME = Slot(uri=DDL.SAMPLE_CONTACT_NAME, name="SAMPLE_CONTACT_NAME", curie=DDL.curie('SAMPLE_CONTACT_NAME'),
                      model_uri=DDL.SAMPLE_CONTACT_NAME, domain=None, range=Optional[str])

slots.SAMPLE_CONTACT_EMAIL = Slot(uri=DDL.SAMPLE_CONTACT_EMAIL, name="SAMPLE_CONTACT_EMAIL", curie=DDL.curie('SAMPLE_CONTACT_EMAIL'),
                      model_uri=DDL.SAMPLE_CONTACT_EMAIL, domain=None, range=Optional[str])

slots.GEOGRAPHIC_LOCATION = Slot(uri=DDL.GEOGRAPHIC_LOCATION, name="GEOGRAPHIC_LOCATION", curie=DDL.curie('GEOGRAPHIC_LOCATION'),
                      model_uri=DDL.GEOGRAPHIC_LOCATION, domain=None, range=Optional[str])

slots.LAT_LONG_INFERRED = Slot(uri=DDL.LAT_LONG_INFERRED, name="LAT_LONG_INFERRED", curie=DDL.curie('LAT_LONG_INFERRED'),
                      model_uri=DDL.LAT_LONG_INFERRED, domain=None, range=Optional[str])

slots.SALINITY = Slot(uri=DDL.SALINITY, name="SALINITY", curie=DDL.curie('SALINITY'),
                      model_uri=DDL.SALINITY, domain=None, range=Optional[str])

slots.PRESSURE = Slot(uri=DDL.PRESSURE, name="PRESSURE", curie=DDL.curie('PRESSURE'),
                      model_uri=DDL.PRESSURE, domain=None, range=Optional[str])

slots.PH = Slot(uri=DDL.PH, name="PH", curie=DDL.curie('PH'),
                      model_uri=DDL.PH, domain=None, range=Optional[str])

slots.HABITAT = Slot(uri=DDL.HABITAT, name="HABITAT", curie=DDL.curie('HABITAT'),
                      model_uri=DDL.HABITAT, domain=None, range=Optional[str])

slots.HOST_NAME = Slot(uri=DDL.HOST_NAME, name="HOST_NAME", curie=DDL.curie('HOST_NAME'),
                      model_uri=DDL.HOST_NAME, domain=None, range=Optional[str])

slots.HOST_TAXONOMY_ID = Slot(uri=DDL.HOST_TAXONOMY_ID, name="HOST_TAXONOMY_ID", curie=DDL.curie('HOST_TAXONOMY_ID'),
                      model_uri=DDL.HOST_TAXONOMY_ID, domain=None, range=Optional[int])

slots.HOST_GENDER = Slot(uri=DDL.HOST_GENDER, name="HOST_GENDER", curie=DDL.curie('HOST_GENDER'),
                      model_uri=DDL.HOST_GENDER, domain=None, range=Optional[str])

slots.HOST_RACE = Slot(uri=DDL.HOST_RACE, name="HOST_RACE", curie=DDL.curie('HOST_RACE'),
                      model_uri=DDL.HOST_RACE, domain=None, range=Optional[str])

slots.HOST_AGE = Slot(uri=DDL.HOST_AGE, name="HOST_AGE", curie=DDL.curie('HOST_AGE'),
                      model_uri=DDL.HOST_AGE, domain=None, range=Optional[str])

slots.HOST_HEALTH_CONDITION = Slot(uri=DDL.HOST_HEALTH_CONDITION, name="HOST_HEALTH_CONDITION", curie=DDL.curie('HOST_HEALTH_CONDITION'),
                      model_uri=DDL.HOST_HEALTH_CONDITION, domain=None, range=Optional[str])

slots.PATIENT_VISIT_NUMBER = Slot(uri=DDL.PATIENT_VISIT_NUMBER, name="PATIENT_VISIT_NUMBER", curie=DDL.curie('PATIENT_VISIT_NUMBER'),
                      model_uri=DDL.PATIENT_VISIT_NUMBER, domain=None, range=Optional[float])

slots.HOST_MEDICATION = Slot(uri=DDL.HOST_MEDICATION, name="HOST_MEDICATION", curie=DDL.curie('HOST_MEDICATION'),
                      model_uri=DDL.HOST_MEDICATION, domain=None, range=Optional[str])

slots.MRN = Slot(uri=DDL.MRN, name="MRN", curie=DDL.curie('MRN'),
                      model_uri=DDL.MRN, domain=None, range=Optional[str])

slots.HOST_BODY_SITE = Slot(uri=DDL.HOST_BODY_SITE, name="HOST_BODY_SITE", curie=DDL.curie('HOST_BODY_SITE'),
                      model_uri=DDL.HOST_BODY_SITE, domain=None, range=Optional[str])

slots.HOST_BODY_SUBSITE = Slot(uri=DDL.HOST_BODY_SUBSITE, name="HOST_BODY_SUBSITE", curie=DDL.curie('HOST_BODY_SUBSITE'),
                      model_uri=DDL.HOST_BODY_SUBSITE, domain=None, range=Optional[str])

slots.HOST_BODY_PRODUCT = Slot(uri=DDL.HOST_BODY_PRODUCT, name="HOST_BODY_PRODUCT", curie=DDL.curie('HOST_BODY_PRODUCT'),
                      model_uri=DDL.HOST_BODY_PRODUCT, domain=None, range=Optional[str])

slots.HOST_SPECIFICITY = Slot(uri=DDL.HOST_SPECIFICITY, name="HOST_SPECIFICITY", curie=DDL.curie('HOST_SPECIFICITY'),
                      model_uri=DDL.HOST_SPECIFICITY, domain=None, range=Optional[str])

slots.HOST_COMMENTS = Slot(uri=DDL.HOST_COMMENTS, name="HOST_COMMENTS", curie=DDL.curie('HOST_COMMENTS'),
                      model_uri=DDL.HOST_COMMENTS, domain=None, range=Optional[str])

slots.ACTIVE = Slot(uri=DDL.ACTIVE, name="ACTIVE", curie=DDL.curie('ACTIVE'),
                      model_uri=DDL.ACTIVE, domain=None, range=Optional[str])

slots.PROJECT_OID = Slot(uri=DDL.PROJECT_OID, name="PROJECT_OID", curie=DDL.curie('PROJECT_OID'),
                      model_uri=DDL.PROJECT_OID, domain=None, range=Optional[float])

slots.SAMPLE_OID = Slot(uri=DDL.SAMPLE_OID, name="SAMPLE_OID", curie=DDL.curie('SAMPLE_OID'),
                      model_uri=DDL.SAMPLE_OID, domain=None, range=Optional[float])

slots.SUBMIT_BIOSAMPLE_NAME = Slot(uri=DDL.SUBMIT_BIOSAMPLE_NAME, name="SUBMIT_BIOSAMPLE_NAME", curie=DDL.curie('SUBMIT_BIOSAMPLE_NAME'),
                      model_uri=DDL.SUBMIT_BIOSAMPLE_NAME, domain=None, range=Optional[str])

slots.NCBI_TAXONOMY_ID = Slot(uri=DDL.NCBI_TAXONOMY_ID, name="NCBI_TAXONOMY_ID", curie=DDL.curie('NCBI_TAXONOMY_ID'),
                      model_uri=DDL.NCBI_TAXONOMY_ID, domain=None, range=Optional[int])

slots.COMMUNITY = Slot(uri=DDL.COMMUNITY, name="COMMUNITY", curie=DDL.curie('COMMUNITY'),
                      model_uri=DDL.COMMUNITY, domain=None, range=Optional[str])

slots.LOCATION = Slot(uri=DDL.LOCATION, name="LOCATION", curie=DDL.curie('LOCATION'),
                      model_uri=DDL.LOCATION, domain=None, range=Optional[str])

slots.IDENTIFIER = Slot(uri=DDL.IDENTIFIER, name="IDENTIFIER", curie=DDL.curie('IDENTIFIER'),
                      model_uri=DDL.IDENTIFIER, domain=None, range=Optional[str])

slots.ENV_PACKAGE = Slot(uri=DDL.ENV_PACKAGE, name="ENV_PACKAGE", curie=DDL.curie('ENV_PACKAGE'),
                      model_uri=DDL.ENV_PACKAGE, domain=None, range=Optional[str])

slots.SAMPLE_COLLECTION_DAY = Slot(uri=DDL.SAMPLE_COLLECTION_DAY, name="SAMPLE_COLLECTION_DAY", curie=DDL.curie('SAMPLE_COLLECTION_DAY'),
                      model_uri=DDL.SAMPLE_COLLECTION_DAY, domain=None, range=Optional[float])

slots.SAMPLE_COLLECTION_MONTH = Slot(uri=DDL.SAMPLE_COLLECTION_MONTH, name="SAMPLE_COLLECTION_MONTH", curie=DDL.curie('SAMPLE_COLLECTION_MONTH'),
                      model_uri=DDL.SAMPLE_COLLECTION_MONTH, domain=None, range=Optional[float])

slots.SAMPLE_COLLECTION_YEAR = Slot(uri=DDL.SAMPLE_COLLECTION_YEAR, name="SAMPLE_COLLECTION_YEAR", curie=DDL.curie('SAMPLE_COLLECTION_YEAR'),
                      model_uri=DDL.SAMPLE_COLLECTION_YEAR, domain=None, range=Optional[float])

slots.SUBMITTER_ID = Slot(uri=DDL.SUBMITTER_ID, name="SUBMITTER_ID", curie=DDL.curie('SUBMITTER_ID'),
                      model_uri=DDL.SUBMITTER_ID, domain=None, range=Optional[int])

slots.GROWTH_CONDITIONS = Slot(uri=DDL.GROWTH_CONDITIONS, name="GROWTH_CONDITIONS", curie=DDL.curie('GROWTH_CONDITIONS'),
                      model_uri=DDL.GROWTH_CONDITIONS, domain=None, range=Optional[str])

slots.JPA_ENTITY = Slot(uri=DDL.JPA_ENTITY, name="JPA_ENTITY", curie=DDL.curie('JPA_ENTITY'),
                      model_uri=DDL.JPA_ENTITY, domain=None, range=Optional[str])

slots.OTHER_HOSTS = Slot(uri=DDL.OTHER_HOSTS, name="OTHER_HOSTS", curie=DDL.curie('OTHER_HOSTS'),
                      model_uri=DDL.OTHER_HOSTS, domain=None, range=Optional[str])

slots.KNOWN_NON_HOSTS = Slot(uri=DDL.KNOWN_NON_HOSTS, name="KNOWN_NON_HOSTS", curie=DDL.curie('KNOWN_NON_HOSTS'),
                      model_uri=DDL.KNOWN_NON_HOSTS, domain=None, range=Optional[str])

slots.ISOLATION_PUBMED_ID = Slot(uri=DDL.ISOLATION_PUBMED_ID, name="ISOLATION_PUBMED_ID", curie=DDL.curie('ISOLATION_PUBMED_ID'),
                      model_uri=DDL.ISOLATION_PUBMED_ID, domain=None, range=Optional[int])

slots.HOST_BODY_SITE_ID = Slot(uri=DDL.HOST_BODY_SITE_ID, name="HOST_BODY_SITE_ID", curie=DDL.curie('HOST_BODY_SITE_ID'),
                      model_uri=DDL.HOST_BODY_SITE_ID, domain=None, range=Optional[int])

slots.HOST_BODY_SUBSITE_ID = Slot(uri=DDL.HOST_BODY_SUBSITE_ID, name="HOST_BODY_SUBSITE_ID", curie=DDL.curie('HOST_BODY_SUBSITE_ID'),
                      model_uri=DDL.HOST_BODY_SUBSITE_ID, domain=None, range=Optional[int])

slots.HOST_BODY_PRODUCT_ID = Slot(uri=DDL.HOST_BODY_PRODUCT_ID, name="HOST_BODY_PRODUCT_ID", curie=DDL.curie('HOST_BODY_PRODUCT_ID'),
                      model_uri=DDL.HOST_BODY_PRODUCT_ID, domain=None, range=Optional[int])

slots.IS_DRAFT = Slot(uri=DDL.IS_DRAFT, name="IS_DRAFT", curie=DDL.curie('IS_DRAFT'),
                      model_uri=DDL.IS_DRAFT, domain=None, range=Optional[str])

slots.SAMPLE_ISOLATION_COUNTRY_ID = Slot(uri=DDL.SAMPLE_ISOLATION_COUNTRY_ID, name="SAMPLE_ISOLATION_COUNTRY_ID", curie=DDL.curie('SAMPLE_ISOLATION_COUNTRY_ID'),
                      model_uri=DDL.SAMPLE_ISOLATION_COUNTRY_ID, domain=None, range=Optional[int])

slots.OTHER_ECOSYSTEM = Slot(uri=DDL.OTHER_ECOSYSTEM, name="OTHER_ECOSYSTEM", curie=DDL.curie('OTHER_ECOSYSTEM'),
                      model_uri=DDL.OTHER_ECOSYSTEM, domain=None, range=Optional[str])

slots.LONGHURST_CODE = Slot(uri=DDL.LONGHURST_CODE, name="LONGHURST_CODE", curie=DDL.curie('LONGHURST_CODE'),
                      model_uri=DDL.LONGHURST_CODE, domain=None, range=Optional[str])

slots.SAMPLE_COLLECTION_HOUR = Slot(uri=DDL.SAMPLE_COLLECTION_HOUR, name="SAMPLE_COLLECTION_HOUR", curie=DDL.curie('SAMPLE_COLLECTION_HOUR'),
                      model_uri=DDL.SAMPLE_COLLECTION_HOUR, domain=None, range=Optional[float])

slots.SAMPLE_COLLECTION_MINUTE = Slot(uri=DDL.SAMPLE_COLLECTION_MINUTE, name="SAMPLE_COLLECTION_MINUTE", curie=DDL.curie('SAMPLE_COLLECTION_MINUTE'),
                      model_uri=DDL.SAMPLE_COLLECTION_MINUTE, domain=None, range=Optional[float])

slots.CHLOROPHYLL_CONCENTRATION = Slot(uri=DDL.CHLOROPHYLL_CONCENTRATION, name="CHLOROPHYLL_CONCENTRATION", curie=DDL.curie('CHLOROPHYLL_CONCENTRATION'),
                      model_uri=DDL.CHLOROPHYLL_CONCENTRATION, domain=None, range=Optional[str])

slots.NITRATE_CONCENTRATION = Slot(uri=DDL.NITRATE_CONCENTRATION, name="NITRATE_CONCENTRATION", curie=DDL.curie('NITRATE_CONCENTRATION'),
                      model_uri=DDL.NITRATE_CONCENTRATION, domain=None, range=Optional[str])

slots.OXYGEN_CONCENTRATION = Slot(uri=DDL.OXYGEN_CONCENTRATION, name="OXYGEN_CONCENTRATION", curie=DDL.curie('OXYGEN_CONCENTRATION'),
                      model_uri=DDL.OXYGEN_CONCENTRATION, domain=None, range=Optional[str])

slots.SALINITY_CONCENTRATION = Slot(uri=DDL.SALINITY_CONCENTRATION, name="SALINITY_CONCENTRATION", curie=DDL.curie('SALINITY_CONCENTRATION'),
                      model_uri=DDL.SALINITY_CONCENTRATION, domain=None, range=Optional[str])

slots.PUBLIC_SP_COUNT = Slot(uri=DDL.PUBLIC_SP_COUNT, name="PUBLIC_SP_COUNT", curie=DDL.curie('PUBLIC_SP_COUNT'),
                      model_uri=DDL.PUBLIC_SP_COUNT, domain=None, range=Optional[float])

slots.ADMIN_SP_COUNT = Slot(uri=DDL.ADMIN_SP_COUNT, name="ADMIN_SP_COUNT", curie=DDL.curie('ADMIN_SP_COUNT'),
                      model_uri=DDL.ADMIN_SP_COUNT, domain=None, range=Optional[float])

slots.PUBLIC_AP_COUNT = Slot(uri=DDL.PUBLIC_AP_COUNT, name="PUBLIC_AP_COUNT", curie=DDL.curie('PUBLIC_AP_COUNT'),
                      model_uri=DDL.PUBLIC_AP_COUNT, domain=None, range=Optional[float])

slots.ADMIN_AP_COUNT = Slot(uri=DDL.ADMIN_AP_COUNT, name="ADMIN_AP_COUNT", curie=DDL.curie('ADMIN_AP_COUNT'),
                      model_uri=DDL.ADMIN_AP_COUNT, domain=None, range=Optional[float])

slots.PUBLIC_DAP_COUNT = Slot(uri=DDL.PUBLIC_DAP_COUNT, name="PUBLIC_DAP_COUNT", curie=DDL.curie('PUBLIC_DAP_COUNT'),
                      model_uri=DDL.PUBLIC_DAP_COUNT, domain=None, range=Optional[float])

slots.ADMIN_DAP_COUNT = Slot(uri=DDL.ADMIN_DAP_COUNT, name="ADMIN_DAP_COUNT", curie=DDL.curie('ADMIN_DAP_COUNT'),
                      model_uri=DDL.ADMIN_DAP_COUNT, domain=None, range=Optional[float])

slots.CRUISE_LINE_NAME = Slot(uri=DDL.CRUISE_LINE_NAME, name="CRUISE_LINE_NAME", curie=DDL.curie('CRUISE_LINE_NAME'),
                      model_uri=DDL.CRUISE_LINE_NAME, domain=None, range=Optional[str])

slots.PROPORT_OCEAN = Slot(uri=DDL.PROPORT_OCEAN, name="PROPORT_OCEAN", curie=DDL.curie('PROPORT_OCEAN'),
                      model_uri=DDL.PROPORT_OCEAN, domain=None, range=Optional[str])

slots.PROPORT_ISOLATION = Slot(uri=DDL.PROPORT_ISOLATION, name="PROPORT_ISOLATION", curie=DDL.curie('PROPORT_ISOLATION'),
                      model_uri=DDL.PROPORT_ISOLATION, domain=None, range=Optional[str])

slots.PROPORT_STATION = Slot(uri=DDL.PROPORT_STATION, name="PROPORT_STATION", curie=DDL.curie('PROPORT_STATION'),
                      model_uri=DDL.PROPORT_STATION, domain=None, range=Optional[str])

slots.PROPORT_WOA_TEMPERATURE = Slot(uri=DDL.PROPORT_WOA_TEMPERATURE, name="PROPORT_WOA_TEMPERATURE", curie=DDL.curie('PROPORT_WOA_TEMPERATURE'),
                      model_uri=DDL.PROPORT_WOA_TEMPERATURE, domain=None, range=Optional[float])

slots.PROPORT_WOA_SALINITY = Slot(uri=DDL.PROPORT_WOA_SALINITY, name="PROPORT_WOA_SALINITY", curie=DDL.curie('PROPORT_WOA_SALINITY'),
                      model_uri=DDL.PROPORT_WOA_SALINITY, domain=None, range=Optional[float])

slots.PROPORT_WOA_DISSOLVED_OXYGEN = Slot(uri=DDL.PROPORT_WOA_DISSOLVED_OXYGEN, name="PROPORT_WOA_DISSOLVED_OXYGEN", curie=DDL.curie('PROPORT_WOA_DISSOLVED_OXYGEN'),
                      model_uri=DDL.PROPORT_WOA_DISSOLVED_OXYGEN, domain=None, range=Optional[float])

slots.PROPORT_WOA_SILICATE = Slot(uri=DDL.PROPORT_WOA_SILICATE, name="PROPORT_WOA_SILICATE", curie=DDL.curie('PROPORT_WOA_SILICATE'),
                      model_uri=DDL.PROPORT_WOA_SILICATE, domain=None, range=Optional[float])

slots.PROPORT_WOA_PHOSPHATE = Slot(uri=DDL.PROPORT_WOA_PHOSPHATE, name="PROPORT_WOA_PHOSPHATE", curie=DDL.curie('PROPORT_WOA_PHOSPHATE'),
                      model_uri=DDL.PROPORT_WOA_PHOSPHATE, domain=None, range=Optional[float])

slots.PROPORT_WOA_NITRATE = Slot(uri=DDL.PROPORT_WOA_NITRATE, name="PROPORT_WOA_NITRATE", curie=DDL.curie('PROPORT_WOA_NITRATE'),
                      model_uri=DDL.PROPORT_WOA_NITRATE, domain=None, range=Optional[float])

slots.NCBI_TAXONOMY_NAME = Slot(uri=DDL.NCBI_TAXONOMY_NAME, name="NCBI_TAXONOMY_NAME", curie=DDL.curie('NCBI_TAXONOMY_NAME'),
                      model_uri=DDL.NCBI_TAXONOMY_NAME, domain=None, range=Optional[str])

slots.ITS_GROWTH_CONDITIONS = Slot(uri=DDL.ITS_GROWTH_CONDITIONS, name="ITS_GROWTH_CONDITIONS", curie=DDL.curie('ITS_GROWTH_CONDITIONS'),
                      model_uri=DDL.ITS_GROWTH_CONDITIONS, domain=None, range=Optional[str])

slots.BIOGAS_FED_SUBSTRATES = Slot(uri=DDL.BIOGAS_FED_SUBSTRATES, name="BIOGAS_FED_SUBSTRATES", curie=DDL.curie('BIOGAS_FED_SUBSTRATES'),
                      model_uri=DDL.BIOGAS_FED_SUBSTRATES, domain=None, range=Optional[str])

slots.BIOGAS_RETENTION_TIME = Slot(uri=DDL.BIOGAS_RETENTION_TIME, name="BIOGAS_RETENTION_TIME", curie=DDL.curie('BIOGAS_RETENTION_TIME'),
                      model_uri=DDL.BIOGAS_RETENTION_TIME, domain=None, range=Optional[str])

slots.BIOGAS_TEMPERATURE = Slot(uri=DDL.BIOGAS_TEMPERATURE, name="BIOGAS_TEMPERATURE", curie=DDL.curie('BIOGAS_TEMPERATURE'),
                      model_uri=DDL.BIOGAS_TEMPERATURE, domain=None, range=Optional[str])

slots.BIOGAS_YIELD = Slot(uri=DDL.BIOGAS_YIELD, name="BIOGAS_YIELD", curie=DDL.curie('BIOGAS_YIELD'),
                      model_uri=DDL.BIOGAS_YIELD, domain=None, range=Optional[str])

slots.BIOGAS_VOLATILE_ORGANIC_ACIDS = Slot(uri=DDL.BIOGAS_VOLATILE_ORGANIC_ACIDS, name="BIOGAS_VOLATILE_ORGANIC_ACIDS", curie=DDL.curie('BIOGAS_VOLATILE_ORGANIC_ACIDS'),
                      model_uri=DDL.BIOGAS_VOLATILE_ORGANIC_ACIDS, domain=None, range=Optional[str])

slots.BIOGAS_TOTAL_INORGANIC_CARBON = Slot(uri=DDL.BIOGAS_TOTAL_INORGANIC_CARBON, name="BIOGAS_TOTAL_INORGANIC_CARBON", curie=DDL.curie('BIOGAS_TOTAL_INORGANIC_CARBON'),
                      model_uri=DDL.BIOGAS_TOTAL_INORGANIC_CARBON, domain=None, range=Optional[str])

slots.BIOGAS_VOA_TIC = Slot(uri=DDL.BIOGAS_VOA_TIC, name="BIOGAS_VOA_TIC", curie=DDL.curie('BIOGAS_VOA_TIC'),
                      model_uri=DDL.BIOGAS_VOA_TIC, domain=None, range=Optional[str])

slots.BIOGAS_AMMONIUM_NH4 = Slot(uri=DDL.BIOGAS_AMMONIUM_NH4, name="BIOGAS_AMMONIUM_NH4", curie=DDL.curie('BIOGAS_AMMONIUM_NH4'),
                      model_uri=DDL.BIOGAS_AMMONIUM_NH4, domain=None, range=Optional[str])

slots.BIOGAS_BUTANOL = Slot(uri=DDL.BIOGAS_BUTANOL, name="BIOGAS_BUTANOL", curie=DDL.curie('BIOGAS_BUTANOL'),
                      model_uri=DDL.BIOGAS_BUTANOL, domain=None, range=Optional[str])

slots.BIOGAS_ETHANOL = Slot(uri=DDL.BIOGAS_ETHANOL, name="BIOGAS_ETHANOL", curie=DDL.curie('BIOGAS_ETHANOL'),
                      model_uri=DDL.BIOGAS_ETHANOL, domain=None, range=Optional[str])

slots.BIOGAS_PROPANOL = Slot(uri=DDL.BIOGAS_PROPANOL, name="BIOGAS_PROPANOL", curie=DDL.curie('BIOGAS_PROPANOL'),
                      model_uri=DDL.BIOGAS_PROPANOL, domain=None, range=Optional[str])

slots.BIOGAS_METHANOL = Slot(uri=DDL.BIOGAS_METHANOL, name="BIOGAS_METHANOL", curie=DDL.curie('BIOGAS_METHANOL'),
                      model_uri=DDL.BIOGAS_METHANOL, domain=None, range=Optional[str])

slots.BIOGAS_ACETIC_ACID = Slot(uri=DDL.BIOGAS_ACETIC_ACID, name="BIOGAS_ACETIC_ACID", curie=DDL.curie('BIOGAS_ACETIC_ACID'),
                      model_uri=DDL.BIOGAS_ACETIC_ACID, domain=None, range=Optional[str])

slots.BIOGAS_BUTYL_ACID = Slot(uri=DDL.BIOGAS_BUTYL_ACID, name="BIOGAS_BUTYL_ACID", curie=DDL.curie('BIOGAS_BUTYL_ACID'),
                      model_uri=DDL.BIOGAS_BUTYL_ACID, domain=None, range=Optional[str])

slots.BIOGAS_ISO_BUTYL_ACID = Slot(uri=DDL.BIOGAS_ISO_BUTYL_ACID, name="BIOGAS_ISO_BUTYL_ACID", curie=DDL.curie('BIOGAS_ISO_BUTYL_ACID'),
                      model_uri=DDL.BIOGAS_ISO_BUTYL_ACID, domain=None, range=Optional[str])

slots.BIOGAS_VALERIC_ACID = Slot(uri=DDL.BIOGAS_VALERIC_ACID, name="BIOGAS_VALERIC_ACID", curie=DDL.curie('BIOGAS_VALERIC_ACID'),
                      model_uri=DDL.BIOGAS_VALERIC_ACID, domain=None, range=Optional[str])

slots.BIOGAS_ISO_VALERIC_ACID = Slot(uri=DDL.BIOGAS_ISO_VALERIC_ACID, name="BIOGAS_ISO_VALERIC_ACID", curie=DDL.curie('BIOGAS_ISO_VALERIC_ACID'),
                      model_uri=DDL.BIOGAS_ISO_VALERIC_ACID, domain=None, range=Optional[str])

slots.BIOGAS_PROPIONIC_ACID = Slot(uri=DDL.BIOGAS_PROPIONIC_ACID, name="BIOGAS_PROPIONIC_ACID", curie=DDL.curie('BIOGAS_PROPIONIC_ACID'),
                      model_uri=DDL.BIOGAS_PROPIONIC_ACID, domain=None, range=Optional[str])

slots.BIOGAS_METHANE_PCT = Slot(uri=DDL.BIOGAS_METHANE_PCT, name="BIOGAS_METHANE_PCT", curie=DDL.curie('BIOGAS_METHANE_PCT'),
                      model_uri=DDL.BIOGAS_METHANE_PCT, domain=None, range=Optional[float])

slots.SAMPLE_CONDUCTIVITY = Slot(uri=DDL.SAMPLE_CONDUCTIVITY, name="SAMPLE_CONDUCTIVITY", curie=DDL.curie('SAMPLE_CONDUCTIVITY'),
                      model_uri=DDL.SAMPLE_CONDUCTIVITY, domain=None, range=Optional[str])

slots.GROWTH_TEMPERATURE = Slot(uri=DDL.GROWTH_TEMPERATURE, name="GROWTH_TEMPERATURE", curie=DDL.curie('GROWTH_TEMPERATURE'),
                      model_uri=DDL.GROWTH_TEMPERATURE, domain=None, range=Optional[float])

slots.SUBSURFACE_DEPTH = Slot(uri=DDL.SUBSURFACE_DEPTH, name="SUBSURFACE_DEPTH", curie=DDL.curie('SUBSURFACE_DEPTH'),
                      model_uri=DDL.SUBSURFACE_DEPTH, domain=None, range=Optional[float])

slots.LEGACY_DEPTH_DATA = Slot(uri=DDL.LEGACY_DEPTH_DATA, name="LEGACY_DEPTH_DATA", curie=DDL.curie('LEGACY_DEPTH_DATA'),
                      model_uri=DDL.LEGACY_DEPTH_DATA, domain=None, range=Optional[str])

slots.LATITUDE_TEST = Slot(uri=DDL.LATITUDE_TEST, name="LATITUDE_TEST", curie=DDL.curie('LATITUDE_TEST'),
                      model_uri=DDL.LATITUDE_TEST, domain=None, range=Optional[float])

slots.LONGITUDE_TEST = Slot(uri=DDL.LONGITUDE_TEST, name="LONGITUDE_TEST", curie=DDL.curie('LONGITUDE_TEST'),
                      model_uri=DDL.LONGITUDE_TEST, domain=None, range=Optional[float])

slots.ELEVATION = Slot(uri=DDL.ELEVATION, name="ELEVATION", curie=DDL.curie('ELEVATION'),
                      model_uri=DDL.ELEVATION, domain=None, range=Optional[float])

slots.ELEVATION2 = Slot(uri=DDL.ELEVATION2, name="ELEVATION2", curie=DDL.curie('ELEVATION2'),
                      model_uri=DDL.ELEVATION2, domain=None, range=Optional[float])

slots.SOIL_CURR_LAND_USE = Slot(uri=DDL.SOIL_CURR_LAND_USE, name="SOIL_CURR_LAND_USE", curie=DDL.curie('SOIL_CURR_LAND_USE'),
                      model_uri=DDL.SOIL_CURR_LAND_USE, domain=None, range=Optional[str])

slots.SOIL_CURR_VEGETATION = Slot(uri=DDL.SOIL_CURR_VEGETATION, name="SOIL_CURR_VEGETATION", curie=DDL.curie('SOIL_CURR_VEGETATION'),
                      model_uri=DDL.SOIL_CURR_VEGETATION, domain=None, range=Optional[str])

slots.SOIL_CURR_VEGETATION_METHOD = Slot(uri=DDL.SOIL_CURR_VEGETATION_METHOD, name="SOIL_CURR_VEGETATION_METHOD", curie=DDL.curie('SOIL_CURR_VEGETATION_METHOD'),
                      model_uri=DDL.SOIL_CURR_VEGETATION_METHOD, domain=None, range=Optional[str])

slots.SOIL_PREV_LAND_USE = Slot(uri=DDL.SOIL_PREV_LAND_USE, name="SOIL_PREV_LAND_USE", curie=DDL.curie('SOIL_PREV_LAND_USE'),
                      model_uri=DDL.SOIL_PREV_LAND_USE, domain=None, range=Optional[str])

slots.SOIL_PREV_LAND_USE_METH = Slot(uri=DDL.SOIL_PREV_LAND_USE_METH, name="SOIL_PREV_LAND_USE_METH", curie=DDL.curie('SOIL_PREV_LAND_USE_METH'),
                      model_uri=DDL.SOIL_PREV_LAND_USE_METH, domain=None, range=Optional[str])

slots.SOIL_CROP_ROTATION = Slot(uri=DDL.SOIL_CROP_ROTATION, name="SOIL_CROP_ROTATION", curie=DDL.curie('SOIL_CROP_ROTATION'),
                      model_uri=DDL.SOIL_CROP_ROTATION, domain=None, range=Optional[str])

slots.SOIL_AGROCHEM_ADDITION = Slot(uri=DDL.SOIL_AGROCHEM_ADDITION, name="SOIL_AGROCHEM_ADDITION", curie=DDL.curie('SOIL_AGROCHEM_ADDITION'),
                      model_uri=DDL.SOIL_AGROCHEM_ADDITION, domain=None, range=Optional[str])

slots.SOIL_TILLAGE = Slot(uri=DDL.SOIL_TILLAGE, name="SOIL_TILLAGE", curie=DDL.curie('SOIL_TILLAGE'),
                      model_uri=DDL.SOIL_TILLAGE, domain=None, range=Optional[str])

slots.SOIL_FIRE = Slot(uri=DDL.SOIL_FIRE, name="SOIL_FIRE", curie=DDL.curie('SOIL_FIRE'),
                      model_uri=DDL.SOIL_FIRE, domain=None, range=Optional[str])

slots.SOIL_FLOODING = Slot(uri=DDL.SOIL_FLOODING, name="SOIL_FLOODING", curie=DDL.curie('SOIL_FLOODING'),
                      model_uri=DDL.SOIL_FLOODING, domain=None, range=Optional[str])

slots.SOIL_EXTREME_EVENT = Slot(uri=DDL.SOIL_EXTREME_EVENT, name="SOIL_EXTREME_EVENT", curie=DDL.curie('SOIL_EXTREME_EVENT'),
                      model_uri=DDL.SOIL_EXTREME_EVENT, domain=None, range=Optional[str])

slots.SOIL_HORIZON = Slot(uri=DDL.SOIL_HORIZON, name="SOIL_HORIZON", curie=DDL.curie('SOIL_HORIZON'),
                      model_uri=DDL.SOIL_HORIZON, domain=None, range=Optional[str])

slots.SOIL_HORIZON_METHOD = Slot(uri=DDL.SOIL_HORIZON_METHOD, name="SOIL_HORIZON_METHOD", curie=DDL.curie('SOIL_HORIZON_METHOD'),
                      model_uri=DDL.SOIL_HORIZON_METHOD, domain=None, range=Optional[str])

slots.SOIL_SIEVING = Slot(uri=DDL.SOIL_SIEVING, name="SOIL_SIEVING", curie=DDL.curie('SOIL_SIEVING'),
                      model_uri=DDL.SOIL_SIEVING, domain=None, range=Optional[str])

slots.SOIL_WATER_CONTENT = Slot(uri=DDL.SOIL_WATER_CONTENT, name="SOIL_WATER_CONTENT", curie=DDL.curie('SOIL_WATER_CONTENT'),
                      model_uri=DDL.SOIL_WATER_CONTENT, domain=None, range=Optional[str])

slots.SOIL_WATER_CONTENT_SOIL_METH = Slot(uri=DDL.SOIL_WATER_CONTENT_SOIL_METH, name="SOIL_WATER_CONTENT_SOIL_METH", curie=DDL.curie('SOIL_WATER_CONTENT_SOIL_METH'),
                      model_uri=DDL.SOIL_WATER_CONTENT_SOIL_METH, domain=None, range=Optional[str])

slots.SAMPLE_WEIGHT_DNA_EXT = Slot(uri=DDL.SAMPLE_WEIGHT_DNA_EXT, name="SAMPLE_WEIGHT_DNA_EXT", curie=DDL.curie('SAMPLE_WEIGHT_DNA_EXT'),
                      model_uri=DDL.SAMPLE_WEIGHT_DNA_EXT, domain=None, range=Optional[str])

slots.SOIL_POOL_DNA_EXTRACTS = Slot(uri=DDL.SOIL_POOL_DNA_EXTRACTS, name="SOIL_POOL_DNA_EXTRACTS", curie=DDL.curie('SOIL_POOL_DNA_EXTRACTS'),
                      model_uri=DDL.SOIL_POOL_DNA_EXTRACTS, domain=None, range=Optional[str])

slots.SOIL_STORAGE_CONDITION = Slot(uri=DDL.SOIL_STORAGE_CONDITION, name="SOIL_STORAGE_CONDITION", curie=DDL.curie('SOIL_STORAGE_CONDITION'),
                      model_uri=DDL.SOIL_STORAGE_CONDITION, domain=None, range=Optional[str])

slots.SOIL_LINK_CLIMATE_INFO = Slot(uri=DDL.SOIL_LINK_CLIMATE_INFO, name="SOIL_LINK_CLIMATE_INFO", curie=DDL.curie('SOIL_LINK_CLIMATE_INFO'),
                      model_uri=DDL.SOIL_LINK_CLIMATE_INFO, domain=None, range=Optional[str])

slots.SOIL_LINK_CLASS_INFO = Slot(uri=DDL.SOIL_LINK_CLASS_INFO, name="SOIL_LINK_CLASS_INFO", curie=DDL.curie('SOIL_LINK_CLASS_INFO'),
                      model_uri=DDL.SOIL_LINK_CLASS_INFO, domain=None, range=Optional[str])

slots.SOIL_FAO_CLASS = Slot(uri=DDL.SOIL_FAO_CLASS, name="SOIL_FAO_CLASS", curie=DDL.curie('SOIL_FAO_CLASS'),
                      model_uri=DDL.SOIL_FAO_CLASS, domain=None, range=Optional[str])

slots.SOIL_LOCAL_CLASS = Slot(uri=DDL.SOIL_LOCAL_CLASS, name="SOIL_LOCAL_CLASS", curie=DDL.curie('SOIL_LOCAL_CLASS'),
                      model_uri=DDL.SOIL_LOCAL_CLASS, domain=None, range=Optional[str])

slots.SOIL_LOCAL_CLASS_METHOD = Slot(uri=DDL.SOIL_LOCAL_CLASS_METHOD, name="SOIL_LOCAL_CLASS_METHOD", curie=DDL.curie('SOIL_LOCAL_CLASS_METHOD'),
                      model_uri=DDL.SOIL_LOCAL_CLASS_METHOD, domain=None, range=Optional[str])

slots.SOIL_TYPE = Slot(uri=DDL.SOIL_TYPE, name="SOIL_TYPE", curie=DDL.curie('SOIL_TYPE'),
                      model_uri=DDL.SOIL_TYPE, domain=None, range=Optional[str])

slots.SOIL_TYPE_METHOD = Slot(uri=DDL.SOIL_TYPE_METHOD, name="SOIL_TYPE_METHOD", curie=DDL.curie('SOIL_TYPE_METHOD'),
                      model_uri=DDL.SOIL_TYPE_METHOD, domain=None, range=Optional[str])

slots.SOIL_SLOPE_GRADIENT = Slot(uri=DDL.SOIL_SLOPE_GRADIENT, name="SOIL_SLOPE_GRADIENT", curie=DDL.curie('SOIL_SLOPE_GRADIENT'),
                      model_uri=DDL.SOIL_SLOPE_GRADIENT, domain=None, range=Optional[float])

slots.SOIL_SLOPE_ASPECT = Slot(uri=DDL.SOIL_SLOPE_ASPECT, name="SOIL_SLOPE_ASPECT", curie=DDL.curie('SOIL_SLOPE_ASPECT'),
                      model_uri=DDL.SOIL_SLOPE_ASPECT, domain=None, range=Optional[float])

slots.SOIL_PROFILE_POSITION = Slot(uri=DDL.SOIL_PROFILE_POSITION, name="SOIL_PROFILE_POSITION", curie=DDL.curie('SOIL_PROFILE_POSITION'),
                      model_uri=DDL.SOIL_PROFILE_POSITION, domain=None, range=Optional[str])

slots.SOIL_DRAINAGE_CLASS = Slot(uri=DDL.SOIL_DRAINAGE_CLASS, name="SOIL_DRAINAGE_CLASS", curie=DDL.curie('SOIL_DRAINAGE_CLASS'),
                      model_uri=DDL.SOIL_DRAINAGE_CLASS, domain=None, range=Optional[str])

slots.SOIL_TEXTURE = Slot(uri=DDL.SOIL_TEXTURE, name="SOIL_TEXTURE", curie=DDL.curie('SOIL_TEXTURE'),
                      model_uri=DDL.SOIL_TEXTURE, domain=None, range=Optional[str])

slots.SOIL_TEXTURE_METHOD = Slot(uri=DDL.SOIL_TEXTURE_METHOD, name="SOIL_TEXTURE_METHOD", curie=DDL.curie('SOIL_TEXTURE_METHOD'),
                      model_uri=DDL.SOIL_TEXTURE_METHOD, domain=None, range=Optional[str])

slots.SOIL_PH_METHOD = Slot(uri=DDL.SOIL_PH_METHOD, name="SOIL_PH_METHOD", curie=DDL.curie('SOIL_PH_METHOD'),
                      model_uri=DDL.SOIL_PH_METHOD, domain=None, range=Optional[str])

slots.TOT_ORG_CARBON = Slot(uri=DDL.TOT_ORG_CARBON, name="TOT_ORG_CARBON", curie=DDL.curie('TOT_ORG_CARBON'),
                      model_uri=DDL.TOT_ORG_CARBON, domain=None, range=Optional[float])

slots.SOIL_TOT_ORG_C_METHOD = Slot(uri=DDL.SOIL_TOT_ORG_C_METHOD, name="SOIL_TOT_ORG_C_METHOD", curie=DDL.curie('SOIL_TOT_ORG_C_METHOD'),
                      model_uri=DDL.SOIL_TOT_ORG_C_METHOD, domain=None, range=Optional[str])

slots.TOT_NITROGEN = Slot(uri=DDL.TOT_NITROGEN, name="TOT_NITROGEN", curie=DDL.curie('TOT_NITROGEN'),
                      model_uri=DDL.TOT_NITROGEN, domain=None, range=Optional[str])

slots.SOIL_TOT_N_METHOD = Slot(uri=DDL.SOIL_TOT_N_METHOD, name="SOIL_TOT_N_METHOD", curie=DDL.curie('SOIL_TOT_N_METHOD'),
                      model_uri=DDL.SOIL_TOT_N_METHOD, domain=None, range=Optional[str])

slots.SOIL_MICROBIAL_BIOMASS = Slot(uri=DDL.SOIL_MICROBIAL_BIOMASS, name="SOIL_MICROBIAL_BIOMASS", curie=DDL.curie('SOIL_MICROBIAL_BIOMASS'),
                      model_uri=DDL.SOIL_MICROBIAL_BIOMASS, domain=None, range=Optional[str])

slots.SOIL_MICROBIAL_BIOMASS_METHOD = Slot(uri=DDL.SOIL_MICROBIAL_BIOMASS_METHOD, name="SOIL_MICROBIAL_BIOMASS_METHOD", curie=DDL.curie('SOIL_MICROBIAL_BIOMASS_METHOD'),
                      model_uri=DDL.SOIL_MICROBIAL_BIOMASS_METHOD, domain=None, range=Optional[str])

slots.SOIL_LINK_ADDIT_ANALYS = Slot(uri=DDL.SOIL_LINK_ADDIT_ANALYS, name="SOIL_LINK_ADDIT_ANALYS", curie=DDL.curie('SOIL_LINK_ADDIT_ANALYS'),
                      model_uri=DDL.SOIL_LINK_ADDIT_ANALYS, domain=None, range=Optional[str])

slots.SOIL_SALINITY_METHOD = Slot(uri=DDL.SOIL_SALINITY_METHOD, name="SOIL_SALINITY_METHOD", curie=DDL.curie('SOIL_SALINITY_METHOD'),
                      model_uri=DDL.SOIL_SALINITY_METHOD, domain=None, range=Optional[str])

slots.SOIL_HEAVY_METALS = Slot(uri=DDL.SOIL_HEAVY_METALS, name="SOIL_HEAVY_METALS", curie=DDL.curie('SOIL_HEAVY_METALS'),
                      model_uri=DDL.SOIL_HEAVY_METALS, domain=None, range=Optional[float])

slots.SOIL_HEAVY_METALS_METHOD = Slot(uri=DDL.SOIL_HEAVY_METALS_METHOD, name="SOIL_HEAVY_METALS_METHOD", curie=DDL.curie('SOIL_HEAVY_METALS_METHOD'),
                      model_uri=DDL.SOIL_HEAVY_METALS_METHOD, domain=None, range=Optional[str])

slots.SOIL_ALUMINIUM_SAT = Slot(uri=DDL.SOIL_ALUMINIUM_SAT, name="SOIL_ALUMINIUM_SAT", curie=DDL.curie('SOIL_ALUMINIUM_SAT'),
                      model_uri=DDL.SOIL_ALUMINIUM_SAT, domain=None, range=Optional[float])

slots.SOIL_ALUMINIUM_SAT_METHOD = Slot(uri=DDL.SOIL_ALUMINIUM_SAT_METHOD, name="SOIL_ALUMINIUM_SAT_METHOD", curie=DDL.curie('SOIL_ALUMINIUM_SAT_METHOD'),
                      model_uri=DDL.SOIL_ALUMINIUM_SAT_METHOD, domain=None, range=Optional[str])

slots.SOIL_MISC_PARAM = Slot(uri=DDL.SOIL_MISC_PARAM, name="SOIL_MISC_PARAM", curie=DDL.curie('SOIL_MISC_PARAM'),
                      model_uri=DDL.SOIL_MISC_PARAM, domain=None, range=Optional[str])

slots.WATER_ALKALINITY = Slot(uri=DDL.WATER_ALKALINITY, name="WATER_ALKALINITY", curie=DDL.curie('WATER_ALKALINITY'),
                      model_uri=DDL.WATER_ALKALINITY, domain=None, range=Optional[float])

slots.WATER_ALKYL_DIETHERS = Slot(uri=DDL.WATER_ALKYL_DIETHERS, name="WATER_ALKYL_DIETHERS", curie=DDL.curie('WATER_ALKYL_DIETHERS'),
                      model_uri=DDL.WATER_ALKYL_DIETHERS, domain=None, range=Optional[float])

slots.WATER_AMINOPEPT_ACT = Slot(uri=DDL.WATER_AMINOPEPT_ACT, name="WATER_AMINOPEPT_ACT", curie=DDL.curie('WATER_AMINOPEPT_ACT'),
                      model_uri=DDL.WATER_AMINOPEPT_ACT, domain=None, range=Optional[float])

slots.WATER_AMMONIUM = Slot(uri=DDL.WATER_AMMONIUM, name="WATER_AMMONIUM", curie=DDL.curie('WATER_AMMONIUM'),
                      model_uri=DDL.WATER_AMMONIUM, domain=None, range=Optional[float])

slots.WATER_ATMOSPHERIC_DATA = Slot(uri=DDL.WATER_ATMOSPHERIC_DATA, name="WATER_ATMOSPHERIC_DATA", curie=DDL.curie('WATER_ATMOSPHERIC_DATA'),
                      model_uri=DDL.WATER_ATMOSPHERIC_DATA, domain=None, range=Optional[str])

slots.WATER_BACTERIAL_PROD = Slot(uri=DDL.WATER_BACTERIAL_PROD, name="WATER_BACTERIAL_PROD", curie=DDL.curie('WATER_BACTERIAL_PROD'),
                      model_uri=DDL.WATER_BACTERIAL_PROD, domain=None, range=Optional[float])

slots.WATER_BACTERIAL_RESP = Slot(uri=DDL.WATER_BACTERIAL_RESP, name="WATER_BACTERIAL_RESP", curie=DDL.curie('WATER_BACTERIAL_RESP'),
                      model_uri=DDL.WATER_BACTERIAL_RESP, domain=None, range=Optional[float])

slots.WATER_BACTERIAL_CARBON_PROD = Slot(uri=DDL.WATER_BACTERIAL_CARBON_PROD, name="WATER_BACTERIAL_CARBON_PROD", curie=DDL.curie('WATER_BACTERIAL_CARBON_PROD'),
                      model_uri=DDL.WATER_BACTERIAL_CARBON_PROD, domain=None, range=Optional[float])

slots.WATER_BISHOMOHOPANOL = Slot(uri=DDL.WATER_BISHOMOHOPANOL, name="WATER_BISHOMOHOPANOL", curie=DDL.curie('WATER_BISHOMOHOPANOL'),
                      model_uri=DDL.WATER_BISHOMOHOPANOL, domain=None, range=Optional[str])

slots.WATER_BROMIDE = Slot(uri=DDL.WATER_BROMIDE, name="WATER_BROMIDE", curie=DDL.curie('WATER_BROMIDE'),
                      model_uri=DDL.WATER_BROMIDE, domain=None, range=Optional[float])

slots.WATER_CALCIUM = Slot(uri=DDL.WATER_CALCIUM, name="WATER_CALCIUM", curie=DDL.curie('WATER_CALCIUM'),
                      model_uri=DDL.WATER_CALCIUM, domain=None, range=Optional[str])

slots.WATER_CARBON_NITROG_RATIO = Slot(uri=DDL.WATER_CARBON_NITROG_RATIO, name="WATER_CARBON_NITROG_RATIO", curie=DDL.curie('WATER_CARBON_NITROG_RATIO'),
                      model_uri=DDL.WATER_CARBON_NITROG_RATIO, domain=None, range=Optional[str])

slots.WATER_CHEM_ADMINISTRATION = Slot(uri=DDL.WATER_CHEM_ADMINISTRATION, name="WATER_CHEM_ADMINISTRATION", curie=DDL.curie('WATER_CHEM_ADMINISTRATION'),
                      model_uri=DDL.WATER_CHEM_ADMINISTRATION, domain=None, range=Optional[str])

slots.WATER_CHLORIDE = Slot(uri=DDL.WATER_CHLORIDE, name="WATER_CHLORIDE", curie=DDL.curie('WATER_CHLORIDE'),
                      model_uri=DDL.WATER_CHLORIDE, domain=None, range=Optional[float])

slots.WATER_DENSITY = Slot(uri=DDL.WATER_DENSITY, name="WATER_DENSITY", curie=DDL.curie('WATER_DENSITY'),
                      model_uri=DDL.WATER_DENSITY, domain=None, range=Optional[float])

slots.WATER_DIETHER_LIPIDS = Slot(uri=DDL.WATER_DIETHER_LIPIDS, name="WATER_DIETHER_LIPIDS", curie=DDL.curie('WATER_DIETHER_LIPIDS'),
                      model_uri=DDL.WATER_DIETHER_LIPIDS, domain=None, range=Optional[float])

slots.WATER_DISS_CARBON_DIOXIDE = Slot(uri=DDL.WATER_DISS_CARBON_DIOXIDE, name="WATER_DISS_CARBON_DIOXIDE", curie=DDL.curie('WATER_DISS_CARBON_DIOXIDE'),
                      model_uri=DDL.WATER_DISS_CARBON_DIOXIDE, domain=None, range=Optional[float])

slots.WATER_DISS_HYDROGEN = Slot(uri=DDL.WATER_DISS_HYDROGEN, name="WATER_DISS_HYDROGEN", curie=DDL.curie('WATER_DISS_HYDROGEN'),
                      model_uri=DDL.WATER_DISS_HYDROGEN, domain=None, range=Optional[float])

slots.WATER_DISS_INORG_CARBON = Slot(uri=DDL.WATER_DISS_INORG_CARBON, name="WATER_DISS_INORG_CARBON", curie=DDL.curie('WATER_DISS_INORG_CARBON'),
                      model_uri=DDL.WATER_DISS_INORG_CARBON, domain=None, range=Optional[float])

slots.WATER_DISS_INORG_NITRO = Slot(uri=DDL.WATER_DISS_INORG_NITRO, name="WATER_DISS_INORG_NITRO", curie=DDL.curie('WATER_DISS_INORG_NITRO'),
                      model_uri=DDL.WATER_DISS_INORG_NITRO, domain=None, range=Optional[float])

slots.WATER_DISS_INORG_PHOSPHORUS = Slot(uri=DDL.WATER_DISS_INORG_PHOSPHORUS, name="WATER_DISS_INORG_PHOSPHORUS", curie=DDL.curie('WATER_DISS_INORG_PHOSPHORUS'),
                      model_uri=DDL.WATER_DISS_INORG_PHOSPHORUS, domain=None, range=Optional[float])

slots.WATER_DISS_ORG_CARBON = Slot(uri=DDL.WATER_DISS_ORG_CARBON, name="WATER_DISS_ORG_CARBON", curie=DDL.curie('WATER_DISS_ORG_CARBON'),
                      model_uri=DDL.WATER_DISS_ORG_CARBON, domain=None, range=Optional[float])

slots.WATER_DISS_ORG_NITROGEN = Slot(uri=DDL.WATER_DISS_ORG_NITROGEN, name="WATER_DISS_ORG_NITROGEN", curie=DDL.curie('WATER_DISS_ORG_NITROGEN'),
                      model_uri=DDL.WATER_DISS_ORG_NITROGEN, domain=None, range=Optional[float])

slots.WATER_DOWNWARD_PAR = Slot(uri=DDL.WATER_DOWNWARD_PAR, name="WATER_DOWNWARD_PAR", curie=DDL.curie('WATER_DOWNWARD_PAR'),
                      model_uri=DDL.WATER_DOWNWARD_PAR, domain=None, range=Optional[float])

slots.WATER_FLUORESCENCE = Slot(uri=DDL.WATER_FLUORESCENCE, name="WATER_FLUORESCENCE", curie=DDL.curie('WATER_FLUORESCENCE'),
                      model_uri=DDL.WATER_FLUORESCENCE, domain=None, range=Optional[float])

slots.WATER_GLUCOSIDASE_ACTIVITY = Slot(uri=DDL.WATER_GLUCOSIDASE_ACTIVITY, name="WATER_GLUCOSIDASE_ACTIVITY", curie=DDL.curie('WATER_GLUCOSIDASE_ACTIVITY'),
                      model_uri=DDL.WATER_GLUCOSIDASE_ACTIVITY, domain=None, range=Optional[float])

slots.WATER_LIGHT_INTENSITY = Slot(uri=DDL.WATER_LIGHT_INTENSITY, name="WATER_LIGHT_INTENSITY", curie=DDL.curie('WATER_LIGHT_INTENSITY'),
                      model_uri=DDL.WATER_LIGHT_INTENSITY, domain=None, range=Optional[float])

slots.WATER_MAGNESIUM = Slot(uri=DDL.WATER_MAGNESIUM, name="WATER_MAGNESIUM", curie=DDL.curie('WATER_MAGNESIUM'),
                      model_uri=DDL.WATER_MAGNESIUM, domain=None, range=Optional[str])

slots.WATER_MEAN_FRICT_VEL = Slot(uri=DDL.WATER_MEAN_FRICT_VEL, name="WATER_MEAN_FRICT_VEL", curie=DDL.curie('WATER_MEAN_FRICT_VEL'),
                      model_uri=DDL.WATER_MEAN_FRICT_VEL, domain=None, range=Optional[float])

slots.WATER_MEAN_PEAK_FRICT_VEL = Slot(uri=DDL.WATER_MEAN_PEAK_FRICT_VEL, name="WATER_MEAN_PEAK_FRICT_VEL", curie=DDL.curie('WATER_MEAN_PEAK_FRICT_VEL'),
                      model_uri=DDL.WATER_MEAN_PEAK_FRICT_VEL, domain=None, range=Optional[float])

slots.WATER_MISC_PARAMETER = Slot(uri=DDL.WATER_MISC_PARAMETER, name="WATER_MISC_PARAMETER", curie=DDL.curie('WATER_MISC_PARAMETER'),
                      model_uri=DDL.WATER_MISC_PARAMETER, domain=None, range=Optional[str])

slots.WATER_N_ALKANES = Slot(uri=DDL.WATER_N_ALKANES, name="WATER_N_ALKANES", curie=DDL.curie('WATER_N_ALKANES'),
                      model_uri=DDL.WATER_N_ALKANES, domain=None, range=Optional[float])

slots.WATER_NITRITE = Slot(uri=DDL.WATER_NITRITE, name="WATER_NITRITE", curie=DDL.curie('WATER_NITRITE'),
                      model_uri=DDL.WATER_NITRITE, domain=None, range=Optional[float])

slots.WATER_ORG_MATTER = Slot(uri=DDL.WATER_ORG_MATTER, name="WATER_ORG_MATTER", curie=DDL.curie('WATER_ORG_MATTER'),
                      model_uri=DDL.WATER_ORG_MATTER, domain=None, range=Optional[float])

slots.WATER_ORG_NITROGEN = Slot(uri=DDL.WATER_ORG_NITROGEN, name="WATER_ORG_NITROGEN", curie=DDL.curie('WATER_ORG_NITROGEN'),
                      model_uri=DDL.WATER_ORG_NITROGEN, domain=None, range=Optional[float])

slots.WATER_ORGANISM_COUNT = Slot(uri=DDL.WATER_ORGANISM_COUNT, name="WATER_ORGANISM_COUNT", curie=DDL.curie('WATER_ORGANISM_COUNT'),
                      model_uri=DDL.WATER_ORGANISM_COUNT, domain=None, range=Optional[float])

slots.WATER_OXY_STAT_SAMPLE = Slot(uri=DDL.WATER_OXY_STAT_SAMPLE, name="WATER_OXY_STAT_SAMPLE", curie=DDL.curie('WATER_OXY_STAT_SAMPLE'),
                      model_uri=DDL.WATER_OXY_STAT_SAMPLE, domain=None, range=Optional[str])

slots.WATER_PART_ORG_CARBON = Slot(uri=DDL.WATER_PART_ORG_CARBON, name="WATER_PART_ORG_CARBON", curie=DDL.curie('WATER_PART_ORG_CARBON'),
                      model_uri=DDL.WATER_PART_ORG_CARBON, domain=None, range=Optional[float])

slots.WATER_PART_ORG_NITROGEN = Slot(uri=DDL.WATER_PART_ORG_NITROGEN, name="WATER_PART_ORG_NITROGEN", curie=DDL.curie('WATER_PART_ORG_NITROGEN'),
                      model_uri=DDL.WATER_PART_ORG_NITROGEN, domain=None, range=Optional[float])

slots.WATER_PERTURBATION = Slot(uri=DDL.WATER_PERTURBATION, name="WATER_PERTURBATION", curie=DDL.curie('WATER_PERTURBATION'),
                      model_uri=DDL.WATER_PERTURBATION, domain=None, range=Optional[str])

slots.WATER_PETROLEUM_HYDROCARBON = Slot(uri=DDL.WATER_PETROLEUM_HYDROCARBON, name="WATER_PETROLEUM_HYDROCARBON", curie=DDL.curie('WATER_PETROLEUM_HYDROCARBON'),
                      model_uri=DDL.WATER_PETROLEUM_HYDROCARBON, domain=None, range=Optional[float])

slots.WATER_PHAEOPIGMENTS = Slot(uri=DDL.WATER_PHAEOPIGMENTS, name="WATER_PHAEOPIGMENTS", curie=DDL.curie('WATER_PHAEOPIGMENTS'),
                      model_uri=DDL.WATER_PHAEOPIGMENTS, domain=None, range=Optional[float])

slots.WATER_PHOSPLIPID_FATT_ACID = Slot(uri=DDL.WATER_PHOSPLIPID_FATT_ACID, name="WATER_PHOSPLIPID_FATT_ACID", curie=DDL.curie('WATER_PHOSPLIPID_FATT_ACID'),
                      model_uri=DDL.WATER_PHOSPLIPID_FATT_ACID, domain=None, range=Optional[str])

slots.WATER_PHOTON_FLUX = Slot(uri=DDL.WATER_PHOTON_FLUX, name="WATER_PHOTON_FLUX", curie=DDL.curie('WATER_PHOTON_FLUX'),
                      model_uri=DDL.WATER_PHOTON_FLUX, domain=None, range=Optional[float])

slots.WATER_POTASSIUM = Slot(uri=DDL.WATER_POTASSIUM, name="WATER_POTASSIUM", curie=DDL.curie('WATER_POTASSIUM'),
                      model_uri=DDL.WATER_POTASSIUM, domain=None, range=Optional[float])

slots.WATER_PRIMARY_PROD = Slot(uri=DDL.WATER_PRIMARY_PROD, name="WATER_PRIMARY_PROD", curie=DDL.curie('WATER_PRIMARY_PROD'),
                      model_uri=DDL.WATER_PRIMARY_PROD, domain=None, range=Optional[float])

slots.WATER_REDOX_POTENTIAL = Slot(uri=DDL.WATER_REDOX_POTENTIAL, name="WATER_REDOX_POTENTIAL", curie=DDL.curie('WATER_REDOX_POTENTIAL'),
                      model_uri=DDL.WATER_REDOX_POTENTIAL, domain=None, range=Optional[float])

slots.WATER_SAMP_STORE_DUR = Slot(uri=DDL.WATER_SAMP_STORE_DUR, name="WATER_SAMP_STORE_DUR", curie=DDL.curie('WATER_SAMP_STORE_DUR'),
                      model_uri=DDL.WATER_SAMP_STORE_DUR, domain=None, range=Optional[str])

slots.WATER_SAMP_STORE_LOC = Slot(uri=DDL.WATER_SAMP_STORE_LOC, name="WATER_SAMP_STORE_LOC", curie=DDL.curie('WATER_SAMP_STORE_LOC'),
                      model_uri=DDL.WATER_SAMP_STORE_LOC, domain=None, range=Optional[str])

slots.WATER_SAMP_STORE_TEMP = Slot(uri=DDL.WATER_SAMP_STORE_TEMP, name="WATER_SAMP_STORE_TEMP", curie=DDL.curie('WATER_SAMP_STORE_TEMP'),
                      model_uri=DDL.WATER_SAMP_STORE_TEMP, domain=None, range=Optional[float])

slots.WATER_SODIUM = Slot(uri=DDL.WATER_SODIUM, name="WATER_SODIUM", curie=DDL.curie('WATER_SODIUM'),
                      model_uri=DDL.WATER_SODIUM, domain=None, range=Optional[float])

slots.WATER_SOLUBLE_REACT_PHOSP = Slot(uri=DDL.WATER_SOLUBLE_REACT_PHOSP, name="WATER_SOLUBLE_REACT_PHOSP", curie=DDL.curie('WATER_SOLUBLE_REACT_PHOSP'),
                      model_uri=DDL.WATER_SOLUBLE_REACT_PHOSP, domain=None, range=Optional[float])

slots.WATER_SULFATE = Slot(uri=DDL.WATER_SULFATE, name="WATER_SULFATE", curie=DDL.curie('WATER_SULFATE'),
                      model_uri=DDL.WATER_SULFATE, domain=None, range=Optional[str])

slots.WATER_SULFIDE = Slot(uri=DDL.WATER_SULFIDE, name="WATER_SULFIDE", curie=DDL.curie('WATER_SULFIDE'),
                      model_uri=DDL.WATER_SULFIDE, domain=None, range=Optional[str])

slots.WATER_SUSPEND_PART_MATTER = Slot(uri=DDL.WATER_SUSPEND_PART_MATTER, name="WATER_SUSPEND_PART_MATTER", curie=DDL.curie('WATER_SUSPEND_PART_MATTER'),
                      model_uri=DDL.WATER_SUSPEND_PART_MATTER, domain=None, range=Optional[float])

slots.WATER_TIDAL_STAGE = Slot(uri=DDL.WATER_TIDAL_STAGE, name="WATER_TIDAL_STAGE", curie=DDL.curie('WATER_TIDAL_STAGE'),
                      model_uri=DDL.WATER_TIDAL_STAGE, domain=None, range=Optional[str])

slots.WATER_TOT_DEPTH_WATER_COL = Slot(uri=DDL.WATER_TOT_DEPTH_WATER_COL, name="WATER_TOT_DEPTH_WATER_COL", curie=DDL.curie('WATER_TOT_DEPTH_WATER_COL'),
                      model_uri=DDL.WATER_TOT_DEPTH_WATER_COL, domain=None, range=Optional[float])

slots.WATER_TOT_DISS_NITRO = Slot(uri=DDL.WATER_TOT_DISS_NITRO, name="WATER_TOT_DISS_NITRO", curie=DDL.curie('WATER_TOT_DISS_NITRO'),
                      model_uri=DDL.WATER_TOT_DISS_NITRO, domain=None, range=Optional[float])

slots.WATER_TOT_INORG_NITRO = Slot(uri=DDL.WATER_TOT_INORG_NITRO, name="WATER_TOT_INORG_NITRO", curie=DDL.curie('WATER_TOT_INORG_NITRO'),
                      model_uri=DDL.WATER_TOT_INORG_NITRO, domain=None, range=Optional[float])

slots.WATER_TOT_PART_CARBON = Slot(uri=DDL.WATER_TOT_PART_CARBON, name="WATER_TOT_PART_CARBON", curie=DDL.curie('WATER_TOT_PART_CARBON'),
                      model_uri=DDL.WATER_TOT_PART_CARBON, domain=None, range=Optional[str])

slots.WATER_TOT_PHOSPHORUS = Slot(uri=DDL.WATER_TOT_PHOSPHORUS, name="WATER_TOT_PHOSPHORUS", curie=DDL.curie('WATER_TOT_PHOSPHORUS'),
                      model_uri=DDL.WATER_TOT_PHOSPHORUS, domain=None, range=Optional[float])

slots.WATER_CURRENT = Slot(uri=DDL.WATER_CURRENT, name="WATER_CURRENT", curie=DDL.curie('WATER_CURRENT'),
                      model_uri=DDL.WATER_CURRENT, domain=None, range=Optional[str])

slots.LATITUDE = Slot(uri=DDL.LATITUDE, name="LATITUDE", curie=DDL.curie('LATITUDE'),
                      model_uri=DDL.LATITUDE, domain=None, range=Optional[float])

slots.LONGITUDE = Slot(uri=DDL.LONGITUDE, name="LONGITUDE", curie=DDL.curie('LONGITUDE'),
                      model_uri=DDL.LONGITUDE, domain=None, range=Optional[float])

slots.DEPTH = Slot(uri=DDL.DEPTH, name="DEPTH", curie=DDL.curie('DEPTH'),
                      model_uri=DDL.DEPTH, domain=None, range=Optional[float])

slots.DEPTH2 = Slot(uri=DDL.DEPTH2, name="DEPTH2", curie=DDL.curie('DEPTH2'),
                      model_uri=DDL.DEPTH2, domain=None, range=Optional[float])

slots.ALTITUDE = Slot(uri=DDL.ALTITUDE, name="ALTITUDE", curie=DDL.curie('ALTITUDE'),
                      model_uri=DDL.ALTITUDE, domain=None, range=Optional[float])

slots.ALTITUDE2 = Slot(uri=DDL.ALTITUDE2, name="ALTITUDE2", curie=DDL.curie('ALTITUDE2'),
                      model_uri=DDL.ALTITUDE2, domain=None, range=Optional[float])

slots.SOLUBLE_IRON_MICROMOL = Slot(uri=DDL.SOLUBLE_IRON_MICROMOL, name="SOLUBLE_IRON_MICROMOL", curie=DDL.curie('SOLUBLE_IRON_MICROMOL'),
                      model_uri=DDL.SOLUBLE_IRON_MICROMOL, domain=None, range=Optional[float])

slots.BICARBONATE_MILLIMOL = Slot(uri=DDL.BICARBONATE_MILLIMOL, name="BICARBONATE_MILLIMOL", curie=DDL.curie('BICARBONATE_MILLIMOL'),
                      model_uri=DDL.BICARBONATE_MILLIMOL, domain=None, range=Optional[float])

slots.H2S_MILLIMOL = Slot(uri=DDL.H2S_MILLIMOL, name="H2S_MILLIMOL", curie=DDL.curie('H2S_MILLIMOL'),
                      model_uri=DDL.H2S_MILLIMOL, domain=None, range=Optional[float])

slots.H2S_PRESENT = Slot(uri=DDL.H2S_PRESENT, name="H2S_PRESENT", curie=DDL.curie('H2S_PRESENT'),
                      model_uri=DDL.H2S_PRESENT, domain=None, range=Optional[str])

slots.IRRADIANCE = Slot(uri=DDL.IRRADIANCE, name="IRRADIANCE", curie=DDL.curie('IRRADIANCE'),
                      model_uri=DDL.IRRADIANCE, domain=None, range=Optional[str])

slots.OXYGEN_PRESENCE = Slot(uri=DDL.OXYGEN_PRESENCE, name="OXYGEN_PRESENCE", curie=DDL.curie('OXYGEN_PRESENCE'),
                      model_uri=DDL.OXYGEN_PRESENCE, domain=None, range=Optional[str])

slots.METHANE_CONC_MILLIMOL = Slot(uri=DDL.METHANE_CONC_MILLIMOL, name="METHANE_CONC_MILLIMOL", curie=DDL.curie('METHANE_CONC_MILLIMOL'),
                      model_uri=DDL.METHANE_CONC_MILLIMOL, domain=None, range=Optional[float])

slots.GROWTH_TEMPERATURE2 = Slot(uri=DDL.GROWTH_TEMPERATURE2, name="GROWTH_TEMPERATURE2", curie=DDL.curie('GROWTH_TEMPERATURE2'),
                      model_uri=DDL.GROWTH_TEMPERATURE2, domain=None, range=Optional[float])

slots.SUBSURFACE_DEPTH2 = Slot(uri=DDL.SUBSURFACE_DEPTH2, name="SUBSURFACE_DEPTH2", curie=DDL.curie('SUBSURFACE_DEPTH2'),
                      model_uri=DDL.SUBSURFACE_DEPTH2, domain=None, range=Optional[float])

slots.PH1 = Slot(uri=DDL.PH1, name="PH1", curie=DDL.curie('PH1'),
                      model_uri=DDL.PH1, domain=None, range=Optional[float])

slots.PH2 = Slot(uri=DDL.PH2, name="PH2", curie=DDL.curie('PH2'),
                      model_uri=DDL.PH2, domain=None, range=Optional[float])

slots.PH_OLD = Slot(uri=DDL.PH_OLD, name="PH_OLD", curie=DDL.curie('PH_OLD'),
                      model_uri=DDL.PH_OLD, domain=None, range=Optional[str])

slots.WATER_ALKALINITY_METHOD = Slot(uri=DDL.WATER_ALKALINITY_METHOD, name="WATER_ALKALINITY_METHOD", curie=DDL.curie('WATER_ALKALINITY_METHOD'),
                      model_uri=DDL.WATER_ALKALINITY_METHOD, domain=None, range=Optional[str])

slots.WATER_TURBIDITY = Slot(uri=DDL.WATER_TURBIDITY, name="WATER_TURBIDITY", curie=DDL.curie('WATER_TURBIDITY'),
                      model_uri=DDL.WATER_TURBIDITY, domain=None, range=Optional[str])

slots.WATER_SIZE_FRAC_LOW = Slot(uri=DDL.WATER_SIZE_FRAC_LOW, name="WATER_SIZE_FRAC_LOW", curie=DDL.curie('WATER_SIZE_FRAC_LOW'),
                      model_uri=DDL.WATER_SIZE_FRAC_LOW, domain=None, range=Optional[float])

slots.WATER_SIZE_FRAC_UP = Slot(uri=DDL.WATER_SIZE_FRAC_UP, name="WATER_SIZE_FRAC_UP", curie=DDL.curie('WATER_SIZE_FRAC_UP'),
                      model_uri=DDL.WATER_SIZE_FRAC_UP, domain=None, range=Optional[float])

slots.SOIL_MEAN_ANNUAL_TEMP = Slot(uri=DDL.SOIL_MEAN_ANNUAL_TEMP, name="SOIL_MEAN_ANNUAL_TEMP", curie=DDL.curie('SOIL_MEAN_ANNUAL_TEMP'),
                      model_uri=DDL.SOIL_MEAN_ANNUAL_TEMP, domain=None, range=Optional[float])

slots.SOIL_MEAN_SEASONAL_TEMP = Slot(uri=DDL.SOIL_MEAN_SEASONAL_TEMP, name="SOIL_MEAN_SEASONAL_TEMP", curie=DDL.curie('SOIL_MEAN_SEASONAL_TEMP'),
                      model_uri=DDL.SOIL_MEAN_SEASONAL_TEMP, domain=None, range=Optional[float])

slots.SOIL_MEAN_ANNUAL_PRECPT = Slot(uri=DDL.SOIL_MEAN_ANNUAL_PRECPT, name="SOIL_MEAN_ANNUAL_PRECPT", curie=DDL.curie('SOIL_MEAN_ANNUAL_PRECPT'),
                      model_uri=DDL.SOIL_MEAN_ANNUAL_PRECPT, domain=None, range=Optional[float])

slots.SOIL_MEAN_SEASONAL_PRECPT = Slot(uri=DDL.SOIL_MEAN_SEASONAL_PRECPT, name="SOIL_MEAN_SEASONAL_PRECPT", curie=DDL.curie('SOIL_MEAN_SEASONAL_PRECPT'),
                      model_uri=DDL.SOIL_MEAN_SEASONAL_PRECPT, domain=None, range=Optional[float])

slots.TEST_PACKAGE_ID = Slot(uri=DDL.TEST_PACKAGE_ID, name="TEST_PACKAGE_ID", curie=DDL.curie('TEST_PACKAGE_ID'),
                      model_uri=DDL.TEST_PACKAGE_ID, domain=None, range=Optional[int])

slots.SOIL_PACKAGE_ID = Slot(uri=DDL.SOIL_PACKAGE_ID, name="SOIL_PACKAGE_ID", curie=DDL.curie('SOIL_PACKAGE_ID'),
                      model_uri=DDL.SOIL_PACKAGE_ID, domain=None, range=Optional[int])

slots.WATER_PACKAGE_ID = Slot(uri=DDL.WATER_PACKAGE_ID, name="WATER_PACKAGE_ID", curie=DDL.curie('WATER_PACKAGE_ID'),
                      model_uri=DDL.WATER_PACKAGE_ID, domain=None, range=Optional[int])

slots.GLOBAL_PACKAGE_ID = Slot(uri=DDL.GLOBAL_PACKAGE_ID, name="GLOBAL_PACKAGE_ID", curie=DDL.curie('GLOBAL_PACKAGE_ID'),
                      model_uri=DDL.GLOBAL_PACKAGE_ID, domain=None, range=Optional[int])

slots.ENVO_BIOME_ID = Slot(uri=DDL.ENVO_BIOME_ID, name="ENVO_BIOME_ID", curie=DDL.curie('ENVO_BIOME_ID'),
                      model_uri=DDL.ENVO_BIOME_ID, domain=None, range=Optional[str])

slots.ENVO_FEATURE_ID = Slot(uri=DDL.ENVO_FEATURE_ID, name="ENVO_FEATURE_ID", curie=DDL.curie('ENVO_FEATURE_ID'),
                      model_uri=DDL.ENVO_FEATURE_ID, domain=None, range=Optional[str])

slots.ENVO_MATERIAL_ID = Slot(uri=DDL.ENVO_MATERIAL_ID, name="ENVO_MATERIAL_ID", curie=DDL.curie('ENVO_MATERIAL_ID'),
                      model_uri=DDL.ENVO_MATERIAL_ID, domain=None, range=Optional[str])

slots.USERNAME = Slot(uri=DDL.USERNAME, name="USERNAME", curie=DDL.curie('USERNAME'),
                      model_uri=DDL.USERNAME, domain=None, range=Optional[str])

slots.PASSWORD = Slot(uri=DDL.PASSWORD, name="PASSWORD", curie=DDL.curie('PASSWORD'),
                      model_uri=DDL.PASSWORD, domain=None, range=Optional[str])

slots.NAME = Slot(uri=DDL.NAME, name="NAME", curie=DDL.curie('NAME'),
                      model_uri=DDL.NAME, domain=None, range=Optional[str])

slots.TITLE = Slot(uri=DDL.TITLE, name="TITLE", curie=DDL.curie('TITLE'),
                      model_uri=DDL.TITLE, domain=None, range=Optional[str])

slots.DEPARTMENT = Slot(uri=DDL.DEPARTMENT, name="DEPARTMENT", curie=DDL.curie('DEPARTMENT'),
                      model_uri=DDL.DEPARTMENT, domain=None, range=Optional[str])

slots.EMAIL = Slot(uri=DDL.EMAIL, name="EMAIL", curie=DDL.curie('EMAIL'),
                      model_uri=DDL.EMAIL, domain=None, range=Optional[str])

slots.PHONE = Slot(uri=DDL.PHONE, name="PHONE", curie=DDL.curie('PHONE'),
                      model_uri=DDL.PHONE, domain=None, range=Optional[str])

slots.ORGANIZATION = Slot(uri=DDL.ORGANIZATION, name="ORGANIZATION", curie=DDL.curie('ORGANIZATION'),
                      model_uri=DDL.ORGANIZATION, domain=None, range=Optional[str])

slots.ADDRESS = Slot(uri=DDL.ADDRESS, name="ADDRESS", curie=DDL.curie('ADDRESS'),
                      model_uri=DDL.ADDRESS, domain=None, range=Optional[str])

slots.CITY = Slot(uri=DDL.CITY, name="CITY", curie=DDL.curie('CITY'),
                      model_uri=DDL.CITY, domain=None, range=Optional[str])

slots.STATE = Slot(uri=DDL.STATE, name="STATE", curie=DDL.curie('STATE'),
                      model_uri=DDL.STATE, domain=None, range=Optional[str])

slots.COUNTRY = Slot(uri=DDL.COUNTRY, name="COUNTRY", curie=DDL.curie('COUNTRY'),
                      model_uri=DDL.COUNTRY, domain=None, range=Optional[str])

slots.X_SUPER_USER = Slot(uri=DDL.X_SUPER_USER, name="X_SUPER_USER", curie=DDL.curie('X_SUPER_USER'),
                      model_uri=DDL.X_SUPER_USER, domain=None, range=Optional[str])

slots.X_IMG_EDITOR = Slot(uri=DDL.X_IMG_EDITOR, name="X_IMG_EDITOR", curie=DDL.curie('X_IMG_EDITOR'),
                      model_uri=DDL.X_IMG_EDITOR, domain=None, range=Optional[str])

slots.X_IMG_GROUP = Slot(uri=DDL.X_IMG_GROUP, name="X_IMG_GROUP", curie=DDL.curie('X_IMG_GROUP'),
                      model_uri=DDL.X_IMG_GROUP, domain=None, range=Optional[float])

slots.JGI_USER = Slot(uri=DDL.JGI_USER, name="JGI_USER", curie=DDL.curie('JGI_USER'),
                      model_uri=DDL.JGI_USER, domain=None, range=Optional[str])

slots.X_IMG_EDITING_LEVEL = Slot(uri=DDL.X_IMG_EDITING_LEVEL, name="X_IMG_EDITING_LEVEL", curie=DDL.curie('X_IMG_EDITING_LEVEL'),
                      model_uri=DDL.X_IMG_EDITING_LEVEL, domain=None, range=Optional[str])

slots.CALIBAN_ID = Slot(uri=DDL.CALIBAN_ID, name="CALIBAN_ID", curie=DDL.curie('CALIBAN_ID'),
                      model_uri=DDL.CALIBAN_ID, domain=None, range=Optional[int])

slots.CALIBAN_USER_NAME = Slot(uri=DDL.CALIBAN_USER_NAME, name="CALIBAN_USER_NAME", curie=DDL.curie('CALIBAN_USER_NAME'),
                      model_uri=DDL.CALIBAN_USER_NAME, domain=None, range=Optional[str])

slots.URL = Slot(uri=DDL.URL, name="URL", curie=DDL.curie('URL'),
                      model_uri=DDL.URL, domain=None, range=Optional[str])

slots.X_IMG_CONTACT_ID = Slot(uri=DDL.X_IMG_CONTACT_ID, name="X_IMG_CONTACT_ID", curie=DDL.curie('X_IMG_CONTACT_ID'),
                      model_uri=DDL.X_IMG_CONTACT_ID, domain=None, range=Optional[int])

slots.MASTER_CONTACT_ID = Slot(uri=DDL.MASTER_CONTACT_ID, name="MASTER_CONTACT_ID", curie=DDL.curie('MASTER_CONTACT_ID'),
                      model_uri=DDL.MASTER_CONTACT_ID, domain=None, range=Optional[int])

slots.ORACLE_USER_NAME = Slot(uri=DDL.ORACLE_USER_NAME, name="ORACLE_USER_NAME", curie=DDL.curie('ORACLE_USER_NAME'),
                      model_uri=DDL.ORACLE_USER_NAME, domain=None, range=Optional[str])

slots.USER_ROLE = Slot(uri=DDL.USER_ROLE, name="USER_ROLE", curie=DDL.curie('USER_ROLE'),
                      model_uri=DDL.USER_ROLE, domain=None, range=Optional[str])

slots.GEBA_ORGANISM_AVAIL_COUNT = Slot(uri=DDL.GEBA_ORGANISM_AVAIL_COUNT, name="GEBA_ORGANISM_AVAIL_COUNT", curie=DDL.curie('GEBA_ORGANISM_AVAIL_COUNT'),
                      model_uri=DDL.GEBA_ORGANISM_AVAIL_COUNT, domain=None, range=Optional[float])

slots.GEBA_REVIEWER = Slot(uri=DDL.GEBA_REVIEWER, name="GEBA_REVIEWER", curie=DDL.curie('GEBA_REVIEWER'),
                      model_uri=DDL.GEBA_REVIEWER, domain=None, range=Optional[str])

slots.TERM = Slot(uri=DDL.TERM, name="TERM", curie=DDL.curie('TERM'),
                      model_uri=DDL.TERM, domain=None, range=Optional[str])

slots.SEQUENCE = Slot(uri=DDL.SEQUENCE, name="SEQUENCE", curie=DDL.curie('SEQUENCE'),
                      model_uri=DDL.SEQUENCE, domain=None, range=Optional[float])

slots.ENVO_LABEL = Slot(uri=DDL.ENVO_LABEL, name="ENVO_LABEL", curie=DDL.curie('ENVO_LABEL'),
                      model_uri=DDL.ENVO_LABEL, domain=None, range=Optional[str])

slots.LABORATORY = Slot(uri=DDL.LABORATORY, name="LABORATORY", curie=DDL.curie('LABORATORY'),
                      model_uri=DDL.LABORATORY, domain=None, range=Optional[str])

slots.IS_CURATED = Slot(uri=DDL.IS_CURATED, name="IS_CURATED", curie=DDL.curie('IS_CURATED'),
                      model_uri=DDL.IS_CURATED, domain=None, range=Optional[str])

slots.BIOTIC_RELATIONSHIP_ID = Slot(uri=DDL.BIOTIC_RELATIONSHIP_ID, name="BIOTIC_RELATIONSHIP_ID", curie=DDL.curie('BIOTIC_RELATIONSHIP_ID'),
                      model_uri=DDL.BIOTIC_RELATIONSHIP_ID, domain=None, range=Optional[int])

slots.BODY_PRODUCT_ID = Slot(uri=DDL.BODY_PRODUCT_ID, name="BODY_PRODUCT_ID", curie=DDL.curie('BODY_PRODUCT_ID'),
                      model_uri=DDL.BODY_PRODUCT_ID, domain=None, range=Optional[int])

slots.CELL_ARRANGEMENT_ID = Slot(uri=DDL.CELL_ARRANGEMENT_ID, name="CELL_ARRANGEMENT_ID", curie=DDL.curie('CELL_ARRANGEMENT_ID'),
                      model_uri=DDL.CELL_ARRANGEMENT_ID, domain=None, range=Optional[int])

slots.DISEASE_ID = Slot(uri=DDL.DISEASE_ID, name="DISEASE_ID", curie=DDL.curie('DISEASE_ID'),
                      model_uri=DDL.DISEASE_ID, domain=None, range=Optional[int])

slots.ENERGY_SOURCE_ID = Slot(uri=DDL.ENERGY_SOURCE_ID, name="ENERGY_SOURCE_ID", curie=DDL.curie('ENERGY_SOURCE_ID'),
                      model_uri=DDL.ENERGY_SOURCE_ID, domain=None, range=Optional[int])

slots.HABITAT_ID = Slot(uri=DDL.HABITAT_ID, name="HABITAT_ID", curie=DDL.curie('HABITAT_ID'),
                      model_uri=DDL.HABITAT_ID, domain=None, range=Optional[int])

slots.METABOLISM_ID = Slot(uri=DDL.METABOLISM_ID, name="METABOLISM_ID", curie=DDL.curie('METABOLISM_ID'),
                      model_uri=DDL.METABOLISM_ID, domain=None, range=Optional[int])

slots.PHENOTYPE_ID = Slot(uri=DDL.PHENOTYPE_ID, name="PHENOTYPE_ID", curie=DDL.curie('PHENOTYPE_ID'),
                      model_uri=DDL.PHENOTYPE_ID, domain=None, range=Optional[int])

slots.EXEMPLAR_DOI = Slot(uri=DDL.EXEMPLAR_DOI, name="EXEMPLAR_DOI", curie=DDL.curie('EXEMPLAR_DOI'),
                      model_uri=DDL.EXEMPLAR_DOI, domain=None, range=Optional[str])

slots.EXEMPLAR_NAME = Slot(uri=DDL.EXEMPLAR_NAME, name="EXEMPLAR_NAME", curie=DDL.curie('EXEMPLAR_NAME'),
                      model_uri=DDL.EXEMPLAR_NAME, domain=None, range=Optional[str])

slots.TAXON_DOI = Slot(uri=DDL.TAXON_DOI, name="TAXON_DOI", curie=DDL.curie('TAXON_DOI'),
                      model_uri=DDL.TAXON_DOI, domain=None, range=Optional[str])

slots.CULTURE_COLLECTION_ID = Slot(uri=DDL.CULTURE_COLLECTION_ID, name="CULTURE_COLLECTION_ID", curie=DDL.curie('CULTURE_COLLECTION_ID'),
                      model_uri=DDL.CULTURE_COLLECTION_ID, domain=None, range=Optional[str])

slots.TYPE_STRAIN = Slot(uri=DDL.TYPE_STRAIN, name="TYPE_STRAIN", curie=DDL.curie('TYPE_STRAIN'),
                      model_uri=DDL.TYPE_STRAIN, domain=None, range=Optional[str])

slots.BIOSAFETY_LEVEL = Slot(uri=DDL.BIOSAFETY_LEVEL, name="BIOSAFETY_LEVEL", curie=DDL.curie('BIOSAFETY_LEVEL'),
                      model_uri=DDL.BIOSAFETY_LEVEL, domain=None, range=Optional[str])

slots.STRAIN_INFO_ID = Slot(uri=DDL.STRAIN_INFO_ID, name="STRAIN_INFO_ID", curie=DDL.curie('STRAIN_INFO_ID'),
                      model_uri=DDL.STRAIN_INFO_ID, domain=None, range=Optional[int])

slots.GENBANK_16S_ID = Slot(uri=DDL.GENBANK_16S_ID, name="GENBANK_16S_ID", curie=DDL.curie('GENBANK_16S_ID'),
                      model_uri=DDL.GENBANK_16S_ID, domain=None, range=Optional[str])

slots.OXYGEN_REQUIREMENT = Slot(uri=DDL.OXYGEN_REQUIREMENT, name="OXYGEN_REQUIREMENT", curie=DDL.curie('OXYGEN_REQUIREMENT'),
                      model_uri=DDL.OXYGEN_REQUIREMENT, domain=None, range=Optional[str])

slots.CELL_SHAPE = Slot(uri=DDL.CELL_SHAPE, name="CELL_SHAPE", curie=DDL.curie('CELL_SHAPE'),
                      model_uri=DDL.CELL_SHAPE, domain=None, range=Optional[str])

slots.MOTILITY = Slot(uri=DDL.MOTILITY, name="MOTILITY", curie=DDL.curie('MOTILITY'),
                      model_uri=DDL.MOTILITY, domain=None, range=Optional[str])

slots.SPORULATION = Slot(uri=DDL.SPORULATION, name="SPORULATION", curie=DDL.curie('SPORULATION'),
                      model_uri=DDL.SPORULATION, domain=None, range=Optional[str])

slots.TEMPERATURE_RANGE = Slot(uri=DDL.TEMPERATURE_RANGE, name="TEMPERATURE_RANGE", curie=DDL.curie('TEMPERATURE_RANGE'),
                      model_uri=DDL.TEMPERATURE_RANGE, domain=None, range=Optional[str])

slots.COLOR = Slot(uri=DDL.COLOR, name="COLOR", curie=DDL.curie('COLOR'),
                      model_uri=DDL.COLOR, domain=None, range=Optional[str])

slots.GRAM_STAIN = Slot(uri=DDL.GRAM_STAIN, name="GRAM_STAIN", curie=DDL.curie('GRAM_STAIN'),
                      model_uri=DDL.GRAM_STAIN, domain=None, range=Optional[str])

slots.COMMON_NAME = Slot(uri=DDL.COMMON_NAME, name="COMMON_NAME", curie=DDL.curie('COMMON_NAME'),
                      model_uri=DDL.COMMON_NAME, domain=None, range=Optional[str])

slots.SYMBIOTIC_RELATIONSHIP = Slot(uri=DDL.SYMBIOTIC_RELATIONSHIP, name="SYMBIOTIC_RELATIONSHIP", curie=DDL.curie('SYMBIOTIC_RELATIONSHIP'),
                      model_uri=DDL.SYMBIOTIC_RELATIONSHIP, domain=None, range=Optional[str])

slots.SYMBIOTIC_PHYSICAL_INTERACTION = Slot(uri=DDL.SYMBIOTIC_PHYSICAL_INTERACTION, name="SYMBIOTIC_PHYSICAL_INTERACTION", curie=DDL.curie('SYMBIOTIC_PHYSICAL_INTERACTION'),
                      model_uri=DDL.SYMBIOTIC_PHYSICAL_INTERACTION, domain=None, range=Optional[str])

slots.SYMBIONT_NAME = Slot(uri=DDL.SYMBIONT_NAME, name="SYMBIONT_NAME", curie=DDL.curie('SYMBIONT_NAME'),
                      model_uri=DDL.SYMBIONT_NAME, domain=None, range=Optional[str])

slots.SYMBIONT_TAXON_ID = Slot(uri=DDL.SYMBIONT_TAXON_ID, name="SYMBIONT_TAXON_ID", curie=DDL.curie('SYMBIONT_TAXON_ID'),
                      model_uri=DDL.SYMBIONT_TAXON_ID, domain=None, range=Optional[int])

slots.CELL_LENGTH = Slot(uri=DDL.CELL_LENGTH, name="CELL_LENGTH", curie=DDL.curie('CELL_LENGTH'),
                      model_uri=DDL.CELL_LENGTH, domain=None, range=Optional[str])

slots.COMMERCIAL = Slot(uri=DDL.COMMERCIAL, name="COMMERCIAL", curie=DDL.curie('COMMERCIAL'),
                      model_uri=DDL.COMMERCIAL, domain=None, range=Optional[str])

slots.COMMERCIAL_COMMENTS = Slot(uri=DDL.COMMERCIAL_COMMENTS, name="COMMERCIAL_COMMENTS", curie=DDL.curie('COMMERCIAL_COMMENTS'),
                      model_uri=DDL.COMMERCIAL_COMMENTS, domain=None, range=Optional[str])

slots.OTHER_NAMES = Slot(uri=DDL.OTHER_NAMES, name="OTHER_NAMES", curie=DDL.curie('OTHER_NAMES'),
                      model_uri=DDL.OTHER_NAMES, domain=None, range=Optional[str])

slots.SYNONYM_GROUP_ID = Slot(uri=DDL.SYNONYM_GROUP_ID, name="SYNONYM_GROUP_ID", curie=DDL.curie('SYNONYM_GROUP_ID'),
                      model_uri=DDL.SYNONYM_GROUP_ID, domain=None, range=Optional[int])

slots.VIRAL_GROUP = Slot(uri=DDL.VIRAL_GROUP, name="VIRAL_GROUP", curie=DDL.curie('VIRAL_GROUP'),
                      model_uri=DDL.VIRAL_GROUP, domain=None, range=Optional[str])

slots.VIRAL_SUBGROUP = Slot(uri=DDL.VIRAL_SUBGROUP, name="VIRAL_SUBGROUP", curie=DDL.curie('VIRAL_SUBGROUP'),
                      model_uri=DDL.VIRAL_SUBGROUP, domain=None, range=Optional[str])

slots.CULTURE_TYPE = Slot(uri=DDL.CULTURE_TYPE, name="CULTURE_TYPE", curie=DDL.curie('CULTURE_TYPE'),
                      model_uri=DDL.CULTURE_TYPE, domain=None, range=Optional[str])

slots.UNCULTURED_TYPE = Slot(uri=DDL.UNCULTURED_TYPE, name="UNCULTURED_TYPE", curie=DDL.curie('UNCULTURED_TYPE'),
                      model_uri=DDL.UNCULTURED_TYPE, domain=None, range=Optional[str])

slots.ORGANISM_TYPE = Slot(uri=DDL.ORGANISM_TYPE, name="ORGANISM_TYPE", curie=DDL.curie('ORGANISM_TYPE'),
                      model_uri=DDL.ORGANISM_TYPE, domain=None, range=Optional[str])

slots.CULTURED = Slot(uri=DDL.CULTURED, name="CULTURED", curie=DDL.curie('CULTURED'),
                      model_uri=DDL.CULTURED, domain=None, range=Optional[str])

slots.CLADE = Slot(uri=DDL.CLADE, name="CLADE", curie=DDL.curie('CLADE'),
                      model_uri=DDL.CLADE, domain=None, range=Optional[str])

slots.MASTER_GROUP_ID = Slot(uri=DDL.MASTER_GROUP_ID, name="MASTER_GROUP_ID", curie=DDL.curie('MASTER_GROUP_ID'),
                      model_uri=DDL.MASTER_GROUP_ID, domain=None, range=Optional[int])

slots.ECOTYPE = Slot(uri=DDL.ECOTYPE, name="ECOTYPE", curie=DDL.curie('ECOTYPE'),
                      model_uri=DDL.ECOTYPE, domain=None, range=Optional[str])

slots.BIOSAMPLE_ID = Slot(uri=DDL.BIOSAMPLE_ID, name="BIOSAMPLE_ID", curie=DDL.curie('BIOSAMPLE_ID'),
                      model_uri=DDL.BIOSAMPLE_ID, domain=None, range=Optional[int])

slots.CARBON_SOURCE = Slot(uri=DDL.CARBON_SOURCE, name="CARBON_SOURCE", curie=DDL.curie('CARBON_SOURCE'),
                      model_uri=DDL.CARBON_SOURCE, domain=None, range=Optional[str])

slots.IMAGE_ID = Slot(uri=DDL.IMAGE_ID, name="IMAGE_ID", curie=DDL.curie('IMAGE_ID'),
                      model_uri=DDL.IMAGE_ID, domain=None, range=Optional[int])

slots.NCBI_BIOSAMPLE_ID = Slot(uri=DDL.NCBI_BIOSAMPLE_ID, name="NCBI_BIOSAMPLE_ID", curie=DDL.curie('NCBI_BIOSAMPLE_ID'),
                      model_uri=DDL.NCBI_BIOSAMPLE_ID, domain=None, range=Optional[str])

slots.ORGANISM_NAME = Slot(uri=DDL.ORGANISM_NAME, name="ORGANISM_NAME", curie=DDL.curie('ORGANISM_NAME'),
                      model_uri=DDL.ORGANISM_NAME, domain=None, range=Optional[str])

slots.SUBMIT_ORGANISM_NAME = Slot(uri=DDL.SUBMIT_ORGANISM_NAME, name="SUBMIT_ORGANISM_NAME", curie=DDL.curie('SUBMIT_ORGANISM_NAME'),
                      model_uri=DDL.SUBMIT_ORGANISM_NAME, domain=None, range=Optional[str])

slots.GENUS_SYNONYMS = Slot(uri=DDL.GENUS_SYNONYMS, name="GENUS_SYNONYMS", curie=DDL.curie('GENUS_SYNONYMS'),
                      model_uri=DDL.GENUS_SYNONYMS, domain=None, range=Optional[str])

slots.SPECIES_SYNONYMS = Slot(uri=DDL.SPECIES_SYNONYMS, name="SPECIES_SYNONYMS", curie=DDL.curie('SPECIES_SYNONYMS'),
                      model_uri=DDL.SPECIES_SYNONYMS, domain=None, range=Optional[str])

slots.CELL_DIAMETER = Slot(uri=DDL.CELL_DIAMETER, name="CELL_DIAMETER", curie=DDL.curie('CELL_DIAMETER'),
                      model_uri=DDL.CELL_DIAMETER, domain=None, range=Optional[str])

slots.IS_VIROCELL = Slot(uri=DDL.IS_VIROCELL, name="IS_VIROCELL", curie=DDL.curie('IS_VIROCELL'),
                      model_uri=DDL.IS_VIROCELL, domain=None, range=Optional[str])

slots.STRAININFO_GROUP_ID = Slot(uri=DDL.STRAININFO_GROUP_ID, name="STRAININFO_GROUP_ID", curie=DDL.curie('STRAININFO_GROUP_ID'),
                      model_uri=DDL.STRAININFO_GROUP_ID, domain=None, range=Optional[int])

slots.SOURCE = Slot(uri=DDL.SOURCE, name="SOURCE", curie=DDL.curie('SOURCE'),
                      model_uri=DDL.SOURCE, domain=None, range=Optional[str])

slots.GOLD_CLASS = Slot(uri=DDL.GOLD_CLASS, name="GOLD_CLASS", curie=DDL.curie('GOLD_CLASS'),
                      model_uri=DDL.GOLD_CLASS, domain=None, range=Optional[str])

slots.GOLD_ORDER = Slot(uri=DDL.GOLD_ORDER, name="GOLD_ORDER", curie=DDL.curie('GOLD_ORDER'),
                      model_uri=DDL.GOLD_ORDER, domain=None, range=Optional[str])

slots.GOLD_FAMILY = Slot(uri=DDL.GOLD_FAMILY, name="GOLD_FAMILY", curie=DDL.curie('GOLD_FAMILY'),
                      model_uri=DDL.GOLD_FAMILY, domain=None, range=Optional[str])

slots.TAXONOMY_STATUS = Slot(uri=DDL.TAXONOMY_STATUS, name="TAXONOMY_STATUS", curie=DDL.curie('TAXONOMY_STATUS'),
                      model_uri=DDL.TAXONOMY_STATUS, domain=None, range=Optional[str])

slots.SOIL_SAMPLE_BIOMASS = Slot(uri=DDL.SOIL_SAMPLE_BIOMASS, name="SOIL_SAMPLE_BIOMASS", curie=DDL.curie('SOIL_SAMPLE_BIOMASS'),
                      model_uri=DDL.SOIL_SAMPLE_BIOMASS, domain=None, range=Optional[float])

slots.SOIL_SAMPLE_VOLUME = Slot(uri=DDL.SOIL_SAMPLE_VOLUME, name="SOIL_SAMPLE_VOLUME", curie=DDL.curie('SOIL_SAMPLE_VOLUME'),
                      model_uri=DDL.SOIL_SAMPLE_VOLUME, domain=None, range=Optional[float])

slots.IMG_BREADTH_CALC = Slot(uri=DDL.IMG_BREADTH_CALC, name="IMG_BREADTH_CALC", curie=DDL.curie('IMG_BREADTH_CALC'),
                      model_uri=DDL.IMG_BREADTH_CALC, domain=None, range=Optional[float])

slots.SAMPLE_COLLECTION_TEMPERATURE = Slot(uri=DDL.SAMPLE_COLLECTION_TEMPERATURE, name="SAMPLE_COLLECTION_TEMPERATURE", curie=DDL.curie('SAMPLE_COLLECTION_TEMPERATURE'),
                      model_uri=DDL.SAMPLE_COLLECTION_TEMPERATURE, domain=None, range=Optional[float])

slots.SAMPLE_COLLECTION_TEMPERATURE2 = Slot(uri=DDL.SAMPLE_COLLECTION_TEMPERATURE2, name="SAMPLE_COLLECTION_TEMPERATURE2", curie=DDL.curie('SAMPLE_COLLECTION_TEMPERATURE2'),
                      model_uri=DDL.SAMPLE_COLLECTION_TEMPERATURE2, domain=None, range=Optional[float])

slots.SUBSURFACE_DEPTH1 = Slot(uri=DDL.SUBSURFACE_DEPTH1, name="SUBSURFACE_DEPTH1", curie=DDL.curie('SUBSURFACE_DEPTH1'),
                      model_uri=DDL.SUBSURFACE_DEPTH1, domain=None, range=Optional[float])

slots.PROJECT_NAME = Slot(uri=DDL.PROJECT_NAME, name="PROJECT_NAME", curie=DDL.curie('PROJECT_NAME'),
                      model_uri=DDL.PROJECT_NAME, domain=None, range=Optional[str])

slots.SPECIMEN_ID = Slot(uri=DDL.SPECIMEN_ID, name="SPECIMEN_ID", curie=DDL.curie('SPECIMEN_ID'),
                      model_uri=DDL.SPECIMEN_ID, domain=None, range=Optional[int])

slots.NUCLEIC_ACID = Slot(uri=DDL.NUCLEIC_ACID, name="NUCLEIC_ACID", curie=DDL.curie('NUCLEIC_ACID'),
                      model_uri=DDL.NUCLEIC_ACID, domain=None, range=Optional[str])

slots.SUBMITTER_PROJECT_NAME = Slot(uri=DDL.SUBMITTER_PROJECT_NAME, name="SUBMITTER_PROJECT_NAME", curie=DDL.curie('SUBMITTER_PROJECT_NAME'),
                      model_uri=DDL.SUBMITTER_PROJECT_NAME, domain=None, range=Optional[str])

slots.NCBI_PROJECT_NAME = Slot(uri=DDL.NCBI_PROJECT_NAME, name="NCBI_PROJECT_NAME", curie=DDL.curie('NCBI_PROJECT_NAME'),
                      model_uri=DDL.NCBI_PROJECT_NAME, domain=None, range=Optional[str])

slots.PMO_PROJECT_ID = Slot(uri=DDL.PMO_PROJECT_ID, name="PMO_PROJECT_ID", curie=DDL.curie('PMO_PROJECT_ID'),
                      model_uri=DDL.PMO_PROJECT_ID, domain=None, range=Optional[int])

slots.ITS_SPID = Slot(uri=DDL.ITS_SPID, name="ITS_SPID", curie=DDL.curie('ITS_SPID'),
                      model_uri=DDL.ITS_SPID, domain=None, range=Optional[float])

slots.OLD_LEGACY_GOLD_ID = Slot(uri=DDL.OLD_LEGACY_GOLD_ID, name="OLD_LEGACY_GOLD_ID", curie=DDL.curie('OLD_LEGACY_GOLD_ID'),
                      model_uri=DDL.OLD_LEGACY_GOLD_ID, domain=None, range=Optional[str])

slots.LEGACY_GOLD_ID = Slot(uri=DDL.LEGACY_GOLD_ID, name="LEGACY_GOLD_ID", curie=DDL.curie('LEGACY_GOLD_ID'),
                      model_uri=DDL.LEGACY_GOLD_ID, domain=None, range=Optional[str])

slots.SEQUENCING_STATUS_ID = Slot(uri=DDL.SEQUENCING_STATUS_ID, name="SEQUENCING_STATUS_ID", curie=DDL.curie('SEQUENCING_STATUS_ID'),
                      model_uri=DDL.SEQUENCING_STATUS_ID, domain=None, range=Optional[int])

slots.SEQUENCING_QUALITY_ID = Slot(uri=DDL.SEQUENCING_QUALITY_ID, name="SEQUENCING_QUALITY_ID", curie=DDL.curie('SEQUENCING_QUALITY_ID'),
                      model_uri=DDL.SEQUENCING_QUALITY_ID, domain=None, range=Optional[int])

slots.FINISHING_GOAL_ID = Slot(uri=DDL.FINISHING_GOAL_ID, name="FINISHING_GOAL_ID", curie=DDL.curie('FINISHING_GOAL_ID'),
                      model_uri=DDL.FINISHING_GOAL_ID, domain=None, range=Optional[int])

slots.SEQUENCING_COMMENTS = Slot(uri=DDL.SEQUENCING_COMMENTS, name="SEQUENCING_COMMENTS", curie=DDL.curie('SEQUENCING_COMMENTS'),
                      model_uri=DDL.SEQUENCING_COMMENTS, domain=None, range=Optional[str])

slots.GC_PERCENT = Slot(uri=DDL.GC_PERCENT, name="GC_PERCENT", curie=DDL.curie('GC_PERCENT'),
                      model_uri=DDL.GC_PERCENT, domain=None, range=Optional[float])

slots.CHROMOSOME_COUNT = Slot(uri=DDL.CHROMOSOME_COUNT, name="CHROMOSOME_COUNT", curie=DDL.curie('CHROMOSOME_COUNT'),
                      model_uri=DDL.CHROMOSOME_COUNT, domain=None, range=Optional[float])

slots.PLASMID_COUNT = Slot(uri=DDL.PLASMID_COUNT, name="PLASMID_COUNT", curie=DDL.curie('PLASMID_COUNT'),
                      model_uri=DDL.PLASMID_COUNT, domain=None, range=Optional[float])

slots.EST_COUNT = Slot(uri=DDL.EST_COUNT, name="EST_COUNT", curie=DDL.curie('EST_COUNT'),
                      model_uri=DDL.EST_COUNT, domain=None, range=Optional[float])

slots.PROJECT_COMMENTS = Slot(uri=DDL.PROJECT_COMMENTS, name="PROJECT_COMMENTS", curie=DDL.curie('PROJECT_COMMENTS'),
                      model_uri=DDL.PROJECT_COMMENTS, domain=None, range=Optional[str])

slots.ITS_PROPOSAL_ID = Slot(uri=DDL.ITS_PROPOSAL_ID, name="ITS_PROPOSAL_ID", curie=DDL.curie('ITS_PROPOSAL_ID'),
                      model_uri=DDL.ITS_PROPOSAL_ID, domain=None, range=Optional[int])

slots.GPTS_PROPOSAL_ID = Slot(uri=DDL.GPTS_PROPOSAL_ID, name="GPTS_PROPOSAL_ID", curie=DDL.curie('GPTS_PROPOSAL_ID'),
                      model_uri=DDL.GPTS_PROPOSAL_ID, domain=None, range=Optional[int])

slots.NCBI_SRA_ID = Slot(uri=DDL.NCBI_SRA_ID, name="NCBI_SRA_ID", curie=DDL.curie('NCBI_SRA_ID'),
                      model_uri=DDL.NCBI_SRA_ID, domain=None, range=Optional[str])

slots.LIBRARY_METHOD = Slot(uri=DDL.LIBRARY_METHOD, name="LIBRARY_METHOD", curie=DDL.curie('LIBRARY_METHOD'),
                      model_uri=DDL.LIBRARY_METHOD, domain=None, range=Optional[str])

slots.READ_COUNT = Slot(uri=DDL.READ_COUNT, name="READ_COUNT", curie=DDL.curie('READ_COUNT'),
                      model_uri=DDL.READ_COUNT, domain=None, range=Optional[str])

slots.VECTOR = Slot(uri=DDL.VECTOR, name="VECTOR", curie=DDL.curie('VECTOR'),
                      model_uri=DDL.VECTOR, domain=None, range=Optional[str])

slots.READ_SIZE = Slot(uri=DDL.READ_SIZE, name="READ_SIZE", curie=DDL.curie('READ_SIZE'),
                      model_uri=DDL.READ_SIZE, domain=None, range=Optional[str])

slots.NCBI_LOCUS_TAG = Slot(uri=DDL.NCBI_LOCUS_TAG, name="NCBI_LOCUS_TAG", curie=DDL.curie('NCBI_LOCUS_TAG'),
                      model_uri=DDL.NCBI_LOCUS_TAG, domain=None, range=Optional[str])

slots.ASSEMBLY_ACCESSION = Slot(uri=DDL.ASSEMBLY_ACCESSION, name="ASSEMBLY_ACCESSION", curie=DDL.curie('ASSEMBLY_ACCESSION'),
                      model_uri=DDL.ASSEMBLY_ACCESSION, domain=None, range=Optional[str])

slots.NUCLEIC_ACID_ID = Slot(uri=DDL.NUCLEIC_ACID_ID, name="NUCLEIC_ACID_ID", curie=DDL.curie('NUCLEIC_ACID_ID'),
                      model_uri=DDL.NUCLEIC_ACID_ID, domain=None, range=Optional[int])

slots.PROJECT_STATUS = Slot(uri=DDL.PROJECT_STATUS, name="PROJECT_STATUS", curie=DDL.curie('PROJECT_STATUS'),
                      model_uri=DDL.PROJECT_STATUS, domain=None, range=Optional[str])

slots.MASTER_STUDY_ID = Slot(uri=DDL.MASTER_STUDY_ID, name="MASTER_STUDY_ID", curie=DDL.curie('MASTER_STUDY_ID'),
                      model_uri=DDL.MASTER_STUDY_ID, domain=None, range=Optional[int])

slots.OTHER_PROJECT_NAMES = Slot(uri=DDL.OTHER_PROJECT_NAMES, name="OTHER_PROJECT_NAMES", curie=DDL.curie('OTHER_PROJECT_NAMES'),
                      model_uri=DDL.OTHER_PROJECT_NAMES, domain=None, range=Optional[str])

slots.ITS_PROJECT_NAME = Slot(uri=DDL.ITS_PROJECT_NAME, name="ITS_PROJECT_NAME", curie=DDL.curie('ITS_PROJECT_NAME'),
                      model_uri=DDL.ITS_PROJECT_NAME, domain=None, range=Optional[str])

slots.IS_SINGLE_CELL_MATERIAL = Slot(uri=DDL.IS_SINGLE_CELL_MATERIAL, name="IS_SINGLE_CELL_MATERIAL", curie=DDL.curie('IS_SINGLE_CELL_MATERIAL'),
                      model_uri=DDL.IS_SINGLE_CELL_MATERIAL, domain=None, range=Optional[str])

slots.ITS_SEQUENCING_PRODUCT_NAME = Slot(uri=DDL.ITS_SEQUENCING_PRODUCT_NAME, name="ITS_SEQUENCING_PRODUCT_NAME", curie=DDL.curie('ITS_SEQUENCING_PRODUCT_NAME'),
                      model_uri=DDL.ITS_SEQUENCING_PRODUCT_NAME, domain=None, range=Optional[str])

slots.PROJECT_MANAGER_ID = Slot(uri=DDL.PROJECT_MANAGER_ID, name="PROJECT_MANAGER_ID", curie=DDL.curie('PROJECT_MANAGER_ID'),
                      model_uri=DDL.PROJECT_MANAGER_ID, domain=None, range=Optional[int])

slots.LOW_QUALITY_GENOME = Slot(uri=DDL.LOW_QUALITY_GENOME, name="LOW_QUALITY_GENOME", curie=DDL.curie('LOW_QUALITY_GENOME'),
                      model_uri=DDL.LOW_QUALITY_GENOME, domain=None, range=Optional[str])

slots.SEQUENCING_STRATEGY = Slot(uri=DDL.SEQUENCING_STRATEGY, name="SEQUENCING_STRATEGY", curie=DDL.curie('SEQUENCING_STRATEGY'),
                      model_uri=DDL.SEQUENCING_STRATEGY, domain=None, range=Optional[str])

slots.IS_JGI = Slot(uri=DDL.IS_JGI, name="IS_JGI", curie=DDL.curie('IS_JGI'),
                      model_uri=DDL.IS_JGI, domain=None, range=Optional[str])

slots.SRA_SRS_ACCESSION = Slot(uri=DDL.SRA_SRS_ACCESSION, name="SRA_SRS_ACCESSION", curie=DDL.curie('SRA_SRS_ACCESSION'),
                      model_uri=DDL.SRA_SRS_ACCESSION, domain=None, range=Optional[str])

slots.SRA_SRX_ACCESSION = Slot(uri=DDL.SRA_SRX_ACCESSION, name="SRA_SRX_ACCESSION", curie=DDL.curie('SRA_SRX_ACCESSION'),
                      model_uri=DDL.SRA_SRX_ACCESSION, domain=None, range=Optional[str])

slots.FUNDING_PROGRAM = Slot(uri=DDL.FUNDING_PROGRAM, name="FUNDING_PROGRAM", curie=DDL.curie('FUNDING_PROGRAM'),
                      model_uri=DDL.FUNDING_PROGRAM, domain=None, range=Optional[str])

slots.FUNDING_YEAR = Slot(uri=DDL.FUNDING_YEAR, name="FUNDING_YEAR", curie=DDL.curie('FUNDING_YEAR'),
                      model_uri=DDL.FUNDING_YEAR, domain=None, range=Optional[float])

slots.ITS_SAMPLE_ID = Slot(uri=DDL.ITS_SAMPLE_ID, name="ITS_SAMPLE_ID", curie=DDL.curie('ITS_SAMPLE_ID'),
                      model_uri=DDL.ITS_SAMPLE_ID, domain=None, range=Optional[int])

slots.ITS_SAMPLE_GROUP_NAME = Slot(uri=DDL.ITS_SAMPLE_GROUP_NAME, name="ITS_SAMPLE_GROUP_NAME", curie=DDL.curie('ITS_SAMPLE_GROUP_NAME'),
                      model_uri=DDL.ITS_SAMPLE_GROUP_NAME, domain=None, range=Optional[str])

slots.EXPERIMENTAL_CONDITIONS = Slot(uri=DDL.EXPERIMENTAL_CONDITIONS, name="EXPERIMENTAL_CONDITIONS", curie=DDL.curie('EXPERIMENTAL_CONDITIONS'),
                      model_uri=DDL.EXPERIMENTAL_CONDITIONS, domain=None, range=Optional[str])

slots.SAMPLE_GROUP_NAME = Slot(uri=DDL.SAMPLE_GROUP_NAME, name="SAMPLE_GROUP_NAME", curie=DDL.curie('SAMPLE_GROUP_NAME'),
                      model_uri=DDL.SAMPLE_GROUP_NAME, domain=None, range=Optional[str])

slots.ITS_SAMPLE_NAME = Slot(uri=DDL.ITS_SAMPLE_NAME, name="ITS_SAMPLE_NAME", curie=DDL.curie('ITS_SAMPLE_NAME'),
                      model_uri=DDL.ITS_SAMPLE_NAME, domain=None, range=Optional[str])

slots.PROJECT_SUBTYPE = Slot(uri=DDL.PROJECT_SUBTYPE, name="PROJECT_SUBTYPE", curie=DDL.curie('PROJECT_SUBTYPE'),
                      model_uri=DDL.PROJECT_SUBTYPE, domain=None, range=Optional[str])

slots.SEQUENCING_STRATEGY_FULL = Slot(uri=DDL.SEQUENCING_STRATEGY_FULL, name="SEQUENCING_STRATEGY_FULL", curie=DDL.curie('SEQUENCING_STRATEGY_FULL'),
                      model_uri=DDL.SEQUENCING_STRATEGY_FULL, domain=None, range=Optional[str])

slots.IS_APPROVED = Slot(uri=DDL.IS_APPROVED, name="IS_APPROVED", curie=DDL.curie('IS_APPROVED'),
                      model_uri=DDL.IS_APPROVED, domain=None, range=Optional[str])

slots.IS_LOCKED = Slot(uri=DDL.IS_LOCKED, name="IS_LOCKED", curie=DDL.curie('IS_LOCKED'),
                      model_uri=DDL.IS_LOCKED, domain=None, range=Optional[str])

slots.GPTS_SAMPLE_ID = Slot(uri=DDL.GPTS_SAMPLE_ID, name="GPTS_SAMPLE_ID", curie=DDL.curie('GPTS_SAMPLE_ID'),
                      model_uri=DDL.GPTS_SAMPLE_ID, domain=None, range=Optional[int])

slots.GPTS_DISAMBIGUATOR = Slot(uri=DDL.GPTS_DISAMBIGUATOR, name="GPTS_DISAMBIGUATOR", curie=DDL.curie('GPTS_DISAMBIGUATOR'),
                      model_uri=DDL.GPTS_DISAMBIGUATOR, domain=None, range=Optional[str])

slots.ANALYSIS_PROJECT_ID = Slot(uri=DDL.ANALYSIS_PROJECT_ID, name="ANALYSIS_PROJECT_ID", curie=DDL.curie('ANALYSIS_PROJECT_ID'),
                      model_uri=DDL.ANALYSIS_PROJECT_ID, domain=None, range=Optional[int])

slots.INSTITUTION_ID = Slot(uri=DDL.INSTITUTION_ID, name="INSTITUTION_ID", curie=DDL.curie('INSTITUTION_ID'),
                      model_uri=DDL.INSTITUTION_ID, domain=None, range=Optional[int])

slots.PUBLICATION_ID = Slot(uri=DDL.PUBLICATION_ID, name="PUBLICATION_ID", curie=DDL.curie('PUBLICATION_ID'),
                      model_uri=DDL.PUBLICATION_ID, domain=None, range=Optional[int])

slots.RELEVANCE_ID = Slot(uri=DDL.RELEVANCE_ID, name="RELEVANCE_ID", curie=DDL.curie('RELEVANCE_ID'),
                      model_uri=DDL.RELEVANCE_ID, domain=None, range=Optional[int])

slots.SEQUENCING_METHOD_ID = Slot(uri=DDL.SEQUENCING_METHOD_ID, name="SEQUENCING_METHOD_ID", curie=DDL.curie('SEQUENCING_METHOD_ID'),
                      model_uri=DDL.SEQUENCING_METHOD_ID, domain=None, range=Optional[int])

slots.DOI = Slot(uri=DDL.DOI, name="DOI", curie=DDL.curie('DOI'),
                      model_uri=DDL.DOI, domain=None, range=Optional[str])

slots.PUBMED_ID = Slot(uri=DDL.PUBMED_ID, name="PUBMED_ID", curie=DDL.curie('PUBMED_ID'),
                      model_uri=DDL.PUBMED_ID, domain=None, range=Optional[int])

slots.JOURNAL_ID = Slot(uri=DDL.JOURNAL_ID, name="JOURNAL_ID", curie=DDL.curie('JOURNAL_ID'),
                      model_uri=DDL.JOURNAL_ID, domain=None, range=Optional[int])

slots.PUBMODEL = Slot(uri=DDL.PUBMODEL, name="PUBMODEL", curie=DDL.curie('PUBMODEL'),
                      model_uri=DDL.PUBMODEL, domain=None, range=Optional[str])

slots.VOLUME = Slot(uri=DDL.VOLUME, name="VOLUME", curie=DDL.curie('VOLUME'),
                      model_uri=DDL.VOLUME, domain=None, range=Optional[str])

slots.ISSUE = Slot(uri=DDL.ISSUE, name="ISSUE", curie=DDL.curie('ISSUE'),
                      model_uri=DDL.ISSUE, domain=None, range=Optional[str])

slots.PAGE = Slot(uri=DDL.PAGE, name="PAGE", curie=DDL.curie('PAGE'),
                      model_uri=DDL.PAGE, domain=None, range=Optional[str])

slots.PUBLICATION_DATE = Slot(uri=DDL.PUBLICATION_DATE, name="PUBLICATION_DATE", curie=DDL.curie('PUBLICATION_DATE'),
                      model_uri=DDL.PUBLICATION_DATE, domain=None, range=Optional[str])

slots.ABSTRACT = Slot(uri=DDL.ABSTRACT, name="ABSTRACT", curie=DDL.curie('ABSTRACT'),
                      model_uri=DDL.ABSTRACT, domain=None, range=Optional[str])

slots.AFFILIATION = Slot(uri=DDL.AFFILIATION, name="AFFILIATION", curie=DDL.curie('AFFILIATION'),
                      model_uri=DDL.AFFILIATION, domain=None, range=Optional[str])

slots.LAST_AUTHOR_ID = Slot(uri=DDL.LAST_AUTHOR_ID, name="LAST_AUTHOR_ID", curie=DDL.curie('LAST_AUTHOR_ID'),
                      model_uri=DDL.LAST_AUTHOR_ID, domain=None, range=Optional[int])

slots.FIRST_AUTHOR_ID = Slot(uri=DDL.FIRST_AUTHOR_ID, name="FIRST_AUTHOR_ID", curie=DDL.curie('FIRST_AUTHOR_ID'),
                      model_uri=DDL.FIRST_AUTHOR_ID, domain=None, range=Optional[int])

slots.STUDY_NAME = Slot(uri=DDL.STUDY_NAME, name="STUDY_NAME", curie=DDL.curie('STUDY_NAME'),
                      model_uri=DDL.STUDY_NAME, domain=None, range=Optional[str])

slots.NCBI_PROJECT_ID = Slot(uri=DDL.NCBI_PROJECT_ID, name="NCBI_PROJECT_ID", curie=DDL.curie('NCBI_PROJECT_ID'),
                      model_uri=DDL.NCBI_PROJECT_ID, domain=None, range=Optional[int])

slots.CONTACT_ID = Slot(uri=DDL.CONTACT_ID, name="CONTACT_ID", curie=DDL.curie('CONTACT_ID'),
                      model_uri=DDL.CONTACT_ID, domain=None, range=Optional[int])

slots.LAST_MOD_BY = Slot(uri=DDL.LAST_MOD_BY, name="LAST_MOD_BY", curie=DDL.curie('LAST_MOD_BY'),
                      model_uri=DDL.LAST_MOD_BY, domain=None, range=Optional[float])

slots.BIOPROJECT_NAME = Slot(uri=DDL.BIOPROJECT_NAME, name="BIOPROJECT_NAME", curie=DDL.curie('BIOPROJECT_NAME'),
                      model_uri=DDL.BIOPROJECT_NAME, domain=None, range=Optional[str])

slots.GOLD_STUDY_NAME = Slot(uri=DDL.GOLD_STUDY_NAME, name="GOLD_STUDY_NAME", curie=DDL.curie('GOLD_STUDY_NAME'),
                      model_uri=DDL.GOLD_STUDY_NAME, domain=None, range=Optional[str])

slots.METAGENOMIC = Slot(uri=DDL.METAGENOMIC, name="METAGENOMIC", curie=DDL.curie('METAGENOMIC'),
                      model_uri=DDL.METAGENOMIC, domain=None, range=Optional[str])

slots.STUDY_TYPE_ID = Slot(uri=DDL.STUDY_TYPE_ID, name="STUDY_TYPE_ID", curie=DDL.curie('STUDY_TYPE_ID'),
                      model_uri=DDL.STUDY_TYPE_ID, domain=None, range=Optional[int])

slots.OWNER_ID = Slot(uri=DDL.OWNER_ID, name="OWNER_ID", curie=DDL.curie('OWNER_ID'),
                      model_uri=DDL.OWNER_ID, domain=None, range=Optional[int])

slots.PUBLIC_BIOSAMPLE_COUNT = Slot(uri=DDL.PUBLIC_BIOSAMPLE_COUNT, name="PUBLIC_BIOSAMPLE_COUNT", curie=DDL.curie('PUBLIC_BIOSAMPLE_COUNT'),
                      model_uri=DDL.PUBLIC_BIOSAMPLE_COUNT, domain=None, range=Optional[float])

slots.ADMIN_BIOSAMPLE_COUNT = Slot(uri=DDL.ADMIN_BIOSAMPLE_COUNT, name="ADMIN_BIOSAMPLE_COUNT", curie=DDL.curie('ADMIN_BIOSAMPLE_COUNT'),
                      model_uri=DDL.ADMIN_BIOSAMPLE_COUNT, domain=None, range=Optional[float])

slots.IS_GEBA = Slot(uri=DDL.IS_GEBA, name="IS_GEBA", curie=DDL.curie('IS_GEBA'),
                      model_uri=DDL.IS_GEBA, domain=None, range=Optional[str])

slots.IS_HMP = Slot(uri=DDL.IS_HMP, name="IS_HMP", curie=DDL.curie('IS_HMP'),
                      model_uri=DDL.IS_HMP, domain=None, range=Optional[str])
