# Auto generated from kbase.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-06-26 16:36
# Schema: kbase
#
# id: https://microbiomedata/schema/kbase
# description: NMDC rendering of KBase metadata schema
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
from includes.types import Double, String

metamodel_version = "1.4.4"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
KBASE = CurieNamespace('kbase', 'http://kbase.us/')
DEFAULT_ = KBASE


# Types

# Class references



@dataclass
class SESAR(YAMLRoot):
    """
    TODO
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KBASE.SESAR
    class_class_curie: ClassVar[str] = "kbase:SESAR"
    class_name: ClassVar[str] = "SESAR"
    class_model_uri: ClassVar[URIRef] = KBASE.SESAR

    sample_name: Optional[str] = None
    field_name_informal_classification: Optional[str] = None
    location_description: Optional[str] = None
    locality_description: Optional[str] = None
    collection_method: Optional[str] = None
    purpose: Optional[str] = None
    navigation_type: Optional[str] = None
    primary_physiographic_feature: Optional[str] = None
    name_of_physiographic_feature: Optional[str] = None
    field_program_cruise: Optional[str] = None
    collector_chief_scientist: Optional[str] = None
    collection_date_precision: Optional[str] = None
    current_archive: Optional[str] = None
    related_identifiers: Optional[str] = None
    platform_type: Optional[str] = None
    zone: Optional[str] = None
    state_province: Optional[str] = None
    original_archive_contact: Optional[str] = None
    classification: Optional[str] = None
    vertical_datum: Optional[str] = None
    original_archive: Optional[str] = None
    platform_name: Optional[str] = None
    collection_time_end: Optional[str] = None
    county: Optional[str] = None
    size_unit: Optional[str] = None
    age_unit: Optional[str] = None
    locality: Optional[str] = None
    sample_description: Optional[str] = None
    collection_method_description: Optional[str] = None
    other_names: Optional[str] = None
    geological_unit: Optional[str] = None
    collector_chief_scientist_address: Optional[str] = None
    size: Optional[float] = None
    launch_platform_name: Optional[str] = None
    depth_scale: Optional[str] = None
    city_township: Optional[str] = None
    sub-object_type: Optional[str] = None
    launch_id: Optional[str] = None

@dataclass
class ENIGMA(YAMLRoot):
    """
    TODO
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = KBASE.ENIGMA
    class_class_curie: ClassVar[str] = "kbase:ENIGMA"
    class_name: ClassVar[str] = "ENIGMA"
    class_model_uri: ClassVar[URIRef] = KBASE.ENIGMA

    sampleid: Optional[str] = None
    experiment_name: Optional[str] = None
    area_name: Optional[str] = None
    well_name: Optional[str] = None
    environmental_package: Optional[str] = None
    material: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    collection_time: Optional[str] = None
    time_zone: Optional[str] = None
    geological_zone: Optional[str] = None
    recovery_factor: Optional[str] = None
    method: Optional[str] = None
    fraction: Optional[str] = None
    replicate: Optional[str] = None
    maturation_time: Optional[str] = None
    treatment: Optional[str] = None
    temperature_celsius: Optional[str] = None
    moisture: Optional[float] = None
    pore_water_extraction_microliters: Optional[str] = None
    conductivity_ms_cm: Optional[str] = None
    ph: Optional[float] = None
    dapi_cell_count_cells_g: Optional[str] = None
    dna_picogreen_total_ng: Optional[str] = None
    total_carbon_mg_g_dry_weight: Optional[str] = None
    biomass_carbon_mg_g: Optional[str] = None
    total_nitrogen_mg_g_dry_weight: Optional[str] = None
    leucine_activity_ngc_day_cell: Optional[str] = None
    functional_area: Optional[str] = None
    type_of_well: Optional[str] = None
    ground_elevation_ft_amsl: Optional[str] = None
    installation_method: Optional[str] = None
    boring_ft_bgs: Optional[str] = None
    boring_refusal: Optional[str] = None
    boring_diameter_in: Optional[str] = None
    screen_type: Optional[str] = None
    well_casing_type: Optional[str] = None
    well_casing_od_in: Optional[str] = None
    well_casing_id_in: Optional[str] = None
    drive_casing_type: Optional[str] = None
    drive_casing_id_in: Optional[str] = None
    drive_casing_od_in: Optional[str] = None
    drive_casing_start_depth_ft_bgs: Optional[str] = None
    drive_casing_end_depth_ft_bgs: Optional[str] = None
    packing_type: Optional[str] = None
    packing_depth_start_ft_bgs: Optional[str] = None
    packing_depth_end_ft_bgs: Optional[str] = None
    topofweatheredbedrock_ft_bgs: Optional[str] = None
    topoffreshbedrock_ft_bgs: Optional[str] = None
    aquifer: Optional[str] = None
    fractures_cavities_waterbreaks: Optional[str] = None
    other_name: Optional[str] = None
    screened: Optional[str] = None
    open: Optional[str] = None
    well_status: Optional[str] = None
    condition: Optional[str] = None
    origination_or_plug_abandon: Optional[str] = None
    min_water_level_ft_amsl: Optional[str] = None
    average_water_level_ft_amsl: Optional[str] = None
    max_water_level_ft_amsl: Optional[str] = None
    upper_seal_type: Optional[str] = None
    upper_seal_start_depth_ft_bgs: Optional[str] = None
    upper_seal_end_depth_ft_bgs: Optional[str] = None
    lower_seal_type_ft_bgs: Optional[str] = None
    lower_seal_start_depth_ft_bgs: Optional[str] = None
    lower_seal_end_depth_ft_bgs: Optional[str] = None
    open_casing_type: Optional[str] = None
    open_casing_od_in: Optional[str] = None
    open_casing_id_in: Optional[str] = None
    open_casing_depth_ft_bgs: Optional[str] = None
    open_hole_diameter_in: Optional[str] = None
    open_hole_depth_ft_bgs: Optional[str] = None
    open_interval_start_depth_ft_bgs: Optional[str] = None
    open_interval_end_depth_ft_bgs: Optional[str] = None
    open_interval_diameter_in: Optional[str] = None
    rock_formation: Optional[str] = None
    depth: Optional[float] = None
    elevation: Optional[str] = None
    time: Optional[str] = None
    timezone: Optional[str] = None
    env_package: Optional[str] = None
    continent: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    biome: Optional[str] = None
    feature: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    well: Optional[str] = None
    env_pakcage: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


# Slots
class slots:
    pass

slots.age_max = Slot(uri=KBASE.age_max, name="age_max", curie=KBASE.curie('age_max'),
                      model_uri=KBASE.age_max, domain=None, range=Optional[float])

