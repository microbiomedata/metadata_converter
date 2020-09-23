# Auto generated from gold.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-07-04 19:08
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
class AnalysisProject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.AnalysisProject
    class_class_curie: ClassVar[str] = "ddl:AnalysisProject"
    class_name: ClassVar[str] = "analysis_project"
    class_model_uri: ClassVar[URIRef] = DDL.AnalysisProject

    its_analysis_project_id: Optional[int] = None
    analysis_project_name: Optional[str] = None
    reference_ap_id: Optional[int] = None
    img_taxon_id: Optional[int] = None
    analysis_project_type: Optional[str] = None
    status_id: Optional[int] = None
    ncbi_tax_id: Optional[int] = None
    added_by: Optional[float] = None
    submission_id: Optional[int] = None
    gene_count: Optional[float] = None
    binning_method: Optional[str] = None
    gene_calling_method: Optional[str] = None
    its_analysis_project_name: Optional[str] = None
    its_product_name: Optional[str] = None
    genbank_low_quality_annotation: Optional[str] = None
    img_analysis_complete: Optional[str] = None
    is_gene_primp: Optional[str] = None
    is_decontamination: Optional[str] = None
    is_img_annotation: Optional[str] = None
    its_annotation_at_id: Optional[int] = None
    is_assembled_deleted: Optional[str] = None
    study_id: Optional[int] = None
    its_assembly_at_type: Optional[str] = None
    appended_ap_name: Optional[str] = None
    pi_name: Optional[str] = None
    analysis_project_name_full: Optional[str] = None
    is_primary: Optional[str] = None
    phylogeny_suggestion: Optional[str] = None
    replaces_ap_id: Optional[int] = None
    screening_method: Optional[str] = None
    decontamination_method: Optional[str] = None
    completion: Optional[str] = None
    review_status: Optional[str] = None
    rejection_reasons: Optional[str] = None
    pipeline_annotation_method: Optional[str] = None
    culture_collection: Optional[str] = None
    sequencing_depth: Optional[str] = None
    img_use: Optional[str] = None
    ap_for_nonowner: Optional[str] = None
    its_ncbi_tax_id: Optional[int] = None
    its_version_number: Optional[float] = None
    img_rnaseq_id: Optional[int] = None
    submission_status_id: Optional[int] = None
    submission_status_name: Optional[str] = None
    submission_comments: Optional[str] = None
    img_submission_prority: Optional[str] = None
    contamination_percentage: Optional[float] = None
    completeness_percentage: Optional[float] = None