slots.age_min = Slot(uri=KBASE.age_min, name="age_min", curie=KBASE.curie('age_min'),
                      model_uri=KBASE.age_min, domain=None, range=Optional[float])

slots.aodc = Slot(uri=KBASE.aodc, name="aodc", curie=KBASE.curie('aodc'),
                      model_uri=KBASE.aodc, domain=None, range=Optional[float])

slots.aquifer = Slot(uri=KBASE.aquifer, name="aquifer", curie=KBASE.curie('aquifer'),
                      model_uri=KBASE.aquifer, domain=None, range=Optional[str])

slots.area_name = Slot(uri=KBASE.area_name, name="area_name", curie=KBASE.curie('area_name'),
                      model_uri=KBASE.area_name, domain=None, range=Optional[str])

slots.average_water_level = Slot(uri=KBASE.average_water_level, name="average_water_level", curie=KBASE.curie('average_water_level'),
                      model_uri=KBASE.average_water_level, domain=None, range=Optional[float])

slots.biomass_carbon = Slot(uri=KBASE.biomass_carbon, name="biomass_carbon", curie=KBASE.curie('biomass_carbon'),
                      model_uri=KBASE.biomass_carbon, domain=None, range=Optional[float])

slots.biome = Slot(uri=KBASE.biome, name="biome", curie=KBASE.curie('biome'),
                      model_uri=KBASE.biome, domain=None, range=Optional[str])

slots.boncat_activity = Slot(uri=KBASE.boncat_activity, name="boncat_activity", curie=KBASE.curie('boncat_activity'),
                      model_uri=KBASE.boncat_activity, domain=None, range=Optional[float])

slots.boring = Slot(uri=KBASE.boring, name="boring", curie=KBASE.curie('boring'),
                      model_uri=KBASE.boring, domain=None, range=Optional[float])

slots.boring_diameter = Slot(uri=KBASE.boring_diameter, name="boring_diameter", curie=KBASE.curie('boring_diameter'),
                      model_uri=KBASE.boring_diameter, domain=None, range=Optional[float])

slots.boring_refusal = Slot(uri=KBASE.boring_refusal, name="boring_refusal", curie=KBASE.curie('boring_refusal'),
                      model_uri=KBASE.boring_refusal, domain=None, range=Optional[str])

slots.city_township = Slot(uri=KBASE.city_township, name="city_township", curie=KBASE.curie('city_township'),
                      model_uri=KBASE.city_township, domain=None, range=Optional[str])

slots.classification = Slot(uri=KBASE.classification, name="classification", curie=KBASE.curie('classification'),
                      model_uri=KBASE.classification, domain=None, range=Optional[str])

slots.collection_date = Slot(uri=KBASE.collection_date, name="collection_date", curie=KBASE.curie('collection_date'),
                      model_uri=KBASE.collection_date, domain=None, range=Optional[str])

slots.collection_date_end = Slot(uri=KBASE.collection_date_end, name="collection_date_end", curie=KBASE.curie('collection_date_end'),
                      model_uri=KBASE.collection_date_end, domain=None, range=Optional[str])

slots.collection_date_precision = Slot(uri=KBASE.collection_date_precision, name="collection_date_precision", curie=KBASE.curie('collection_date_precision'),
                      model_uri=KBASE.collection_date_precision, domain=None, range=Optional[str])

slots.collection_method = Slot(uri=KBASE.collection_method, name="collection_method", curie=KBASE.curie('collection_method'),
                      model_uri=KBASE.collection_method, domain=None, range=Optional[str])

slots.collection_method_description = Slot(uri=KBASE.collection_method_description, name="collection_method_description", curie=KBASE.curie('collection_method_description'),
                      model_uri=KBASE.collection_method_description, domain=None, range=Optional[str])

slots.collection_time = Slot(uri=KBASE.collection_time, name="collection_time", curie=KBASE.curie('collection_time'),
                      model_uri=KBASE.collection_time, domain=None, range=Optional[str])

slots.collection_time_end = Slot(uri=KBASE.collection_time_end, name="collection_time_end", curie=KBASE.curie('collection_time_end'),
                      model_uri=KBASE.collection_time_end, domain=None, range=Optional[str])

slots.collector_chief_scientist = Slot(uri=KBASE.collector_chief_scientist, name="collector_chief_scientist", curie=KBASE.curie('collector_chief_scientist'),
                      model_uri=KBASE.collector_chief_scientist, domain=None, range=Optional[str])

slots.collector_chief_scientist_address = Slot(uri=KBASE.collector_chief_scientist_address, name="collector_chief_scientist_address", curie=KBASE.curie('collector_chief_scientist_address'),
                      model_uri=KBASE.collector_chief_scientist_address, domain=None, range=Optional[str])

slots.condition = Slot(uri=KBASE.condition, name="condition", curie=KBASE.curie('condition'),
                      model_uri=KBASE.condition, domain=None, range=Optional[str])

slots.conductivity = Slot(uri=KBASE.conductivity, name="conductivity", curie=KBASE.curie('conductivity'),
                      model_uri=KBASE.conductivity, domain=None, range=Optional[float])

slots.continent = Slot(uri=KBASE.continent, name="continent", curie=KBASE.curie('continent'),
                      model_uri=KBASE.continent, domain=None, range=Optional[str])

slots.coordinate_precision? = Slot(uri=KBASE['coordinate_precision?'], name="coordinate_precision?", curie=KBASE.curie('coordinate_precision?'),
                      model_uri=KBASE['coordinate_precision?'], domain=None, range=Optional[str])

slots.country = Slot(uri=KBASE.country, name="country", curie=KBASE.curie('country'),
                      model_uri=KBASE.country, domain=None, range=Optional[str])

slots.county = Slot(uri=KBASE.county, name="county", curie=KBASE.curie('county'),
                      model_uri=KBASE.county, domain=None, range=Optional[str])

slots.current_archive = Slot(uri=KBASE.current_archive, name="current_archive", curie=KBASE.curie('current_archive'),
                      model_uri=KBASE.current_archive, domain=None, range=Optional[str])

slots.current_archive_contact = Slot(uri=KBASE.current_archive_contact, name="current_archive_contact", curie=KBASE.curie('current_archive_contact'),
                      model_uri=KBASE.current_archive_contact, domain=None, range=Optional[str])

slots.dapi_cell_count = Slot(uri=KBASE.dapi_cell_count, name="dapi_cell_count", curie=KBASE.curie('dapi_cell_count'),
                      model_uri=KBASE.dapi_cell_count, domain=None, range=Optional[str])

slots.date = Slot(uri=KBASE.date, name="date", curie=KBASE.curie('date'),
                      model_uri=KBASE.date, domain=None, range=Optional[str])

slots.depth = Slot(uri=KBASE.depth, name="depth", curie=KBASE.curie('depth'),
                      model_uri=KBASE.depth, domain=None, range=Optional[float])

slots.depth_in_core_max = Slot(uri=KBASE.depth_in_core_max, name="depth_in_core_max", curie=KBASE.curie('depth_in_core_max'),
                      model_uri=KBASE.depth_in_core_max, domain=None, range=Optional[float])

slots.depth_in_core_min = Slot(uri=KBASE.depth_in_core_min, name="depth_in_core_min", curie=KBASE.curie('depth_in_core_min'),
                      model_uri=KBASE.depth_in_core_min, domain=None, range=Optional[float])

slots.depth_scale = Slot(uri=KBASE.depth_scale, name="depth_scale", curie=KBASE.curie('depth_scale'),
                      model_uri=KBASE.depth_scale, domain=None, range=Optional[str])

slots.description = Slot(uri=KBASE.description, name="description", curie=KBASE.curie('description'),
                      model_uri=KBASE.description, domain=None, range=Optional[str])

slots.dna_picogreen_total = Slot(uri=KBASE.dna_picogreen_total, name="dna_picogreen_total", curie=KBASE.curie('dna_picogreen_total'),
                      model_uri=KBASE.dna_picogreen_total, domain=None, range=Optional[float])

slots.drive_casing_end_depth = Slot(uri=KBASE.drive_casing_end_depth, name="drive_casing_end_depth", curie=KBASE.curie('drive_casing_end_depth'),
                      model_uri=KBASE.drive_casing_end_depth, domain=None, range=Optional[float])

slots.drive_casing_id = Slot(uri=KBASE.drive_casing_id, name="drive_casing_id", curie=KBASE.curie('drive_casing_id'),
                      model_uri=KBASE.drive_casing_id, domain=None, range=Optional[float])

slots.drive_casing_od = Slot(uri=KBASE.drive_casing_od, name="drive_casing_od", curie=KBASE.curie('drive_casing_od'),
                      model_uri=KBASE.drive_casing_od, domain=None, range=Optional[float])

slots.drive_casing_start_depth = Slot(uri=KBASE.drive_casing_start_depth, name="drive_casing_start_depth", curie=KBASE.curie('drive_casing_start_depth'),
                      model_uri=KBASE.drive_casing_start_depth, domain=None, range=Optional[float])

slots.drive_casing_type = Slot(uri=KBASE.drive_casing_type, name="drive_casing_type", curie=KBASE.curie('drive_casing_type'),
                      model_uri=KBASE.drive_casing_type, domain=None, range=Optional[str])

slots.easting = Slot(uri=KBASE.easting, name="easting", curie=KBASE.curie('easting'),
                      model_uri=KBASE.easting, domain=None, range=Optional[float])

slots.elevation = Slot(uri=KBASE.elevation, name="elevation", curie=KBASE.curie('elevation'),
                      model_uri=KBASE.elevation, domain=None, range=Optional[str])

slots.elevation_end = Slot(uri=KBASE.elevation_end, name="elevation_end", curie=KBASE.curie('elevation_end'),
                      model_uri=KBASE.elevation_end, domain=None, range=Optional[float])

slots.elevation_start = Slot(uri=KBASE.elevation_start, name="elevation_start", curie=KBASE.curie('elevation_start'),
                      model_uri=KBASE.elevation_start, domain=None, range=Optional[float])

slots.env_package = Slot(uri=KBASE.env_package, name="env_package", curie=KBASE.curie('env_package'),
                      model_uri=KBASE.env_package, domain=None, range=Optional[str])

slots.environmental_package = Slot(uri=KBASE.environmental_package, name="environmental_package", curie=KBASE.curie('environmental_package'),
                      model_uri=KBASE.environmental_package, domain=None, range=Optional[str])

slots.experiment_name = Slot(uri=KBASE.experiment_name, name="experiment_name", curie=KBASE.curie('experiment_name'),
                      model_uri=KBASE.experiment_name, domain=None, range=Optional[str])

slots.feature = Slot(uri=KBASE.feature, name="feature", curie=KBASE.curie('feature'),
                      model_uri=KBASE.feature, domain=None, range=Optional[str])

slots.field_name_informal_classification = Slot(uri=KBASE.field_name_informal_classification, name="field_name_informal_classification", curie=KBASE.curie('field_name_informal_classification'),
                      model_uri=KBASE.field_name_informal_classification, domain=None, range=Optional[str])

slots.field_program_cruise = Slot(uri=KBASE.field_program_cruise, name="field_program_cruise", curie=KBASE.curie('field_program_cruise'),
                      model_uri=KBASE.field_program_cruise, domain=None, range=Optional[str])

slots.filter = Slot(uri=KBASE.filter, name="filter", curie=KBASE.curie('filter'),
                      model_uri=KBASE.filter, domain=None, range=Optional[float])

slots.fraction = Slot(uri=KBASE.fraction, name="fraction", curie=KBASE.curie('fraction'),
                      model_uri=KBASE.fraction, domain=None, range=Optional[str])

slots.fractures_cavities_waterbreaks = Slot(uri=KBASE.fractures_cavities_waterbreaks, name="fractures_cavities_waterbreaks", curie=KBASE.curie('fractures_cavities_waterbreaks'),
                      model_uri=KBASE.fractures_cavities_waterbreaks, domain=None, range=Optional[str])

slots.functional_area = Slot(uri=KBASE.functional_area, name="functional_area", curie=KBASE.curie('functional_area'),
                      model_uri=KBASE.functional_area, domain=None, range=Optional[str])

slots.geological_age = Slot(uri=KBASE.geological_age, name="geological_age", curie=KBASE.curie('geological_age'),
                      model_uri=KBASE.geological_age, domain=None, range=Optional[float])

slots.geological_zone = Slot(uri=KBASE.geological_zone, name="geological_zone", curie=KBASE.curie('geological_zone'),
                      model_uri=KBASE.geological_zone, domain=None, range=Optional[str])

slots.ground_elevation = Slot(uri=KBASE.ground_elevation, name="ground_elevation", curie=KBASE.curie('ground_elevation'),
                      model_uri=KBASE.ground_elevation, domain=None, range=Optional[float])

slots.id = Slot(uri=KBASE.id, name="id", curie=KBASE.curie('id'),
                      model_uri=KBASE.id, domain=None, range=Optional[str])

slots.igsn = Slot(uri=KBASE.igsn, name="igsn", curie=KBASE.curie('igsn'),
                      model_uri=KBASE.igsn, domain=None, range=Optional[str])