@dataclass
class AnalysisProjectSraRunV2(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.AnalysisProjectSraRunV2
    class_class_curie: ClassVar[str] = "ddl:AnalysisProjectSraRunV2"
    class_name: ClassVar[str] = "analysis_project_sra_run_v2"
    class_model_uri: ClassVar[URIRef] = DDL.AnalysisProjectSraRunV2

    sra_run_id: Optional[str] = None

@dataclass
class Biosample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Biosample
    class_class_curie: ClassVar[str] = "ddl:Biosample"
    class_name: ClassVar[str] = "biosample"
    class_model_uri: ClassVar[URIRef] = DDL.Biosample

    biosample_name: Optional[str] = None
    habitat: Optional[str] = None
    community: Optional[str] = None
    location: Optional[str] = None
    identifier: Optional[str] = None
    jpa_entity: Optional[str] = None
    biogas_fed_substrates: Optional[str] = None
    biogas_retention_time: Optional[str] = None
    biogas_temperature: Optional[str] = None
    biogas_yield: Optional[str] = None
    biogas_volatile_organic_acids: Optional[str] = None
    biogas_total_inorganic_carbon: Optional[str] = None
    biogas_voa_tic: Optional[str] = None
    biogas_ammonium_nh4: Optional[str] = None
    biogas_butanol: Optional[str] = None
    biogas_ethanol: Optional[str] = None
    biogas_propanol: Optional[str] = None
    biogas_methanol: Optional[str] = None
    biogas_acetic_acid: Optional[str] = None
    biogas_butyl_acid: Optional[str] = None
    biogas_iso_butyl_acid: Optional[str] = None
    biogas_valeric_acid: Optional[str] = None
    biogas_iso_valeric_acid: Optional[str] = None
    biogas_propionic_acid: Optional[str] = None
    biogas_methane_pct: Optional[float] = None
    oxygen_presence: Optional[str] = None
    test_package_id: Optional[int] = None
    global_package_id: Optional[int] = None

@dataclass
class Contact(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Contact
    class_class_curie: ClassVar[str] = "ddl:Contact"
    class_name: ClassVar[str] = "contact"
    class_model_uri: ClassVar[URIRef] = DDL.Contact

    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    x_super_user: Optional[str] = None
    x_img_editor: Optional[str] = None
    x_img_group: Optional[float] = None
    jgi_user: Optional[str] = None
    x_img_editing_level: Optional[str] = None
    caliban_id: Optional[int] = None
    caliban_user_name: Optional[str] = None
    x_img_contact_id: Optional[int] = None
    master_contact_id: Optional[int] = None
    oracle_user_name: Optional[str] = None
    user_role: Optional[str] = None
    geba_organism_avail_count: Optional[float] = None
    geba_reviewer: Optional[str] = None

class CvapCompletion(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvapCompletion
    class_class_curie: ClassVar[str] = "ddl:CvapCompletion"
    class_name: ClassVar[str] = "cvap_completion"
    class_model_uri: ClassVar[URIRef] = DDL.CvapCompletion


class CvapReviewStatus(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvapReviewStatus
    class_class_curie: ClassVar[str] = "ddl:CvapReviewStatus"
    class_name: ClassVar[str] = "cvap_review_status"
    class_model_uri: ClassVar[URIRef] = DDL.CvapReviewStatus


class CvapStatus(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvapStatus
    class_class_curie: ClassVar[str] = "ddl:CvapStatus"
    class_name: ClassVar[str] = "cvap_status"
    class_model_uri: ClassVar[URIRef] = DDL.CvapStatus


class CvapType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvapType
    class_class_curie: ClassVar[str] = "ddl:CvapType"
    class_name: ClassVar[str] = "cvap_type"
    class_model_uri: ClassVar[URIRef] = DDL.CvapType


class Cvavailability(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvavailability
    class_class_curie: ClassVar[str] = "ddl:Cvavailability"
    class_name: ClassVar[str] = "cvavailability"
    class_model_uri: ClassVar[URIRef] = DDL.Cvavailability


class Cvbiome(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvbiome
    class_class_curie: ClassVar[str] = "ddl:Cvbiome"
    class_name: ClassVar[str] = "cvbiome"
    class_model_uri: ClassVar[URIRef] = DDL.Cvbiome


class Cvbiosafety(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvbiosafety
    class_class_curie: ClassVar[str] = "ddl:Cvbiosafety"
    class_name: ClassVar[str] = "cvbiosafety"
    class_model_uri: ClassVar[URIRef] = DDL.Cvbiosafety


class CvbioticRelationship(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvbioticRelationship
    class_class_curie: ClassVar[str] = "ddl:CvbioticRelationship"
    class_name: ClassVar[str] = "cvbiotic_relationship"
    class_model_uri: ClassVar[URIRef] = DDL.CvbioticRelationship


class CvbodyProduct(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvbodyProduct
    class_class_curie: ClassVar[str] = "ddl:CvbodyProduct"
    class_name: ClassVar[str] = "cvbody_product"
    class_model_uri: ClassVar[URIRef] = DDL.CvbodyProduct


class CvbodySite(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvbodySite
    class_class_curie: ClassVar[str] = "ddl:CvbodySite"
    class_name: ClassVar[str] = "cvbody_site"
    class_model_uri: ClassVar[URIRef] = DDL.CvbodySite


class CvbodySubsite(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvbodySubsite
    class_class_curie: ClassVar[str] = "ddl:CvbodySubsite"
    class_name: ClassVar[str] = "cvbody_subsite"
    class_model_uri: ClassVar[URIRef] = DDL.CvbodySubsite


class CvcellArrangement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvcellArrangement
    class_class_curie: ClassVar[str] = "ddl:CvcellArrangement"
    class_name: ClassVar[str] = "cvcell_arrangement"
    class_model_uri: ClassVar[URIRef] = DDL.CvcellArrangement


class CvcellShape(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvcellShape
    class_class_curie: ClassVar[str] = "ddl:CvcellShape"
    class_name: ClassVar[str] = "cvcell_shape"
    class_model_uri: ClassVar[URIRef] = DDL.CvcellShape


class Cvcolor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvcolor
    class_class_curie: ClassVar[str] = "ddl:Cvcolor"
    class_name: ClassVar[str] = "cvcolor"
    class_model_uri: ClassVar[URIRef] = DDL.Cvcolor


class Cvcountry(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvcountry
    class_class_curie: ClassVar[str] = "ddl:Cvcountry"
    class_name: ClassVar[str] = "cvcountry"
    class_model_uri: ClassVar[URIRef] = DDL.Cvcountry


class CvcultureType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvcultureType
    class_class_curie: ClassVar[str] = "ddl:CvcultureType"
    class_name: ClassVar[str] = "cvculture_type"
    class_model_uri: ClassVar[URIRef] = DDL.CvcultureType


class CvcurrentLandUse(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvcurrentLandUse
    class_class_curie: ClassVar[str] = "ddl:CvcurrentLandUse"
    class_name: ClassVar[str] = "cvcurrent_land_use"
    class_model_uri: ClassVar[URIRef] = DDL.CvcurrentLandUse


class CvdataValidityType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvdataValidityType
    class_class_curie: ClassVar[str] = "ddl:CvdataValidityType"
    class_name: ClassVar[str] = "cvdata_validity_type"
    class_model_uri: ClassVar[URIRef] = DDL.CvdataValidityType


class Cvdisease(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvdisease
    class_class_curie: ClassVar[str] = "ddl:Cvdisease"
    class_name: ClassVar[str] = "cvdisease"
    class_model_uri: ClassVar[URIRef] = DDL.Cvdisease


class Cvdomain(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvdomain
    class_class_curie: ClassVar[str] = "ddl:Cvdomain"
    class_name: ClassVar[str] = "cvdomain"
    class_model_uri: ClassVar[URIRef] = DDL.Cvdomain


class CvdrainageClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvdrainageClass
    class_class_curie: ClassVar[str] = "ddl:CvdrainageClass"
    class_name: ClassVar[str] = "cvdrainage_class"
    class_model_uri: ClassVar[URIRef] = DDL.CvdrainageClass


class CvenergySource(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvenergySource
    class_class_curie: ClassVar[str] = "ddl:CvenergySource"
    class_name: ClassVar[str] = "cvenergy_source"
    class_model_uri: ClassVar[URIRef] = DDL.CvenergySource


class Cvenvpackage(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvenvpackage
    class_class_curie: ClassVar[str] = "ddl:Cvenvpackage"
    class_name: ClassVar[str] = "cvenvpackage"
    class_model_uri: ClassVar[URIRef] = DDL.Cvenvpackage


class Cvfastadownloadstatus(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvfastadownloadstatus
    class_class_curie: ClassVar[str] = "ddl:Cvfastadownloadstatus"
    class_name: ClassVar[str] = "cvfastadownloadstatus"
    class_model_uri: ClassVar[URIRef] = DDL.Cvfastadownloadstatus


class CvfinishingGoal(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvfinishingGoal
    class_class_curie: ClassVar[str] = "ddl:CvfinishingGoal"
    class_name: ClassVar[str] = "cvfinishing_goal"
    class_model_uri: ClassVar[URIRef] = DDL.CvfinishingGoal


class CvgebaPriorityStatus(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvgebaPriorityStatus
    class_class_curie: ClassVar[str] = "ddl:CvgebaPriorityStatus"
    class_name: ClassVar[str] = "cvgeba_priority_status"
    class_model_uri: ClassVar[URIRef] = DDL.CvgebaPriorityStatus


class CvgebaReviewStatus(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvgebaReviewStatus
    class_class_curie: ClassVar[str] = "ddl:CvgebaReviewStatus"
    class_name: ClassVar[str] = "cvgeba_review_status"
    class_model_uri: ClassVar[URIRef] = DDL.CvgebaReviewStatus


class CvgebaSampleType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvgebaSampleType
    class_class_curie: ClassVar[str] = "ddl:CvgebaSampleType"
    class_name: ClassVar[str] = "cvgeba_sample_type"
    class_model_uri: ClassVar[URIRef] = DDL.CvgebaSampleType


class CvgebaTypes(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvgebaTypes
    class_class_curie: ClassVar[str] = "ddl:CvgebaTypes"
    class_name: ClassVar[str] = "cvgeba_types"
    class_model_uri: ClassVar[URIRef] = DDL.CvgebaTypes


class CvgramStain(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvgramStain
    class_class_curie: ClassVar[str] = "ddl:CvgramStain"
    class_name: ClassVar[str] = "cvgram_stain"
    class_model_uri: ClassVar[URIRef] = DDL.CvgramStain


class Cvhabitat(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvhabitat
    class_class_curie: ClassVar[str] = "ddl:Cvhabitat"
    class_name: ClassVar[str] = "cvhabitat"
    class_model_uri: ClassVar[URIRef] = DDL.Cvhabitat


class Cvhorizon(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvhorizon
    class_class_curie: ClassVar[str] = "ddl:Cvhorizon"
    class_name: ClassVar[str] = "cvhorizon"
    class_model_uri: ClassVar[URIRef] = DDL.Cvhorizon


class CvhostGender(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvhostGender
    class_class_curie: ClassVar[str] = "ddl:CvhostGender"
    class_name: ClassVar[str] = "cvhost_gender"
    class_model_uri: ClassVar[URIRef] = DDL.CvhostGender


class Cvimguse(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvimguse
    class_class_curie: ClassVar[str] = "ddl:Cvimguse"
    class_name: ClassVar[str] = "cvimguse"
    class_model_uri: ClassVar[URIRef] = DDL.Cvimguse


class Cvirradiance(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvirradiance
    class_class_curie: ClassVar[str] = "ddl:Cvirradiance"
    class_name: ClassVar[str] = "cvirradiance"
    class_model_uri: ClassVar[URIRef] = DDL.Cvirradiance


class Cvlatlong(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvlatlong
    class_class_curie: ClassVar[str] = "ddl:Cvlatlong"
    class_name: ClassVar[str] = "cvlatlong"
    class_model_uri: ClassVar[URIRef] = DDL.Cvlatlong


class Cvmetabolism(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvmetabolism
    class_class_curie: ClassVar[str] = "ddl:Cvmetabolism"
    class_name: ClassVar[str] = "cvmetabolism"
    class_model_uri: ClassVar[URIRef] = DDL.Cvmetabolism


class Cvmodel(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvmodel
    class_class_curie: ClassVar[str] = "ddl:Cvmodel"
    class_name: ClassVar[str] = "cvmodel"
    class_model_uri: ClassVar[URIRef] = DDL.Cvmodel


class Cvmonth(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvmonth
    class_class_curie: ClassVar[str] = "ddl:Cvmonth"
    class_name: ClassVar[str] = "cvmonth"
    class_model_uri: ClassVar[URIRef] = DDL.Cvmonth


class Cvmotility(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvmotility
    class_class_curie: ClassVar[str] = "ddl:Cvmotility"
    class_name: ClassVar[str] = "cvmotility"
    class_model_uri: ClassVar[URIRef] = DDL.Cvmotility


class CvnucleicAcid(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvnucleicAcid
    class_class_curie: ClassVar[str] = "ddl:CvnucleicAcid"
    class_name: ClassVar[str] = "cvnucleic_acid"
    class_model_uri: ClassVar[URIRef] = DDL.CvnucleicAcid


class CvorganismType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvorganismType
    class_class_curie: ClassVar[str] = "ddl:CvorganismType"
    class_name: ClassVar[str] = "cvorganism_type"
    class_model_uri: ClassVar[URIRef] = DDL.CvorganismType


class Cvoxygen(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvoxygen
    class_class_curie: ClassVar[str] = "ddl:Cvoxygen"
    class_name: ClassVar[str] = "cvoxygen"
    class_model_uri: ClassVar[URIRef] = DDL.Cvoxygen


class CvoxygenPresence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvoxygenPresence
    class_class_curie: ClassVar[str] = "ddl:CvoxygenPresence"
    class_name: ClassVar[str] = "cvoxygen_presence"
    class_model_uri: ClassVar[URIRef] = DDL.CvoxygenPresence


class CvoxygenStatSample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvoxygenStatSample
    class_class_curie: ClassVar[str] = "ddl:CvoxygenStatSample"
    class_name: ClassVar[str] = "cvoxygen_stat_sample"
    class_model_uri: ClassVar[URIRef] = DDL.CvoxygenStatSample


class Cvpackages(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvpackages
    class_class_curie: ClassVar[str] = "ddl:Cvpackages"
    class_name: ClassVar[str] = "cvpackages"
    class_model_uri: ClassVar[URIRef] = DDL.Cvpackages


class Cvphenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvphenotype
    class_class_curie: ClassVar[str] = "ddl:Cvphenotype"
    class_name: ClassVar[str] = "cvphenotype"
    class_model_uri: ClassVar[URIRef] = DDL.Cvphenotype


class Cvphylogeny(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvphylogeny
    class_class_curie: ClassVar[str] = "ddl:Cvphylogeny"
    class_name: ClassVar[str] = "cvphylogeny"
    class_model_uri: ClassVar[URIRef] = DDL.Cvphylogeny


class CvprofilePosition(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvprofilePosition
    class_class_curie: ClassVar[str] = "ddl:CvprofilePosition"
    class_name: ClassVar[str] = "cvprofile_position"
    class_model_uri: ClassVar[URIRef] = DDL.CvprofilePosition


class CvprojectStatus(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvprojectStatus
    class_class_curie: ClassVar[str] = "ddl:CvprojectStatus"
    class_name: ClassVar[str] = "cvproject_status"
    class_model_uri: ClassVar[URIRef] = DDL.CvprojectStatus


class CvprojectSubtype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvprojectSubtype
    class_class_curie: ClassVar[str] = "ddl:CvprojectSubtype"
    class_name: ClassVar[str] = "cvproject_subtype"
    class_model_uri: ClassVar[URIRef] = DDL.CvprojectSubtype


class CvprojectType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvprojectType
    class_class_curie: ClassVar[str] = "ddl:CvprojectType"
    class_name: ClassVar[str] = "cvproject_type"
    class_model_uri: ClassVar[URIRef] = DDL.CvprojectType


class Cvrelevance(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvrelevance
    class_class_curie: ClassVar[str] = "ddl:Cvrelevance"
    class_name: ClassVar[str] = "cvrelevance"
    class_model_uri: ClassVar[URIRef] = DDL.Cvrelevance


class Cvroles(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvroles
    class_class_curie: ClassVar[str] = "ddl:Cvroles"
    class_name: ClassVar[str] = "cvroles"
    class_model_uri: ClassVar[URIRef] = DDL.Cvroles


class Cvsalinity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvsalinity
    class_class_curie: ClassVar[str] = "ddl:Cvsalinity"
    class_name: ClassVar[str] = "cvsalinity"
    class_model_uri: ClassVar[URIRef] = DDL.Cvsalinity


class CvseqQuality(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvseqQuality
    class_class_curie: ClassVar[str] = "ddl:CvseqQuality"
    class_name: ClassVar[str] = "cvseq_quality"
    class_model_uri: ClassVar[URIRef] = DDL.CvseqQuality


class CvseqStatus(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvseqStatus
    class_class_curie: ClassVar[str] = "ddl:CvseqStatus"
    class_name: ClassVar[str] = "cvseq_status"
    class_model_uri: ClassVar[URIRef] = DDL.CvseqStatus


class Cvsoilfaoclass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvsoilfaoclass
    class_class_curie: ClassVar[str] = "ddl:Cvsoilfaoclass"
    class_name: ClassVar[str] = "cvsoilfaoclass"
    class_model_uri: ClassVar[URIRef] = DDL.Cvsoilfaoclass


class Cvspecimen(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvspecimen
    class_class_curie: ClassVar[str] = "ddl:Cvspecimen"
    class_name: ClassVar[str] = "cvspecimen"
    class_model_uri: ClassVar[URIRef] = DDL.Cvspecimen


class Cvsporulation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvsporulation
    class_class_curie: ClassVar[str] = "ddl:Cvsporulation"
    class_name: ClassVar[str] = "cvsporulation"
    class_model_uri: ClassVar[URIRef] = DDL.Cvsporulation


class CvstudyType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvstudyType
    class_class_curie: ClassVar[str] = "ddl:CvstudyType"
    class_name: ClassVar[str] = "cvstudy_type"
    class_model_uri: ClassVar[URIRef] = DDL.CvstudyType


class CvtempRange(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvtempRange
    class_class_curie: ClassVar[str] = "ddl:CvtempRange"
    class_name: ClassVar[str] = "cvtemp_range"
    class_model_uri: ClassVar[URIRef] = DDL.CvtempRange


class CvtidalStage(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvtidalStage
    class_class_curie: ClassVar[str] = "ddl:CvtidalStage"
    class_name: ClassVar[str] = "cvtidal_stage"
    class_model_uri: ClassVar[URIRef] = DDL.CvtidalStage


class Cvtillage(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Cvtillage
    class_class_curie: ClassVar[str] = "ddl:Cvtillage"
    class_name: ClassVar[str] = "cvtillage"
    class_model_uri: ClassVar[URIRef] = DDL.Cvtillage


class CvunculturedType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvunculturedType
    class_class_curie: ClassVar[str] = "ddl:CvunculturedType"
    class_name: ClassVar[str] = "cvuncultured_type"
    class_model_uri: ClassVar[URIRef] = DDL.CvunculturedType


class CvyesNo(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvyesNo
    class_class_curie: ClassVar[str] = "ddl:CvyesNo"
    class_name: ClassVar[str] = "cvyes_no"
    class_model_uri: ClassVar[URIRef] = DDL.CvyesNo


@dataclass
class CvyesNoOnly(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.CvyesNoOnly
    class_class_curie: ClassVar[str] = "ddl:CvyesNoOnly"
    class_name: ClassVar[str] = "cvyes_no_only"
    class_model_uri: ClassVar[URIRef] = DDL.CvyesNoOnly

    term: Optional[str] = None
    sequence: Optional[float] = None

@dataclass
class EnvoLabels(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.EnvoLabels
    class_class_curie: ClassVar[str] = "ddl:EnvoLabels"
    class_name: ClassVar[str] = "envo_labels"
    class_model_uri: ClassVar[URIRef] = DDL.EnvoLabels

    envo_label: Optional[str] = None

@dataclass
class Institution(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Institution
    class_class_curie: ClassVar[str] = "ddl:Institution"
    class_name: ClassVar[str] = "institution"
    class_model_uri: ClassVar[URIRef] = DDL.Institution

    name: Optional[str] = None
    url: Optional[str] = None
    country: Optional[str] = None
    organization: Optional[str] = None
    department: Optional[str] = None
    laboratory: Optional[str] = None
    is_curated: Optional[str] = None

@dataclass
class OrganismBioticRel(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.OrganismBioticRel
    class_class_curie: ClassVar[str] = "ddl:OrganismBioticRel"
    class_name: ClassVar[str] = "organism_biotic_rel"
    class_model_uri: ClassVar[URIRef] = DDL.OrganismBioticRel

    biotic_relationship_id: Optional[int] = None

@dataclass
class OrganismBodyProduct(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.OrganismBodyProduct
    class_class_curie: ClassVar[str] = "ddl:OrganismBodyProduct"
    class_name: ClassVar[str] = "organism_body_product"
    class_model_uri: ClassVar[URIRef] = DDL.OrganismBodyProduct

    body_product_id: Optional[int] = None

@dataclass
class OrganismCellArrangement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.OrganismCellArrangement
    class_class_curie: ClassVar[str] = "ddl:OrganismCellArrangement"
    class_name: ClassVar[str] = "organism_cell_arrangement"
    class_model_uri: ClassVar[URIRef] = DDL.OrganismCellArrangement

    cell_arrangement_id: Optional[int] = None

@dataclass
class OrganismDisease(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.OrganismDisease
    class_class_curie: ClassVar[str] = "ddl:OrganismDisease"
    class_name: ClassVar[str] = "organism_disease"
    class_model_uri: ClassVar[URIRef] = DDL.OrganismDisease

    disease_id: Optional[int] = None

@dataclass
class OrganismEnergySource(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.OrganismEnergySource
    class_class_curie: ClassVar[str] = "ddl:OrganismEnergySource"
    class_name: ClassVar[str] = "organism_energy_source"
    class_model_uri: ClassVar[URIRef] = DDL.OrganismEnergySource

    energy_source_id: Optional[int] = None

@dataclass
class OrganismHabitat(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.OrganismHabitat
    class_class_curie: ClassVar[str] = "ddl:OrganismHabitat"
    class_name: ClassVar[str] = "organism_habitat"
    class_model_uri: ClassVar[URIRef] = DDL.OrganismHabitat

    habitat_id: Optional[int] = None

@dataclass
class OrganismMetabolism(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.OrganismMetabolism
    class_class_curie: ClassVar[str] = "ddl:OrganismMetabolism"
    class_name: ClassVar[str] = "organism_metabolism"
    class_model_uri: ClassVar[URIRef] = DDL.OrganismMetabolism

    metabolism_id: Optional[int] = None

@dataclass
class OrganismPhenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.OrganismPhenotype
    class_class_curie: ClassVar[str] = "ddl:OrganismPhenotype"
    class_name: ClassVar[str] = "organism_phenotype"
    class_model_uri: ClassVar[URIRef] = DDL.OrganismPhenotype

    phenotype_id: Optional[int] = None

@dataclass
class OrganismV2(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.OrganismV2
    class_class_curie: ClassVar[str] = "ddl:OrganismV2"
    class_name: ClassVar[str] = "organism_v2"
    class_model_uri: ClassVar[URIRef] = DDL.OrganismV2

    exemplar_doi: Optional[str] = None
    exemplar_name: Optional[str] = None
    taxon_doi: Optional[str] = None
    culture_collection_id: Optional[str] = None
    type_strain: Optional[str] = None
    biosafety_level: Optional[str] = None
    ncbi_taxonomy_id: Optional[int] = None
    ncbi_kingdom: Optional[str] = None
    ncbi_phylum: Optional[str] = None
    ncbi_class: Optional[str] = None
    ncbi_order: Optional[str] = None
    ncbi_family: Optional[str] = None
    ncbi_genus: Optional[str] = None
    domain: Optional[str] = None
    strain_info_id: Optional[int] = None
    genbank_16s_id: Optional[str] = None
    oxygen_requirement: Optional[str] = None
    cell_shape: Optional[str] = None
    motility: Optional[str] = None
    sporulation: Optional[str] = None
    temperature_range: Optional[str] = None
    color: Optional[str] = None
    gram_stain: Optional[str] = None
    common_name: Optional[str] = None
    symbiotic_relationship: Optional[str] = None
    symbiotic_physical_interaction: Optional[str] = None
    symbiont_name: Optional[str] = None
    symbiont_taxon_id: Optional[int] = None
    cell_length: Optional[str] = None
    subspecies: Optional[str] = None
    commercial: Optional[str] = None
    commercial_comments: Optional[str] = None
    other_names: Optional[str] = None
    synonym_group_id: Optional[int] = None
    viral_group: Optional[str] = None
    viral_subgroup: Optional[str] = None
    gold_phylogeny: Optional[str] = None
    culture_type: Optional[str] = None
    uncultured_type: Optional[str] = None
    cultured: Optional[str] = None
    clade: Optional[str] = None
    master_group_id: Optional[int] = None
    ecotype: Optional[str] = None
    carbon_source: Optional[str] = None
    image_id: Optional[int] = None
    ncbi_biosample_id: Optional[str] = None
    other_ecosystem: Optional[str] = None
    sample_collection_site: Optional[str] = None
    sample_isolation_comments: Optional[str] = None
    sampling_strategy: Optional[str] = None
    replicate_number: Optional[float] = None
    sample_volume: Optional[str] = None
    sample_biomass: Optional[str] = None
    sample_contact_name: Optional[str] = None
    sample_contact_email: Optional[str] = None
    geographic_location: Optional[str] = None
    lat_long_inferred: Optional[str] = None
    host_name: Optional[str] = None
    host_taxonomy_id: Optional[int] = None
    host_gender: Optional[str] = None
    host_race: Optional[str] = None
    host_age: Optional[str] = None
    host_health_condition: Optional[str] = None
    patient_visit_number: Optional[float] = None
    host_medication: Optional[str] = None
    mrn: Optional[str] = None
    host_body_site: Optional[str] = None
    host_body_subsite: Optional[str] = None
    host_body_product: Optional[str] = None
    host_specificity: Optional[str] = None
    host_comments: Optional[str] = None
    specimen: Optional[str] = None
    submit_biosample_name: Optional[str] = None
    env_package: Optional[str] = None
    sample_collection_day: Optional[float] = None
    sample_collection_month: Optional[float] = None
    sample_collection_year: Optional[float] = None
    sample_collection_hour: Optional[float] = None
    sample_collection_minute: Optional[float] = None
    growth_conditions: Optional[str] = None
    other_hosts: Optional[str] = None
    known_non_hosts: Optional[str] = None
    isolation_pubmed_id: Optional[int] = None
    host_body_site_id: Optional[int] = None
    host_body_subsite_id: Optional[int] = None
    host_body_product_id: Optional[int] = None
    sample_isolation_country_id: Optional[int] = None
    longhurst_code: Optional[str] = None
    chlorophyll_concentration: Optional[str] = None
    nitrate_concentration: Optional[str] = None
    oxygen_concentration: Optional[str] = None
    salinity_concentration: Optional[str] = None
    cruise_line_name: Optional[str] = None
    proport_ocean: Optional[str] = None
    proport_isolation: Optional[str] = None
    proport_station: Optional[str] = None
    proport_woa_temperature: Optional[float] = None
    proport_woa_salinity: Optional[float] = None
    proport_woa_dissolved_oxygen: Optional[float] = None
    proport_woa_silicate: Optional[float] = None
    proport_woa_phosphate: Optional[float] = None
    proport_woa_nitrate: Optional[float] = None
    its_growth_conditions: Optional[str] = None
    organism_name: Optional[str] = None
    submit_organism_name: Optional[str] = None
    ncbi_taxonomy_name: Optional[str] = None
    genus: Optional[str] = None
    genus_synonyms: Optional[str] = None
    species: Optional[str] = None
    species_synonyms: Optional[str] = None
    strain: Optional[str] = None
    serovar: Optional[str] = None
    comments: Optional[str] = None
    ncbi_species: Optional[str] = None
    salinity: Optional[str] = None
    pressure: Optional[str] = None
    ph: Optional[str] = None
    cell_diameter: Optional[str] = None
    is_virocell: Optional[str] = None
    straininfo_group_id: Optional[int] = None
    source: Optional[str] = None
    gold_class: Optional[str] = None
    gold_order: Optional[str] = None
    gold_family: Optional[str] = None
    ncbi_superkingdom: Optional[str] = None
    taxonomy_status: Optional[str] = None
    growth_temperature: Optional[float] = None
    subsurface_depth: Optional[float] = None
    legacy_depth_data: Optional[str] = None
    latitude_test: Optional[float] = None
    longitude_test: Optional[float] = None
    elevation: Optional[float] = None
    elevation2: Optional[float] = None
    soil_curr_land_use: Optional[str] = None
    soil_curr_vegetation: Optional[str] = None
    soil_curr_vegetation_method: Optional[str] = None
    soil_prev_land_use: Optional[str] = None
    soil_prev_land_use_meth: Optional[str] = None
    soil_crop_rotation: Optional[str] = None
    soil_agrochem_addition: Optional[str] = None
    soil_tillage: Optional[str] = None
    soil_fire: Optional[str] = None
    soil_flooding: Optional[str] = None
    soil_extreme_event: Optional[str] = None
    soil_horizon: Optional[str] = None
    soil_horizon_method: Optional[str] = None
    soil_sieving: Optional[str] = None
    soil_water_content: Optional[str] = None
    soil_water_content_soil_meth: Optional[str] = None
    sample_weight_dna_ext: Optional[str] = None
    soil_pool_dna_extracts: Optional[str] = None
    soil_storage_condition: Optional[str] = None
    soil_link_climate_info: Optional[str] = None
    soil_link_class_info: Optional[str] = None
    soil_fao_class: Optional[str] = None
    soil_local_class: Optional[str] = None
    soil_local_class_method: Optional[str] = None
    soil_type: Optional[str] = None
    soil_type_method: Optional[str] = None
    soil_slope_gradient: Optional[float] = None
    soil_slope_aspect: Optional[float] = None
    soil_profile_position: Optional[str] = None
    soil_drainage_class: Optional[str] = None
    soil_texture: Optional[str] = None
    soil_texture_method: Optional[str] = None
    soil_ph_method: Optional[str] = None
    tot_org_carbon: Optional[float] = None
    soil_tot_org_c_method: Optional[str] = None
    tot_nitrogen: Optional[str] = None
    soil_tot_n_method: Optional[str] = None
    soil_microbial_biomass: Optional[str] = None
    soil_microbial_biomass_method: Optional[str] = None
    soil_link_addit_analys: Optional[str] = None
    soil_salinity_method: Optional[str] = None
    soil_heavy_metals: Optional[float] = None
    soil_heavy_metals_method: Optional[str] = None
    soil_aluminium_sat: Optional[float] = None
    soil_aluminium_sat_method: Optional[str] = None
    soil_misc_param: Optional[str] = None
    water_alkalinity: Optional[float] = None
    water_alkyl_diethers: Optional[float] = None
    water_aminopept_act: Optional[float] = None
    water_ammonium: Optional[float] = None
    water_atmospheric_data: Optional[str] = None
    water_bacterial_prod: Optional[float] = None
    water_bacterial_resp: Optional[float] = None
    water_bacterial_carbon_prod: Optional[float] = None
    water_bishomohopanol: Optional[str] = None
    water_bromide: Optional[float] = None
    water_calcium: Optional[str] = None
    water_carbon_nitrog_ratio: Optional[str] = None
    water_chem_administration: Optional[str] = None
    water_chloride: Optional[float] = None
    water_density: Optional[float] = None
    water_diether_lipids: Optional[float] = None
    water_diss_carbon_dioxide: Optional[float] = None
    water_diss_hydrogen: Optional[float] = None
    water_diss_inorg_carbon: Optional[float] = None
    water_diss_inorg_nitro: Optional[float] = None
    water_diss_inorg_phosphorus: Optional[float] = None
    water_diss_org_carbon: Optional[float] = None
    water_diss_org_nitrogen: Optional[float] = None
    water_downward_par: Optional[float] = None
    water_fluorescence: Optional[float] = None
    water_glucosidase_activity: Optional[float] = None
    water_light_intensity: Optional[float] = None
    water_magnesium: Optional[str] = None
    water_mean_frict_vel: Optional[float] = None
    water_mean_peak_frict_vel: Optional[float] = None
    water_misc_parameter: Optional[str] = None
    water_n_alkanes: Optional[float] = None
    water_nitrite: Optional[float] = None
    water_org_matter: Optional[float] = None
    water_org_nitrogen: Optional[float] = None
    water_organism_count: Optional[float] = None
    water_oxy_stat_sample: Optional[str] = None
    water_part_org_carbon: Optional[float] = None
    water_part_org_nitrogen: Optional[float] = None
    water_perturbation: Optional[str] = None
    water_petroleum_hydrocarbon: Optional[float] = None
    water_phaeopigments: Optional[float] = None
    water_phosplipid_fatt_acid: Optional[str] = None
    water_photon_flux: Optional[float] = None
    water_potassium: Optional[float] = None
    water_primary_prod: Optional[float] = None
    water_redox_potential: Optional[float] = None
    water_samp_store_dur: Optional[str] = None
    water_samp_store_loc: Optional[str] = None
    water_samp_store_temp: Optional[float] = None
    water_sodium: Optional[float] = None
    water_soluble_react_phosp: Optional[float] = None
    water_sulfate: Optional[str] = None
    water_sulfide: Optional[str] = None
    water_suspend_part_matter: Optional[float] = None
    water_tidal_stage: Optional[str] = None
    water_tot_depth_water_col: Optional[float] = None
    water_tot_diss_nitro: Optional[float] = None
    water_tot_inorg_nitro: Optional[float] = None
    water_tot_part_carbon: Optional[str] = None
    water_tot_phosphorus: Optional[float] = None
    water_current: Optional[str] = None
    altitude: Optional[float] = None
    altitude2: Optional[float] = None
    depth: Optional[float] = None
    depth2: Optional[float] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    bicarbonate_millimol: Optional[float] = None
    soluble_iron_micromol: Optional[float] = None
    h2s_millimol: Optional[float] = None
    h2s_present: Optional[str] = None
    irradiance: Optional[str] = None
    methane_conc_millimol: Optional[float] = None
    sample_conductivity: Optional[str] = None
    soil_sample_biomass: Optional[float] = None
    soil_sample_volume: Optional[float] = None
    img_breadth_calc: Optional[float] = None
    growth_temperature2: Optional[float] = None
    sample_collection_temperature: Optional[float] = None
    sample_collection_temperature2: Optional[float] = None
    subsurface_depth1: Optional[float] = None
    subsurface_depth2: Optional[float] = None
    ph1: Optional[float] = None
    ph2: Optional[float] = None
    ph_old: Optional[str] = None
    water_alkalinity_method: Optional[str] = None
    water_turbidity: Optional[str] = None
    water_size_frac_low: Optional[float] = None
    water_size_frac_up: Optional[float] = None
    soil_mean_annual_temp: Optional[float] = None
    soil_mean_seasonal_temp: Optional[float] = None
    soil_mean_annual_precpt: Optional[float] = None
    soil_mean_seasonal_precpt: Optional[float] = None
    soil_package_id: Optional[int] = None
    water_package_id: Optional[int] = None
    envo_biome_id: Optional[str] = None
    envo_feature_id: Optional[str] = None
    envo_material_id: Optional[str] = None

@dataclass
class Project(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Project
    class_class_curie: ClassVar[str] = "ddl:Project"
    class_name: ClassVar[str] = "project"
    class_model_uri: ClassVar[URIRef] = DDL.Project

    project_name: Optional[str] = None
    ncbi_bioproject_id: Optional[int] = None
    mod_by: Optional[float] = None
    specimen_id: Optional[int] = None
    organism_type: Optional[str] = None
    nucleic_acid: Optional[str] = None
    submitter_project_name: Optional[str] = None
    ncbi_project_name: Optional[str] = None
    isolation_publication_id: Optional[int] = None
    completion_date: Optional[Union[str, XSDTime]] = None
    pmo_project_id: Optional[int] = None
    its_spid: Optional[float] = None
    sample_oid: Optional[float] = None
    old_legacy_gold_id: Optional[str] = None
    organism_id: Optional[int] = None
    sequencing_status_id: Optional[int] = None
    sequencing_quality_id: Optional[int] = None
    finishing_goal_id: Optional[int] = None
    sequencing_comments: Optional[str] = None
    gc_percent: Optional[float] = None
    contig_count: Optional[float] = None
    est_size: Optional[float] = None
    chromosome_count: Optional[float] = None
    plasmid_count: Optional[float] = None
    scaffold_count: Optional[float] = None
    est_count: Optional[float] = None
    submitter_id: Optional[int] = None
    ncbi_bioproject_accession: Optional[str] = None
    project_comments: Optional[str] = None
    annotator_comments: Optional[str] = None
    ncbi_sra_id: Optional[str] = None
    library_method: Optional[str] = None
    read_count: Optional[str] = None
    vector: Optional[str] = None
    read_size: Optional[str] = None
    ncbi_locus_tag: Optional[str] = None
    assembly_accession: Optional[str] = None
    nucleic_acid_id: Optional[int] = None
    pi_id: Optional[int] = None
    project_status: Optional[str] = None
    master_study_id: Optional[int] = None
    other_project_names: Optional[str] = None
    its_project_name: Optional[str] = None
    is_single_cell_material: Optional[str] = None
    its_sequencing_product_name: Optional[str] = None
    project_manager_id: Optional[int] = None
    ncbi_biosample_accession: Optional[str] = None
    low_quality_genome: Optional[str] = None
    sequencing_strategy: Optional[str] = None
    is_jgi: Optional[str] = None
    sra_srs_accession: Optional[str] = None
    sra_srx_accession: Optional[str] = None
    funding_program: Optional[str] = None
    funding_year: Optional[float] = None
    its_sample_id: Optional[int] = None
    its_sample_group_name: Optional[str] = None
    experimental_conditions: Optional[str] = None
    sample_group_name: Optional[str] = None
    its_sample_name: Optional[str] = None
    project_subtype: Optional[str] = None
    sequencing_strategy_full: Optional[str] = None
    is_approved: Optional[str] = None
    is_locked: Optional[str] = None
    gpts_sample_id: Optional[int] = None
    gpts_disambiguator: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.completion_date is not None and not isinstance(self.completion_date, XSDTime):
            self.completion_date = XSDTime(self.completion_date)
        super().__post_init__(**kwargs)


@dataclass
class ProjectAnalysisProject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ProjectAnalysisProject
    class_class_curie: ClassVar[str] = "ddl:ProjectAnalysisProject"
    class_name: ClassVar[str] = "project_analysis_project"
    class_model_uri: ClassVar[URIRef] = DDL.ProjectAnalysisProject

    analysis_project_id: Optional[int] = None

@dataclass
class ProjectBiosample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ProjectBiosample
    class_class_curie: ClassVar[str] = "ddl:ProjectBiosample"
    class_name: ClassVar[str] = "project_biosample"
    class_model_uri: ClassVar[URIRef] = DDL.ProjectBiosample

    biosample_id: Optional[int] = None

class ProjectCollaborator(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ProjectCollaborator
    class_class_curie: ClassVar[str] = "ddl:ProjectCollaborator"
    class_name: ClassVar[str] = "project_collaborator"
    class_model_uri: ClassVar[URIRef] = DDL.ProjectCollaborator


class ProjectFundingAgency(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ProjectFundingAgency
    class_class_curie: ClassVar[str] = "ddl:ProjectFundingAgency"
    class_name: ClassVar[str] = "project_funding_agency"
    class_model_uri: ClassVar[URIRef] = DDL.ProjectFundingAgency


class ProjectGenomePublication(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ProjectGenomePublication
    class_class_curie: ClassVar[str] = "ddl:ProjectGenomePublication"
    class_name: ClassVar[str] = "project_genome_publication"
    class_model_uri: ClassVar[URIRef] = DDL.ProjectGenomePublication


@dataclass
class ProjectOtherPublication(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ProjectOtherPublication
    class_class_curie: ClassVar[str] = "ddl:ProjectOtherPublication"
    class_name: ClassVar[str] = "project_other_publication"
    class_model_uri: ClassVar[URIRef] = DDL.ProjectOtherPublication

    publication_id: Optional[int] = None

@dataclass
class ProjectRelevance(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ProjectRelevance
    class_class_curie: ClassVar[str] = "ddl:ProjectRelevance"
    class_name: ClassVar[str] = "project_relevance"
    class_model_uri: ClassVar[URIRef] = DDL.ProjectRelevance

    relevance_id: Optional[int] = None

@dataclass
class ProjectSequencingCenter(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ProjectSequencingCenter
    class_class_curie: ClassVar[str] = "ddl:ProjectSequencingCenter"
    class_name: ClassVar[str] = "project_sequencing_center"
    class_model_uri: ClassVar[URIRef] = DDL.ProjectSequencingCenter

    institution_id: Optional[int] = None

@dataclass
class ProjectSequencingMethod(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.ProjectSequencingMethod
    class_class_curie: ClassVar[str] = "ddl:ProjectSequencingMethod"
    class_name: ClassVar[str] = "project_sequencing_method"
    class_model_uri: ClassVar[URIRef] = DDL.ProjectSequencingMethod

    sequencing_method_id: Optional[int] = None

@dataclass
class Publication(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Publication
    class_class_curie: ClassVar[str] = "ddl:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = DDL.Publication

    doi: Optional[str] = None
    pubmed_id: Optional[int] = None
    journal_id: Optional[int] = None
    pubmodel: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    page: Optional[str] = None
    publication_date: Optional[str] = None
    abstract: Optional[str] = None
    affiliation: Optional[str] = None
    title: Optional[str] = None
    last_author_id: Optional[int] = None
    first_author_id: Optional[int] = None

@dataclass
class Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DDL.Study
    class_class_curie: ClassVar[str] = "ddl:Study"
    class_name: ClassVar[str] = "study"
    class_model_uri: ClassVar[URIRef] = DDL.Study

    study_name: Optional[str] = None
    its_proposal_id: Optional[int] = None
    ncbi_project_id: Optional[int] = None
    add_date: Optional[Union[str, XSDTime]] = None
    mod_date: Optional[Union[str, XSDTime]] = None
    contact_id: Optional[int] = None
    last_mod_by: Optional[float] = None
    is_public: Optional[str] = None
    gpts_proposal_id: Optional[int] = None
    project_oid: Optional[float] = None
    active: Optional[str] = None
    legacy_gold_id: Optional[str] = None
    bioproject_name: Optional[str] = None
    gold_study_name: Optional[str] = None
    description: Optional[str] = None
    gold_id: Optional[str] = None
    metagenomic: Optional[str] = None
    study_type_id: Optional[int] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_type: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    owner_id: Optional[int] = None
    is_draft: Optional[str] = None
    public_sp_count: Optional[float] = None
    admin_sp_count: Optional[float] = None
    public_ap_count: Optional[float] = None
    admin_ap_count: Optional[float] = None
    public_dap_count: Optional[float] = None
    admin_dap_count: Optional[float] = None
    public_biosample_count: Optional[float] = None
    admin_biosample_count: Optional[float] = None
    is_geba: Optional[str] = None
    is_hmp: Optional[str] = None
    ecosystem_path_id: Optional[int] = None
    is_test: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.add_date is not None and not isinstance(self.add_date, XSDTime):
            self.add_date = XSDTime(self.add_date)
        if self.mod_date is not None and not isinstance(self.mod_date, XSDTime):
            self.mod_date = XSDTime(self.mod_date)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.its_analysis_project_id = Slot(uri=DDL.its_analysis_project_id, name="its_analysis_project_id", curie=DDL.curie('its_analysis_project_id'),
                      model_uri=DDL.its_analysis_project_id, domain=None, range=Optional[int])

slots.analysis_project_name = Slot(uri=DDL.analysis_project_name, name="analysis_project_name", curie=DDL.curie('analysis_project_name'),
                      model_uri=DDL.analysis_project_name, domain=None, range=Optional[str])

slots.gold_id = Slot(uri=DDL.gold_id, name="gold_id", curie=DDL.curie('gold_id'),
                      model_uri=DDL.gold_id, domain=None, range=Optional[str])

slots.reference_ap_id = Slot(uri=DDL.reference_ap_id, name="reference_ap_id", curie=DDL.curie('reference_ap_id'),
                      model_uri=DDL.reference_ap_id, domain=None, range=Optional[int])

slots.img_taxon_id = Slot(uri=DDL.img_taxon_id, name="img_taxon_id", curie=DDL.curie('img_taxon_id'),
                      model_uri=DDL.img_taxon_id, domain=None, range=Optional[int])

slots.analysis_project_type = Slot(uri=DDL.analysis_project_type, name="analysis_project_type", curie=DDL.curie('analysis_project_type'),
                      model_uri=DDL.analysis_project_type, domain=None, range=Optional[str])

slots.status_id = Slot(uri=DDL.status_id, name="status_id", curie=DDL.curie('status_id'),
                      model_uri=DDL.status_id, domain=None, range=Optional[int])

slots.comments = Slot(uri=DDL.comments, name="comments", curie=DDL.curie('comments'),
                      model_uri=DDL.comments, domain=None, range=Optional[str])

slots.ncbi_tax_id = Slot(uri=DDL.ncbi_tax_id, name="ncbi_tax_id", curie=DDL.curie('ncbi_tax_id'),
                      model_uri=DDL.ncbi_tax_id, domain=None, range=Optional[int])

slots.is_public = Slot(uri=DDL.is_public, name="is_public", curie=DDL.curie('is_public'),
                      model_uri=DDL.is_public, domain=None, range=Optional[str])

slots.added_by = Slot(uri=DDL.added_by, name="added_by", curie=DDL.curie('added_by'),
                      model_uri=DDL.added_by, domain=None, range=Optional[float])

slots.add_date = Slot(uri=DDL.add_date, name="add_date", curie=DDL.curie('add_date'),
                      model_uri=DDL.add_date, domain=None, range=Optional[Union[str, XSDTime]])

slots.pi_id = Slot(uri=DDL.pi_id, name="pi_id", curie=DDL.curie('pi_id'),
                      model_uri=DDL.pi_id, domain=None, range=Optional[int])

slots.submission_id = Slot(uri=DDL.submission_id, name="submission_id", curie=DDL.curie('submission_id'),
                      model_uri=DDL.submission_id, domain=None, range=Optional[int])

slots.scaffold_count = Slot(uri=DDL.scaffold_count, name="scaffold_count", curie=DDL.curie('scaffold_count'),
                      model_uri=DDL.scaffold_count, domain=None, range=Optional[float])

slots.contig_count = Slot(uri=DDL.contig_count, name="contig_count", curie=DDL.curie('contig_count'),
                      model_uri=DDL.contig_count, domain=None, range=Optional[float])

slots.gene_count = Slot(uri=DDL.gene_count, name="gene_count", curie=DDL.curie('gene_count'),
                      model_uri=DDL.gene_count, domain=None, range=Optional[float])

slots.binning_method = Slot(uri=DDL.binning_method, name="binning_method", curie=DDL.curie('binning_method'),
                      model_uri=DDL.binning_method, domain=None, range=Optional[str])

slots.gene_calling_method = Slot(uri=DDL.gene_calling_method, name="gene_calling_method", curie=DDL.curie('gene_calling_method'),
                      model_uri=DDL.gene_calling_method, domain=None, range=Optional[str])

slots.its_analysis_project_name = Slot(uri=DDL.its_analysis_project_name, name="its_analysis_project_name", curie=DDL.curie('its_analysis_project_name'),
                      model_uri=DDL.its_analysis_project_name, domain=None, range=Optional[str])

slots.its_product_name = Slot(uri=DDL.its_product_name, name="its_product_name", curie=DDL.curie('its_product_name'),
                      model_uri=DDL.its_product_name, domain=None, range=Optional[str])

slots.completion_date = Slot(uri=DDL.completion_date, name="completion_date", curie=DDL.curie('completion_date'),
                      model_uri=DDL.completion_date, domain=None, range=Optional[Union[str, XSDTime]])

slots.est_size = Slot(uri=DDL.est_size, name="est_size", curie=DDL.curie('est_size'),
                      model_uri=DDL.est_size, domain=None, range=Optional[float])

slots.genbank_low_quality_annotation = Slot(uri=DDL.genbank_low_quality_annotation, name="genbank_low_quality_annotation", curie=DDL.curie('genbank_low_quality_annotation'),
                      model_uri=DDL.genbank_low_quality_annotation, domain=None, range=Optional[str])

slots.ecosystem = Slot(uri=DDL.ecosystem, name="ecosystem", curie=DDL.curie('ecosystem'),
                      model_uri=DDL.ecosystem, domain=None, range=Optional[str])

slots.ecosystem_category = Slot(uri=DDL.ecosystem_category, name="ecosystem_category", curie=DDL.curie('ecosystem_category'),
                      model_uri=DDL.ecosystem_category, domain=None, range=Optional[str])

slots.ecosystem_type = Slot(uri=DDL.ecosystem_type, name="ecosystem_type", curie=DDL.curie('ecosystem_type'),
                      model_uri=DDL.ecosystem_type, domain=None, range=Optional[str])

slots.ecosystem_subtype = Slot(uri=DDL.ecosystem_subtype, name="ecosystem_subtype", curie=DDL.curie('ecosystem_subtype'),
                      model_uri=DDL.ecosystem_subtype, domain=None, range=Optional[str])

slots.specific_ecosystem = Slot(uri=DDL.specific_ecosystem, name="specific_ecosystem", curie=DDL.curie('specific_ecosystem'),
                      model_uri=DDL.specific_ecosystem, domain=None, range=Optional[str])

slots.img_analysis_complete = Slot(uri=DDL.img_analysis_complete, name="img_analysis_complete", curie=DDL.curie('img_analysis_complete'),
                      model_uri=DDL.img_analysis_complete, domain=None, range=Optional[str])

slots.is_gene_primp = Slot(uri=DDL.is_gene_primp, name="is_gene_primp", curie=DDL.curie('is_gene_primp'),
                      model_uri=DDL.is_gene_primp, domain=None, range=Optional[str])

slots.is_decontamination = Slot(uri=DDL.is_decontamination, name="is_decontamination", curie=DDL.curie('is_decontamination'),
                      model_uri=DDL.is_decontamination, domain=None, range=Optional[str])

slots.is_img_annotation = Slot(uri=DDL.is_img_annotation, name="is_img_annotation", curie=DDL.curie('is_img_annotation'),
                      model_uri=DDL.is_img_annotation, domain=None, range=Optional[str])

slots.its_annotation_at_id = Slot(uri=DDL.its_annotation_at_id, name="its_annotation_at_id", curie=DDL.curie('its_annotation_at_id'),
                      model_uri=DDL.its_annotation_at_id, domain=None, range=Optional[int])

slots.is_assembled_deleted = Slot(uri=DDL.is_assembled_deleted, name="is_assembled_deleted", curie=DDL.curie('is_assembled_deleted'),
                      model_uri=DDL.is_assembled_deleted, domain=None, range=Optional[str])

slots.study_id = Slot(uri=DDL.study_id, name="study_id", curie=DDL.curie('study_id'),
                      model_uri=DDL.study_id, domain=None, range=Optional[int])

slots.specimen = Slot(uri=DDL.specimen, name="specimen", curie=DDL.curie('specimen'),
                      model_uri=DDL.specimen, domain=None, range=Optional[str])

slots.its_assembly_at_type = Slot(uri=DDL.its_assembly_at_type, name="its_assembly_at_type", curie=DDL.curie('its_assembly_at_type'),
                      model_uri=DDL.its_assembly_at_type, domain=None, range=Optional[str])

slots.domain = Slot(uri=DDL.domain, name="domain", curie=DDL.curie('domain'),
                      model_uri=DDL.domain, domain=None, range=Optional[str])

slots.ncbi_phylum = Slot(uri=DDL.ncbi_phylum, name="ncbi_phylum", curie=DDL.curie('ncbi_phylum'),
                      model_uri=DDL.ncbi_phylum, domain=None, range=Optional[str])

slots.ncbi_class = Slot(uri=DDL.ncbi_class, name="ncbi_class", curie=DDL.curie('ncbi_class'),
                      model_uri=DDL.ncbi_class, domain=None, range=Optional[str])

slots.ncbi_order = Slot(uri=DDL.ncbi_order, name="ncbi_order", curie=DDL.curie('ncbi_order'),
                      model_uri=DDL.ncbi_order, domain=None, range=Optional[str])

slots.ncbi_family = Slot(uri=DDL.ncbi_family, name="ncbi_family", curie=DDL.curie('ncbi_family'),
                      model_uri=DDL.ncbi_family, domain=None, range=Optional[str])

slots.ncbi_genus = Slot(uri=DDL.ncbi_genus, name="ncbi_genus", curie=DDL.curie('ncbi_genus'),
                      model_uri=DDL.ncbi_genus, domain=None, range=Optional[str])

slots.ncbi_species = Slot(uri=DDL.ncbi_species, name="ncbi_species", curie=DDL.curie('ncbi_species'),
                      model_uri=DDL.ncbi_species, domain=None, range=Optional[str])

slots.appended_ap_name = Slot(uri=DDL.appended_ap_name, name="appended_ap_name", curie=DDL.curie('appended_ap_name'),
                      model_uri=DDL.appended_ap_name, domain=None, range=Optional[str])

slots.mod_by = Slot(uri=DDL.mod_by, name="mod_by", curie=DDL.curie('mod_by'),
                      model_uri=DDL.mod_by, domain=None, range=Optional[float])

slots.mod_date = Slot(uri=DDL.mod_date, name="mod_date", curie=DDL.curie('mod_date'),
                      model_uri=DDL.mod_date, domain=None, range=Optional[Union[str, XSDTime]])

slots.pi_name = Slot(uri=DDL.pi_name, name="pi_name", curie=DDL.curie('pi_name'),
                      model_uri=DDL.pi_name, domain=None, range=Optional[str])

slots.analysis_project_name_full = Slot(uri=DDL.analysis_project_name_full, name="analysis_project_name_full", curie=DDL.curie('analysis_project_name_full'),
                      model_uri=DDL.analysis_project_name_full, domain=None, range=Optional[str])

slots.is_primary = Slot(uri=DDL.is_primary, name="is_primary", curie=DDL.curie('is_primary'),
                      model_uri=DDL.is_primary, domain=None, range=Optional[str])

slots.gold_phylogeny = Slot(uri=DDL.gold_phylogeny, name="gold_phylogeny", curie=DDL.curie('gold_phylogeny'),
                      model_uri=DDL.gold_phylogeny, domain=None, range=Optional[str])

slots.phylogeny_suggestion = Slot(uri=DDL.phylogeny_suggestion, name="phylogeny_suggestion", curie=DDL.curie('phylogeny_suggestion'),
                      model_uri=DDL.phylogeny_suggestion, domain=None, range=Optional[str])

slots.replaces_ap_id = Slot(uri=DDL.replaces_ap_id, name="replaces_ap_id", curie=DDL.curie('replaces_ap_id'),
                      model_uri=DDL.replaces_ap_id, domain=None, range=Optional[int])

slots.ncbi_bioproject_id = Slot(uri=DDL.ncbi_bioproject_id, name="ncbi_bioproject_id", curie=DDL.curie('ncbi_bioproject_id'),
                      model_uri=DDL.ncbi_bioproject_id, domain=None, range=Optional[int])

slots.screening_method = Slot(uri=DDL.screening_method, name="screening_method", curie=DDL.curie('screening_method'),
                      model_uri=DDL.screening_method, domain=None, range=Optional[str])

slots.decontamination_method = Slot(uri=DDL.decontamination_method, name="decontamination_method", curie=DDL.curie('decontamination_method'),
                      model_uri=DDL.decontamination_method, domain=None, range=Optional[str])

slots.ncbi_biosample_accession = Slot(uri=DDL.ncbi_biosample_accession, name="ncbi_biosample_accession", curie=DDL.curie('ncbi_biosample_accession'),
                      model_uri=DDL.ncbi_biosample_accession, domain=None, range=Optional[str])

slots.ncbi_bioproject_accession = Slot(uri=DDL.ncbi_bioproject_accession, name="ncbi_bioproject_accession", curie=DDL.curie('ncbi_bioproject_accession'),
                      model_uri=DDL.ncbi_bioproject_accession, domain=None, range=Optional[str])

slots.completion = Slot(uri=DDL.completion, name="completion", curie=DDL.curie('completion'),
                      model_uri=DDL.completion, domain=None, range=Optional[str])

slots.ncbi_kingdom = Slot(uri=DDL.ncbi_kingdom, name="ncbi_kingdom", curie=DDL.curie('ncbi_kingdom'),
                      model_uri=DDL.ncbi_kingdom, domain=None, range=Optional[str])

slots.review_status = Slot(uri=DDL.review_status, name="review_status", curie=DDL.curie('review_status'),
                      model_uri=DDL.review_status, domain=None, range=Optional[str])

slots.rejection_reasons = Slot(uri=DDL.rejection_reasons, name="rejection_reasons", curie=DDL.curie('rejection_reasons'),
                      model_uri=DDL.rejection_reasons, domain=None, range=Optional[str])

slots.organism_id = Slot(uri=DDL.organism_id, name="organism_id", curie=DDL.curie('organism_id'),
                      model_uri=DDL.organism_id, domain=None, range=Optional[int])

slots.pipeline_annotation_method = Slot(uri=DDL.pipeline_annotation_method, name="pipeline_annotation_method", curie=DDL.curie('pipeline_annotation_method'),
                      model_uri=DDL.pipeline_annotation_method, domain=None, range=Optional[str])

slots.genus = Slot(uri=DDL.genus, name="genus", curie=DDL.curie('genus'),
                      model_uri=DDL.genus, domain=None, range=Optional[str])

slots.species = Slot(uri=DDL.species, name="species", curie=DDL.curie('species'),
                      model_uri=DDL.species, domain=None, range=Optional[str])

slots.subspecies = Slot(uri=DDL.subspecies, name="subspecies", curie=DDL.curie('subspecies'),
                      model_uri=DDL.subspecies, domain=None, range=Optional[str])

slots.culture_collection = Slot(uri=DDL.culture_collection, name="culture_collection", curie=DDL.curie('culture_collection'),
                      model_uri=DDL.culture_collection, domain=None, range=Optional[str])

slots.serovar = Slot(uri=DDL.serovar, name="serovar", curie=DDL.curie('serovar'),
                      model_uri=DDL.serovar, domain=None, range=Optional[str])

slots.strain = Slot(uri=DDL.strain, name="strain", curie=DDL.curie('strain'),
                      model_uri=DDL.strain, domain=None, range=Optional[str])

slots.ecosystem_path_id = Slot(uri=DDL.ecosystem_path_id, name="ecosystem_path_id", curie=DDL.curie('ecosystem_path_id'),
                      model_uri=DDL.ecosystem_path_id, domain=None, range=Optional[int])

slots.sequencing_depth = Slot(uri=DDL.sequencing_depth, name="sequencing_depth", curie=DDL.curie('sequencing_depth'),
                      model_uri=DDL.sequencing_depth, domain=None, range=Optional[str])

slots.img_use = Slot(uri=DDL.img_use, name="img_use", curie=DDL.curie('img_use'),
                      model_uri=DDL.img_use, domain=None, range=Optional[str])

slots.annotator_comments = Slot(uri=DDL.annotator_comments, name="annotator_comments", curie=DDL.curie('annotator_comments'),
                      model_uri=DDL.annotator_comments, domain=None, range=Optional[str])

slots.ap_for_nonowner = Slot(uri=DDL.ap_for_nonowner, name="ap_for_nonowner", curie=DDL.curie('ap_for_nonowner'),
                      model_uri=DDL.ap_for_nonowner, domain=None, range=Optional[str])

slots.ncbi_superkingdom = Slot(uri=DDL.ncbi_superkingdom, name="ncbi_superkingdom", curie=DDL.curie('ncbi_superkingdom'),
                      model_uri=DDL.ncbi_superkingdom, domain=None, range=Optional[str])

slots.is_test = Slot(uri=DDL.is_test, name="is_test", curie=DDL.curie('is_test'),
                      model_uri=DDL.is_test, domain=None, range=Optional[str])

slots.its_ncbi_tax_id = Slot(uri=DDL.its_ncbi_tax_id, name="its_ncbi_tax_id", curie=DDL.curie('its_ncbi_tax_id'),
                      model_uri=DDL.its_ncbi_tax_id, domain=None, range=Optional[int])

slots.its_version_number = Slot(uri=DDL.its_version_number, name="its_version_number", curie=DDL.curie('its_version_number'),
                      model_uri=DDL.its_version_number, domain=None, range=Optional[float])

slots.img_rnaseq_id = Slot(uri=DDL.img_rnaseq_id, name="img_rnaseq_id", curie=DDL.curie('img_rnaseq_id'),
                      model_uri=DDL.img_rnaseq_id, domain=None, range=Optional[int])

slots.submission_status_id = Slot(uri=DDL.submission_status_id, name="submission_status_id", curie=DDL.curie('submission_status_id'),
                      model_uri=DDL.submission_status_id, domain=None, range=Optional[int])

slots.submission_status_name = Slot(uri=DDL.submission_status_name, name="submission_status_name", curie=DDL.curie('submission_status_name'),
                      model_uri=DDL.submission_status_name, domain=None, range=Optional[str])

slots.submission_comments = Slot(uri=DDL.submission_comments, name="submission_comments", curie=DDL.curie('submission_comments'),
                      model_uri=DDL.submission_comments, domain=None, range=Optional[str])

slots.img_submission_prority = Slot(uri=DDL.img_submission_prority, name="img_submission_prority", curie=DDL.curie('img_submission_prority'),
                      model_uri=DDL.img_submission_prority, domain=None, range=Optional[str])

slots.contamination_percentage = Slot(uri=DDL.contamination_percentage, name="contamination_percentage", curie=DDL.curie('contamination_percentage'),
                      model_uri=DDL.contamination_percentage, domain=None, range=Optional[float])

slots.completeness_percentage = Slot(uri=DDL.completeness_percentage, name="completeness_percentage", curie=DDL.curie('completeness_percentage'),
                      model_uri=DDL.completeness_percentage, domain=None, range=Optional[float])

slots.sra_run_id = Slot(uri=DDL.sra_run_id, name="sra_run_id", curie=DDL.curie('sra_run_id'),
                      model_uri=DDL.sra_run_id, domain=None, range=Optional[str])

slots.biosample_name = Slot(uri=DDL.biosample_name, name="biosample_name", curie=DDL.curie('biosample_name'),
                      model_uri=DDL.biosample_name, domain=None, range=Optional[str])

slots.description = Slot(uri=DDL.description, name="description", curie=DDL.curie('description'),
                      model_uri=DDL.description, domain=None, range=Optional[str])

slots.sample_collection_site = Slot(uri=DDL.sample_collection_site, name="sample_collection_site", curie=DDL.curie('sample_collection_site'),
                      model_uri=DDL.sample_collection_site, domain=None, range=Optional[str])

slots.isolation_publication_id = Slot(uri=DDL.isolation_publication_id, name="isolation_publication_id", curie=DDL.curie('isolation_publication_id'),
                      model_uri=DDL.isolation_publication_id, domain=None, range=Optional[int])

slots.sample_isolation_comments = Slot(uri=DDL.sample_isolation_comments, name="sample_isolation_comments", curie=DDL.curie('sample_isolation_comments'),
                      model_uri=DDL.sample_isolation_comments, domain=None, range=Optional[str])

slots.sampling_strategy = Slot(uri=DDL.sampling_strategy, name="sampling_strategy", curie=DDL.curie('sampling_strategy'),
                      model_uri=DDL.sampling_strategy, domain=None, range=Optional[str])

slots.replicate_number = Slot(uri=DDL.replicate_number, name="replicate_number", curie=DDL.curie('replicate_number'),
                      model_uri=DDL.replicate_number, domain=None, range=Optional[float])

slots.sample_volume = Slot(uri=DDL.sample_volume, name="sample_volume", curie=DDL.curie('sample_volume'),
                      model_uri=DDL.sample_volume, domain=None, range=Optional[str])

slots.sample_biomass = Slot(uri=DDL.sample_biomass, name="sample_biomass", curie=DDL.curie('sample_biomass'),
                      model_uri=DDL.sample_biomass, domain=None, range=Optional[str])

slots.sample_contact_name = Slot(uri=DDL.sample_contact_name, name="sample_contact_name", curie=DDL.curie('sample_contact_name'),
                      model_uri=DDL.sample_contact_name, domain=None, range=Optional[str])

slots.sample_contact_email = Slot(uri=DDL.sample_contact_email, name="sample_contact_email", curie=DDL.curie('sample_contact_email'),
                      model_uri=DDL.sample_contact_email, domain=None, range=Optional[str])

slots.geographic_location = Slot(uri=DDL.geographic_location, name="geographic_location", curie=DDL.curie('geographic_location'),
                      model_uri=DDL.geographic_location, domain=None, range=Optional[str])

slots.lat_long_inferred = Slot(uri=DDL.lat_long_inferred, name="lat_long_inferred", curie=DDL.curie('lat_long_inferred'),
                      model_uri=DDL.lat_long_inferred, domain=None, range=Optional[str])

slots.salinity = Slot(uri=DDL.salinity, name="salinity", curie=DDL.curie('salinity'),
                      model_uri=DDL.salinity, domain=None, range=Optional[str])

slots.pressure = Slot(uri=DDL.pressure, name="pressure", curie=DDL.curie('pressure'),
                      model_uri=DDL.pressure, domain=None, range=Optional[str])

slots.ph = Slot(uri=DDL.ph, name="ph", curie=DDL.curie('ph'),
                      model_uri=DDL.ph, domain=None, range=Optional[str])

slots.habitat = Slot(uri=DDL.habitat, name="habitat", curie=DDL.curie('habitat'),
                      model_uri=DDL.habitat, domain=None, range=Optional[str])

slots.host_name = Slot(uri=DDL.host_name, name="host_name", curie=DDL.curie('host_name'),
                      model_uri=DDL.host_name, domain=None, range=Optional[str])

slots.host_taxonomy_id = Slot(uri=DDL.host_taxonomy_id, name="host_taxonomy_id", curie=DDL.curie('host_taxonomy_id'),
                      model_uri=DDL.host_taxonomy_id, domain=None, range=Optional[int])

slots.host_gender = Slot(uri=DDL.host_gender, name="host_gender", curie=DDL.curie('host_gender'),
                      model_uri=DDL.host_gender, domain=None, range=Optional[str])

slots.host_race = Slot(uri=DDL.host_race, name="host_race", curie=DDL.curie('host_race'),
                      model_uri=DDL.host_race, domain=None, range=Optional[str])

slots.host_age = Slot(uri=DDL.host_age, name="host_age", curie=DDL.curie('host_age'),
                      model_uri=DDL.host_age, domain=None, range=Optional[str])

slots.host_health_condition = Slot(uri=DDL.host_health_condition, name="host_health_condition", curie=DDL.curie('host_health_condition'),
                      model_uri=DDL.host_health_condition, domain=None, range=Optional[str])

slots.patient_visit_number = Slot(uri=DDL.patient_visit_number, name="patient_visit_number", curie=DDL.curie('patient_visit_number'),
                      model_uri=DDL.patient_visit_number, domain=None, range=Optional[float])

slots.host_medication = Slot(uri=DDL.host_medication, name="host_medication", curie=DDL.curie('host_medication'),
                      model_uri=DDL.host_medication, domain=None, range=Optional[str])

slots.mrn = Slot(uri=DDL.mrn, name="mrn", curie=DDL.curie('mrn'),
                      model_uri=DDL.mrn, domain=None, range=Optional[str])

slots.host_body_site = Slot(uri=DDL.host_body_site, name="host_body_site", curie=DDL.curie('host_body_site'),
                      model_uri=DDL.host_body_site, domain=None, range=Optional[str])

slots.host_body_subsite = Slot(uri=DDL.host_body_subsite, name="host_body_subsite", curie=DDL.curie('host_body_subsite'),
                      model_uri=DDL.host_body_subsite, domain=None, range=Optional[str])

slots.host_body_product = Slot(uri=DDL.host_body_product, name="host_body_product", curie=DDL.curie('host_body_product'),
                      model_uri=DDL.host_body_product, domain=None, range=Optional[str])

slots.host_specificity = Slot(uri=DDL.host_specificity, name="host_specificity", curie=DDL.curie('host_specificity'),
                      model_uri=DDL.host_specificity, domain=None, range=Optional[str])

slots.host_comments = Slot(uri=DDL.host_comments, name="host_comments", curie=DDL.curie('host_comments'),
                      model_uri=DDL.host_comments, domain=None, range=Optional[str])

slots.active = Slot(uri=DDL.active, name="active", curie=DDL.curie('active'),
                      model_uri=DDL.active, domain=None, range=Optional[str])

slots.project_oid = Slot(uri=DDL.project_oid, name="project_oid", curie=DDL.curie('project_oid'),
                      model_uri=DDL.project_oid, domain=None, range=Optional[float])

slots.sample_oid = Slot(uri=DDL.sample_oid, name="sample_oid", curie=DDL.curie('sample_oid'),
                      model_uri=DDL.sample_oid, domain=None, range=Optional[float])

slots.submit_biosample_name = Slot(uri=DDL.submit_biosample_name, name="submit_biosample_name", curie=DDL.curie('submit_biosample_name'),
                      model_uri=DDL.submit_biosample_name, domain=None, range=Optional[str])

slots.ncbi_taxonomy_id = Slot(uri=DDL.ncbi_taxonomy_id, name="ncbi_taxonomy_id", curie=DDL.curie('ncbi_taxonomy_id'),
                      model_uri=DDL.ncbi_taxonomy_id, domain=None, range=Optional[int])

slots.community = Slot(uri=DDL.community, name="community", curie=DDL.curie('community'),
                      model_uri=DDL.community, domain=None, range=Optional[str])

slots.location = Slot(uri=DDL.location, name="location", curie=DDL.curie('location'),
                      model_uri=DDL.location, domain=None, range=Optional[str])

slots.identifier = Slot(uri=DDL.identifier, name="identifier", curie=DDL.curie('identifier'),
                      model_uri=DDL.identifier, domain=None, range=Optional[str])

slots.env_package = Slot(uri=DDL.env_package, name="env_package", curie=DDL.curie('env_package'),
                      model_uri=DDL.env_package, domain=None, range=Optional[str])

slots.sample_collection_day = Slot(uri=DDL.sample_collection_day, name="sample_collection_day", curie=DDL.curie('sample_collection_day'),
                      model_uri=DDL.sample_collection_day, domain=None, range=Optional[float])

slots.sample_collection_month = Slot(uri=DDL.sample_collection_month, name="sample_collection_month", curie=DDL.curie('sample_collection_month'),
                      model_uri=DDL.sample_collection_month, domain=None, range=Optional[float])

slots.sample_collection_year = Slot(uri=DDL.sample_collection_year, name="sample_collection_year", curie=DDL.curie('sample_collection_year'),
                      model_uri=DDL.sample_collection_year, domain=None, range=Optional[float])

slots.submitter_id = Slot(uri=DDL.submitter_id, name="submitter_id", curie=DDL.curie('submitter_id'),
                      model_uri=DDL.submitter_id, domain=None, range=Optional[int])

slots.growth_conditions = Slot(uri=DDL.growth_conditions, name="growth_conditions", curie=DDL.curie('growth_conditions'),
                      model_uri=DDL.growth_conditions, domain=None, range=Optional[str])

slots.jpa_entity = Slot(uri=DDL.jpa_entity, name="jpa_entity", curie=DDL.curie('jpa_entity'),
                      model_uri=DDL.jpa_entity, domain=None, range=Optional[str])

slots.other_hosts = Slot(uri=DDL.other_hosts, name="other_hosts", curie=DDL.curie('other_hosts'),
                      model_uri=DDL.other_hosts, domain=None, range=Optional[str])

slots.known_non_hosts = Slot(uri=DDL.known_non_hosts, name="known_non_hosts", curie=DDL.curie('known_non_hosts'),
                      model_uri=DDL.known_non_hosts, domain=None, range=Optional[str])

slots.isolation_pubmed_id = Slot(uri=DDL.isolation_pubmed_id, name="isolation_pubmed_id", curie=DDL.curie('isolation_pubmed_id'),
                      model_uri=DDL.isolation_pubmed_id, domain=None, range=Optional[int])

slots.host_body_site_id = Slot(uri=DDL.host_body_site_id, name="host_body_site_id", curie=DDL.curie('host_body_site_id'),
                      model_uri=DDL.host_body_site_id, domain=None, range=Optional[int])

slots.host_body_subsite_id = Slot(uri=DDL.host_body_subsite_id, name="host_body_subsite_id", curie=DDL.curie('host_body_subsite_id'),
                      model_uri=DDL.host_body_subsite_id, domain=None, range=Optional[int])

slots.host_body_product_id = Slot(uri=DDL.host_body_product_id, name="host_body_product_id", curie=DDL.curie('host_body_product_id'),
                      model_uri=DDL.host_body_product_id, domain=None, range=Optional[int])

slots.is_draft = Slot(uri=DDL.is_draft, name="is_draft", curie=DDL.curie('is_draft'),
                      model_uri=DDL.is_draft, domain=None, range=Optional[str])

slots.sample_isolation_country_id = Slot(uri=DDL.sample_isolation_country_id, name="sample_isolation_country_id", curie=DDL.curie('sample_isolation_country_id'),
                      model_uri=DDL.sample_isolation_country_id, domain=None, range=Optional[int])

slots.other_ecosystem = Slot(uri=DDL.other_ecosystem, name="other_ecosystem", curie=DDL.curie('other_ecosystem'),
                      model_uri=DDL.other_ecosystem, domain=None, range=Optional[str])

slots.longhurst_code = Slot(uri=DDL.longhurst_code, name="longhurst_code", curie=DDL.curie('longhurst_code'),
                      model_uri=DDL.longhurst_code, domain=None, range=Optional[str])

slots.sample_collection_hour = Slot(uri=DDL.sample_collection_hour, name="sample_collection_hour", curie=DDL.curie('sample_collection_hour'),
                      model_uri=DDL.sample_collection_hour, domain=None, range=Optional[float])

slots.sample_collection_minute = Slot(uri=DDL.sample_collection_minute, name="sample_collection_minute", curie=DDL.curie('sample_collection_minute'),
                      model_uri=DDL.sample_collection_minute, domain=None, range=Optional[float])

slots.chlorophyll_concentration = Slot(uri=DDL.chlorophyll_concentration, name="chlorophyll_concentration", curie=DDL.curie('chlorophyll_concentration'),
                      model_uri=DDL.chlorophyll_concentration, domain=None, range=Optional[str])

slots.nitrate_concentration = Slot(uri=DDL.nitrate_concentration, name="nitrate_concentration", curie=DDL.curie('nitrate_concentration'),
                      model_uri=DDL.nitrate_concentration, domain=None, range=Optional[str])

slots.oxygen_concentration = Slot(uri=DDL.oxygen_concentration, name="oxygen_concentration", curie=DDL.curie('oxygen_concentration'),
                      model_uri=DDL.oxygen_concentration, domain=None, range=Optional[str])

slots.salinity_concentration = Slot(uri=DDL.salinity_concentration, name="salinity_concentration", curie=DDL.curie('salinity_concentration'),
                      model_uri=DDL.salinity_concentration, domain=None, range=Optional[str])

slots.public_sp_count = Slot(uri=DDL.public_sp_count, name="public_sp_count", curie=DDL.curie('public_sp_count'),
                      model_uri=DDL.public_sp_count, domain=None, range=Optional[float])

slots.admin_sp_count = Slot(uri=DDL.admin_sp_count, name="admin_sp_count", curie=DDL.curie('admin_sp_count'),
                      model_uri=DDL.admin_sp_count, domain=None, range=Optional[float])

slots.public_ap_count = Slot(uri=DDL.public_ap_count, name="public_ap_count", curie=DDL.curie('public_ap_count'),
                      model_uri=DDL.public_ap_count, domain=None, range=Optional[float])

slots.admin_ap_count = Slot(uri=DDL.admin_ap_count, name="admin_ap_count", curie=DDL.curie('admin_ap_count'),
                      model_uri=DDL.admin_ap_count, domain=None, range=Optional[float])

slots.public_dap_count = Slot(uri=DDL.public_dap_count, name="public_dap_count", curie=DDL.curie('public_dap_count'),
                      model_uri=DDL.public_dap_count, domain=None, range=Optional[float])

slots.admin_dap_count = Slot(uri=DDL.admin_dap_count, name="admin_dap_count", curie=DDL.curie('admin_dap_count'),
                      model_uri=DDL.admin_dap_count, domain=None, range=Optional[float])

slots.cruise_line_name = Slot(uri=DDL.cruise_line_name, name="cruise_line_name", curie=DDL.curie('cruise_line_name'),
                      model_uri=DDL.cruise_line_name, domain=None, range=Optional[str])

slots.proport_ocean = Slot(uri=DDL.proport_ocean, name="proport_ocean", curie=DDL.curie('proport_ocean'),
                      model_uri=DDL.proport_ocean, domain=None, range=Optional[str])

slots.proport_isolation = Slot(uri=DDL.proport_isolation, name="proport_isolation", curie=DDL.curie('proport_isolation'),
                      model_uri=DDL.proport_isolation, domain=None, range=Optional[str])

slots.proport_station = Slot(uri=DDL.proport_station, name="proport_station", curie=DDL.curie('proport_station'),
                      model_uri=DDL.proport_station, domain=None, range=Optional[str])

slots.proport_woa_temperature = Slot(uri=DDL.proport_woa_temperature, name="proport_woa_temperature", curie=DDL.curie('proport_woa_temperature'),
                      model_uri=DDL.proport_woa_temperature, domain=None, range=Optional[float])

slots.proport_woa_salinity = Slot(uri=DDL.proport_woa_salinity, name="proport_woa_salinity", curie=DDL.curie('proport_woa_salinity'),
                      model_uri=DDL.proport_woa_salinity, domain=None, range=Optional[float])

slots.proport_woa_dissolved_oxygen = Slot(uri=DDL.proport_woa_dissolved_oxygen, name="proport_woa_dissolved_oxygen", curie=DDL.curie('proport_woa_dissolved_oxygen'),
                      model_uri=DDL.proport_woa_dissolved_oxygen, domain=None, range=Optional[float])

slots.proport_woa_silicate = Slot(uri=DDL.proport_woa_silicate, name="proport_woa_silicate", curie=DDL.curie('proport_woa_silicate'),
                      model_uri=DDL.proport_woa_silicate, domain=None, range=Optional[float])

slots.proport_woa_phosphate = Slot(uri=DDL.proport_woa_phosphate, name="proport_woa_phosphate", curie=DDL.curie('proport_woa_phosphate'),
                      model_uri=DDL.proport_woa_phosphate, domain=None, range=Optional[float])

slots.proport_woa_nitrate = Slot(uri=DDL.proport_woa_nitrate, name="proport_woa_nitrate", curie=DDL.curie('proport_woa_nitrate'),
                      model_uri=DDL.proport_woa_nitrate, domain=None, range=Optional[float])

slots.ncbi_taxonomy_name = Slot(uri=DDL.ncbi_taxonomy_name, name="ncbi_taxonomy_name", curie=DDL.curie('ncbi_taxonomy_name'),
                      model_uri=DDL.ncbi_taxonomy_name, domain=None, range=Optional[str])

slots.its_growth_conditions = Slot(uri=DDL.its_growth_conditions, name="its_growth_conditions", curie=DDL.curie('its_growth_conditions'),
                      model_uri=DDL.its_growth_conditions, domain=None, range=Optional[str])

slots.biogas_fed_substrates = Slot(uri=DDL.biogas_fed_substrates, name="biogas_fed_substrates", curie=DDL.curie('biogas_fed_substrates'),
                      model_uri=DDL.biogas_fed_substrates, domain=None, range=Optional[str])

slots.biogas_retention_time = Slot(uri=DDL.biogas_retention_time, name="biogas_retention_time", curie=DDL.curie('biogas_retention_time'),
                      model_uri=DDL.biogas_retention_time, domain=None, range=Optional[str])

slots.biogas_temperature = Slot(uri=DDL.biogas_temperature, name="biogas_temperature", curie=DDL.curie('biogas_temperature'),
                      model_uri=DDL.biogas_temperature, domain=None, range=Optional[str])

slots.biogas_yield = Slot(uri=DDL.biogas_yield, name="biogas_yield", curie=DDL.curie('biogas_yield'),
                      model_uri=DDL.biogas_yield, domain=None, range=Optional[str])

slots.biogas_volatile_organic_acids = Slot(uri=DDL.biogas_volatile_organic_acids, name="biogas_volatile_organic_acids", curie=DDL.curie('biogas_volatile_organic_acids'),
                      model_uri=DDL.biogas_volatile_organic_acids, domain=None, range=Optional[str])

slots.biogas_total_inorganic_carbon = Slot(uri=DDL.biogas_total_inorganic_carbon, name="biogas_total_inorganic_carbon", curie=DDL.curie('biogas_total_inorganic_carbon'),
                      model_uri=DDL.biogas_total_inorganic_carbon, domain=None, range=Optional[str])

slots.biogas_voa_tic = Slot(uri=DDL.biogas_voa_tic, name="biogas_voa_tic", curie=DDL.curie('biogas_voa_tic'),
                      model_uri=DDL.biogas_voa_tic, domain=None, range=Optional[str])

slots.biogas_ammonium_nh4 = Slot(uri=DDL.biogas_ammonium_nh4, name="biogas_ammonium_nh4", curie=DDL.curie('biogas_ammonium_nh4'),
                      model_uri=DDL.biogas_ammonium_nh4, domain=None, range=Optional[str])

slots.biogas_butanol = Slot(uri=DDL.biogas_butanol, name="biogas_butanol", curie=DDL.curie('biogas_butanol'),
                      model_uri=DDL.biogas_butanol, domain=None, range=Optional[str])

slots.biogas_ethanol = Slot(uri=DDL.biogas_ethanol, name="biogas_ethanol", curie=DDL.curie('biogas_ethanol'),
                      model_uri=DDL.biogas_ethanol, domain=None, range=Optional[str])

slots.biogas_propanol = Slot(uri=DDL.biogas_propanol, name="biogas_propanol", curie=DDL.curie('biogas_propanol'),
                      model_uri=DDL.biogas_propanol, domain=None, range=Optional[str])

slots.biogas_methanol = Slot(uri=DDL.biogas_methanol, name="biogas_methanol", curie=DDL.curie('biogas_methanol'),
                      model_uri=DDL.biogas_methanol, domain=None, range=Optional[str])

slots.biogas_acetic_acid = Slot(uri=DDL.biogas_acetic_acid, name="biogas_acetic_acid", curie=DDL.curie('biogas_acetic_acid'),
                      model_uri=DDL.biogas_acetic_acid, domain=None, range=Optional[str])

slots.biogas_butyl_acid = Slot(uri=DDL.biogas_butyl_acid, name="biogas_butyl_acid", curie=DDL.curie('biogas_butyl_acid'),
                      model_uri=DDL.biogas_butyl_acid, domain=None, range=Optional[str])

slots.biogas_iso_butyl_acid = Slot(uri=DDL.biogas_iso_butyl_acid, name="biogas_iso_butyl_acid", curie=DDL.curie('biogas_iso_butyl_acid'),
                      model_uri=DDL.biogas_iso_butyl_acid, domain=None, range=Optional[str])

slots.biogas_valeric_acid = Slot(uri=DDL.biogas_valeric_acid, name="biogas_valeric_acid", curie=DDL.curie('biogas_valeric_acid'),
                      model_uri=DDL.biogas_valeric_acid, domain=None, range=Optional[str])

slots.biogas_iso_valeric_acid = Slot(uri=DDL.biogas_iso_valeric_acid, name="biogas_iso_valeric_acid", curie=DDL.curie('biogas_iso_valeric_acid'),
                      model_uri=DDL.biogas_iso_valeric_acid, domain=None, range=Optional[str])

slots.biogas_propionic_acid = Slot(uri=DDL.biogas_propionic_acid, name="biogas_propionic_acid", curie=DDL.curie('biogas_propionic_acid'),
                      model_uri=DDL.biogas_propionic_acid, domain=None, range=Optional[str])

slots.biogas_methane_pct = Slot(uri=DDL.biogas_methane_pct, name="biogas_methane_pct", curie=DDL.curie('biogas_methane_pct'),
                      model_uri=DDL.biogas_methane_pct, domain=None, range=Optional[float])

slots.sample_conductivity = Slot(uri=DDL.sample_conductivity, name="sample_conductivity", curie=DDL.curie('sample_conductivity'),
                      model_uri=DDL.sample_conductivity, domain=None, range=Optional[str])

slots.growth_temperature = Slot(uri=DDL.growth_temperature, name="growth_temperature", curie=DDL.curie('growth_temperature'),
                      model_uri=DDL.growth_temperature, domain=None, range=Optional[float])

slots.subsurface_depth = Slot(uri=DDL.subsurface_depth, name="subsurface_depth", curie=DDL.curie('subsurface_depth'),
                      model_uri=DDL.subsurface_depth, domain=None, range=Optional[float])

slots.legacy_depth_data = Slot(uri=DDL.legacy_depth_data, name="legacy_depth_data", curie=DDL.curie('legacy_depth_data'),
                      model_uri=DDL.legacy_depth_data, domain=None, range=Optional[str])

slots.latitude_test = Slot(uri=DDL.latitude_test, name="latitude_test", curie=DDL.curie('latitude_test'),
                      model_uri=DDL.latitude_test, domain=None, range=Optional[float])

slots.longitude_test = Slot(uri=DDL.longitude_test, name="longitude_test", curie=DDL.curie('longitude_test'),
                      model_uri=DDL.longitude_test, domain=None, range=Optional[float])

slots.elevation = Slot(uri=DDL.elevation, name="elevation", curie=DDL.curie('elevation'),
                      model_uri=DDL.elevation, domain=None, range=Optional[float])

slots.elevation2 = Slot(uri=DDL.elevation2, name="elevation2", curie=DDL.curie('elevation2'),
                      model_uri=DDL.elevation2, domain=None, range=Optional[float])

slots.soil_curr_land_use = Slot(uri=DDL.soil_curr_land_use, name="soil_curr_land_use", curie=DDL.curie('soil_curr_land_use'),
                      model_uri=DDL.soil_curr_land_use, domain=None, range=Optional[str])

slots.soil_curr_vegetation = Slot(uri=DDL.soil_curr_vegetation, name="soil_curr_vegetation", curie=DDL.curie('soil_curr_vegetation'),
                      model_uri=DDL.soil_curr_vegetation, domain=None, range=Optional[str])

slots.soil_curr_vegetation_method = Slot(uri=DDL.soil_curr_vegetation_method, name="soil_curr_vegetation_method", curie=DDL.curie('soil_curr_vegetation_method'),
                      model_uri=DDL.soil_curr_vegetation_method, domain=None, range=Optional[str])

slots.soil_prev_land_use = Slot(uri=DDL.soil_prev_land_use, name="soil_prev_land_use", curie=DDL.curie('soil_prev_land_use'),
                      model_uri=DDL.soil_prev_land_use, domain=None, range=Optional[str])

slots.soil_prev_land_use_meth = Slot(uri=DDL.soil_prev_land_use_meth, name="soil_prev_land_use_meth", curie=DDL.curie('soil_prev_land_use_meth'),
                      model_uri=DDL.soil_prev_land_use_meth, domain=None, range=Optional[str])

slots.soil_crop_rotation = Slot(uri=DDL.soil_crop_rotation, name="soil_crop_rotation", curie=DDL.curie('soil_crop_rotation'),
                      model_uri=DDL.soil_crop_rotation, domain=None, range=Optional[str])

slots.soil_agrochem_addition = Slot(uri=DDL.soil_agrochem_addition, name="soil_agrochem_addition", curie=DDL.curie('soil_agrochem_addition'),
                      model_uri=DDL.soil_agrochem_addition, domain=None, range=Optional[str])

slots.soil_tillage = Slot(uri=DDL.soil_tillage, name="soil_tillage", curie=DDL.curie('soil_tillage'),
                      model_uri=DDL.soil_tillage, domain=None, range=Optional[str])

slots.soil_fire = Slot(uri=DDL.soil_fire, name="soil_fire", curie=DDL.curie('soil_fire'),
                      model_uri=DDL.soil_fire, domain=None, range=Optional[str])

slots.soil_flooding = Slot(uri=DDL.soil_flooding, name="soil_flooding", curie=DDL.curie('soil_flooding'),
                      model_uri=DDL.soil_flooding, domain=None, range=Optional[str])

slots.soil_extreme_event = Slot(uri=DDL.soil_extreme_event, name="soil_extreme_event", curie=DDL.curie('soil_extreme_event'),
                      model_uri=DDL.soil_extreme_event, domain=None, range=Optional[str])

slots.soil_horizon = Slot(uri=DDL.soil_horizon, name="soil_horizon", curie=DDL.curie('soil_horizon'),
                      model_uri=DDL.soil_horizon, domain=None, range=Optional[str])

slots.soil_horizon_method = Slot(uri=DDL.soil_horizon_method, name="soil_horizon_method", curie=DDL.curie('soil_horizon_method'),
                      model_uri=DDL.soil_horizon_method, domain=None, range=Optional[str])

slots.soil_sieving = Slot(uri=DDL.soil_sieving, name="soil_sieving", curie=DDL.curie('soil_sieving'),
                      model_uri=DDL.soil_sieving, domain=None, range=Optional[str])

slots.soil_water_content = Slot(uri=DDL.soil_water_content, name="soil_water_content", curie=DDL.curie('soil_water_content'),
                      model_uri=DDL.soil_water_content, domain=None, range=Optional[str])

slots.soil_water_content_soil_meth = Slot(uri=DDL.soil_water_content_soil_meth, name="soil_water_content_soil_meth", curie=DDL.curie('soil_water_content_soil_meth'),
                      model_uri=DDL.soil_water_content_soil_meth, domain=None, range=Optional[str])

slots.sample_weight_dna_ext = Slot(uri=DDL.sample_weight_dna_ext, name="sample_weight_dna_ext", curie=DDL.curie('sample_weight_dna_ext'),
                      model_uri=DDL.sample_weight_dna_ext, domain=None, range=Optional[str])

slots.soil_pool_dna_extracts = Slot(uri=DDL.soil_pool_dna_extracts, name="soil_pool_dna_extracts", curie=DDL.curie('soil_pool_dna_extracts'),
                      model_uri=DDL.soil_pool_dna_extracts, domain=None, range=Optional[str])

slots.soil_storage_condition = Slot(uri=DDL.soil_storage_condition, name="soil_storage_condition", curie=DDL.curie('soil_storage_condition'),
                      model_uri=DDL.soil_storage_condition, domain=None, range=Optional[str])

slots.soil_link_climate_info = Slot(uri=DDL.soil_link_climate_info, name="soil_link_climate_info", curie=DDL.curie('soil_link_climate_info'),
                      model_uri=DDL.soil_link_climate_info, domain=None, range=Optional[str])

slots.soil_link_class_info = Slot(uri=DDL.soil_link_class_info, name="soil_link_class_info", curie=DDL.curie('soil_link_class_info'),
                      model_uri=DDL.soil_link_class_info, domain=None, range=Optional[str])

slots.soil_fao_class = Slot(uri=DDL.soil_fao_class, name="soil_fao_class", curie=DDL.curie('soil_fao_class'),
                      model_uri=DDL.soil_fao_class, domain=None, range=Optional[str])

slots.soil_local_class = Slot(uri=DDL.soil_local_class, name="soil_local_class", curie=DDL.curie('soil_local_class'),
                      model_uri=DDL.soil_local_class, domain=None, range=Optional[str])

slots.soil_local_class_method = Slot(uri=DDL.soil_local_class_method, name="soil_local_class_method", curie=DDL.curie('soil_local_class_method'),
                      model_uri=DDL.soil_local_class_method, domain=None, range=Optional[str])

slots.soil_type = Slot(uri=DDL.soil_type, name="soil_type", curie=DDL.curie('soil_type'),
                      model_uri=DDL.soil_type, domain=None, range=Optional[str])

slots.soil_type_method = Slot(uri=DDL.soil_type_method, name="soil_type_method", curie=DDL.curie('soil_type_method'),
                      model_uri=DDL.soil_type_method, domain=None, range=Optional[str])

slots.soil_slope_gradient = Slot(uri=DDL.soil_slope_gradient, name="soil_slope_gradient", curie=DDL.curie('soil_slope_gradient'),
                      model_uri=DDL.soil_slope_gradient, domain=None, range=Optional[float])

slots.soil_slope_aspect = Slot(uri=DDL.soil_slope_aspect, name="soil_slope_aspect", curie=DDL.curie('soil_slope_aspect'),
                      model_uri=DDL.soil_slope_aspect, domain=None, range=Optional[float])

slots.soil_profile_position = Slot(uri=DDL.soil_profile_position, name="soil_profile_position", curie=DDL.curie('soil_profile_position'),
                      model_uri=DDL.soil_profile_position, domain=None, range=Optional[str])

slots.soil_drainage_class = Slot(uri=DDL.soil_drainage_class, name="soil_drainage_class", curie=DDL.curie('soil_drainage_class'),
                      model_uri=DDL.soil_drainage_class, domain=None, range=Optional[str])

slots.soil_texture = Slot(uri=DDL.soil_texture, name="soil_texture", curie=DDL.curie('soil_texture'),
                      model_uri=DDL.soil_texture, domain=None, range=Optional[str])

slots.soil_texture_method = Slot(uri=DDL.soil_texture_method, name="soil_texture_method", curie=DDL.curie('soil_texture_method'),
                      model_uri=DDL.soil_texture_method, domain=None, range=Optional[str])

slots.soil_ph_method = Slot(uri=DDL.soil_ph_method, name="soil_ph_method", curie=DDL.curie('soil_ph_method'),
                      model_uri=DDL.soil_ph_method, domain=None, range=Optional[str])

slots.tot_org_carbon = Slot(uri=DDL.tot_org_carbon, name="tot_org_carbon", curie=DDL.curie('tot_org_carbon'),
                      model_uri=DDL.tot_org_carbon, domain=None, range=Optional[float])

slots.soil_tot_org_c_method = Slot(uri=DDL.soil_tot_org_c_method, name="soil_tot_org_c_method", curie=DDL.curie('soil_tot_org_c_method'),
                      model_uri=DDL.soil_tot_org_c_method, domain=None, range=Optional[str])

slots.tot_nitrogen = Slot(uri=DDL.tot_nitrogen, name="tot_nitrogen", curie=DDL.curie('tot_nitrogen'),
                      model_uri=DDL.tot_nitrogen, domain=None, range=Optional[str])

slots.soil_tot_n_method = Slot(uri=DDL.soil_tot_n_method, name="soil_tot_n_method", curie=DDL.curie('soil_tot_n_method'),
                      model_uri=DDL.soil_tot_n_method, domain=None, range=Optional[str])

slots.soil_microbial_biomass = Slot(uri=DDL.soil_microbial_biomass, name="soil_microbial_biomass", curie=DDL.curie('soil_microbial_biomass'),
                      model_uri=DDL.soil_microbial_biomass, domain=None, range=Optional[str])

slots.soil_microbial_biomass_method = Slot(uri=DDL.soil_microbial_biomass_method, name="soil_microbial_biomass_method", curie=DDL.curie('soil_microbial_biomass_method'),
                      model_uri=DDL.soil_microbial_biomass_method, domain=None, range=Optional[str])

slots.soil_link_addit_analys = Slot(uri=DDL.soil_link_addit_analys, name="soil_link_addit_analys", curie=DDL.curie('soil_link_addit_analys'),
                      model_uri=DDL.soil_link_addit_analys, domain=None, range=Optional[str])

slots.soil_salinity_method = Slot(uri=DDL.soil_salinity_method, name="soil_salinity_method", curie=DDL.curie('soil_salinity_method'),
                      model_uri=DDL.soil_salinity_method, domain=None, range=Optional[str])

slots.soil_heavy_metals = Slot(uri=DDL.soil_heavy_metals, name="soil_heavy_metals", curie=DDL.curie('soil_heavy_metals'),
                      model_uri=DDL.soil_heavy_metals, domain=None, range=Optional[float])

slots.soil_heavy_metals_method = Slot(uri=DDL.soil_heavy_metals_method, name="soil_heavy_metals_method", curie=DDL.curie('soil_heavy_metals_method'),
                      model_uri=DDL.soil_heavy_metals_method, domain=None, range=Optional[str])

slots.soil_aluminium_sat = Slot(uri=DDL.soil_aluminium_sat, name="soil_aluminium_sat", curie=DDL.curie('soil_aluminium_sat'),
                      model_uri=DDL.soil_aluminium_sat, domain=None, range=Optional[float])

slots.soil_aluminium_sat_method = Slot(uri=DDL.soil_aluminium_sat_method, name="soil_aluminium_sat_method", curie=DDL.curie('soil_aluminium_sat_method'),
                      model_uri=DDL.soil_aluminium_sat_method, domain=None, range=Optional[str])

slots.soil_misc_param = Slot(uri=DDL.soil_misc_param, name="soil_misc_param", curie=DDL.curie('soil_misc_param'),
                      model_uri=DDL.soil_misc_param, domain=None, range=Optional[str])

slots.water_alkalinity = Slot(uri=DDL.water_alkalinity, name="water_alkalinity", curie=DDL.curie('water_alkalinity'),
                      model_uri=DDL.water_alkalinity, domain=None, range=Optional[float])

slots.water_alkyl_diethers = Slot(uri=DDL.water_alkyl_diethers, name="water_alkyl_diethers", curie=DDL.curie('water_alkyl_diethers'),
                      model_uri=DDL.water_alkyl_diethers, domain=None, range=Optional[float])

slots.water_aminopept_act = Slot(uri=DDL.water_aminopept_act, name="water_aminopept_act", curie=DDL.curie('water_aminopept_act'),
                      model_uri=DDL.water_aminopept_act, domain=None, range=Optional[float])

slots.water_ammonium = Slot(uri=DDL.water_ammonium, name="water_ammonium", curie=DDL.curie('water_ammonium'),
                      model_uri=DDL.water_ammonium, domain=None, range=Optional[float])

slots.water_atmospheric_data = Slot(uri=DDL.water_atmospheric_data, name="water_atmospheric_data", curie=DDL.curie('water_atmospheric_data'),
                      model_uri=DDL.water_atmospheric_data, domain=None, range=Optional[str])

slots.water_bacterial_prod = Slot(uri=DDL.water_bacterial_prod, name="water_bacterial_prod", curie=DDL.curie('water_bacterial_prod'),
                      model_uri=DDL.water_bacterial_prod, domain=None, range=Optional[float])

slots.water_bacterial_resp = Slot(uri=DDL.water_bacterial_resp, name="water_bacterial_resp", curie=DDL.curie('water_bacterial_resp'),
                      model_uri=DDL.water_bacterial_resp, domain=None, range=Optional[float])

slots.water_bacterial_carbon_prod = Slot(uri=DDL.water_bacterial_carbon_prod, name="water_bacterial_carbon_prod", curie=DDL.curie('water_bacterial_carbon_prod'),
                      model_uri=DDL.water_bacterial_carbon_prod, domain=None, range=Optional[float])

slots.water_bishomohopanol = Slot(uri=DDL.water_bishomohopanol, name="water_bishomohopanol", curie=DDL.curie('water_bishomohopanol'),
                      model_uri=DDL.water_bishomohopanol, domain=None, range=Optional[str])

slots.water_bromide = Slot(uri=DDL.water_bromide, name="water_bromide", curie=DDL.curie('water_bromide'),
                      model_uri=DDL.water_bromide, domain=None, range=Optional[float])

slots.water_calcium = Slot(uri=DDL.water_calcium, name="water_calcium", curie=DDL.curie('water_calcium'),
                      model_uri=DDL.water_calcium, domain=None, range=Optional[str])

slots.water_carbon_nitrog_ratio = Slot(uri=DDL.water_carbon_nitrog_ratio, name="water_carbon_nitrog_ratio", curie=DDL.curie('water_carbon_nitrog_ratio'),
                      model_uri=DDL.water_carbon_nitrog_ratio, domain=None, range=Optional[str])

slots.water_chem_administration = Slot(uri=DDL.water_chem_administration, name="water_chem_administration", curie=DDL.curie('water_chem_administration'),
                      model_uri=DDL.water_chem_administration, domain=None, range=Optional[str])

slots.water_chloride = Slot(uri=DDL.water_chloride, name="water_chloride", curie=DDL.curie('water_chloride'),
                      model_uri=DDL.water_chloride, domain=None, range=Optional[float])

slots.water_density = Slot(uri=DDL.water_density, name="water_density", curie=DDL.curie('water_density'),
                      model_uri=DDL.water_density, domain=None, range=Optional[float])

slots.water_diether_lipids = Slot(uri=DDL.water_diether_lipids, name="water_diether_lipids", curie=DDL.curie('water_diether_lipids'),
                      model_uri=DDL.water_diether_lipids, domain=None, range=Optional[float])

slots.water_diss_carbon_dioxide = Slot(uri=DDL.water_diss_carbon_dioxide, name="water_diss_carbon_dioxide", curie=DDL.curie('water_diss_carbon_dioxide'),
                      model_uri=DDL.water_diss_carbon_dioxide, domain=None, range=Optional[float])

slots.water_diss_hydrogen = Slot(uri=DDL.water_diss_hydrogen, name="water_diss_hydrogen", curie=DDL.curie('water_diss_hydrogen'),
                      model_uri=DDL.water_diss_hydrogen, domain=None, range=Optional[float])

slots.water_diss_inorg_carbon = Slot(uri=DDL.water_diss_inorg_carbon, name="water_diss_inorg_carbon", curie=DDL.curie('water_diss_inorg_carbon'),
                      model_uri=DDL.water_diss_inorg_carbon, domain=None, range=Optional[float])

slots.water_diss_inorg_nitro = Slot(uri=DDL.water_diss_inorg_nitro, name="water_diss_inorg_nitro", curie=DDL.curie('water_diss_inorg_nitro'),
                      model_uri=DDL.water_diss_inorg_nitro, domain=None, range=Optional[float])

slots.water_diss_inorg_phosphorus = Slot(uri=DDL.water_diss_inorg_phosphorus, name="water_diss_inorg_phosphorus", curie=DDL.curie('water_diss_inorg_phosphorus'),
                      model_uri=DDL.water_diss_inorg_phosphorus, domain=None, range=Optional[float])

slots.water_diss_org_carbon = Slot(uri=DDL.water_diss_org_carbon, name="water_diss_org_carbon", curie=DDL.curie('water_diss_org_carbon'),
                      model_uri=DDL.water_diss_org_carbon, domain=None, range=Optional[float])

slots.water_diss_org_nitrogen = Slot(uri=DDL.water_diss_org_nitrogen, name="water_diss_org_nitrogen", curie=DDL.curie('water_diss_org_nitrogen'),
                      model_uri=DDL.water_diss_org_nitrogen, domain=None, range=Optional[float])

slots.water_downward_par = Slot(uri=DDL.water_downward_par, name="water_downward_par", curie=DDL.curie('water_downward_par'),
                      model_uri=DDL.water_downward_par, domain=None, range=Optional[float])

slots.water_fluorescence = Slot(uri=DDL.water_fluorescence, name="water_fluorescence", curie=DDL.curie('water_fluorescence'),
                      model_uri=DDL.water_fluorescence, domain=None, range=Optional[float])

slots.water_glucosidase_activity = Slot(uri=DDL.water_glucosidase_activity, name="water_glucosidase_activity", curie=DDL.curie('water_glucosidase_activity'),
                      model_uri=DDL.water_glucosidase_activity, domain=None, range=Optional[float])

slots.water_light_intensity = Slot(uri=DDL.water_light_intensity, name="water_light_intensity", curie=DDL.curie('water_light_intensity'),
                      model_uri=DDL.water_light_intensity, domain=None, range=Optional[float])

slots.water_magnesium = Slot(uri=DDL.water_magnesium, name="water_magnesium", curie=DDL.curie('water_magnesium'),
                      model_uri=DDL.water_magnesium, domain=None, range=Optional[str])

slots.water_mean_frict_vel = Slot(uri=DDL.water_mean_frict_vel, name="water_mean_frict_vel", curie=DDL.curie('water_mean_frict_vel'),
                      model_uri=DDL.water_mean_frict_vel, domain=None, range=Optional[float])

slots.water_mean_peak_frict_vel = Slot(uri=DDL.water_mean_peak_frict_vel, name="water_mean_peak_frict_vel", curie=DDL.curie('water_mean_peak_frict_vel'),
                      model_uri=DDL.water_mean_peak_frict_vel, domain=None, range=Optional[float])

slots.water_misc_parameter = Slot(uri=DDL.water_misc_parameter, name="water_misc_parameter", curie=DDL.curie('water_misc_parameter'),
                      model_uri=DDL.water_misc_parameter, domain=None, range=Optional[str])

slots.water_n_alkanes = Slot(uri=DDL.water_n_alkanes, name="water_n_alkanes", curie=DDL.curie('water_n_alkanes'),
                      model_uri=DDL.water_n_alkanes, domain=None, range=Optional[float])

slots.water_nitrite = Slot(uri=DDL.water_nitrite, name="water_nitrite", curie=DDL.curie('water_nitrite'),
                      model_uri=DDL.water_nitrite, domain=None, range=Optional[float])

slots.water_org_matter = Slot(uri=DDL.water_org_matter, name="water_org_matter", curie=DDL.curie('water_org_matter'),
                      model_uri=DDL.water_org_matter, domain=None, range=Optional[float])

slots.water_org_nitrogen = Slot(uri=DDL.water_org_nitrogen, name="water_org_nitrogen", curie=DDL.curie('water_org_nitrogen'),
                      model_uri=DDL.water_org_nitrogen, domain=None, range=Optional[float])

slots.water_organism_count = Slot(uri=DDL.water_organism_count, name="water_organism_count", curie=DDL.curie('water_organism_count'),
                      model_uri=DDL.water_organism_count, domain=None, range=Optional[float])

slots.water_oxy_stat_sample = Slot(uri=DDL.water_oxy_stat_sample, name="water_oxy_stat_sample", curie=DDL.curie('water_oxy_stat_sample'),
                      model_uri=DDL.water_oxy_stat_sample, domain=None, range=Optional[str])

slots.water_part_org_carbon = Slot(uri=DDL.water_part_org_carbon, name="water_part_org_carbon", curie=DDL.curie('water_part_org_carbon'),
                      model_uri=DDL.water_part_org_carbon, domain=None, range=Optional[float])

slots.water_part_org_nitrogen = Slot(uri=DDL.water_part_org_nitrogen, name="water_part_org_nitrogen", curie=DDL.curie('water_part_org_nitrogen'),
                      model_uri=DDL.water_part_org_nitrogen, domain=None, range=Optional[float])

slots.water_perturbation = Slot(uri=DDL.water_perturbation, name="water_perturbation", curie=DDL.curie('water_perturbation'),
                      model_uri=DDL.water_perturbation, domain=None, range=Optional[str])

slots.water_petroleum_hydrocarbon = Slot(uri=DDL.water_petroleum_hydrocarbon, name="water_petroleum_hydrocarbon", curie=DDL.curie('water_petroleum_hydrocarbon'),
                      model_uri=DDL.water_petroleum_hydrocarbon, domain=None, range=Optional[float])

slots.water_phaeopigments = Slot(uri=DDL.water_phaeopigments, name="water_phaeopigments", curie=DDL.curie('water_phaeopigments'),
                      model_uri=DDL.water_phaeopigments, domain=None, range=Optional[float])

slots.water_phosplipid_fatt_acid = Slot(uri=DDL.water_phosplipid_fatt_acid, name="water_phosplipid_fatt_acid", curie=DDL.curie('water_phosplipid_fatt_acid'),
                      model_uri=DDL.water_phosplipid_fatt_acid, domain=None, range=Optional[str])

slots.water_photon_flux = Slot(uri=DDL.water_photon_flux, name="water_photon_flux", curie=DDL.curie('water_photon_flux'),
                      model_uri=DDL.water_photon_flux, domain=None, range=Optional[float])

slots.water_potassium = Slot(uri=DDL.water_potassium, name="water_potassium", curie=DDL.curie('water_potassium'),
                      model_uri=DDL.water_potassium, domain=None, range=Optional[float])

slots.water_primary_prod = Slot(uri=DDL.water_primary_prod, name="water_primary_prod", curie=DDL.curie('water_primary_prod'),
                      model_uri=DDL.water_primary_prod, domain=None, range=Optional[float])

slots.water_redox_potential = Slot(uri=DDL.water_redox_potential, name="water_redox_potential", curie=DDL.curie('water_redox_potential'),
                      model_uri=DDL.water_redox_potential, domain=None, range=Optional[float])

slots.water_samp_store_dur = Slot(uri=DDL.water_samp_store_dur, name="water_samp_store_dur", curie=DDL.curie('water_samp_store_dur'),
                      model_uri=DDL.water_samp_store_dur, domain=None, range=Optional[str])

slots.water_samp_store_loc = Slot(uri=DDL.water_samp_store_loc, name="water_samp_store_loc", curie=DDL.curie('water_samp_store_loc'),
                      model_uri=DDL.water_samp_store_loc, domain=None, range=Optional[str])

slots.water_samp_store_temp = Slot(uri=DDL.water_samp_store_temp, name="water_samp_store_temp", curie=DDL.curie('water_samp_store_temp'),
                      model_uri=DDL.water_samp_store_temp, domain=None, range=Optional[float])

slots.water_sodium = Slot(uri=DDL.water_sodium, name="water_sodium", curie=DDL.curie('water_sodium'),
                      model_uri=DDL.water_sodium, domain=None, range=Optional[float])

slots.water_soluble_react_phosp = Slot(uri=DDL.water_soluble_react_phosp, name="water_soluble_react_phosp", curie=DDL.curie('water_soluble_react_phosp'),
                      model_uri=DDL.water_soluble_react_phosp, domain=None, range=Optional[float])

slots.water_sulfate = Slot(uri=DDL.water_sulfate, name="water_sulfate", curie=DDL.curie('water_sulfate'),
                      model_uri=DDL.water_sulfate, domain=None, range=Optional[str])

slots.water_sulfide = Slot(uri=DDL.water_sulfide, name="water_sulfide", curie=DDL.curie('water_sulfide'),
                      model_uri=DDL.water_sulfide, domain=None, range=Optional[str])

slots.water_suspend_part_matter = Slot(uri=DDL.water_suspend_part_matter, name="water_suspend_part_matter", curie=DDL.curie('water_suspend_part_matter'),
                      model_uri=DDL.water_suspend_part_matter, domain=None, range=Optional[float])

slots.water_tidal_stage = Slot(uri=DDL.water_tidal_stage, name="water_tidal_stage", curie=DDL.curie('water_tidal_stage'),
                      model_uri=DDL.water_tidal_stage, domain=None, range=Optional[str])

slots.water_tot_depth_water_col = Slot(uri=DDL.water_tot_depth_water_col, name="water_tot_depth_water_col", curie=DDL.curie('water_tot_depth_water_col'),
                      model_uri=DDL.water_tot_depth_water_col, domain=None, range=Optional[float])

slots.water_tot_diss_nitro = Slot(uri=DDL.water_tot_diss_nitro, name="water_tot_diss_nitro", curie=DDL.curie('water_tot_diss_nitro'),
                      model_uri=DDL.water_tot_diss_nitro, domain=None, range=Optional[float])

slots.water_tot_inorg_nitro = Slot(uri=DDL.water_tot_inorg_nitro, name="water_tot_inorg_nitro", curie=DDL.curie('water_tot_inorg_nitro'),
                      model_uri=DDL.water_tot_inorg_nitro, domain=None, range=Optional[float])

slots.water_tot_part_carbon = Slot(uri=DDL.water_tot_part_carbon, name="water_tot_part_carbon", curie=DDL.curie('water_tot_part_carbon'),
                      model_uri=DDL.water_tot_part_carbon, domain=None, range=Optional[str])

slots.water_tot_phosphorus = Slot(uri=DDL.water_tot_phosphorus, name="water_tot_phosphorus", curie=DDL.curie('water_tot_phosphorus'),
                      model_uri=DDL.water_tot_phosphorus, domain=None, range=Optional[float])

slots.water_current = Slot(uri=DDL.water_current, name="water_current", curie=DDL.curie('water_current'),
                      model_uri=DDL.water_current, domain=None, range=Optional[str])

slots.latitude = Slot(uri=DDL.latitude, name="latitude", curie=DDL.curie('latitude'),
                      model_uri=DDL.latitude, domain=None, range=Optional[float])

slots.longitude = Slot(uri=DDL.longitude, name="longitude", curie=DDL.curie('longitude'),
                      model_uri=DDL.longitude, domain=None, range=Optional[float])

slots.depth = Slot(uri=DDL.depth, name="depth", curie=DDL.curie('depth'),
                      model_uri=DDL.depth, domain=None, range=Optional[float])

slots.depth2 = Slot(uri=DDL.depth2, name="depth2", curie=DDL.curie('depth2'),
                      model_uri=DDL.depth2, domain=None, range=Optional[float])

slots.altitude = Slot(uri=DDL.altitude, name="altitude", curie=DDL.curie('altitude'),
                      model_uri=DDL.altitude, domain=None, range=Optional[float])

slots.altitude2 = Slot(uri=DDL.altitude2, name="altitude2", curie=DDL.curie('altitude2'),
                      model_uri=DDL.altitude2, domain=None, range=Optional[float])

slots.soluble_iron_micromol = Slot(uri=DDL.soluble_iron_micromol, name="soluble_iron_micromol", curie=DDL.curie('soluble_iron_micromol'),
                      model_uri=DDL.soluble_iron_micromol, domain=None, range=Optional[float])

slots.bicarbonate_millimol = Slot(uri=DDL.bicarbonate_millimol, name="bicarbonate_millimol", curie=DDL.curie('bicarbonate_millimol'),
                      model_uri=DDL.bicarbonate_millimol, domain=None, range=Optional[float])

slots.h2s_millimol = Slot(uri=DDL.h2s_millimol, name="h2s_millimol", curie=DDL.curie('h2s_millimol'),
                      model_uri=DDL.h2s_millimol, domain=None, range=Optional[float])

slots.h2s_present = Slot(uri=DDL.h2s_present, name="h2s_present", curie=DDL.curie('h2s_present'),
                      model_uri=DDL.h2s_present, domain=None, range=Optional[str])

slots.irradiance = Slot(uri=DDL.irradiance, name="irradiance", curie=DDL.curie('irradiance'),
                      model_uri=DDL.irradiance, domain=None, range=Optional[str])

slots.oxygen_presence = Slot(uri=DDL.oxygen_presence, name="oxygen_presence", curie=DDL.curie('oxygen_presence'),
                      model_uri=DDL.oxygen_presence, domain=None, range=Optional[str])

slots.methane_conc_millimol = Slot(uri=DDL.methane_conc_millimol, name="methane_conc_millimol", curie=DDL.curie('methane_conc_millimol'),
                      model_uri=DDL.methane_conc_millimol, domain=None, range=Optional[float])

slots.growth_temperature2 = Slot(uri=DDL.growth_temperature2, name="growth_temperature2", curie=DDL.curie('growth_temperature2'),
                      model_uri=DDL.growth_temperature2, domain=None, range=Optional[float])

slots.subsurface_depth2 = Slot(uri=DDL.subsurface_depth2, name="subsurface_depth2", curie=DDL.curie('subsurface_depth2'),
                      model_uri=DDL.subsurface_depth2, domain=None, range=Optional[float])

slots.ph1 = Slot(uri=DDL.ph1, name="ph1", curie=DDL.curie('ph1'),
                      model_uri=DDL.ph1, domain=None, range=Optional[float])

slots.ph2 = Slot(uri=DDL.ph2, name="ph2", curie=DDL.curie('ph2'),
                      model_uri=DDL.ph2, domain=None, range=Optional[float])

slots.ph_old = Slot(uri=DDL.ph_old, name="ph_old", curie=DDL.curie('ph_old'),
                      model_uri=DDL.ph_old, domain=None, range=Optional[str])

slots.water_alkalinity_method = Slot(uri=DDL.water_alkalinity_method, name="water_alkalinity_method", curie=DDL.curie('water_alkalinity_method'),
                      model_uri=DDL.water_alkalinity_method, domain=None, range=Optional[str])

slots.water_turbidity = Slot(uri=DDL.water_turbidity, name="water_turbidity", curie=DDL.curie('water_turbidity'),
                      model_uri=DDL.water_turbidity, domain=None, range=Optional[str])

slots.water_size_frac_low = Slot(uri=DDL.water_size_frac_low, name="water_size_frac_low", curie=DDL.curie('water_size_frac_low'),
                      model_uri=DDL.water_size_frac_low, domain=None, range=Optional[float])

slots.water_size_frac_up = Slot(uri=DDL.water_size_frac_up, name="water_size_frac_up", curie=DDL.curie('water_size_frac_up'),
                      model_uri=DDL.water_size_frac_up, domain=None, range=Optional[float])

slots.soil_mean_annual_temp = Slot(uri=DDL.soil_mean_annual_temp, name="soil_mean_annual_temp", curie=DDL.curie('soil_mean_annual_temp'),
                      model_uri=DDL.soil_mean_annual_temp, domain=None, range=Optional[float])

slots.soil_mean_seasonal_temp = Slot(uri=DDL.soil_mean_seasonal_temp, name="soil_mean_seasonal_temp", curie=DDL.curie('soil_mean_seasonal_temp'),
                      model_uri=DDL.soil_mean_seasonal_temp, domain=None, range=Optional[float])

slots.soil_mean_annual_precpt = Slot(uri=DDL.soil_mean_annual_precpt, name="soil_mean_annual_precpt", curie=DDL.curie('soil_mean_annual_precpt'),
                      model_uri=DDL.soil_mean_annual_precpt, domain=None, range=Optional[float])

slots.soil_mean_seasonal_precpt = Slot(uri=DDL.soil_mean_seasonal_precpt, name="soil_mean_seasonal_precpt", curie=DDL.curie('soil_mean_seasonal_precpt'),
                      model_uri=DDL.soil_mean_seasonal_precpt, domain=None, range=Optional[float])

slots.test_package_id = Slot(uri=DDL.test_package_id, name="test_package_id", curie=DDL.curie('test_package_id'),
                      model_uri=DDL.test_package_id, domain=None, range=Optional[int])

slots.soil_package_id = Slot(uri=DDL.soil_package_id, name="soil_package_id", curie=DDL.curie('soil_package_id'),
                      model_uri=DDL.soil_package_id, domain=None, range=Optional[int])

slots.water_package_id = Slot(uri=DDL.water_package_id, name="water_package_id", curie=DDL.curie('water_package_id'),
                      model_uri=DDL.water_package_id, domain=None, range=Optional[int])

slots.global_package_id = Slot(uri=DDL.global_package_id, name="global_package_id", curie=DDL.curie('global_package_id'),
                      model_uri=DDL.global_package_id, domain=None, range=Optional[int])

slots.envo_biome_id = Slot(uri=DDL.envo_biome_id, name="envo_biome_id", curie=DDL.curie('envo_biome_id'),
                      model_uri=DDL.envo_biome_id, domain=None, range=Optional[str])

slots.envo_feature_id = Slot(uri=DDL.envo_feature_id, name="envo_feature_id", curie=DDL.curie('envo_feature_id'),
                      model_uri=DDL.envo_feature_id, domain=None, range=Optional[str])

slots.envo_material_id = Slot(uri=DDL.envo_material_id, name="envo_material_id", curie=DDL.curie('envo_material_id'),
                      model_uri=DDL.envo_material_id, domain=None, range=Optional[str])

slots.username = Slot(uri=DDL.username, name="username", curie=DDL.curie('username'),
                      model_uri=DDL.username, domain=None, range=Optional[str])

slots.password = Slot(uri=DDL.password, name="password", curie=DDL.curie('password'),
                      model_uri=DDL.password, domain=None, range=Optional[str])

slots.name = Slot(uri=DDL.name, name="name", curie=DDL.curie('name'),
                      model_uri=DDL.name, domain=None, range=Optional[str])

slots.title = Slot(uri=DDL.title, name="title", curie=DDL.curie('title'),
                      model_uri=DDL.title, domain=None, range=Optional[str])

slots.department = Slot(uri=DDL.department, name="department", curie=DDL.curie('department'),
                      model_uri=DDL.department, domain=None, range=Optional[str])

slots.email = Slot(uri=DDL.email, name="email", curie=DDL.curie('email'),
                      model_uri=DDL.email, domain=None, range=Optional[str])

slots.phone = Slot(uri=DDL.phone, name="phone", curie=DDL.curie('phone'),
                      model_uri=DDL.phone, domain=None, range=Optional[str])

slots.organization = Slot(uri=DDL.organization, name="organization", curie=DDL.curie('organization'),
                      model_uri=DDL.organization, domain=None, range=Optional[str])

slots.address = Slot(uri=DDL.address, name="address", curie=DDL.curie('address'),
                      model_uri=DDL.address, domain=None, range=Optional[str])

slots.city = Slot(uri=DDL.city, name="city", curie=DDL.curie('city'),
                      model_uri=DDL.city, domain=None, range=Optional[str])

slots.state = Slot(uri=DDL.state, name="state", curie=DDL.curie('state'),
                      model_uri=DDL.state, domain=None, range=Optional[str])

slots.country = Slot(uri=DDL.country, name="country", curie=DDL.curie('country'),
                      model_uri=DDL.country, domain=None, range=Optional[str])

slots.x_super_user = Slot(uri=DDL.x_super_user, name="x_super_user", curie=DDL.curie('x_super_user'),
                      model_uri=DDL.x_super_user, domain=None, range=Optional[str])

slots.x_img_editor = Slot(uri=DDL.x_img_editor, name="x_img_editor", curie=DDL.curie('x_img_editor'),
                      model_uri=DDL.x_img_editor, domain=None, range=Optional[str])

slots.x_img_group = Slot(uri=DDL.x_img_group, name="x_img_group", curie=DDL.curie('x_img_group'),
                      model_uri=DDL.x_img_group, domain=None, range=Optional[float])

slots.jgi_user = Slot(uri=DDL.jgi_user, name="jgi_user", curie=DDL.curie('jgi_user'),
                      model_uri=DDL.jgi_user, domain=None, range=Optional[str])

slots.x_img_editing_level = Slot(uri=DDL.x_img_editing_level, name="x_img_editing_level", curie=DDL.curie('x_img_editing_level'),
                      model_uri=DDL.x_img_editing_level, domain=None, range=Optional[str])

slots.caliban_id = Slot(uri=DDL.caliban_id, name="caliban_id", curie=DDL.curie('caliban_id'),
                      model_uri=DDL.caliban_id, domain=None, range=Optional[int])

slots.caliban_user_name = Slot(uri=DDL.caliban_user_name, name="caliban_user_name", curie=DDL.curie('caliban_user_name'),
                      model_uri=DDL.caliban_user_name, domain=None, range=Optional[str])

slots.url = Slot(uri=DDL.url, name="url", curie=DDL.curie('url'),
                      model_uri=DDL.url, domain=None, range=Optional[str])

slots.x_img_contact_id = Slot(uri=DDL.x_img_contact_id, name="x_img_contact_id", curie=DDL.curie('x_img_contact_id'),
                      model_uri=DDL.x_img_contact_id, domain=None, range=Optional[int])

slots.master_contact_id = Slot(uri=DDL.master_contact_id, name="master_contact_id", curie=DDL.curie('master_contact_id'),
                      model_uri=DDL.master_contact_id, domain=None, range=Optional[int])

slots.oracle_user_name = Slot(uri=DDL.oracle_user_name, name="oracle_user_name", curie=DDL.curie('oracle_user_name'),
                      model_uri=DDL.oracle_user_name, domain=None, range=Optional[str])

slots.user_role = Slot(uri=DDL.user_role, name="user_role", curie=DDL.curie('user_role'),
                      model_uri=DDL.user_role, domain=None, range=Optional[str])

slots.geba_organism_avail_count = Slot(uri=DDL.geba_organism_avail_count, name="geba_organism_avail_count", curie=DDL.curie('geba_organism_avail_count'),
                      model_uri=DDL.geba_organism_avail_count, domain=None, range=Optional[float])

slots.geba_reviewer = Slot(uri=DDL.geba_reviewer, name="geba_reviewer", curie=DDL.curie('geba_reviewer'),
                      model_uri=DDL.geba_reviewer, domain=None, range=Optional[str])

slots.term = Slot(uri=DDL.term, name="term", curie=DDL.curie('term'),
                      model_uri=DDL.term, domain=None, range=Optional[str])

slots.sequence = Slot(uri=DDL.sequence, name="sequence", curie=DDL.curie('sequence'),
                      model_uri=DDL.sequence, domain=None, range=Optional[float])

slots.envo_label = Slot(uri=DDL.envo_label, name="envo_label", curie=DDL.curie('envo_label'),
                      model_uri=DDL.envo_label, domain=None, range=Optional[str])

slots.laboratory = Slot(uri=DDL.laboratory, name="laboratory", curie=DDL.curie('laboratory'),
                      model_uri=DDL.laboratory, domain=None, range=Optional[str])

slots.is_curated = Slot(uri=DDL.is_curated, name="is_curated", curie=DDL.curie('is_curated'),
                      model_uri=DDL.is_curated, domain=None, range=Optional[str])

slots.biotic_relationship_id = Slot(uri=DDL.biotic_relationship_id, name="biotic_relationship_id", curie=DDL.curie('biotic_relationship_id'),
                      model_uri=DDL.biotic_relationship_id, domain=None, range=Optional[int])

slots.body_product_id = Slot(uri=DDL.body_product_id, name="body_product_id", curie=DDL.curie('body_product_id'),
                      model_uri=DDL.body_product_id, domain=None, range=Optional[int])

slots.cell_arrangement_id = Slot(uri=DDL.cell_arrangement_id, name="cell_arrangement_id", curie=DDL.curie('cell_arrangement_id'),
                      model_uri=DDL.cell_arrangement_id, domain=None, range=Optional[int])

slots.disease_id = Slot(uri=DDL.disease_id, name="disease_id", curie=DDL.curie('disease_id'),
                      model_uri=DDL.disease_id, domain=None, range=Optional[int])

slots.energy_source_id = Slot(uri=DDL.energy_source_id, name="energy_source_id", curie=DDL.curie('energy_source_id'),
                      model_uri=DDL.energy_source_id, domain=None, range=Optional[int])

slots.habitat_id = Slot(uri=DDL.habitat_id, name="habitat_id", curie=DDL.curie('habitat_id'),
                      model_uri=DDL.habitat_id, domain=None, range=Optional[int])

slots.metabolism_id = Slot(uri=DDL.metabolism_id, name="metabolism_id", curie=DDL.curie('metabolism_id'),
                      model_uri=DDL.metabolism_id, domain=None, range=Optional[int])

slots.phenotype_id = Slot(uri=DDL.phenotype_id, name="phenotype_id", curie=DDL.curie('phenotype_id'),
                      model_uri=DDL.phenotype_id, domain=None, range=Optional[int])

slots.exemplar_doi = Slot(uri=DDL.exemplar_doi, name="exemplar_doi", curie=DDL.curie('exemplar_doi'),
                      model_uri=DDL.exemplar_doi, domain=None, range=Optional[str])

slots.exemplar_name = Slot(uri=DDL.exemplar_name, name="exemplar_name", curie=DDL.curie('exemplar_name'),
                      model_uri=DDL.exemplar_name, domain=None, range=Optional[str])

slots.taxon_doi = Slot(uri=DDL.taxon_doi, name="taxon_doi", curie=DDL.curie('taxon_doi'),
                      model_uri=DDL.taxon_doi, domain=None, range=Optional[str])

slots.culture_collection_id = Slot(uri=DDL.culture_collection_id, name="culture_collection_id", curie=DDL.curie('culture_collection_id'),
                      model_uri=DDL.culture_collection_id, domain=None, range=Optional[str])

slots.type_strain = Slot(uri=DDL.type_strain, name="type_strain", curie=DDL.curie('type_strain'),
                      model_uri=DDL.type_strain, domain=None, range=Optional[str])

slots.biosafety_level = Slot(uri=DDL.biosafety_level, name="biosafety_level", curie=DDL.curie('biosafety_level'),
                      model_uri=DDL.biosafety_level, domain=None, range=Optional[str])

slots.strain_info_id = Slot(uri=DDL.strain_info_id, name="strain_info_id", curie=DDL.curie('strain_info_id'),
                      model_uri=DDL.strain_info_id, domain=None, range=Optional[int])

slots.genbank_16s_id = Slot(uri=DDL.genbank_16s_id, name="genbank_16s_id", curie=DDL.curie('genbank_16s_id'),
                      model_uri=DDL.genbank_16s_id, domain=None, range=Optional[str])

slots.oxygen_requirement = Slot(uri=DDL.oxygen_requirement, name="oxygen_requirement", curie=DDL.curie('oxygen_requirement'),
                      model_uri=DDL.oxygen_requirement, domain=None, range=Optional[str])

slots.cell_shape = Slot(uri=DDL.cell_shape, name="cell_shape", curie=DDL.curie('cell_shape'),
                      model_uri=DDL.cell_shape, domain=None, range=Optional[str])

slots.motility = Slot(uri=DDL.motility, name="motility", curie=DDL.curie('motility'),
                      model_uri=DDL.motility, domain=None, range=Optional[str])

slots.sporulation = Slot(uri=DDL.sporulation, name="sporulation", curie=DDL.curie('sporulation'),
                      model_uri=DDL.sporulation, domain=None, range=Optional[str])

slots.temperature_range = Slot(uri=DDL.temperature_range, name="temperature_range", curie=DDL.curie('temperature_range'),
                      model_uri=DDL.temperature_range, domain=None, range=Optional[str])

slots.color = Slot(uri=DDL.color, name="color", curie=DDL.curie('color'),
                      model_uri=DDL.color, domain=None, range=Optional[str])

slots.gram_stain = Slot(uri=DDL.gram_stain, name="gram_stain", curie=DDL.curie('gram_stain'),
                      model_uri=DDL.gram_stain, domain=None, range=Optional[str])

slots.common_name = Slot(uri=DDL.common_name, name="common_name", curie=DDL.curie('common_name'),
                      model_uri=DDL.common_name, domain=None, range=Optional[str])

slots.symbiotic_relationship = Slot(uri=DDL.symbiotic_relationship, name="symbiotic_relationship", curie=DDL.curie('symbiotic_relationship'),
                      model_uri=DDL.symbiotic_relationship, domain=None, range=Optional[str])

slots.symbiotic_physical_interaction = Slot(uri=DDL.symbiotic_physical_interaction, name="symbiotic_physical_interaction", curie=DDL.curie('symbiotic_physical_interaction'),
                      model_uri=DDL.symbiotic_physical_interaction, domain=None, range=Optional[str])

slots.symbiont_name = Slot(uri=DDL.symbiont_name, name="symbiont_name", curie=DDL.curie('symbiont_name'),
                      model_uri=DDL.symbiont_name, domain=None, range=Optional[str])

slots.symbiont_taxon_id = Slot(uri=DDL.symbiont_taxon_id, name="symbiont_taxon_id", curie=DDL.curie('symbiont_taxon_id'),
                      model_uri=DDL.symbiont_taxon_id, domain=None, range=Optional[int])

slots.cell_length = Slot(uri=DDL.cell_length, name="cell_length", curie=DDL.curie('cell_length'),
                      model_uri=DDL.cell_length, domain=None, range=Optional[str])

slots.commercial = Slot(uri=DDL.commercial, name="commercial", curie=DDL.curie('commercial'),
                      model_uri=DDL.commercial, domain=None, range=Optional[str])

slots.commercial_comments = Slot(uri=DDL.commercial_comments, name="commercial_comments", curie=DDL.curie('commercial_comments'),
                      model_uri=DDL.commercial_comments, domain=None, range=Optional[str])

slots.other_names = Slot(uri=DDL.other_names, name="other_names", curie=DDL.curie('other_names'),
                      model_uri=DDL.other_names, domain=None, range=Optional[str])

slots.synonym_group_id = Slot(uri=DDL.synonym_group_id, name="synonym_group_id", curie=DDL.curie('synonym_group_id'),
                      model_uri=DDL.synonym_group_id, domain=None, range=Optional[int])

slots.viral_group = Slot(uri=DDL.viral_group, name="viral_group", curie=DDL.curie('viral_group'),
                      model_uri=DDL.viral_group, domain=None, range=Optional[str])

slots.viral_subgroup = Slot(uri=DDL.viral_subgroup, name="viral_subgroup", curie=DDL.curie('viral_subgroup'),
                      model_uri=DDL.viral_subgroup, domain=None, range=Optional[str])

slots.culture_type = Slot(uri=DDL.culture_type, name="culture_type", curie=DDL.curie('culture_type'),
                      model_uri=DDL.culture_type, domain=None, range=Optional[str])

slots.uncultured_type = Slot(uri=DDL.uncultured_type, name="uncultured_type", curie=DDL.curie('uncultured_type'),
                      model_uri=DDL.uncultured_type, domain=None, range=Optional[str])

slots.organism_type = Slot(uri=DDL.organism_type, name="organism_type", curie=DDL.curie('organism_type'),
                      model_uri=DDL.organism_type, domain=None, range=Optional[str])

slots.cultured = Slot(uri=DDL.cultured, name="cultured", curie=DDL.curie('cultured'),
                      model_uri=DDL.cultured, domain=None, range=Optional[str])

slots.clade = Slot(uri=DDL.clade, name="clade", curie=DDL.curie('clade'),
                      model_uri=DDL.clade, domain=None, range=Optional[str])

slots.master_group_id = Slot(uri=DDL.master_group_id, name="master_group_id", curie=DDL.curie('master_group_id'),
                      model_uri=DDL.master_group_id, domain=None, range=Optional[int])

slots.ecotype = Slot(uri=DDL.ecotype, name="ecotype", curie=DDL.curie('ecotype'),
                      model_uri=DDL.ecotype, domain=None, range=Optional[str])

slots.biosample_id = Slot(uri=DDL.biosample_id, name="biosample_id", curie=DDL.curie('biosample_id'),
                      model_uri=DDL.biosample_id, domain=None, range=Optional[int])

slots.carbon_source = Slot(uri=DDL.carbon_source, name="carbon_source", curie=DDL.curie('carbon_source'),
                      model_uri=DDL.carbon_source, domain=None, range=Optional[str])

slots.image_id = Slot(uri=DDL.image_id, name="image_id", curie=DDL.curie('image_id'),
                      model_uri=DDL.image_id, domain=None, range=Optional[int])

slots.ncbi_biosample_id = Slot(uri=DDL.ncbi_biosample_id, name="ncbi_biosample_id", curie=DDL.curie('ncbi_biosample_id'),
                      model_uri=DDL.ncbi_biosample_id, domain=None, range=Optional[str])

slots.organism_name = Slot(uri=DDL.organism_name, name="organism_name", curie=DDL.curie('organism_name'),
                      model_uri=DDL.organism_name, domain=None, range=Optional[str])

slots.submit_organism_name = Slot(uri=DDL.submit_organism_name, name="submit_organism_name", curie=DDL.curie('submit_organism_name'),
                      model_uri=DDL.submit_organism_name, domain=None, range=Optional[str])

slots.genus_synonyms = Slot(uri=DDL.genus_synonyms, name="genus_synonyms", curie=DDL.curie('genus_synonyms'),
                      model_uri=DDL.genus_synonyms, domain=None, range=Optional[str])

slots.species_synonyms = Slot(uri=DDL.species_synonyms, name="species_synonyms", curie=DDL.curie('species_synonyms'),
                      model_uri=DDL.species_synonyms, domain=None, range=Optional[str])

slots.cell_diameter = Slot(uri=DDL.cell_diameter, name="cell_diameter", curie=DDL.curie('cell_diameter'),
                      model_uri=DDL.cell_diameter, domain=None, range=Optional[str])

slots.is_virocell = Slot(uri=DDL.is_virocell, name="is_virocell", curie=DDL.curie('is_virocell'),
                      model_uri=DDL.is_virocell, domain=None, range=Optional[str])

slots.straininfo_group_id = Slot(uri=DDL.straininfo_group_id, name="straininfo_group_id", curie=DDL.curie('straininfo_group_id'),
                      model_uri=DDL.straininfo_group_id, domain=None, range=Optional[int])

slots.source = Slot(uri=DDL.source, name="source", curie=DDL.curie('source'),
                      model_uri=DDL.source, domain=None, range=Optional[str])

slots.gold_class = Slot(uri=DDL.gold_class, name="gold_class", curie=DDL.curie('gold_class'),
                      model_uri=DDL.gold_class, domain=None, range=Optional[str])

slots.gold_order = Slot(uri=DDL.gold_order, name="gold_order", curie=DDL.curie('gold_order'),
                      model_uri=DDL.gold_order, domain=None, range=Optional[str])

slots.gold_family = Slot(uri=DDL.gold_family, name="gold_family", curie=DDL.curie('gold_family'),
                      model_uri=DDL.gold_family, domain=None, range=Optional[str])

slots.taxonomy_status = Slot(uri=DDL.taxonomy_status, name="taxonomy_status", curie=DDL.curie('taxonomy_status'),
                      model_uri=DDL.taxonomy_status, domain=None, range=Optional[str])

slots.soil_sample_biomass = Slot(uri=DDL.soil_sample_biomass, name="soil_sample_biomass", curie=DDL.curie('soil_sample_biomass'),
                      model_uri=DDL.soil_sample_biomass, domain=None, range=Optional[float])

slots.soil_sample_volume = Slot(uri=DDL.soil_sample_volume, name="soil_sample_volume", curie=DDL.curie('soil_sample_volume'),
                      model_uri=DDL.soil_sample_volume, domain=None, range=Optional[float])

slots.img_breadth_calc = Slot(uri=DDL.img_breadth_calc, name="img_breadth_calc", curie=DDL.curie('img_breadth_calc'),
                      model_uri=DDL.img_breadth_calc, domain=None, range=Optional[float])

slots.sample_collection_temperature = Slot(uri=DDL.sample_collection_temperature, name="sample_collection_temperature", curie=DDL.curie('sample_collection_temperature'),
                      model_uri=DDL.sample_collection_temperature, domain=None, range=Optional[float])

slots.sample_collection_temperature2 = Slot(uri=DDL.sample_collection_temperature2, name="sample_collection_temperature2", curie=DDL.curie('sample_collection_temperature2'),
                      model_uri=DDL.sample_collection_temperature2, domain=None, range=Optional[float])

slots.subsurface_depth1 = Slot(uri=DDL.subsurface_depth1, name="subsurface_depth1", curie=DDL.curie('subsurface_depth1'),
                      model_uri=DDL.subsurface_depth1, domain=None, range=Optional[float])

slots.project_name = Slot(uri=DDL.project_name, name="project_name", curie=DDL.curie('project_name'),
                      model_uri=DDL.project_name, domain=None, range=Optional[str])

slots.specimen_id = Slot(uri=DDL.specimen_id, name="specimen_id", curie=DDL.curie('specimen_id'),
                      model_uri=DDL.specimen_id, domain=None, range=Optional[int])

slots.nucleic_acid = Slot(uri=DDL.nucleic_acid, name="nucleic_acid", curie=DDL.curie('nucleic_acid'),
                      model_uri=DDL.nucleic_acid, domain=None, range=Optional[str])

slots.submitter_project_name = Slot(uri=DDL.submitter_project_name, name="submitter_project_name", curie=DDL.curie('submitter_project_name'),
                      model_uri=DDL.submitter_project_name, domain=None, range=Optional[str])

slots.ncbi_project_name = Slot(uri=DDL.ncbi_project_name, name="ncbi_project_name", curie=DDL.curie('ncbi_project_name'),
                      model_uri=DDL.ncbi_project_name, domain=None, range=Optional[str])

slots.pmo_project_id = Slot(uri=DDL.pmo_project_id, name="pmo_project_id", curie=DDL.curie('pmo_project_id'),
                      model_uri=DDL.pmo_project_id, domain=None, range=Optional[int])

slots.its_spid = Slot(uri=DDL.its_spid, name="its_spid", curie=DDL.curie('its_spid'),
                      model_uri=DDL.its_spid, domain=None, range=Optional[float])

slots.old_legacy_gold_id = Slot(uri=DDL.old_legacy_gold_id, name="old_legacy_gold_id", curie=DDL.curie('old_legacy_gold_id'),
                      model_uri=DDL.old_legacy_gold_id, domain=None, range=Optional[str])

slots.legacy_gold_id = Slot(uri=DDL.legacy_gold_id, name="legacy_gold_id", curie=DDL.curie('legacy_gold_id'),
                      model_uri=DDL.legacy_gold_id, domain=None, range=Optional[str])

slots.sequencing_status_id = Slot(uri=DDL.sequencing_status_id, name="sequencing_status_id", curie=DDL.curie('sequencing_status_id'),
                      model_uri=DDL.sequencing_status_id, domain=None, range=Optional[int])

slots.sequencing_quality_id = Slot(uri=DDL.sequencing_quality_id, name="sequencing_quality_id", curie=DDL.curie('sequencing_quality_id'),
                      model_uri=DDL.sequencing_quality_id, domain=None, range=Optional[int])

slots.finishing_goal_id = Slot(uri=DDL.finishing_goal_id, name="finishing_goal_id", curie=DDL.curie('finishing_goal_id'),
                      model_uri=DDL.finishing_goal_id, domain=None, range=Optional[int])

slots.sequencing_comments = Slot(uri=DDL.sequencing_comments, name="sequencing_comments", curie=DDL.curie('sequencing_comments'),
                      model_uri=DDL.sequencing_comments, domain=None, range=Optional[str])

slots.gc_percent = Slot(uri=DDL.gc_percent, name="gc_percent", curie=DDL.curie('gc_percent'),
                      model_uri=DDL.gc_percent, domain=None, range=Optional[float])

slots.chromosome_count = Slot(uri=DDL.chromosome_count, name="chromosome_count", curie=DDL.curie('chromosome_count'),
                      model_uri=DDL.chromosome_count, domain=None, range=Optional[float])

slots.plasmid_count = Slot(uri=DDL.plasmid_count, name="plasmid_count", curie=DDL.curie('plasmid_count'),
                      model_uri=DDL.plasmid_count, domain=None, range=Optional[float])

slots.est_count = Slot(uri=DDL.est_count, name="est_count", curie=DDL.curie('est_count'),
                      model_uri=DDL.est_count, domain=None, range=Optional[float])

slots.project_comments = Slot(uri=DDL.project_comments, name="project_comments", curie=DDL.curie('project_comments'),
                      model_uri=DDL.project_comments, domain=None, range=Optional[str])

slots.its_proposal_id = Slot(uri=DDL.its_proposal_id, name="its_proposal_id", curie=DDL.curie('its_proposal_id'),
                      model_uri=DDL.its_proposal_id, domain=None, range=Optional[int])

slots.gpts_proposal_id = Slot(uri=DDL.gpts_proposal_id, name="gpts_proposal_id", curie=DDL.curie('gpts_proposal_id'),
                      model_uri=DDL.gpts_proposal_id, domain=None, range=Optional[int])

slots.ncbi_sra_id = Slot(uri=DDL.ncbi_sra_id, name="ncbi_sra_id", curie=DDL.curie('ncbi_sra_id'),
                      model_uri=DDL.ncbi_sra_id, domain=None, range=Optional[str])

slots.library_method = Slot(uri=DDL.library_method, name="library_method", curie=DDL.curie('library_method'),
                      model_uri=DDL.library_method, domain=None, range=Optional[str])

slots.read_count = Slot(uri=DDL.read_count, name="read_count", curie=DDL.curie('read_count'),
                      model_uri=DDL.read_count, domain=None, range=Optional[str])

slots.vector = Slot(uri=DDL.vector, name="vector", curie=DDL.curie('vector'),
                      model_uri=DDL.vector, domain=None, range=Optional[str])

slots.read_size = Slot(uri=DDL.read_size, name="read_size", curie=DDL.curie('read_size'),
                      model_uri=DDL.read_size, domain=None, range=Optional[str])

slots.ncbi_locus_tag = Slot(uri=DDL.ncbi_locus_tag, name="ncbi_locus_tag", curie=DDL.curie('ncbi_locus_tag'),
                      model_uri=DDL.ncbi_locus_tag, domain=None, range=Optional[str])

slots.assembly_accession = Slot(uri=DDL.assembly_accession, name="assembly_accession", curie=DDL.curie('assembly_accession'),
                      model_uri=DDL.assembly_accession, domain=None, range=Optional[str])

slots.nucleic_acid_id = Slot(uri=DDL.nucleic_acid_id, name="nucleic_acid_id", curie=DDL.curie('nucleic_acid_id'),
                      model_uri=DDL.nucleic_acid_id, domain=None, range=Optional[int])

slots.project_status = Slot(uri=DDL.project_status, name="project_status", curie=DDL.curie('project_status'),
                      model_uri=DDL.project_status, domain=None, range=Optional[str])

slots.master_study_id = Slot(uri=DDL.master_study_id, name="master_study_id", curie=DDL.curie('master_study_id'),
                      model_uri=DDL.master_study_id, domain=None, range=Optional[int])

slots.other_project_names = Slot(uri=DDL.other_project_names, name="other_project_names", curie=DDL.curie('other_project_names'),
                      model_uri=DDL.other_project_names, domain=None, range=Optional[str])

slots.its_project_name = Slot(uri=DDL.its_project_name, name="its_project_name", curie=DDL.curie('its_project_name'),
                      model_uri=DDL.its_project_name, domain=None, range=Optional[str])

slots.is_single_cell_material = Slot(uri=DDL.is_single_cell_material, name="is_single_cell_material", curie=DDL.curie('is_single_cell_material'),
                      model_uri=DDL.is_single_cell_material, domain=None, range=Optional[str])

slots.its_sequencing_product_name = Slot(uri=DDL.its_sequencing_product_name, name="its_sequencing_product_name", curie=DDL.curie('its_sequencing_product_name'),
                      model_uri=DDL.its_sequencing_product_name, domain=None, range=Optional[str])

slots.project_manager_id = Slot(uri=DDL.project_manager_id, name="project_manager_id", curie=DDL.curie('project_manager_id'),
                      model_uri=DDL.project_manager_id, domain=None, range=Optional[int])

slots.low_quality_genome = Slot(uri=DDL.low_quality_genome, name="low_quality_genome", curie=DDL.curie('low_quality_genome'),
                      model_uri=DDL.low_quality_genome, domain=None, range=Optional[str])

slots.sequencing_strategy = Slot(uri=DDL.sequencing_strategy, name="sequencing_strategy", curie=DDL.curie('sequencing_strategy'),
                      model_uri=DDL.sequencing_strategy, domain=None, range=Optional[str])

slots.is_jgi = Slot(uri=DDL.is_jgi, name="is_jgi", curie=DDL.curie('is_jgi'),
                      model_uri=DDL.is_jgi, domain=None, range=Optional[str])

slots.sra_srs_accession = Slot(uri=DDL.sra_srs_accession, name="sra_srs_accession", curie=DDL.curie('sra_srs_accession'),
                      model_uri=DDL.sra_srs_accession, domain=None, range=Optional[str])

slots.sra_srx_accession = Slot(uri=DDL.sra_srx_accession, name="sra_srx_accession", curie=DDL.curie('sra_srx_accession'),
                      model_uri=DDL.sra_srx_accession, domain=None, range=Optional[str])

slots.funding_program = Slot(uri=DDL.funding_program, name="funding_program", curie=DDL.curie('funding_program'),
                      model_uri=DDL.funding_program, domain=None, range=Optional[str])

slots.funding_year = Slot(uri=DDL.funding_year, name="funding_year", curie=DDL.curie('funding_year'),
                      model_uri=DDL.funding_year, domain=None, range=Optional[float])

slots.its_sample_id = Slot(uri=DDL.its_sample_id, name="its_sample_id", curie=DDL.curie('its_sample_id'),
                      model_uri=DDL.its_sample_id, domain=None, range=Optional[int])

slots.its_sample_group_name = Slot(uri=DDL.its_sample_group_name, name="its_sample_group_name", curie=DDL.curie('its_sample_group_name'),
                      model_uri=DDL.its_sample_group_name, domain=None, range=Optional[str])

slots.experimental_conditions = Slot(uri=DDL.experimental_conditions, name="experimental_conditions", curie=DDL.curie('experimental_conditions'),
                      model_uri=DDL.experimental_conditions, domain=None, range=Optional[str])

slots.sample_group_name = Slot(uri=DDL.sample_group_name, name="sample_group_name", curie=DDL.curie('sample_group_name'),
                      model_uri=DDL.sample_group_name, domain=None, range=Optional[str])

slots.its_sample_name = Slot(uri=DDL.its_sample_name, name="its_sample_name", curie=DDL.curie('its_sample_name'),
                      model_uri=DDL.its_sample_name, domain=None, range=Optional[str])

slots.project_subtype = Slot(uri=DDL.project_subtype, name="project_subtype", curie=DDL.curie('project_subtype'),
                      model_uri=DDL.project_subtype, domain=None, range=Optional[str])

slots.sequencing_strategy_full = Slot(uri=DDL.sequencing_strategy_full, name="sequencing_strategy_full", curie=DDL.curie('sequencing_strategy_full'),
                      model_uri=DDL.sequencing_strategy_full, domain=None, range=Optional[str])

slots.is_approved = Slot(uri=DDL.is_approved, name="is_approved", curie=DDL.curie('is_approved'),
                      model_uri=DDL.is_approved, domain=None, range=Optional[str])

slots.is_locked = Slot(uri=DDL.is_locked, name="is_locked", curie=DDL.curie('is_locked'),
                      model_uri=DDL.is_locked, domain=None, range=Optional[str])

slots.gpts_sample_id = Slot(uri=DDL.gpts_sample_id, name="gpts_sample_id", curie=DDL.curie('gpts_sample_id'),
                      model_uri=DDL.gpts_sample_id, domain=None, range=Optional[int])

slots.gpts_disambiguator = Slot(uri=DDL.gpts_disambiguator, name="gpts_disambiguator", curie=DDL.curie('gpts_disambiguator'),
                      model_uri=DDL.gpts_disambiguator, domain=None, range=Optional[str])

slots.analysis_project_id = Slot(uri=DDL.analysis_project_id, name="analysis_project_id", curie=DDL.curie('analysis_project_id'),
                      model_uri=DDL.analysis_project_id, domain=None, range=Optional[int])

slots.institution_id = Slot(uri=DDL.institution_id, name="institution_id", curie=DDL.curie('institution_id'),
                      model_uri=DDL.institution_id, domain=None, range=Optional[int])

slots.publication_id = Slot(uri=DDL.publication_id, name="publication_id", curie=DDL.curie('publication_id'),
                      model_uri=DDL.publication_id, domain=None, range=Optional[int])

slots.relevance_id = Slot(uri=DDL.relevance_id, name="relevance_id", curie=DDL.curie('relevance_id'),
                      model_uri=DDL.relevance_id, domain=None, range=Optional[int])

slots.sequencing_method_id = Slot(uri=DDL.sequencing_method_id, name="sequencing_method_id", curie=DDL.curie('sequencing_method_id'),
                      model_uri=DDL.sequencing_method_id, domain=None, range=Optional[int])

slots.doi = Slot(uri=DDL.doi, name="doi", curie=DDL.curie('doi'),
                      model_uri=DDL.doi, domain=None, range=Optional[str])

slots.pubmed_id = Slot(uri=DDL.pubmed_id, name="pubmed_id", curie=DDL.curie('pubmed_id'),
                      model_uri=DDL.pubmed_id, domain=None, range=Optional[int])

slots.journal_id = Slot(uri=DDL.journal_id, name="journal_id", curie=DDL.curie('journal_id'),
                      model_uri=DDL.journal_id, domain=None, range=Optional[int])

slots.pubmodel = Slot(uri=DDL.pubmodel, name="pubmodel", curie=DDL.curie('pubmodel'),
                      model_uri=DDL.pubmodel, domain=None, range=Optional[str])

slots.volume = Slot(uri=DDL.volume, name="volume", curie=DDL.curie('volume'),
                      model_uri=DDL.volume, domain=None, range=Optional[str])

slots.issue = Slot(uri=DDL.issue, name="issue", curie=DDL.curie('issue'),
                      model_uri=DDL.issue, domain=None, range=Optional[str])

slots.page = Slot(uri=DDL.page, name="page", curie=DDL.curie('page'),
                      model_uri=DDL.page, domain=None, range=Optional[str])

slots.publication_date = Slot(uri=DDL.publication_date, name="publication_date", curie=DDL.curie('publication_date'),
                      model_uri=DDL.publication_date, domain=None, range=Optional[str])

slots.abstract = Slot(uri=DDL.abstract, name="abstract", curie=DDL.curie('abstract'),
                      model_uri=DDL.abstract, domain=None, range=Optional[str])

slots.affiliation = Slot(uri=DDL.affiliation, name="affiliation", curie=DDL.curie('affiliation'),
                      model_uri=DDL.affiliation, domain=None, range=Optional[str])

slots.last_author_id = Slot(uri=DDL.last_author_id, name="last_author_id", curie=DDL.curie('last_author_id'),
                      model_uri=DDL.last_author_id, domain=None, range=Optional[int])

slots.first_author_id = Slot(uri=DDL.first_author_id, name="first_author_id", curie=DDL.curie('first_author_id'),
                      model_uri=DDL.first_author_id, domain=None, range=Optional[int])

slots.study_name = Slot(uri=DDL.study_name, name="study_name", curie=DDL.curie('study_name'),
                      model_uri=DDL.study_name, domain=None, range=Optional[str])

slots.ncbi_project_id = Slot(uri=DDL.ncbi_project_id, name="ncbi_project_id", curie=DDL.curie('ncbi_project_id'),
                      model_uri=DDL.ncbi_project_id, domain=None, range=Optional[int])

slots.contact_id = Slot(uri=DDL.contact_id, name="contact_id", curie=DDL.curie('contact_id'),
                      model_uri=DDL.contact_id, domain=None, range=Optional[int])

slots.last_mod_by = Slot(uri=DDL.last_mod_by, name="last_mod_by", curie=DDL.curie('last_mod_by'),
                      model_uri=DDL.last_mod_by, domain=None, range=Optional[float])

slots.bioproject_name = Slot(uri=DDL.bioproject_name, name="bioproject_name", curie=DDL.curie('bioproject_name'),
                      model_uri=DDL.bioproject_name, domain=None, range=Optional[str])

slots.gold_study_name = Slot(uri=DDL.gold_study_name, name="gold_study_name", curie=DDL.curie('gold_study_name'),
                      model_uri=DDL.gold_study_name, domain=None, range=Optional[str])

slots.metagenomic = Slot(uri=DDL.metagenomic, name="metagenomic", curie=DDL.curie('metagenomic'),
                      model_uri=DDL.metagenomic, domain=None, range=Optional[str])

slots.study_type_id = Slot(uri=DDL.study_type_id, name="study_type_id", curie=DDL.curie('study_type_id'),
                      model_uri=DDL.study_type_id, domain=None, range=Optional[int])

slots.owner_id = Slot(uri=DDL.owner_id, name="owner_id", curie=DDL.curie('owner_id'),
                      model_uri=DDL.owner_id, domain=None, range=Optional[int])

slots.public_biosample_count = Slot(uri=DDL.public_biosample_count, name="public_biosample_count", curie=DDL.curie('public_biosample_count'),
                      model_uri=DDL.public_biosample_count, domain=None, range=Optional[float])

slots.admin_biosample_count = Slot(uri=DDL.admin_biosample_count, name="admin_biosample_count", curie=DDL.curie('admin_biosample_count'),
                      model_uri=DDL.admin_biosample_count, domain=None, range=Optional[float])

slots.is_geba = Slot(uri=DDL.is_geba, name="is_geba", curie=DDL.curie('is_geba'),
                      model_uri=DDL.is_geba, domain=None, range=Optional[str])

slots.is_hmp = Slot(uri=DDL.is_hmp, name="is_hmp", curie=DDL.curie('is_hmp'),
                      model_uri=DDL.is_hmp, domain=None, range=Optional[str])