slots.installation_method = Slot(uri=KBASE.installation_method, name="installation_method", curie=KBASE.curie('installation_method'),
                      model_uri=KBASE.installation_method, domain=None, range=Optional[str])

slots.latitude = Slot(uri=KBASE.latitude, name="latitude", curie=KBASE.curie('latitude'),
                      model_uri=KBASE.latitude, domain=None, range=Optional[float])

slots.launch_id = Slot(uri=KBASE.launch_id, name="launch_id", curie=KBASE.curie('launch_id'),
                      model_uri=KBASE.launch_id, domain=None, range=Optional[str])

slots.launch_platform_name = Slot(uri=KBASE.launch_platform_name, name="launch_platform_name", curie=KBASE.curie('launch_platform_name'),
                      model_uri=KBASE.launch_platform_name, domain=None, range=Optional[str])

slots.leucine_activity_ngc_day_cell = Slot(uri=KBASE.leucine_activity_ngc_day_cell, name="leucine_activity_ngc_day_cell", curie=KBASE.curie('leucine_activity_ngc_day_cell'),
                      model_uri=KBASE.leucine_activity_ngc_day_cell, domain=None, range=Optional[str])

slots.locality = Slot(uri=KBASE.locality, name="locality", curie=KBASE.curie('locality'),
                      model_uri=KBASE.locality, domain=None, range=Optional[str])

slots.locality_description = Slot(uri=KBASE.locality_description, name="locality_description", curie=KBASE.curie('locality_description'),
                      model_uri=KBASE.locality_description, domain=None, range=Optional[str])

slots.location_description = Slot(uri=KBASE.location_description, name="location_description", curie=KBASE.curie('location_description'),
                      model_uri=KBASE.location_description, domain=None, range=Optional[str])

slots.longitude = Slot(uri=KBASE.longitude, name="longitude", curie=KBASE.curie('longitude'),
                      model_uri=KBASE.longitude, domain=None, range=Optional[float])

slots.lower_seal_end_depth = Slot(uri=KBASE.lower_seal_end_depth, name="lower_seal_end_depth", curie=KBASE.curie('lower_seal_end_depth'),
                      model_uri=KBASE.lower_seal_end_depth, domain=None, range=Optional[float])

slots.lower_seal_start_depth = Slot(uri=KBASE.lower_seal_start_depth, name="lower_seal_start_depth", curie=KBASE.curie('lower_seal_start_depth'),
                      model_uri=KBASE.lower_seal_start_depth, domain=None, range=Optional[float])

slots.lower_seal_type = Slot(uri=KBASE.lower_seal_type, name="lower_seal_type", curie=KBASE.curie('lower_seal_type'),
                      model_uri=KBASE.lower_seal_type, domain=None, range=Optional[str])

slots.material = Slot(uri=KBASE.material, name="material", curie=KBASE.curie('material'),
                      model_uri=KBASE.material, domain=None, range=Optional[str])

slots.maturation_time = Slot(uri=KBASE.maturation_time, name="maturation_time", curie=KBASE.curie('maturation_time'),
                      model_uri=KBASE.maturation_time, domain=None, range=Optional[str])

slots.max_water_level = Slot(uri=KBASE.max_water_level, name="max_water_level", curie=KBASE.curie('max_water_level'),
                      model_uri=KBASE.max_water_level, domain=None, range=Optional[float])

slots.method = Slot(uri=KBASE.method, name="method", curie=KBASE.curie('method'),
                      model_uri=KBASE.method, domain=None, range=Optional[str])

slots.min_water_level = Slot(uri=KBASE.min_water_level, name="min_water_level", curie=KBASE.curie('min_water_level'),
                      model_uri=KBASE.min_water_level, domain=None, range=Optional[float])

slots.moisture = Slot(uri=KBASE.moisture, name="moisture", curie=KBASE.curie('moisture'),
                      model_uri=KBASE.moisture, domain=None, range=Optional[float])

slots.name = Slot(uri=KBASE.name, name="name", curie=KBASE.curie('name'),
                      model_uri=KBASE.name, domain=None, range=Optional[str])

slots.name_of_physiographic_feature = Slot(uri=KBASE.name_of_physiographic_feature, name="name_of_physiographic_feature", curie=KBASE.curie('name_of_physiographic_feature'),
                      model_uri=KBASE.name_of_physiographic_feature, domain=None, range=Optional[str])

slots.navigation_type = Slot(uri=KBASE.navigation_type, name="navigation_type", curie=KBASE.curie('navigation_type'),
                      model_uri=KBASE.navigation_type, domain=None, range=Optional[str])

slots.northing = Slot(uri=KBASE.northing, name="northing", curie=KBASE.curie('northing'),
                      model_uri=KBASE.northing, domain=None, range=Optional[float])

slots.open = Slot(uri=KBASE.open, name="open", curie=KBASE.curie('open'),
                      model_uri=KBASE.open, domain=None, range=Optional[str])

slots.open_casing_depth = Slot(uri=KBASE.open_casing_depth, name="open_casing_depth", curie=KBASE.curie('open_casing_depth'),
                      model_uri=KBASE.open_casing_depth, domain=None, range=Optional[float])

slots.open_casing_id = Slot(uri=KBASE.open_casing_id, name="open_casing_id", curie=KBASE.curie('open_casing_id'),
                      model_uri=KBASE.open_casing_id, domain=None, range=Optional[float])

slots.open_casing_od = Slot(uri=KBASE.open_casing_od, name="open_casing_od", curie=KBASE.curie('open_casing_od'),
                      model_uri=KBASE.open_casing_od, domain=None, range=Optional[float])

slots.open_casing_type = Slot(uri=KBASE.open_casing_type, name="open_casing_type", curie=KBASE.curie('open_casing_type'),
                      model_uri=KBASE.open_casing_type, domain=None, range=Optional[str])

slots.open_hole_depth = Slot(uri=KBASE.open_hole_depth, name="open_hole_depth", curie=KBASE.curie('open_hole_depth'),
                      model_uri=KBASE.open_hole_depth, domain=None, range=Optional[float])

slots.open_hole_diameter = Slot(uri=KBASE.open_hole_diameter, name="open_hole_diameter", curie=KBASE.curie('open_hole_diameter'),
                      model_uri=KBASE.open_hole_diameter, domain=None, range=Optional[float])

slots.open_interval_diameter = Slot(uri=KBASE.open_interval_diameter, name="open_interval_diameter", curie=KBASE.curie('open_interval_diameter'),
                      model_uri=KBASE.open_interval_diameter, domain=None, range=Optional[float])

slots.open_interval_end_depth = Slot(uri=KBASE.open_interval_end_depth, name="open_interval_end_depth", curie=KBASE.curie('open_interval_end_depth'),
                      model_uri=KBASE.open_interval_end_depth, domain=None, range=Optional[float])

slots.open_interval_start_depth = Slot(uri=KBASE.open_interval_start_depth, name="open_interval_start_depth", curie=KBASE.curie('open_interval_start_depth'),
                      model_uri=KBASE.open_interval_start_depth, domain=None, range=Optional[float])

slots.organic_carbon = Slot(uri=KBASE.organic_carbon, name="organic_carbon", curie=KBASE.curie('organic_carbon'),
                      model_uri=KBASE.organic_carbon, domain=None, range=Optional[float])

slots.original_archive = Slot(uri=KBASE.original_archive, name="original_archive", curie=KBASE.curie('original_archive'),
                      model_uri=KBASE.original_archive, domain=None, range=Optional[str])

slots.original_archive_contact = Slot(uri=KBASE.original_archive_contact, name="original_archive_contact", curie=KBASE.curie('original_archive_contact'),
                      model_uri=KBASE.original_archive_contact, domain=None, range=Optional[str])

slots.origination_or_plug_abandon = Slot(uri=KBASE.origination_or_plug_abandon, name="origination_or_plug_abandon", curie=KBASE.curie('origination_or_plug_abandon'),
                      model_uri=KBASE.origination_or_plug_abandon, domain=None, range=Optional[str])

slots.other_name = Slot(uri=KBASE.other_name, name="other_name", curie=KBASE.curie('other_name'),
                      model_uri=KBASE.other_name, domain=None, range=Optional[str])

slots.other_names = Slot(uri=KBASE.other_names, name="other_names", curie=KBASE.curie('other_names'),
                      model_uri=KBASE.other_names, domain=None, range=Optional[str])

slots.packing_depth_end = Slot(uri=KBASE.packing_depth_end, name="packing_depth_end", curie=KBASE.curie('packing_depth_end'),
                      model_uri=KBASE.packing_depth_end, domain=None, range=Optional[float])

slots.packing_depth_start = Slot(uri=KBASE.packing_depth_start, name="packing_depth_start", curie=KBASE.curie('packing_depth_start'),
                      model_uri=KBASE.packing_depth_start, domain=None, range=Optional[float])

slots.packing_type = Slot(uri=KBASE.packing_type, name="packing_type", curie=KBASE.curie('packing_type'),
                      model_uri=KBASE.packing_type, domain=None, range=Optional[str])

slots.parent_id = Slot(uri=KBASE.parent_id, name="parent_id", curie=KBASE.curie('parent_id'),
                      model_uri=KBASE.parent_id, domain=None, range=Optional[str])

slots.parent_igsn = Slot(uri=KBASE.parent_igsn, name="parent_igsn", curie=KBASE.curie('parent_igsn'),
                      model_uri=KBASE.parent_igsn, domain=None, range=Optional[str])

slots.ph = Slot(uri=KBASE.ph, name="ph", curie=KBASE.curie('ph'),
                      model_uri=KBASE.ph, domain=None, range=Optional[float])

slots.platform_name = Slot(uri=KBASE.platform_name, name="platform_name", curie=KBASE.curie('platform_name'),
                      model_uri=KBASE.platform_name, domain=None, range=Optional[str])

slots.platform_type = Slot(uri=KBASE.platform_type, name="platform_type", curie=KBASE.curie('platform_type'),
                      model_uri=KBASE.platform_type, domain=None, range=Optional[str])

slots.pore_water_extraction = Slot(uri=KBASE.pore_water_extraction, name="pore_water_extraction", curie=KBASE.curie('pore_water_extraction'),
                      model_uri=KBASE.pore_water_extraction, domain=None, range=Optional[float])

slots.primary_physiographic_feature = Slot(uri=KBASE.primary_physiographic_feature, name="primary_physiographic_feature", curie=KBASE.curie('primary_physiographic_feature'),
                      model_uri=KBASE.primary_physiographic_feature, domain=None, range=Optional[str])

slots.purpose = Slot(uri=KBASE.purpose, name="purpose", curie=KBASE.curie('purpose'),
                      model_uri=KBASE.purpose, domain=None, range=Optional[str])

slots.recovery_factor = Slot(uri=KBASE.recovery_factor, name="recovery_factor", curie=KBASE.curie('recovery_factor'),
                      model_uri=KBASE.recovery_factor, domain=None, range=Optional[str])

slots.redox_potential_? = Slot(uri=KBASE['redox_potential_?'], name="redox_potential_?", curie=KBASE.curie('redox_potential_?'),
                      model_uri=KBASE['redox_potential_?'], domain=None, range=Optional[str])

slots.region = Slot(uri=KBASE.region, name="region", curie=KBASE.curie('region'),
                      model_uri=KBASE.region, domain=None, range=Optional[str])

slots.related_identifiers = Slot(uri=KBASE.related_identifiers, name="related_identifiers", curie=KBASE.curie('related_identifiers'),
                      model_uri=KBASE.related_identifiers, domain=None, range=Optional[str])

slots.relation_type = Slot(uri=KBASE.relation_type, name="relation_type", curie=KBASE.curie('relation_type'),
                      model_uri=KBASE.relation_type, domain=None, range=Optional[str])

slots.release_date = Slot(uri=KBASE.release_date, name="release_date", curie=KBASE.curie('release_date'),
                      model_uri=KBASE.release_date, domain=None, range=Optional[str])

slots.replicate = Slot(uri=KBASE.replicate, name="replicate", curie=KBASE.curie('replicate'),
                      model_uri=KBASE.replicate, domain=None, range=Optional[str])

slots.rock_formation = Slot(uri=KBASE.rock_formation, name="rock_formation", curie=KBASE.curie('rock_formation'),
                      model_uri=KBASE.rock_formation, domain=None, range=Optional[str])

slots.sample_description = Slot(uri=KBASE.sample_description, name="sample_description", curie=KBASE.curie('sample_description'),
                      model_uri=KBASE.sample_description, domain=None, range=Optional[str])

slots.sample_name = Slot(uri=KBASE.sample_name, name="sample_name", curie=KBASE.curie('sample_name'),
                      model_uri=KBASE.sample_name, domain=None, range=Optional[str])

slots.sampleid = Slot(uri=KBASE.sampleid, name="sampleid", curie=KBASE.curie('sampleid'),
                      model_uri=KBASE.sampleid, domain=None, range=Optional[str])

slots.screen_bottom_elevation = Slot(uri=KBASE.screen_bottom_elevation, name="screen_bottom_elevation", curie=KBASE.curie('screen_bottom_elevation'),
                      model_uri=KBASE.screen_bottom_elevation, domain=None, range=Optional[float])

slots.screen_end_depth = Slot(uri=KBASE.screen_end_depth, name="screen_end_depth", curie=KBASE.curie('screen_end_depth'),
                      model_uri=KBASE.screen_end_depth, domain=None, range=Optional[float])

slots.screen_start_depth = Slot(uri=KBASE.screen_start_depth, name="screen_start_depth", curie=KBASE.curie('screen_start_depth'),
                      model_uri=KBASE.screen_start_depth, domain=None, range=Optional[float])

slots.screen_top_elevation = Slot(uri=KBASE.screen_top_elevation, name="screen_top_elevation", curie=KBASE.curie('screen_top_elevation'),
                      model_uri=KBASE.screen_top_elevation, domain=None, range=Optional[float])

slots.screen_type = Slot(uri=KBASE.screen_type, name="screen_type", curie=KBASE.curie('screen_type'),
                      model_uri=KBASE.screen_type, domain=None, range=Optional[str])

slots.screened = Slot(uri=KBASE.screened, name="screened", curie=KBASE.curie('screened'),
                      model_uri=KBASE.screened, domain=None, range=Optional[str])

slots.screened_interval = Slot(uri=KBASE.screened_interval, name="screened_interval", curie=KBASE.curie('screened_interval'),
                      model_uri=KBASE.screened_interval, domain=None, range=Optional[float])

slots.size = Slot(uri=KBASE.size, name="size", curie=KBASE.curie('size'),
                      model_uri=KBASE.size, domain=None, range=Optional[float])

slots.state_province = Slot(uri=KBASE.state_province, name="state_province", curie=KBASE.curie('state_province'),
                      model_uri=KBASE.state_province, domain=None, range=Optional[str])

slots.sub-object_type = Slot(uri=KBASE['sub-object_type'], name="sub-object_type", curie=KBASE.curie('sub-object_type'),
                      model_uri=KBASE['sub-object_type'], domain=None, range=Optional[str])

slots.temperature = Slot(uri=KBASE.temperature, name="temperature", curie=KBASE.curie('temperature'),
                      model_uri=KBASE.temperature, domain=None, range=Optional[float])

slots.time = Slot(uri=KBASE.time, name="time", curie=KBASE.curie('time'),
                      model_uri=KBASE.time, domain=None, range=Optional[str])

slots.time_zone = Slot(uri=KBASE.time_zone, name="time_zone", curie=KBASE.curie('time_zone'),
                      model_uri=KBASE.time_zone, domain=None, range=Optional[str])

slots.timezone = Slot(uri=KBASE.timezone, name="timezone", curie=KBASE.curie('timezone'),
                      model_uri=KBASE.timezone, domain=None, range=Optional[str])

slots.top_of_casing_elevation = Slot(uri=KBASE.top_of_casing_elevation, name="top_of_casing_elevation", curie=KBASE.curie('top_of_casing_elevation'),
                      model_uri=KBASE.top_of_casing_elevation, domain=None, range=Optional[float])

slots.top_of_casing_stickup = Slot(uri=KBASE.top_of_casing_stickup, name="top_of_casing_stickup", curie=KBASE.curie('top_of_casing_stickup'),
                      model_uri=KBASE.top_of_casing_stickup, domain=None, range=Optional[float])

slots.top_of_fresh_bedrock = Slot(uri=KBASE.top_of_fresh_bedrock, name="top_of_fresh_bedrock", curie=KBASE.curie('top_of_fresh_bedrock'),
                      model_uri=KBASE.top_of_fresh_bedrock, domain=None, range=Optional[float])

slots.top_of_weathered_bedrock = Slot(uri=KBASE.top_of_weathered_bedrock, name="top_of_weathered_bedrock", curie=KBASE.curie('top_of_weathered_bedrock'),
                      model_uri=KBASE.top_of_weathered_bedrock, domain=None, range=Optional[float])

slots.total_carbon = Slot(uri=KBASE.total_carbon, name="total_carbon", curie=KBASE.curie('total_carbon'),
                      model_uri=KBASE.total_carbon, domain=None, range=Optional[float])

slots.total_nitrogen = Slot(uri=KBASE.total_nitrogen, name="total_nitrogen", curie=KBASE.curie('total_nitrogen'),
                      model_uri=KBASE.total_nitrogen, domain=None, range=Optional[float])

slots.treatment = Slot(uri=KBASE.treatment, name="treatment", curie=KBASE.curie('treatment'),
                      model_uri=KBASE.treatment, domain=None, range=Optional[str])

slots.type_of_well = Slot(uri=KBASE.type_of_well, name="type_of_well", curie=KBASE.curie('type_of_well'),
                      model_uri=KBASE.type_of_well, domain=None, range=Optional[str])

slots.upper_seal_end_depth = Slot(uri=KBASE.upper_seal_end_depth, name="upper_seal_end_depth", curie=KBASE.curie('upper_seal_end_depth'),
                      model_uri=KBASE.upper_seal_end_depth, domain=None, range=Optional[float])

slots.upper_seal_start_depth = Slot(uri=KBASE.upper_seal_start_depth, name="upper_seal_start_depth", curie=KBASE.curie('upper_seal_start_depth'),
                      model_uri=KBASE.upper_seal_start_depth, domain=None, range=Optional[float])

slots.upper_seal_type = Slot(uri=KBASE.upper_seal_type, name="upper_seal_type", curie=KBASE.curie('upper_seal_type'),
                      model_uri=KBASE.upper_seal_type, domain=None, range=Optional[str])

slots.vertical_datum = Slot(uri=KBASE.vertical_datum, name="vertical_datum", curie=KBASE.curie('vertical_datum'),
                      model_uri=KBASE.vertical_datum, domain=None, range=Optional[str])

slots.well = Slot(uri=KBASE.well, name="well", curie=KBASE.curie('well'),
                      model_uri=KBASE.well, domain=None, range=Optional[str])

slots.well_casing_depth = Slot(uri=KBASE.well_casing_depth, name="well_casing_depth", curie=KBASE.curie('well_casing_depth'),
                      model_uri=KBASE.well_casing_depth, domain=None, range=Optional[float])

slots.well_casing_id = Slot(uri=KBASE.well_casing_id, name="well_casing_id", curie=KBASE.curie('well_casing_id'),
                      model_uri=KBASE.well_casing_id, domain=None, range=Optional[float])

slots.well_casing_od = Slot(uri=KBASE.well_casing_od, name="well_casing_od", curie=KBASE.curie('well_casing_od'),
                      model_uri=KBASE.well_casing_od, domain=None, range=Optional[float])

slots.well_casing_type = Slot(uri=KBASE.well_casing_type, name="well_casing_type", curie=KBASE.curie('well_casing_type'),
                      model_uri=KBASE.well_casing_type, domain=None, range=Optional[str])

slots.well_name = Slot(uri=KBASE.well_name, name="well_name", curie=KBASE.curie('well_name'),
                      model_uri=KBASE.well_name, domain=None, range=Optional[str])

slots.well_status = Slot(uri=KBASE.well_status, name="well_status", curie=KBASE.curie('well_status'),
                      model_uri=KBASE.well_status, domain=None, range=Optional[str])

slots.zone = Slot(uri=KBASE.zone, name="zone", curie=KBASE.curie('zone'),
                      model_uri=KBASE.zone, domain=None, range=Optional[str])

slots.size_unit = Slot(uri=KBASE.size_unit, name="size_unit", curie=KBASE.curie('size_unit'),
                      model_uri=KBASE.size_unit, domain=None, range=Optional[str])

slots.age_unit = Slot(uri=KBASE.age_unit, name="age_unit", curie=KBASE.curie('age_unit'),
                      model_uri=KBASE.age_unit, domain=None, range=Optional[str])

slots.geological_unit = Slot(uri=KBASE.geological_unit, name="geological_unit", curie=KBASE.curie('geological_unit'),
                      model_uri=KBASE.geological_unit, domain=None, range=Optional[str])

slots.env_pakcage = Slot(uri=KBASE.env_pakcage, name="env_pakcage", curie=KBASE.curie('env_pakcage'),
                      model_uri=KBASE.env_pakcage, domain=None, range=Optional[str])

slots.temperature_celsius = Slot(uri=KBASE.temperature_celsius, name="temperature_celsius", curie=KBASE.curie('temperature_celsius'),
                      model_uri=KBASE.temperature_celsius, domain=None, range=Optional[str])

slots.pore_water_extraction_microliters = Slot(uri=KBASE.pore_water_extraction_microliters, name="pore_water_extraction_microliters", curie=KBASE.curie('pore_water_extraction_microliters'),
                      model_uri=KBASE.pore_water_extraction_microliters, domain=None, range=Optional[str])

slots.conductivity_ms_cm = Slot(uri=KBASE.conductivity_ms_cm, name="conductivity_ms_cm", curie=KBASE.curie('conductivity_ms_cm'),
                      model_uri=KBASE.conductivity_ms_cm, domain=None, range=Optional[str])

slots.dapi_cell_count_cells_g = Slot(uri=KBASE.dapi_cell_count_cells_g, name="dapi_cell_count_cells_g", curie=KBASE.curie('dapi_cell_count_cells_g'),
                      model_uri=KBASE.dapi_cell_count_cells_g, domain=None, range=Optional[str])

slots.dna_picogreen_total_ng = Slot(uri=KBASE.dna_picogreen_total_ng, name="dna_picogreen_total_ng", curie=KBASE.curie('dna_picogreen_total_ng'),
                      model_uri=KBASE.dna_picogreen_total_ng, domain=None, range=Optional[str])

slots.total_carbon_mg_g_dry_weight = Slot(uri=KBASE.total_carbon_mg_g_dry_weight, name="total_carbon_mg_g_dry_weight", curie=KBASE.curie('total_carbon_mg_g_dry_weight'),
                      model_uri=KBASE.total_carbon_mg_g_dry_weight, domain=None, range=Optional[str])

slots.biomass_carbon_mg_g = Slot(uri=KBASE.biomass_carbon_mg_g, name="biomass_carbon_mg_g", curie=KBASE.curie('biomass_carbon_mg_g'),
                      model_uri=KBASE.biomass_carbon_mg_g, domain=None, range=Optional[str])

slots.total_nitrogen_mg_g_dry_weight = Slot(uri=KBASE.total_nitrogen_mg_g_dry_weight, name="total_nitrogen_mg_g_dry_weight", curie=KBASE.curie('total_nitrogen_mg_g_dry_weight'),
                      model_uri=KBASE.total_nitrogen_mg_g_dry_weight, domain=None, range=Optional[str])

slots.ground_elevation_ft_amsl = Slot(uri=KBASE.ground_elevation_ft_amsl, name="ground_elevation_ft_amsl", curie=KBASE.curie('ground_elevation_ft_amsl'),
                      model_uri=KBASE.ground_elevation_ft_amsl, domain=None, range=Optional[str])

slots.boring_ft_bgs = Slot(uri=KBASE.boring_ft_bgs, name="boring_ft_bgs", curie=KBASE.curie('boring_ft_bgs'),
                      model_uri=KBASE.boring_ft_bgs, domain=None, range=Optional[str])

slots.boring_diameter_in = Slot(uri=KBASE.boring_diameter_in, name="boring_diameter_in", curie=KBASE.curie('boring_diameter_in'),
                      model_uri=KBASE.boring_diameter_in, domain=None, range=Optional[str])

slots.well_casing_od_in = Slot(uri=KBASE.well_casing_od_in, name="well_casing_od_in", curie=KBASE.curie('well_casing_od_in'),
                      model_uri=KBASE.well_casing_od_in, domain=None, range=Optional[str])

slots.well_casing_id_in = Slot(uri=KBASE.well_casing_id_in, name="well_casing_id_in", curie=KBASE.curie('well_casing_id_in'),
                      model_uri=KBASE.well_casing_id_in, domain=None, range=Optional[str])

slots.drive_casing_id_in = Slot(uri=KBASE.drive_casing_id_in, name="drive_casing_id_in", curie=KBASE.curie('drive_casing_id_in'),
                      model_uri=KBASE.drive_casing_id_in, domain=None, range=Optional[str])

slots.drive_casing_od_in = Slot(uri=KBASE.drive_casing_od_in, name="drive_casing_od_in", curie=KBASE.curie('drive_casing_od_in'),
                      model_uri=KBASE.drive_casing_od_in, domain=None, range=Optional[str])

slots.drive_casing_start_depth_ft_bgs = Slot(uri=KBASE.drive_casing_start_depth_ft_bgs, name="drive_casing_start_depth_ft_bgs", curie=KBASE.curie('drive_casing_start_depth_ft_bgs'),
                      model_uri=KBASE.drive_casing_start_depth_ft_bgs, domain=None, range=Optional[str])

slots.drive_casing_end_depth_ft_bgs = Slot(uri=KBASE.drive_casing_end_depth_ft_bgs, name="drive_casing_end_depth_ft_bgs", curie=KBASE.curie('drive_casing_end_depth_ft_bgs'),
                      model_uri=KBASE.drive_casing_end_depth_ft_bgs, domain=None, range=Optional[str])

slots.packing_depth_start_ft_bgs = Slot(uri=KBASE.packing_depth_start_ft_bgs, name="packing_depth_start_ft_bgs", curie=KBASE.curie('packing_depth_start_ft_bgs'),
                      model_uri=KBASE.packing_depth_start_ft_bgs, domain=None, range=Optional[str])

slots.packing_depth_end_ft_bgs = Slot(uri=KBASE.packing_depth_end_ft_bgs, name="packing_depth_end_ft_bgs", curie=KBASE.curie('packing_depth_end_ft_bgs'),
                      model_uri=KBASE.packing_depth_end_ft_bgs, domain=None, range=Optional[str])

slots.topofweatheredbedrock_ft_bgs = Slot(uri=KBASE.topofweatheredbedrock_ft_bgs, name="topofweatheredbedrock_ft_bgs", curie=KBASE.curie('topofweatheredbedrock_ft_bgs'),
                      model_uri=KBASE.topofweatheredbedrock_ft_bgs, domain=None, range=Optional[str])

slots.topoffreshbedrock_ft_bgs = Slot(uri=KBASE.topoffreshbedrock_ft_bgs, name="topoffreshbedrock_ft_bgs", curie=KBASE.curie('topoffreshbedrock_ft_bgs'),
                      model_uri=KBASE.topoffreshbedrock_ft_bgs, domain=None, range=Optional[str])

slots.min_water_level_ft_amsl = Slot(uri=KBASE.min_water_level_ft_amsl, name="min_water_level_ft_amsl", curie=KBASE.curie('min_water_level_ft_amsl'),
                      model_uri=KBASE.min_water_level_ft_amsl, domain=None, range=Optional[str])

slots.average_water_level_ft_amsl = Slot(uri=KBASE.average_water_level_ft_amsl, name="average_water_level_ft_amsl", curie=KBASE.curie('average_water_level_ft_amsl'),
                      model_uri=KBASE.average_water_level_ft_amsl, domain=None, range=Optional[str])

slots.max_water_level_ft_amsl = Slot(uri=KBASE.max_water_level_ft_amsl, name="max_water_level_ft_amsl", curie=KBASE.curie('max_water_level_ft_amsl'),
                      model_uri=KBASE.max_water_level_ft_amsl, domain=None, range=Optional[str])

slots.upper_seal_start_depth_ft_bgs = Slot(uri=KBASE.upper_seal_start_depth_ft_bgs, name="upper_seal_start_depth_ft_bgs", curie=KBASE.curie('upper_seal_start_depth_ft_bgs'),
                      model_uri=KBASE.upper_seal_start_depth_ft_bgs, domain=None, range=Optional[str])

slots.upper_seal_end_depth_ft_bgs = Slot(uri=KBASE.upper_seal_end_depth_ft_bgs, name="upper_seal_end_depth_ft_bgs", curie=KBASE.curie('upper_seal_end_depth_ft_bgs'),
                      model_uri=KBASE.upper_seal_end_depth_ft_bgs, domain=None, range=Optional[str])

slots.lower_seal_type_ft_bgs = Slot(uri=KBASE.lower_seal_type_ft_bgs, name="lower_seal_type_ft_bgs", curie=KBASE.curie('lower_seal_type_ft_bgs'),
                      model_uri=KBASE.lower_seal_type_ft_bgs, domain=None, range=Optional[str])

slots.lower_seal_start_depth_ft_bgs = Slot(uri=KBASE.lower_seal_start_depth_ft_bgs, name="lower_seal_start_depth_ft_bgs", curie=KBASE.curie('lower_seal_start_depth_ft_bgs'),
                      model_uri=KBASE.lower_seal_start_depth_ft_bgs, domain=None, range=Optional[str])

slots.lower_seal_end_depth_ft_bgs = Slot(uri=KBASE.lower_seal_end_depth_ft_bgs, name="lower_seal_end_depth_ft_bgs", curie=KBASE.curie('lower_seal_end_depth_ft_bgs'),
                      model_uri=KBASE.lower_seal_end_depth_ft_bgs, domain=None, range=Optional[str])

slots.open_casing_od_in = Slot(uri=KBASE.open_casing_od_in, name="open_casing_od_in", curie=KBASE.curie('open_casing_od_in'),
                      model_uri=KBASE.open_casing_od_in, domain=None, range=Optional[str])

slots.open_casing_id_in = Slot(uri=KBASE.open_casing_id_in, name="open_casing_id_in", curie=KBASE.curie('open_casing_id_in'),
                      model_uri=KBASE.open_casing_id_in, domain=None, range=Optional[str])

slots.open_casing_depth_ft_bgs = Slot(uri=KBASE.open_casing_depth_ft_bgs, name="open_casing_depth_ft_bgs", curie=KBASE.curie('open_casing_depth_ft_bgs'),
                      model_uri=KBASE.open_casing_depth_ft_bgs, domain=None, range=Optional[str])

slots.open_hole_diameter_in = Slot(uri=KBASE.open_hole_diameter_in, name="open_hole_diameter_in", curie=KBASE.curie('open_hole_diameter_in'),
                      model_uri=KBASE.open_hole_diameter_in, domain=None, range=Optional[str])

slots.open_hole_depth_ft_bgs = Slot(uri=KBASE.open_hole_depth_ft_bgs, name="open_hole_depth_ft_bgs", curie=KBASE.curie('open_hole_depth_ft_bgs'),
                      model_uri=KBASE.open_hole_depth_ft_bgs, domain=None, range=Optional[str])

slots.open_interval_start_depth_ft_bgs = Slot(uri=KBASE.open_interval_start_depth_ft_bgs, name="open_interval_start_depth_ft_bgs", curie=KBASE.curie('open_interval_start_depth_ft_bgs'),
                      model_uri=KBASE.open_interval_start_depth_ft_bgs, domain=None, range=Optional[str])

slots.open_interval_end_depth_ft_bgs = Slot(uri=KBASE.open_interval_end_depth_ft_bgs, name="open_interval_end_depth_ft_bgs", curie=KBASE.curie('open_interval_end_depth_ft_bgs'),
                      model_uri=KBASE.open_interval_end_depth_ft_bgs, domain=None, range=Optional[str])

slots.open_interval_diameter_in = Slot(uri=KBASE.open_interval_diameter_in, name="open_interval_diameter_in", curie=KBASE.curie('open_interval_diameter_in'),
                      model_uri=KBASE.open_interval_diameter_in, domain=None, range=Optional[str])
