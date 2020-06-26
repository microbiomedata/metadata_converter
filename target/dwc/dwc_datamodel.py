# Auto generated from dwc.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-06-26 16:36
# Schema: terms
#
# id: http://rs.tdwg.org/dwc/terms
# description: DarwinCore biolinkml rendering
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
from includes.types import String

metamodel_version = "1.4.4"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DWC = CurieNamespace('dwc', 'http://rs.tdwg.org/dwc/terms/')
DEFAULT_ = DWC


# Types

# Class references



@dataclass
class Occurrence(YAMLRoot):
    """
    A resource describing an instance of the Occurrence class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.Occurrence
    class_class_curie: ClassVar[str] = "dwc:Occurrence"
    class_name: ClassVar[str] = "Occurrence"
    class_model_uri: ClassVar[URIRef] = DWC.Occurrence

    occurrenceID: Optional[str] = None
    catalogNumber: Optional[str] = None
    recordNumber: Optional[str] = None
    recordedBy: Optional[str] = None
    individualCount: Optional[str] = None
    organismQuantity: Optional[str] = None
    organismQuantityType: Optional[str] = None
    sex: Optional[str] = None
    lifeStage: Optional[str] = None
    reproductiveCondition: Optional[str] = None
    behavior: Optional[str] = None
    establishmentMeans: Optional[str] = None
    occurrenceStatus: Optional[str] = None
    preparations: Optional[str] = None
    disposition: Optional[str] = None
    associatedMedia: Optional[str] = None
    associatedReferences: Optional[str] = None
    associatedSequences: Optional[str] = None
    associatedTaxa: Optional[str] = None
    otherCatalogNumbers: Optional[str] = None
    occurrenceRemarks: Optional[str] = None
    Associated_Media: Optional[str] = None
    Associated_References: Optional[str] = None
    Associated_Sequences: Optional[str] = None
    Associated_Taxa: Optional[str] = None
    Behavior: Optional[str] = None
    Catalog_Number: Optional[str] = None
    Disposition: Optional[str] = None
    Establishment_Means: Optional[str] = None
    Individual_Count: Optional[str] = None
    Life_Stage: Optional[str] = None
    Occurrence_ID: Optional[str] = None
    Occurrence_Remarks: Optional[str] = None
    Occurrence_Status: Optional[str] = None
    Organism_Quantity: Optional[str] = None
    Organism_Quantity_Type: Optional[str] = None
    Other_Catalog_Numbers: Optional[str] = None
    Preparations: Optional[str] = None
    Recorded_By: Optional[str] = None
    Record_Number: Optional[str] = None
    Reproductive_Condition: Optional[str] = None
    Sex: Optional[str] = None

@dataclass
class Organism(YAMLRoot):
    """
    A particular organism or defined group of organisms considered to be taxonomically homogeneous.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.Organism
    class_class_curie: ClassVar[str] = "dwc:Organism"
    class_name: ClassVar[str] = "Organism"
    class_model_uri: ClassVar[URIRef] = DWC.Organism

    organismID: Optional[str] = None
    organismName: Optional[str] = None
    organismScope: Optional[str] = None
    associatedOccurrences: Optional[str] = None
    associatedOrganisms: Optional[str] = None
    previousIdentifications: Optional[str] = None
    organismRemarks: Optional[str] = None
    Associated_Occurrences: Optional[str] = None
    Associated_Organisms: Optional[str] = None
    Organism_ID: Optional[str] = None
    Organism_Name: Optional[str] = None
    Organism_Remarks: Optional[str] = None
    Organism_Scope: Optional[str] = None
    Previous_Identifications: Optional[str] = None

@dataclass
class MaterialSample(YAMLRoot):
    """
    A physical result of a sampling (or subsampling) event. In biological collections, the material sample is
    typically collected, and either preserved or destructively processed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.MaterialSample
    class_class_curie: ClassVar[str] = "dwc:MaterialSample"
    class_name: ClassVar[str] = "MaterialSample"
    class_model_uri: ClassVar[URIRef] = DWC.MaterialSample

    materialSampleID: Optional[str] = None
    Material_Sample_ID: Optional[str] = None

@dataclass
class Event(YAMLRoot):
    """
    An action that occurs at some location during some time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.Event
    class_class_curie: ClassVar[str] = "dwc:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = DWC.Event

    eventID: Optional[str] = None
    parentEventID: Optional[str] = None
    fieldNumber: Optional[str] = None
    eventDate: Optional[str] = None
    eventTime: Optional[str] = None
    startDayOfYear: Optional[str] = None
    endDayOfYear: Optional[str] = None
    year: Optional[str] = None
    month: Optional[str] = None
    day: Optional[str] = None
    verbatimEventDate: Optional[str] = None
    habitat: Optional[str] = None
    samplingProtocol: Optional[str] = None
    sampleSizeValue: Optional[str] = None
    sampleSizeUnit: Optional[str] = None
    samplingEffort: Optional[str] = None
    fieldNotes: Optional[str] = None
    eventRemarks: Optional[str] = None
    Day: Optional[str] = None
    End_Day_Of_Year: Optional[str] = None
    Event_Date: Optional[str] = None
    Event_ID: Optional[str] = None
    Event_Remarks: Optional[str] = None
    Event_Time: Optional[str] = None
    Field_Notes: Optional[str] = None
    Field_Number: Optional[str] = None
    Habitat: Optional[str] = None
    Month: Optional[str] = None
    Parent_Event_ID: Optional[str] = None
    Sample_Size_Unit: Optional[str] = None
    Sample_Size_Value: Optional[str] = None
    Sampling_Effort: Optional[str] = None
    Sampling_Protocol: Optional[str] = None
    Start_Day_Of_Year: Optional[str] = None
    Verbatim_EventDate: Optional[str] = None
    Year: Optional[str] = None

class Location(YAMLRoot):
    """
    A resource describing an instance of the Location class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.Location
    class_class_curie: ClassVar[str] = "dwc:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = DWC.Location


@dataclass
class GeologicalContext(YAMLRoot):
    """
    Geological information, such as stratigraphy, that qualifies a region or place.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.GeologicalContext
    class_class_curie: ClassVar[str] = "dwc:GeologicalContext"
    class_name: ClassVar[str] = "GeologicalContext"
    class_model_uri: ClassVar[URIRef] = DWC.GeologicalContext

    geologicalContextID: Optional[str] = None
    earliestEonOrLowestEonothem: Optional[str] = None
    latestEonOrHighestEonothem: Optional[str] = None
    earliestEraOrLowestErathem: Optional[str] = None
    latestEraOrHighestErathem: Optional[str] = None
    earliestPeriodOrLowestSystem: Optional[str] = None
    latestPeriodOrHighestSystem: Optional[str] = None
    earliestEpochOrLowestSeries: Optional[str] = None
    latestEpochOrHighestSeries: Optional[str] = None
    earliestAgeOrLowestStage: Optional[str] = None
    latestAgeOrHighestStage: Optional[str] = None
    lowestBiostratigraphicZone: Optional[str] = None
    highestBiostratigraphicZone: Optional[str] = None
    lithostratigraphicTerms: Optional[str] = None
    group: Optional[str] = None
    formation: Optional[str] = None
    member: Optional[str] = None
    bed: Optional[str] = None
    Bed: Optional[str] = None
    Earliest_Age_Or_Lowest_Stage: Optional[str] = None
    Earliest_Eon_Or_Lowest_Eonothem: Optional[str] = None
    Earliest_Epoch_Or_Lowest_Series: Optional[str] = None
    Earliest_Era_Or_Lowest_Erathem: Optional[str] = None
    Earliest_Period_Or_Lowest_System: Optional[str] = None
    Formation: Optional[str] = None
    Geological_Context_ID: Optional[str] = None
    Group: Optional[str] = None
    Highest_Biostratigraphic_Zone: Optional[str] = None
    Latest_AgeOr_Highest_Stage: Optional[str] = None
    Latest_Eon_Or_Highest_Eonothem: Optional[str] = None
    Latest_Epoch_Or_Highest_Series: Optional[str] = None
    Latest_Era_Or_Highest_Erathem: Optional[str] = None
    Latest_Period_Or_Highest_System: Optional[str] = None
    Lithostratigraphic_Terms: Optional[str] = None
    Lowest_Biostratigraphic_Zone: Optional[str] = None
    Member: Optional[str] = None

@dataclass
class Identification(YAMLRoot):
    """
    A taxonomic determination (e.g., the assignment to a taxon).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.Identification
    class_class_curie: ClassVar[str] = "dwc:Identification"
    class_name: ClassVar[str] = "Identification"
    class_model_uri: ClassVar[URIRef] = DWC.Identification

    identificationID: Optional[str] = None
    identificationQualifier: Optional[str] = None
    typeStatus: Optional[str] = None
    identifiedBy: Optional[str] = None
    dateIdentified: Optional[str] = None
    identificationReferences: Optional[str] = None
    identificationVerificationStatus: Optional[str] = None
    identificationRemarks: Optional[str] = None
    Date_Identified: Optional[str] = None
    Identification_ID: Optional[str] = None
    Identification_Qualifier: Optional[str] = None
    Identification_References: Optional[str] = None
    Identification_Remarks: Optional[str] = None
    Identification_Verification_Status: Optional[str] = None
    Identified_By: Optional[str] = None
    Type_Status: Optional[str] = None

@dataclass
class Taxon(YAMLRoot):
    """
    A resource describing an instance of the Taxon class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.Taxon
    class_class_curie: ClassVar[str] = "dwc:Taxon"
    class_name: ClassVar[str] = "Taxon"
    class_model_uri: ClassVar[URIRef] = DWC.Taxon

    taxonID: Optional[str] = None
    scientificNameID: Optional[str] = None
    acceptedNameUsageID: Optional[str] = None
    parentNameUsageID: Optional[str] = None
    originalNameUsageID: Optional[str] = None
    nameAccordingToID: Optional[str] = None
    namePublishedInID: Optional[str] = None
    taxonConceptID: Optional[str] = None
    scientificName: Optional[str] = None
    acceptedNameUsage: Optional[str] = None
    parentNameUsage: Optional[str] = None
    originalNameUsage: Optional[str] = None
    nameAccordingTo: Optional[str] = None
    namePublishedIn: Optional[str] = None
    namePublishedInYear: Optional[str] = None
    higherClassification: Optional[str] = None
    kingdom: Optional[str] = None
    phylum: Optional[str] = None
    class: Optional[str] = None
    order: Optional[str] = None
    family: Optional[str] = None
    genus: Optional[str] = None
    subgenus: Optional[str] = None
    specificEpithet: Optional[str] = None
    infraspecificEpithet: Optional[str] = None
    taxonRank: Optional[str] = None
    verbatimTaxonRank: Optional[str] = None
    scientificNameAuthorship: Optional[str] = None
    vernacularName: Optional[str] = None
    nomenclaturalCode: Optional[str] = None
    taxonomicStatus: Optional[str] = None
    nomenclaturalStatus: Optional[str] = None
    taxonRemarks: Optional[str] = None
    Accepted_Name_Usage: Optional[str] = None
    Accepted_Name_Usage_ID: Optional[str] = None
    Class: Optional[str] = None
    Family: Optional[str] = None
    Genus: Optional[str] = None
    Higher_Classification: Optional[str] = None
    Infraspecific_Epithet: Optional[str] = None
    Kingdom: Optional[str] = None
    Name_According_To: Optional[str] = None
    Name_According_To_ID: Optional[str] = None
    Name_Published_In: Optional[str] = None
    Name_Published_In_ID: Optional[str] = None
    Name_Published_In_Year: Optional[str] = None
    Nomenclatural_Code: Optional[str] = None
    Nomenclatural_Status: Optional[str] = None
    Order: Optional[str] = None
    Original_Name_Usage: Optional[str] = None
    Original_Name_Usage_ID: Optional[str] = None
    Parent_Name_Usage: Optional[str] = None
    Parent_Name_Usage_ID: Optional[str] = None
    Phylum: Optional[str] = None
    Scientific_Name: Optional[str] = None
    Scientific_Name_Authorship: Optional[str] = None
    Scientific_Name_ID: Optional[str] = None
    Specific_Epithet: Optional[str] = None
    Subgenus: Optional[str] = None
    Taxon_Concept_ID: Optional[str] = None
    Taxon_ID: Optional[str] = None
    Taxonomic_Status: Optional[str] = None
    Taxon_Rank: Optional[str] = None
    Taxon_Remarks: Optional[str] = None
    Verbatim_Taxon_Rank: Optional[str] = None
    Vernacular_Name: Optional[str] = None

@dataclass
class MeasurementOrFact(YAMLRoot):
    """
    A measurement of or fact about an rdfs:Resource (http://www.w3.org/2000/01/rdf-schema#Resource).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.MeasurementOrFact
    class_class_curie: ClassVar[str] = "dwc:MeasurementOrFact"
    class_name: ClassVar[str] = "MeasurementOrFact"
    class_model_uri: ClassVar[URIRef] = DWC.MeasurementOrFact

    measurementID: Optional[str] = None
    measurementType: Optional[str] = None
    measurementValue: Optional[str] = None
    measurementAccuracy: Optional[str] = None
    measurementUnit: Optional[str] = None
    measurementDeterminedBy: Optional[str] = None
    measurementDeterminedDate: Optional[str] = None
    measurementMethod: Optional[str] = None
    measurementRemarks: Optional[str] = None
    Measurement_Accuracy: Optional[str] = None
    Measurement_Determined_By: Optional[str] = None
    Measurement_Determined_Date: Optional[str] = None
    Measurement_ID: Optional[str] = None
    Measurement_Method: Optional[str] = None
    Measurement_Remarks: Optional[str] = None
    Measurement_Type: Optional[str] = None
    Measurement_Unit: Optional[str] = None
    Measurement_Value: Optional[str] = None

@dataclass
class ResourceRelationship(YAMLRoot):
    """
    A relationship of one rdfs:Resource (http://www.w3.org/2000/01/rdf-schema#Resource) to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.ResourceRelationship
    class_class_curie: ClassVar[str] = "dwc:ResourceRelationship"
    class_name: ClassVar[str] = "ResourceRelationship"
    class_model_uri: ClassVar[URIRef] = DWC.ResourceRelationship

    resourceRelationshipID: Optional[str] = None
    resourceID: Optional[str] = None
    relatedResourceID: Optional[str] = None
    relationshipOfResource: Optional[str] = None
    relationshipAccordingTo: Optional[str] = None
    relationshipEstablishedDate: Optional[str] = None
    relationshipRemarks: Optional[str] = None
    Related_Resource_ID: Optional[str] = None
    Relationship_According_To: Optional[str] = None
    Relationship_Established_Date: Optional[str] = None
    Relationship_Of_Resource: Optional[str] = None
    Relationship_Remarks: Optional[str] = None
    Resource_ID: Optional[str] = None
    Resource_Relationship_ID: Optional[str] = None

class UseWithIRI(YAMLRoot):
    """
    The category of terms that are recommended to have an IRI as a value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.UseWithIRI
    class_class_curie: ClassVar[str] = "dwc:UseWithIRI"
    class_name: ClassVar[str] = "UseWithIRI"
    class_model_uri: ClassVar[URIRef] = DWC.UseWithIRI


class LivingSpecimen(YAMLRoot):
    """
    A specimen that is alive.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.LivingSpecimen
    class_class_curie: ClassVar[str] = "dwc:LivingSpecimen"
    class_name: ClassVar[str] = "LivingSpecimen"
    class_model_uri: ClassVar[URIRef] = DWC.LivingSpecimen


class PreservedSpecimen(YAMLRoot):
    """
    A specimen that has been preserved.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.PreservedSpecimen
    class_class_curie: ClassVar[str] = "dwc:PreservedSpecimen"
    class_name: ClassVar[str] = "PreservedSpecimen"
    class_model_uri: ClassVar[URIRef] = DWC.PreservedSpecimen


class FossilSpecimen(YAMLRoot):
    """
    A preserved specimen that is a fossil.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.FossilSpecimen
    class_class_curie: ClassVar[str] = "dwc:FossilSpecimen"
    class_name: ClassVar[str] = "FossilSpecimen"
    class_model_uri: ClassVar[URIRef] = DWC.FossilSpecimen


class HumanObservation(YAMLRoot):
    """
    An output of a human observation process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.HumanObservation
    class_class_curie: ClassVar[str] = "dwc:HumanObservation"
    class_name: ClassVar[str] = "HumanObservation"
    class_model_uri: ClassVar[URIRef] = DWC.HumanObservation


class MachineObservation(YAMLRoot):
    """
    An output of a machine observation process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.MachineObservation
    class_class_curie: ClassVar[str] = "dwc:MachineObservation"
    class_name: ClassVar[str] = "MachineObservation"
    class_model_uri: ClassVar[URIRef] = DWC.MachineObservation


class Dataset(YAMLRoot):
    """
    The category of information pertaining to a logical set of records.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.Dataset
    class_class_curie: ClassVar[str] = "dwc:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = DWC.Dataset


class EventAttribute(YAMLRoot):
    """
    Container class for information about attributes related to a given sampling event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.EventAttribute
    class_class_curie: ClassVar[str] = "dwc:EventAttribute"
    class_name: ClassVar[str] = "Event Attribute"
    class_model_uri: ClassVar[URIRef] = DWC.EventAttribute


class EventMeasurement(YAMLRoot):
    """
    The category of information pertaining to measurements associated with an event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.EventMeasurement
    class_class_curie: ClassVar[str] = "dwc:EventMeasurement"
    class_name: ClassVar[str] = "Event Measurement"
    class_model_uri: ClassVar[URIRef] = DWC.EventMeasurement


class FossilSpecimen(YAMLRoot):
    """
    A preserved specimen that is a fossil.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.FossilSpecimen
    class_class_curie: ClassVar[str] = "dwc:FossilSpecimen"
    class_name: ClassVar[str] = "Fossil Specimen"
    class_model_uri: ClassVar[URIRef] = DWC.FossilSpecimen


class GeologicalContext(YAMLRoot):
    """
    Geological information, such as stratigraphy, that qualifies a region or place.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.GeologicalContext
    class_class_curie: ClassVar[str] = "dwc:GeologicalContext"
    class_name: ClassVar[str] = "Geological Context"
    class_model_uri: ClassVar[URIRef] = DWC.GeologicalContext


class HumanObservation(YAMLRoot):
    """
    An output of a human observation process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.HumanObservation
    class_class_curie: ClassVar[str] = "dwc:HumanObservation"
    class_name: ClassVar[str] = "Human Observation"
    class_model_uri: ClassVar[URIRef] = DWC.HumanObservation


class LivingSpecimen(YAMLRoot):
    """
    A specimen that is alive.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.LivingSpecimen
    class_class_curie: ClassVar[str] = "dwc:LivingSpecimen"
    class_name: ClassVar[str] = "Living Specimen"
    class_model_uri: ClassVar[URIRef] = DWC.LivingSpecimen


class MachineObservation(YAMLRoot):
    """
    An output of a machine observation process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.MachineObservation
    class_class_curie: ClassVar[str] = "dwc:MachineObservation"
    class_name: ClassVar[str] = "Machine Observation"
    class_model_uri: ClassVar[URIRef] = DWC.MachineObservation


class MaterialSample(YAMLRoot):
    """
    A physical results of a sampling (or subsampling) event. In biological collections, the material sample is
    typically collected, and either preserved or destructively processed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.MaterialSample
    class_class_curie: ClassVar[str] = "dwc:MaterialSample"
    class_name: ClassVar[str] = "Material Sample"
    class_model_uri: ClassVar[URIRef] = DWC.MaterialSample


class MeasurementOrFact(YAMLRoot):
    """
    The category of information pertaining to measurements, facts, characteristics, or assertions about a resource
    (instance of data record, such as Occurrence, Taxon, Location, Event).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.MeasurementOrFact
    class_class_curie: ClassVar[str] = "dwc:MeasurementOrFact"
    class_name: ClassVar[str] = "Measurement Or Fact"
    class_model_uri: ClassVar[URIRef] = DWC.MeasurementOrFact


class MeasurementOrFact(YAMLRoot):
    """
    A measurement of or fact about an rdfs:Resource (http://www.w3.org/2000/01/rdf-schema#Resource).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.MeasurementOrFact
    class_class_curie: ClassVar[str] = "dwc:MeasurementOrFact"
    class_name: ClassVar[str] = "Measurement or Fact"
    class_model_uri: ClassVar[URIRef] = DWC.MeasurementOrFact


class OccurrenceMeasurement(YAMLRoot):
    """
    The category of information pertaining to measurements accociated with an occurrence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.OccurrenceMeasurement
    class_class_curie: ClassVar[str] = "dwc:OccurrenceMeasurement"
    class_name: ClassVar[str] = "Occurrence Measurement"
    class_model_uri: ClassVar[URIRef] = DWC.OccurrenceMeasurement


class PreservedSpecimen(YAMLRoot):
    """
    A specimen that has been preserved.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.PreservedSpecimen
    class_class_curie: ClassVar[str] = "dwc:PreservedSpecimen"
    class_name: ClassVar[str] = "Preserved Specimen"
    class_model_uri: ClassVar[URIRef] = DWC.PreservedSpecimen


class ResourceRelationship(YAMLRoot):
    """
    A relationship of one rdfs:Resource (http://www.w3.org/2000/01/rdf-schema#Resource) to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.ResourceRelationship
    class_class_curie: ClassVar[str] = "dwc:ResourceRelationship"
    class_name: ClassVar[str] = "Resource Relationship"
    class_model_uri: ClassVar[URIRef] = DWC.ResourceRelationship


class Sample(YAMLRoot):
    """
    Container class for information about the results of a sampling event (specimen, observation, etc.)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.Sample
    class_class_curie: ClassVar[str] = "dwc:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = DWC.Sample


class SampleAttribute(YAMLRoot):
    """
    Container class for information about attributes related to a given sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.SampleAttribute
    class_class_curie: ClassVar[str] = "dwc:SampleAttribute"
    class_name: ClassVar[str] = "Sample Attribute"
    class_model_uri: ClassVar[URIRef] = DWC.SampleAttribute


class SamplingEvent(YAMLRoot):
    """
    Container class for information about the conditions and methods of acquisition of samples.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.SamplingEvent
    class_class_curie: ClassVar[str] = "dwc:SamplingEvent"
    class_name: ClassVar[str] = "Sampling Event"
    class_model_uri: ClassVar[URIRef] = DWC.SamplingEvent


class SamplingLocation(YAMLRoot):
    """
    Container class for information about the location where a sampling event occurred.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.SamplingLocation
    class_class_curie: ClassVar[str] = "dwc:SamplingLocation"
    class_name: ClassVar[str] = "Sampling Location"
    class_model_uri: ClassVar[URIRef] = DWC.SamplingLocation


class NomenclaturalChecklist(YAMLRoot):
    """
    A resource describing a nomenclatural checklist.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DWC.NomenclaturalChecklist
    class_class_curie: ClassVar[str] = "dwc:NomenclaturalChecklist"
    class_name: ClassVar[str] = "NomenclaturalChecklist"
    class_model_uri: ClassVar[URIRef] = DWC.NomenclaturalChecklist



# Slots
class slots:
    pass

slots.type = Slot(uri=DWC.type, name="type", curie=DWC.curie('type'),
                      model_uri=DWC.type, domain=None, range=Optional[str])

slots.modified = Slot(uri=DWC.modified, name="modified", curie=DWC.curie('modified'),
                      model_uri=DWC.modified, domain=None, range=Optional[str])

slots.language = Slot(uri=DWC.language, name="language", curie=DWC.curie('language'),
                      model_uri=DWC.language, domain=None, range=Optional[str])

slots.license = Slot(uri=DWC.license, name="license", curie=DWC.curie('license'),
                      model_uri=DWC.license, domain=None, range=Optional[str])

slots.rightsHolder = Slot(uri=DWC.rightsHolder, name="rightsHolder", curie=DWC.curie('rightsHolder'),
                      model_uri=DWC.rightsHolder, domain=None, range=Optional[str])

slots.accessRights = Slot(uri=DWC.accessRights, name="accessRights", curie=DWC.curie('accessRights'),
                      model_uri=DWC.accessRights, domain=None, range=Optional[str])

slots.bibliographicCitation = Slot(uri=DWC.bibliographicCitation, name="bibliographicCitation", curie=DWC.curie('bibliographicCitation'),
                      model_uri=DWC.bibliographicCitation, domain=None, range=Optional[str])

slots.references = Slot(uri=DWC.references, name="references", curie=DWC.curie('references'),
                      model_uri=DWC.references, domain=None, range=Optional[str])

slots.institutionID = Slot(uri=DWC.institutionID, name="institutionID", curie=DWC.curie('institutionID'),
                      model_uri=DWC.institutionID, domain=None, range=Optional[str], mappings = [DWC["version/institutionID-2009-09-11"]])

slots.collectionID = Slot(uri=DWC.collectionID, name="collectionID", curie=DWC.curie('collectionID'),
                      model_uri=DWC.collectionID, domain=None, range=Optional[str], mappings = [DWC["version/collectionID-2009-09-11"]])

slots.datasetID = Slot(uri=DWC.datasetID, name="datasetID", curie=DWC.curie('datasetID'),
                      model_uri=DWC.datasetID, domain=None, range=Optional[str], mappings = [DWC["version/datasetID-2009-09-11"]])

slots.institutionCode = Slot(uri=DWC.institutionCode, name="institutionCode", curie=DWC.curie('institutionCode'),
                      model_uri=DWC.institutionCode, domain=None, range=Optional[str], mappings = [DWC["version/institutionCode-2009-09-11"]])

slots.collectionCode = Slot(uri=DWC.collectionCode, name="collectionCode", curie=DWC.curie('collectionCode'),
                      model_uri=DWC.collectionCode, domain=None, range=Optional[str], mappings = [DWC["version/collectionCode-2009-09-11"]])

slots.datasetName = Slot(uri=DWC.datasetName, name="datasetName", curie=DWC.curie('datasetName'),
                      model_uri=DWC.datasetName, domain=None, range=Optional[str], mappings = [DWC["version/datasetName-2009-09-11"]])

slots.ownerInstitutionCode = Slot(uri=DWC.ownerInstitutionCode, name="ownerInstitutionCode", curie=DWC.curie('ownerInstitutionCode'),
                      model_uri=DWC.ownerInstitutionCode, domain=None, range=Optional[str], mappings = [DWC["version/ownerInstitutionCode-2009-08-24"]])

slots.basisOfRecord = Slot(uri=DWC.basisOfRecord, name="basisOfRecord", curie=DWC.curie('basisOfRecord'),
                      model_uri=DWC.basisOfRecord, domain=None, range=Optional[str], mappings = [DWC["version/basisOfRecord-2014-10-23"]])

slots.informationWithheld = Slot(uri=DWC.informationWithheld, name="informationWithheld", curie=DWC.curie('informationWithheld'),
                      model_uri=DWC.informationWithheld, domain=None, range=Optional[str], mappings = [DWC["version/informationWithheld-2009-04-24"]])

slots.dataGeneralizations = Slot(uri=DWC.dataGeneralizations, name="dataGeneralizations", curie=DWC.curie('dataGeneralizations'),
                      model_uri=DWC.dataGeneralizations, domain=None, range=Optional[str], mappings = [DWC["version/dataGeneralizations-2009-04-24"]])

slots.dynamicProperties = Slot(uri=DWC.dynamicProperties, name="dynamicProperties", curie=DWC.curie('dynamicProperties'),
                      model_uri=DWC.dynamicProperties, domain=None, range=Optional[str], mappings = [DWC["version/dynamicProperties-2014-10-23"]])

slots.occurrenceID = Slot(uri=DWC.occurrenceID, name="occurrenceID", curie=DWC.curie('occurrenceID'),
                      model_uri=DWC.occurrenceID, domain=None, range=Optional[str], mappings = [DWC["version/occurrenceID-2009-04-24"]])

slots.catalogNumber = Slot(uri=DWC.catalogNumber, name="catalogNumber", curie=DWC.curie('catalogNumber'),
                      model_uri=DWC.catalogNumber, domain=None, range=Optional[str], mappings = [DWC["version/catalogNumber-2009-04-24"]])

slots.recordNumber = Slot(uri=DWC.recordNumber, name="recordNumber", curie=DWC.curie('recordNumber'),
                      model_uri=DWC.recordNumber, domain=None, range=Optional[str], mappings = [DWC["version/recordNumber-2009-04-24"]])

slots.recordedBy = Slot(uri=DWC.recordedBy, name="recordedBy", curie=DWC.curie('recordedBy'),
                      model_uri=DWC.recordedBy, domain=None, range=Optional[str], mappings = [DWC["version/recordedBy-2014-10-23"]])

slots.individualCount = Slot(uri=DWC.individualCount, name="individualCount", curie=DWC.curie('individualCount'),
                      model_uri=DWC.individualCount, domain=None, range=Optional[str], mappings = [DWC["version/individualCount-2009-04-24"]])

slots.organismQuantity = Slot(uri=DWC.organismQuantity, name="organismQuantity", curie=DWC.curie('organismQuantity'),
                      model_uri=DWC.organismQuantity, domain=None, range=Optional[str], mappings = [DWC["version/organismQuantity-2014-12-23"]])

slots.organismQuantityType = Slot(uri=DWC.organismQuantityType, name="organismQuantityType", curie=DWC.curie('organismQuantityType'),
                      model_uri=DWC.organismQuantityType, domain=None, range=Optional[str], mappings = [DWC["version/organismQuantityType-2014-12-23"]])

slots.sex = Slot(uri=DWC.sex, name="sex", curie=DWC.curie('sex'),
                      model_uri=DWC.sex, domain=None, range=Optional[str], mappings = [DWC["version/sex-2009-04-24"]])

slots.lifeStage = Slot(uri=DWC.lifeStage, name="lifeStage", curie=DWC.curie('lifeStage'),
                      model_uri=DWC.lifeStage, domain=None, range=Optional[str], mappings = [DWC["version/lifeStage-2009-04-24"]])

slots.reproductiveCondition = Slot(uri=DWC.reproductiveCondition, name="reproductiveCondition", curie=DWC.curie('reproductiveCondition'),
                      model_uri=DWC.reproductiveCondition, domain=None, range=Optional[str], mappings = [DWC["version/reproductiveCondition-2009-04-24"]])

slots.behavior = Slot(uri=DWC.behavior, name="behavior", curie=DWC.curie('behavior'),
                      model_uri=DWC.behavior, domain=None, range=Optional[str], mappings = [DWC["version/behavior-2009-04-24"]])

slots.establishmentMeans = Slot(uri=DWC.establishmentMeans, name="establishmentMeans", curie=DWC.curie('establishmentMeans'),
                      model_uri=DWC.establishmentMeans, domain=None, range=Optional[str], mappings = [DWC["version/establishmentMeans-2009-04-24"]])

slots.occurrenceStatus = Slot(uri=DWC.occurrenceStatus, name="occurrenceStatus", curie=DWC.curie('occurrenceStatus'),
                      model_uri=DWC.occurrenceStatus, domain=None, range=Optional[str], mappings = [DWC["version/occurrenceStatus-2009-09-17"]])

slots.preparations = Slot(uri=DWC.preparations, name="preparations", curie=DWC.curie('preparations'),
                      model_uri=DWC.preparations, domain=None, range=Optional[str], mappings = [DWC["version/preparations-2014-10-23"]])

slots.disposition = Slot(uri=DWC.disposition, name="disposition", curie=DWC.curie('disposition'),
                      model_uri=DWC.disposition, domain=None, range=Optional[str], mappings = [DWC["version/disposition-2009-04-24"]])

slots.associatedMedia = Slot(uri=DWC.associatedMedia, name="associatedMedia", curie=DWC.curie('associatedMedia'),
                      model_uri=DWC.associatedMedia, domain=None, range=Optional[str], mappings = [DWC["version/associatedMedia-2014-10-23"]])

slots.associatedReferences = Slot(uri=DWC.associatedReferences, name="associatedReferences", curie=DWC.curie('associatedReferences'),
                      model_uri=DWC.associatedReferences, domain=None, range=Optional[str], mappings = [DWC["version/associatedReferences-2014-10-23"]])

slots.associatedSequences = Slot(uri=DWC.associatedSequences, name="associatedSequences", curie=DWC.curie('associatedSequences'),
                      model_uri=DWC.associatedSequences, domain=None, range=Optional[str], mappings = [DWC["version/associatedSequences-2014-10-23"]])

slots.associatedTaxa = Slot(uri=DWC.associatedTaxa, name="associatedTaxa", curie=DWC.curie('associatedTaxa'),
                      model_uri=DWC.associatedTaxa, domain=None, range=Optional[str], mappings = [DWC["version/associatedTaxa-2014-10-23"]])

slots.otherCatalogNumbers = Slot(uri=DWC.otherCatalogNumbers, name="otherCatalogNumbers", curie=DWC.curie('otherCatalogNumbers'),
                      model_uri=DWC.otherCatalogNumbers, domain=None, range=Optional[str], mappings = [DWC["version/otherCatalogNumbers-2014-10-23"]])

slots.occurrenceRemarks = Slot(uri=DWC.occurrenceRemarks, name="occurrenceRemarks", curie=DWC.curie('occurrenceRemarks'),
                      model_uri=DWC.occurrenceRemarks, domain=None, range=Optional[str], mappings = [DWC["version/occurrenceRemarks-2009-04-24"]])

slots.organismID = Slot(uri=DWC.organismID, name="organismID", curie=DWC.curie('organismID'),
                      model_uri=DWC.organismID, domain=None, range=Optional[str], mappings = [DWC["version/organismID-2014-10-23"]])

slots.organismName = Slot(uri=DWC.organismName, name="organismName", curie=DWC.curie('organismName'),
                      model_uri=DWC.organismName, domain=None, range=Optional[str], mappings = [DWC["version/organismName-2014-10-23"]])

slots.organismScope = Slot(uri=DWC.organismScope, name="organismScope", curie=DWC.curie('organismScope'),
                      model_uri=DWC.organismScope, domain=None, range=Optional[str], mappings = [DWC["version/organismScope-2014-10-23"]])

slots.associatedOccurrences = Slot(uri=DWC.associatedOccurrences, name="associatedOccurrences", curie=DWC.curie('associatedOccurrences'),
                      model_uri=DWC.associatedOccurrences, domain=None, range=Optional[str], mappings = [DWC["version/associatedOccurrences-2014-10-23"]])

slots.associatedOrganisms = Slot(uri=DWC.associatedOrganisms, name="associatedOrganisms", curie=DWC.curie('associatedOrganisms'),
                      model_uri=DWC.associatedOrganisms, domain=None, range=Optional[str], mappings = [DWC["version/associatedOrganisms-2014-10-23"]])

slots.previousIdentifications = Slot(uri=DWC.previousIdentifications, name="previousIdentifications", curie=DWC.curie('previousIdentifications'),
                      model_uri=DWC.previousIdentifications, domain=None, range=Optional[str], mappings = [DWC["version/previousIdentifications-2014-10-23"]])

slots.organismRemarks = Slot(uri=DWC.organismRemarks, name="organismRemarks", curie=DWC.curie('organismRemarks'),
                      model_uri=DWC.organismRemarks, domain=None, range=Optional[str], mappings = [DWC["version/organismRemarks-2014-10-23"]])

slots.materialSampleID = Slot(uri=DWC.materialSampleID, name="materialSampleID", curie=DWC.curie('materialSampleID'),
                      model_uri=DWC.materialSampleID, domain=None, range=Optional[str], mappings = [DWC["version/materialSampleID-2013-05-25"]])

slots.eventID = Slot(uri=DWC.eventID, name="eventID", curie=DWC.curie('eventID'),
                      model_uri=DWC.eventID, domain=None, range=Optional[str], mappings = [DWC["version/eventID-2009-04-24"]])

slots.parentEventID = Slot(uri=DWC.parentEventID, name="parentEventID", curie=DWC.curie('parentEventID'),
                      model_uri=DWC.parentEventID, domain=None, range=Optional[str], mappings = [DWC["version/parentEventID-2014-12-23"]])

slots.fieldNumber = Slot(uri=DWC.fieldNumber, name="fieldNumber", curie=DWC.curie('fieldNumber'),
                      model_uri=DWC.fieldNumber, domain=None, range=Optional[str], mappings = [DWC["version/fieldNumber-2009-04-24"]])

slots.eventDate = Slot(uri=DWC.eventDate, name="eventDate", curie=DWC.curie('eventDate'),
                      model_uri=DWC.eventDate, domain=None, range=Optional[str], mappings = [DWC["version/eventDate-2009-04-24"]])

slots.eventTime = Slot(uri=DWC.eventTime, name="eventTime", curie=DWC.curie('eventTime'),
                      model_uri=DWC.eventTime, domain=None, range=Optional[str], mappings = [DWC["version/eventTime-2009-04-24"]])

slots.startDayOfYear = Slot(uri=DWC.startDayOfYear, name="startDayOfYear", curie=DWC.curie('startDayOfYear'),
                      model_uri=DWC.startDayOfYear, domain=None, range=Optional[str], mappings = [DWC["version/startDayOfYear-2009-04-24"]])

slots.endDayOfYear = Slot(uri=DWC.endDayOfYear, name="endDayOfYear", curie=DWC.curie('endDayOfYear'),
                      model_uri=DWC.endDayOfYear, domain=None, range=Optional[str], mappings = [DWC["version/endDayOfYear-2009-04-24"]])

slots.year = Slot(uri=DWC.year, name="year", curie=DWC.curie('year'),
                      model_uri=DWC.year, domain=None, range=Optional[str], mappings = [DWC["version/year-2009-04-24"]])

slots.month = Slot(uri=DWC.month, name="month", curie=DWC.curie('month'),
                      model_uri=DWC.month, domain=None, range=Optional[str], mappings = [DWC["version/month-2009-04-24"]])

slots.day = Slot(uri=DWC.day, name="day", curie=DWC.curie('day'),
                      model_uri=DWC.day, domain=None, range=Optional[str], mappings = [DWC["version/day-2009-04-24"]])

slots.verbatimEventDate = Slot(uri=DWC.verbatimEventDate, name="verbatimEventDate", curie=DWC.curie('verbatimEventDate'),
                      model_uri=DWC.verbatimEventDate, domain=None, range=Optional[str], mappings = [DWC["version/verbatimEventDate-2009-04-24"]])

slots.habitat = Slot(uri=DWC.habitat, name="habitat", curie=DWC.curie('habitat'),
                      model_uri=DWC.habitat, domain=None, range=Optional[str], mappings = [DWC["version/habitat-2009-04-24"]])

slots.samplingProtocol = Slot(uri=DWC.samplingProtocol, name="samplingProtocol", curie=DWC.curie('samplingProtocol'),
                      model_uri=DWC.samplingProtocol, domain=None, range=Optional[str], mappings = [DWC["version/samplingProtocol-2009-04-24"]])

slots.sampleSizeValue = Slot(uri=DWC.sampleSizeValue, name="sampleSizeValue", curie=DWC.curie('sampleSizeValue'),
                      model_uri=DWC.sampleSizeValue, domain=None, range=Optional[str], mappings = [DWC["version/sampleSizeValue-2014-12-23"]])

slots.sampleSizeUnit = Slot(uri=DWC.sampleSizeUnit, name="sampleSizeUnit", curie=DWC.curie('sampleSizeUnit'),
                      model_uri=DWC.sampleSizeUnit, domain=None, range=Optional[str], mappings = [DWC["version/sampleSizeUnit-2014-12-23"]])

slots.samplingEffort = Slot(uri=DWC.samplingEffort, name="samplingEffort", curie=DWC.curie('samplingEffort'),
                      model_uri=DWC.samplingEffort, domain=None, range=Optional[str], mappings = [DWC["version/samplingEffort-2009-08-24"]])

slots.fieldNotes = Slot(uri=DWC.fieldNotes, name="fieldNotes", curie=DWC.curie('fieldNotes'),
                      model_uri=DWC.fieldNotes, domain=None, range=Optional[str], mappings = [DWC["version/fieldNotes-2009-04-24"]])

slots.eventRemarks = Slot(uri=DWC.eventRemarks, name="eventRemarks", curie=DWC.curie('eventRemarks'),
                      model_uri=DWC.eventRemarks, domain=None, range=Optional[str], mappings = [DWC["version/eventRemarks-2009-04-24"]])

slots.locationID = Slot(uri=DWC.locationID, name="locationID", curie=DWC.curie('locationID'),
                      model_uri=DWC.locationID, domain=None, range=Optional[str], mappings = [DWC["version/locationID-2009-04-24"]])

slots.higherGeographyID = Slot(uri=DWC.higherGeographyID, name="higherGeographyID", curie=DWC.curie('higherGeographyID'),
                      model_uri=DWC.higherGeographyID, domain=None, range=Optional[str], mappings = [DWC["version/higherGeographyID-2009-04-24"]])

slots.higherGeography = Slot(uri=DWC.higherGeography, name="higherGeography", curie=DWC.curie('higherGeography'),
                      model_uri=DWC.higherGeography, domain=None, range=Optional[str], mappings = [DWC["version/higherGeography-2014-10-23"]])

slots.continent = Slot(uri=DWC.continent, name="continent", curie=DWC.curie('continent'),
                      model_uri=DWC.continent, domain=None, range=Optional[str], mappings = [DWC["version/continent-2009-04-24"]])

slots.waterBody = Slot(uri=DWC.waterBody, name="waterBody", curie=DWC.curie('waterBody'),
                      model_uri=DWC.waterBody, domain=None, range=Optional[str], mappings = [DWC["version/waterBody-2009-04-24"]])

slots.islandGroup = Slot(uri=DWC.islandGroup, name="islandGroup", curie=DWC.curie('islandGroup'),
                      model_uri=DWC.islandGroup, domain=None, range=Optional[str], mappings = [DWC["version/islandGroup-2009-04-24"]])

slots.island = Slot(uri=DWC.island, name="island", curie=DWC.curie('island'),
                      model_uri=DWC.island, domain=None, range=Optional[str], mappings = [DWC["version/island-2009-04-24"]])

slots.country = Slot(uri=DWC.country, name="country", curie=DWC.curie('country'),
                      model_uri=DWC.country, domain=None, range=Optional[str], mappings = [DWC["version/country-2009-04-24"]])

slots.countryCode = Slot(uri=DWC.countryCode, name="countryCode", curie=DWC.curie('countryCode'),
                      model_uri=DWC.countryCode, domain=None, range=Optional[str], mappings = [DWC["version/countryCode-2009-04-24"]])

slots.stateProvince = Slot(uri=DWC.stateProvince, name="stateProvince", curie=DWC.curie('stateProvince'),
                      model_uri=DWC.stateProvince, domain=None, range=Optional[str], mappings = [DWC["version/stateProvince-2009-04-24"]])

slots.county = Slot(uri=DWC.county, name="county", curie=DWC.curie('county'),
                      model_uri=DWC.county, domain=None, range=Optional[str], mappings = [DWC["version/county-2009-04-24"]])

slots.municipality = Slot(uri=DWC.municipality, name="municipality", curie=DWC.curie('municipality'),
                      model_uri=DWC.municipality, domain=None, range=Optional[str], mappings = [DWC["version/municipality-2009-08-24"]])

slots.locality = Slot(uri=DWC.locality, name="locality", curie=DWC.curie('locality'),
                      model_uri=DWC.locality, domain=None, range=Optional[str], mappings = [DWC["version/locality-2009-04-24"]])

slots.verbatimLocality = Slot(uri=DWC.verbatimLocality, name="verbatimLocality", curie=DWC.curie('verbatimLocality'),
                      model_uri=DWC.verbatimLocality, domain=None, range=Optional[str], mappings = [DWC["version/verbatimLocality-2009-04-24"]])

slots.minimumElevationInMeters = Slot(uri=DWC.minimumElevationInMeters, name="minimumElevationInMeters", curie=DWC.curie('minimumElevationInMeters'),
                      model_uri=DWC.minimumElevationInMeters, domain=None, range=Optional[str], mappings = [DWC["version/minimumElevationInMeters-2009-04-24"]])

slots.maximumElevationInMeters = Slot(uri=DWC.maximumElevationInMeters, name="maximumElevationInMeters", curie=DWC.curie('maximumElevationInMeters'),
                      model_uri=DWC.maximumElevationInMeters, domain=None, range=Optional[str], mappings = [DWC["version/maximumElevationInMeters-2009-04-24"]])

slots.verbatimElevation = Slot(uri=DWC.verbatimElevation, name="verbatimElevation", curie=DWC.curie('verbatimElevation'),
                      model_uri=DWC.verbatimElevation, domain=None, range=Optional[str], mappings = [DWC["version/verbatimElevation-2009-04-24"]])

slots.minimumDepthInMeters = Slot(uri=DWC.minimumDepthInMeters, name="minimumDepthInMeters", curie=DWC.curie('minimumDepthInMeters'),
                      model_uri=DWC.minimumDepthInMeters, domain=None, range=Optional[str], mappings = [DWC["version/minimumDepthInMeters-2009-04-24"]])

slots.maximumDepthInMeters = Slot(uri=DWC.maximumDepthInMeters, name="maximumDepthInMeters", curie=DWC.curie('maximumDepthInMeters'),
                      model_uri=DWC.maximumDepthInMeters, domain=None, range=Optional[str], mappings = [DWC["version/maximumDepthInMeters-2009-04-24"]])

slots.verbatimDepth = Slot(uri=DWC.verbatimDepth, name="verbatimDepth", curie=DWC.curie('verbatimDepth'),
                      model_uri=DWC.verbatimDepth, domain=None, range=Optional[str], mappings = [DWC["version/verbatimDepth-2009-04-24"]])

slots.minimumDistanceAboveSurfaceInMeters = Slot(uri=DWC.minimumDistanceAboveSurfaceInMeters, name="minimumDistanceAboveSurfaceInMeters", curie=DWC.curie('minimumDistanceAboveSurfaceInMeters'),
                      model_uri=DWC.minimumDistanceAboveSurfaceInMeters, domain=None, range=Optional[str], mappings = [DWC["version/minimumDistanceAboveSurfaceInMeters-2009-04-24"]])

slots.maximumDistanceAboveSurfaceInMeters = Slot(uri=DWC.maximumDistanceAboveSurfaceInMeters, name="maximumDistanceAboveSurfaceInMeters", curie=DWC.curie('maximumDistanceAboveSurfaceInMeters'),
                      model_uri=DWC.maximumDistanceAboveSurfaceInMeters, domain=None, range=Optional[str], mappings = [DWC["version/maximumDistanceAboveSurfaceInMeters-2009-04-24"]])

slots.locationAccordingTo = Slot(uri=DWC.locationAccordingTo, name="locationAccordingTo", curie=DWC.curie('locationAccordingTo'),
                      model_uri=DWC.locationAccordingTo, domain=None, range=Optional[str], mappings = [DWC["version/locationAccordingTo-2009-08-24"]])

slots.locationRemarks = Slot(uri=DWC.locationRemarks, name="locationRemarks", curie=DWC.curie('locationRemarks'),
                      model_uri=DWC.locationRemarks, domain=None, range=Optional[str], mappings = [DWC["version/locationRemarks-2009-04-24"]])

slots.decimalLatitude = Slot(uri=DWC.decimalLatitude, name="decimalLatitude", curie=DWC.curie('decimalLatitude'),
                      model_uri=DWC.decimalLatitude, domain=None, range=Optional[str], mappings = [DWC["version/decimalLatitude-2009-04-24"]])

slots.decimalLongitude = Slot(uri=DWC.decimalLongitude, name="decimalLongitude", curie=DWC.curie('decimalLongitude'),
                      model_uri=DWC.decimalLongitude, domain=None, range=Optional[str], mappings = [DWC["version/decimalLongitude-2009-04-24"]])

slots.geodeticDatum = Slot(uri=DWC.geodeticDatum, name="geodeticDatum", curie=DWC.curie('geodeticDatum'),
                      model_uri=DWC.geodeticDatum, domain=None, range=Optional[str], mappings = [DWC["version/geodeticDatum-2009-04-24"]])

slots.coordinateUncertaintyInMeters = Slot(uri=DWC.coordinateUncertaintyInMeters, name="coordinateUncertaintyInMeters", curie=DWC.curie('coordinateUncertaintyInMeters'),
                      model_uri=DWC.coordinateUncertaintyInMeters, domain=None, range=Optional[str], mappings = [DWC["version/coordinateUncertaintyInMeters-2009-04-24"]])

slots.coordinatePrecision = Slot(uri=DWC.coordinatePrecision, name="coordinatePrecision", curie=DWC.curie('coordinatePrecision'),
                      model_uri=DWC.coordinatePrecision, domain=None, range=Optional[str], mappings = [DWC["version/coordinatePrecision-2009-04-24"]])

slots.pointRadiusSpatialFit = Slot(uri=DWC.pointRadiusSpatialFit, name="pointRadiusSpatialFit", curie=DWC.curie('pointRadiusSpatialFit'),
                      model_uri=DWC.pointRadiusSpatialFit, domain=None, range=Optional[str], mappings = [DWC["version/pointRadiusSpatialFit-2009-04-24"]])

slots.verbatimCoordinates = Slot(uri=DWC.verbatimCoordinates, name="verbatimCoordinates", curie=DWC.curie('verbatimCoordinates'),
                      model_uri=DWC.verbatimCoordinates, domain=None, range=Optional[str], mappings = [DWC["version/verbatimCoordinates-2009-04-24"]])

slots.verbatimLatitude = Slot(uri=DWC.verbatimLatitude, name="verbatimLatitude", curie=DWC.curie('verbatimLatitude'),
                      model_uri=DWC.verbatimLatitude, domain=None, range=Optional[str], mappings = [DWC["version/verbatimLatitude-2009-04-24"]])

slots.verbatimLongitude = Slot(uri=DWC.verbatimLongitude, name="verbatimLongitude", curie=DWC.curie('verbatimLongitude'),
                      model_uri=DWC.verbatimLongitude, domain=None, range=Optional[str], mappings = [DWC["version/verbatimLongitude-2009-04-24"]])

slots.verbatimCoordinateSystem = Slot(uri=DWC.verbatimCoordinateSystem, name="verbatimCoordinateSystem", curie=DWC.curie('verbatimCoordinateSystem'),
                      model_uri=DWC.verbatimCoordinateSystem, domain=None, range=Optional[str], mappings = [DWC["version/verbatimCoordinateSystem-2009-04-24"]])

slots.verbatimSRS = Slot(uri=DWC.verbatimSRS, name="verbatimSRS", curie=DWC.curie('verbatimSRS'),
                      model_uri=DWC.verbatimSRS, domain=None, range=Optional[str], mappings = [DWC["version/verbatimSRS-2009-07-06"]])

slots.footprintWKT = Slot(uri=DWC.footprintWKT, name="footprintWKT", curie=DWC.curie('footprintWKT'),
                      model_uri=DWC.footprintWKT, domain=None, range=Optional[str], mappings = [DWC["version/footprintWKT-2009-04-24"]])

slots.footprintSRS = Slot(uri=DWC.footprintSRS, name="footprintSRS", curie=DWC.curie('footprintSRS'),
                      model_uri=DWC.footprintSRS, domain=None, range=Optional[str], mappings = [DWC["version/footprintSRS-2009-07-06"]])

slots.footprintSpatialFit = Slot(uri=DWC.footprintSpatialFit, name="footprintSpatialFit", curie=DWC.curie('footprintSpatialFit'),
                      model_uri=DWC.footprintSpatialFit, domain=None, range=Optional[str], mappings = [DWC["version/footprintSpatialFit-2009-04-24"]])

slots.georeferencedBy = Slot(uri=DWC.georeferencedBy, name="georeferencedBy", curie=DWC.curie('georeferencedBy'),
                      model_uri=DWC.georeferencedBy, domain=None, range=Optional[str], mappings = [DWC["version/georeferencedBy-2014-10-23"]])

slots.georeferencedDate = Slot(uri=DWC.georeferencedDate, name="georeferencedDate", curie=DWC.curie('georeferencedDate'),
                      model_uri=DWC.georeferencedDate, domain=None, range=Optional[str], mappings = [DWC["version/georeferencedDate-2011-10-16"]])

slots.georeferenceProtocol = Slot(uri=DWC.georeferenceProtocol, name="georeferenceProtocol", curie=DWC.curie('georeferenceProtocol'),
                      model_uri=DWC.georeferenceProtocol, domain=None, range=Optional[str], mappings = [DWC["version/georeferenceProtocol-2009-04-24"]])

slots.georeferenceSources = Slot(uri=DWC.georeferenceSources, name="georeferenceSources", curie=DWC.curie('georeferenceSources'),
                      model_uri=DWC.georeferenceSources, domain=None, range=Optional[str], mappings = [DWC["version/georeferenceSources-2014-10-23"]])

slots.georeferenceVerificationStatus = Slot(uri=DWC.georeferenceVerificationStatus, name="georeferenceVerificationStatus", curie=DWC.curie('georeferenceVerificationStatus'),
                      model_uri=DWC.georeferenceVerificationStatus, domain=None, range=Optional[str], mappings = [DWC["version/georeferenceVerificationStatus-2009-04-24"]])

slots.georeferenceRemarks = Slot(uri=DWC.georeferenceRemarks, name="georeferenceRemarks", curie=DWC.curie('georeferenceRemarks'),
                      model_uri=DWC.georeferenceRemarks, domain=None, range=Optional[str], mappings = [DWC["version/georeferenceRemarks-2009-04-24"]])

slots.geologicalContextID = Slot(uri=DWC.geologicalContextID, name="geologicalContextID", curie=DWC.curie('geologicalContextID'),
                      model_uri=DWC.geologicalContextID, domain=None, range=Optional[str], mappings = [DWC["version/geologicalContextID-2009-07-06"]])

slots.earliestEonOrLowestEonothem = Slot(uri=DWC.earliestEonOrLowestEonothem, name="earliestEonOrLowestEonothem", curie=DWC.curie('earliestEonOrLowestEonothem'),
                      model_uri=DWC.earliestEonOrLowestEonothem, domain=None, range=Optional[str], mappings = [DWC["version/earliestEonOrLowestEonothem-2009-04-24"]])

slots.latestEonOrHighestEonothem = Slot(uri=DWC.latestEonOrHighestEonothem, name="latestEonOrHighestEonothem", curie=DWC.curie('latestEonOrHighestEonothem'),
                      model_uri=DWC.latestEonOrHighestEonothem, domain=None, range=Optional[str], mappings = [DWC["version/latestEonOrHighestEonothem-2009-04-24"]])

slots.earliestEraOrLowestErathem = Slot(uri=DWC.earliestEraOrLowestErathem, name="earliestEraOrLowestErathem", curie=DWC.curie('earliestEraOrLowestErathem'),
                      model_uri=DWC.earliestEraOrLowestErathem, domain=None, range=Optional[str], mappings = [DWC["version/earliestEraOrLowestErathem-2009-04-24"]])

slots.latestEraOrHighestErathem = Slot(uri=DWC.latestEraOrHighestErathem, name="latestEraOrHighestErathem", curie=DWC.curie('latestEraOrHighestErathem'),
                      model_uri=DWC.latestEraOrHighestErathem, domain=None, range=Optional[str], mappings = [DWC["version/latestEraOrHighestErathem-2009-04-24"]])

slots.earliestPeriodOrLowestSystem = Slot(uri=DWC.earliestPeriodOrLowestSystem, name="earliestPeriodOrLowestSystem", curie=DWC.curie('earliestPeriodOrLowestSystem'),
                      model_uri=DWC.earliestPeriodOrLowestSystem, domain=None, range=Optional[str], mappings = [DWC["version/earliestPeriodOrLowestSystem-2009-04-24"]])

slots.latestPeriodOrHighestSystem = Slot(uri=DWC.latestPeriodOrHighestSystem, name="latestPeriodOrHighestSystem", curie=DWC.curie('latestPeriodOrHighestSystem'),
                      model_uri=DWC.latestPeriodOrHighestSystem, domain=None, range=Optional[str], mappings = [DWC["version/latestPeriodOrHighestSystem-2009-04-24"]])

slots.earliestEpochOrLowestSeries = Slot(uri=DWC.earliestEpochOrLowestSeries, name="earliestEpochOrLowestSeries", curie=DWC.curie('earliestEpochOrLowestSeries'),
                      model_uri=DWC.earliestEpochOrLowestSeries, domain=None, range=Optional[str], mappings = [DWC["version/earliestEpochOrLowestSeries-2009-04-24"]])

slots.latestEpochOrHighestSeries = Slot(uri=DWC.latestEpochOrHighestSeries, name="latestEpochOrHighestSeries", curie=DWC.curie('latestEpochOrHighestSeries'),
                      model_uri=DWC.latestEpochOrHighestSeries, domain=None, range=Optional[str], mappings = [DWC["version/latestEpochOrHighestSeries-2009-04-24"]])

slots.earliestAgeOrLowestStage = Slot(uri=DWC.earliestAgeOrLowestStage, name="earliestAgeOrLowestStage", curie=DWC.curie('earliestAgeOrLowestStage'),
                      model_uri=DWC.earliestAgeOrLowestStage, domain=None, range=Optional[str], mappings = [DWC["version/earliestAgeOrLowestStage-2009-04-24"]])

slots.latestAgeOrHighestStage = Slot(uri=DWC.latestAgeOrHighestStage, name="latestAgeOrHighestStage", curie=DWC.curie('latestAgeOrHighestStage'),
                      model_uri=DWC.latestAgeOrHighestStage, domain=None, range=Optional[str], mappings = [DWC["version/latestAgeOrHighestStage-2009-04-24"]])

slots.lowestBiostratigraphicZone = Slot(uri=DWC.lowestBiostratigraphicZone, name="lowestBiostratigraphicZone", curie=DWC.curie('lowestBiostratigraphicZone'),
                      model_uri=DWC.lowestBiostratigraphicZone, domain=None, range=Optional[str], mappings = [DWC["version/lowestBiostratigraphicZone-2009-04-24"]])

slots.highestBiostratigraphicZone = Slot(uri=DWC.highestBiostratigraphicZone, name="highestBiostratigraphicZone", curie=DWC.curie('highestBiostratigraphicZone'),
                      model_uri=DWC.highestBiostratigraphicZone, domain=None, range=Optional[str], mappings = [DWC["version/highestBiostratigraphicZone-2009-04-24"]])

slots.lithostratigraphicTerms = Slot(uri=DWC.lithostratigraphicTerms, name="lithostratigraphicTerms", curie=DWC.curie('lithostratigraphicTerms'),
                      model_uri=DWC.lithostratigraphicTerms, domain=None, range=Optional[str], mappings = [DWC["version/lithostratigraphicTerms-2009-04-24"]])

slots.group = Slot(uri=DWC.group, name="group", curie=DWC.curie('group'),
                      model_uri=DWC.group, domain=None, range=Optional[str], mappings = [DWC["version/group-2009-04-24"]])

slots.formation = Slot(uri=DWC.formation, name="formation", curie=DWC.curie('formation'),
                      model_uri=DWC.formation, domain=None, range=Optional[str], mappings = [DWC["version/formation-2009-04-24"]])

slots.member = Slot(uri=DWC.member, name="member", curie=DWC.curie('member'),
                      model_uri=DWC.member, domain=None, range=Optional[str], mappings = [DWC["version/member-2009-04-24"]])

slots.bed = Slot(uri=DWC.bed, name="bed", curie=DWC.curie('bed'),
                      model_uri=DWC.bed, domain=None, range=Optional[str], mappings = [DWC["version/bed-2009-04-24"]])

slots.identificationID = Slot(uri=DWC.identificationID, name="identificationID", curie=DWC.curie('identificationID'),
                      model_uri=DWC.identificationID, domain=None, range=Optional[str], mappings = [DWC["version/identificationID-2009-04-24"]])

slots.identificationQualifier = Slot(uri=DWC.identificationQualifier, name="identificationQualifier", curie=DWC.curie('identificationQualifier'),
                      model_uri=DWC.identificationQualifier, domain=None, range=Optional[str], mappings = [DWC["version/identificationQualifier-2009-04-24"]])

slots.typeStatus = Slot(uri=DWC.typeStatus, name="typeStatus", curie=DWC.curie('typeStatus'),
                      model_uri=DWC.typeStatus, domain=None, range=Optional[str], mappings = [DWC["version/typeStatus-2014-10-23"]])

slots.identifiedBy = Slot(uri=DWC.identifiedBy, name="identifiedBy", curie=DWC.curie('identifiedBy'),
                      model_uri=DWC.identifiedBy, domain=None, range=Optional[str], mappings = [DWC["version/identifiedBy-2014-10-23"]])

slots.dateIdentified = Slot(uri=DWC.dateIdentified, name="dateIdentified", curie=DWC.curie('dateIdentified'),
                      model_uri=DWC.dateIdentified, domain=None, range=Optional[str], mappings = [DWC["version/dateIdentified-2009-08-24"]])

slots.identificationReferences = Slot(uri=DWC.identificationReferences, name="identificationReferences", curie=DWC.curie('identificationReferences'),
                      model_uri=DWC.identificationReferences, domain=None, range=Optional[str], mappings = [DWC["version/identificationReferences-2014-10-23"]])

slots.identificationVerificationStatus = Slot(uri=DWC.identificationVerificationStatus, name="identificationVerificationStatus", curie=DWC.curie('identificationVerificationStatus'),
                      model_uri=DWC.identificationVerificationStatus, domain=None, range=Optional[str], mappings = [DWC["version/identificationVerificationStatus-2011-10-16"]])

slots.identificationRemarks = Slot(uri=DWC.identificationRemarks, name="identificationRemarks", curie=DWC.curie('identificationRemarks'),
                      model_uri=DWC.identificationRemarks, domain=None, range=Optional[str], mappings = [DWC["version/identificationRemarks-2009-04-24"]])

slots.taxonID = Slot(uri=DWC.taxonID, name="taxonID", curie=DWC.curie('taxonID'),
                      model_uri=DWC.taxonID, domain=None, range=Optional[str], mappings = [DWC["version/taxonID-2009-08-24"]])

slots.scientificNameID = Slot(uri=DWC.scientificNameID, name="scientificNameID", curie=DWC.curie('scientificNameID'),
                      model_uri=DWC.scientificNameID, domain=None, range=Optional[str], mappings = [DWC["version/scientificNameID-2009-08-24"]])

slots.acceptedNameUsageID = Slot(uri=DWC.acceptedNameUsageID, name="acceptedNameUsageID", curie=DWC.curie('acceptedNameUsageID'),
                      model_uri=DWC.acceptedNameUsageID, domain=None, range=Optional[str], mappings = [DWC["version/acceptedNameUsageID-2009-09-21"]])

slots.parentNameUsageID = Slot(uri=DWC.parentNameUsageID, name="parentNameUsageID", curie=DWC.curie('parentNameUsageID'),
                      model_uri=DWC.parentNameUsageID, domain=None, range=Optional[str], mappings = [DWC["version/parentNameUsageID-2009-09-21"]])

slots.originalNameUsageID = Slot(uri=DWC.originalNameUsageID, name="originalNameUsageID", curie=DWC.curie('originalNameUsageID'),
                      model_uri=DWC.originalNameUsageID, domain=None, range=Optional[str], mappings = [DWC["version/originalNameUsageID-2009-09-21"]])

slots.nameAccordingToID = Slot(uri=DWC.nameAccordingToID, name="nameAccordingToID", curie=DWC.curie('nameAccordingToID'),
                      model_uri=DWC.nameAccordingToID, domain=None, range=Optional[str], mappings = [DWC["version/nameAccordingToID-2009-09-21"]])

slots.namePublishedInID = Slot(uri=DWC.namePublishedInID, name="namePublishedInID", curie=DWC.curie('namePublishedInID'),
                      model_uri=DWC.namePublishedInID, domain=None, range=Optional[str], mappings = [DWC["version/namePublishedInID-2009-09-21"]])

slots.taxonConceptID = Slot(uri=DWC.taxonConceptID, name="taxonConceptID", curie=DWC.curie('taxonConceptID'),
                      model_uri=DWC.taxonConceptID, domain=None, range=Optional[str], mappings = [DWC["version/taxonConceptID-2009-09-21"]])

slots.scientificName = Slot(uri=DWC.scientificName, name="scientificName", curie=DWC.curie('scientificName'),
                      model_uri=DWC.scientificName, domain=None, range=Optional[str], mappings = [DWC["version/scientificName-2009-09-21"]])

slots.acceptedNameUsage = Slot(uri=DWC.acceptedNameUsage, name="acceptedNameUsage", curie=DWC.curie('acceptedNameUsage'),
                      model_uri=DWC.acceptedNameUsage, domain=None, range=Optional[str], mappings = [DWC["version/acceptedNameUsage-2009-09-21"]])

slots.parentNameUsage = Slot(uri=DWC.parentNameUsage, name="parentNameUsage", curie=DWC.curie('parentNameUsage'),
                      model_uri=DWC.parentNameUsage, domain=None, range=Optional[str], mappings = [DWC["version/parentNameUsage-2009-09-21"]])

slots.originalNameUsage = Slot(uri=DWC.originalNameUsage, name="originalNameUsage", curie=DWC.curie('originalNameUsage'),
                      model_uri=DWC.originalNameUsage, domain=None, range=Optional[str], mappings = [DWC["version/originalNameUsage-2009-09-21"]])

slots.nameAccordingTo = Slot(uri=DWC.nameAccordingTo, name="nameAccordingTo", curie=DWC.curie('nameAccordingTo'),
                      model_uri=DWC.nameAccordingTo, domain=None, range=Optional[str], mappings = [DWC["version/nameAccordingTo-2009-09-21"]])

slots.namePublishedIn = Slot(uri=DWC.namePublishedIn, name="namePublishedIn", curie=DWC.curie('namePublishedIn'),
                      model_uri=DWC.namePublishedIn, domain=None, range=Optional[str], mappings = [DWC["version/namePublishedIn-2009-09-21"]])

slots.namePublishedInYear = Slot(uri=DWC.namePublishedInYear, name="namePublishedInYear", curie=DWC.curie('namePublishedInYear'),
                      model_uri=DWC.namePublishedInYear, domain=None, range=Optional[str], mappings = [DWC["version/namePublishedInYear-2011-10-16"]])

slots.higherClassification = Slot(uri=DWC.higherClassification, name="higherClassification", curie=DWC.curie('higherClassification'),
                      model_uri=DWC.higherClassification, domain=None, range=Optional[str], mappings = [DWC["version/higherClassification-2014-10-23"]])

slots.kingdom = Slot(uri=DWC.kingdom, name="kingdom", curie=DWC.curie('kingdom'),
                      model_uri=DWC.kingdom, domain=None, range=Optional[str], mappings = [DWC["version/kingdom-2009-08-24"]])

slots.phylum = Slot(uri=DWC.phylum, name="phylum", curie=DWC.curie('phylum'),
                      model_uri=DWC.phylum, domain=None, range=Optional[str], mappings = [DWC["version/phylum-2009-08-24"]])

slots.class = Slot(uri=DWC.class, name="class", curie=DWC.curie('class'),
                      model_uri=DWC.class, domain=None, range=Optional[str], mappings = [DWC["version/class-2009-08-24"]])

slots.order = Slot(uri=DWC.order, name="order", curie=DWC.curie('order'),
                      model_uri=DWC.order, domain=None, range=Optional[str], mappings = [DWC["version/order-2009-08-24"]])

slots.family = Slot(uri=DWC.family, name="family", curie=DWC.curie('family'),
                      model_uri=DWC.family, domain=None, range=Optional[str], mappings = [DWC["version/family-2009-08-24"]])

slots.genus = Slot(uri=DWC.genus, name="genus", curie=DWC.curie('genus'),
                      model_uri=DWC.genus, domain=None, range=Optional[str], mappings = [DWC["version/genus-2009-08-24"]])

slots.subgenus = Slot(uri=DWC.subgenus, name="subgenus", curie=DWC.curie('subgenus'),
                      model_uri=DWC.subgenus, domain=None, range=Optional[str], mappings = [DWC["version/subgenus-2009-08-24"]])

slots.specificEpithet = Slot(uri=DWC.specificEpithet, name="specificEpithet", curie=DWC.curie('specificEpithet'),
                      model_uri=DWC.specificEpithet, domain=None, range=Optional[str], mappings = [DWC["version/specificEpithet-2009-04-24"]])

slots.infraspecificEpithet = Slot(uri=DWC.infraspecificEpithet, name="infraspecificEpithet", curie=DWC.curie('infraspecificEpithet'),
                      model_uri=DWC.infraspecificEpithet, domain=None, range=Optional[str], mappings = [DWC["version/infraspecificEpithet-2009-08-24"]])

slots.taxonRank = Slot(uri=DWC.taxonRank, name="taxonRank", curie=DWC.curie('taxonRank'),
                      model_uri=DWC.taxonRank, domain=None, range=Optional[str], mappings = [DWC["version/taxonRank-2009-09-21"]])

slots.verbatimTaxonRank = Slot(uri=DWC.verbatimTaxonRank, name="verbatimTaxonRank", curie=DWC.curie('verbatimTaxonRank'),
                      model_uri=DWC.verbatimTaxonRank, domain=None, range=Optional[str], mappings = [DWC["version/verbatimTaxonRank-2009-09-21"]])

slots.scientificNameAuthorship = Slot(uri=DWC.scientificNameAuthorship, name="scientificNameAuthorship", curie=DWC.curie('scientificNameAuthorship'),
                      model_uri=DWC.scientificNameAuthorship, domain=None, range=Optional[str], mappings = [DWC["version/scientificNameAuthorship-2009-04-24"]])

slots.vernacularName = Slot(uri=DWC.vernacularName, name="vernacularName", curie=DWC.curie('vernacularName'),
                      model_uri=DWC.vernacularName, domain=None, range=Optional[str], mappings = [DWC["version/vernacularName-2009-07-06"]])

slots.nomenclaturalCode = Slot(uri=DWC.nomenclaturalCode, name="nomenclaturalCode", curie=DWC.curie('nomenclaturalCode'),
                      model_uri=DWC.nomenclaturalCode, domain=None, range=Optional[str], mappings = [DWC["version/nomenclaturalCode-2009-09-21"]])

slots.taxonomicStatus = Slot(uri=DWC.taxonomicStatus, name="taxonomicStatus", curie=DWC.curie('taxonomicStatus'),
                      model_uri=DWC.taxonomicStatus, domain=None, range=Optional[str], mappings = [DWC["version/taxonomicStatus-2009-04-24"]])

slots.nomenclaturalStatus = Slot(uri=DWC.nomenclaturalStatus, name="nomenclaturalStatus", curie=DWC.curie('nomenclaturalStatus'),
                      model_uri=DWC.nomenclaturalStatus, domain=None, range=Optional[str], mappings = [DWC["version/nomenclaturalStatus-2009-04-24"]])

slots.taxonRemarks = Slot(uri=DWC.taxonRemarks, name="taxonRemarks", curie=DWC.curie('taxonRemarks'),
                      model_uri=DWC.taxonRemarks, domain=None, range=Optional[str], mappings = [DWC["version/taxonRemarks-2009-08-24"]])

slots.measurementID = Slot(uri=DWC.measurementID, name="measurementID", curie=DWC.curie('measurementID'),
                      model_uri=DWC.measurementID, domain=None, range=Optional[str], mappings = [DWC["version/measurementID-2009-04-24"]])

slots.measurementType = Slot(uri=DWC.measurementType, name="measurementType", curie=DWC.curie('measurementType'),
                      model_uri=DWC.measurementType, domain=None, range=Optional[str], mappings = [DWC["version/measurementType-2009-04-24"]])

slots.measurementValue = Slot(uri=DWC.measurementValue, name="measurementValue", curie=DWC.curie('measurementValue'),
                      model_uri=DWC.measurementValue, domain=None, range=Optional[str], mappings = [DWC["version/measurementValue-2009-04-24"]])

slots.measurementAccuracy = Slot(uri=DWC.measurementAccuracy, name="measurementAccuracy", curie=DWC.curie('measurementAccuracy'),
                      model_uri=DWC.measurementAccuracy, domain=None, range=Optional[str], mappings = [DWC["version/measurementAccuracy-2009-04-24"]])

slots.measurementUnit = Slot(uri=DWC.measurementUnit, name="measurementUnit", curie=DWC.curie('measurementUnit'),
                      model_uri=DWC.measurementUnit, domain=None, range=Optional[str], mappings = [DWC["version/measurementUnit-2009-04-24"]])

slots.measurementDeterminedBy = Slot(uri=DWC.measurementDeterminedBy, name="measurementDeterminedBy", curie=DWC.curie('measurementDeterminedBy'),
                      model_uri=DWC.measurementDeterminedBy, domain=None, range=Optional[str], mappings = [DWC["version/measurementDeterminedBy-2014-10-23"]])

slots.measurementDeterminedDate = Slot(uri=DWC.measurementDeterminedDate, name="measurementDeterminedDate", curie=DWC.curie('measurementDeterminedDate'),
                      model_uri=DWC.measurementDeterminedDate, domain=None, range=Optional[str], mappings = [DWC["version/measurementDeterminedDate-2009-04-24"]])

slots.measurementMethod = Slot(uri=DWC.measurementMethod, name="measurementMethod", curie=DWC.curie('measurementMethod'),
                      model_uri=DWC.measurementMethod, domain=None, range=Optional[str], mappings = [DWC["version/measurementMethod-2009-04-24"]])

slots.measurementRemarks = Slot(uri=DWC.measurementRemarks, name="measurementRemarks", curie=DWC.curie('measurementRemarks'),
                      model_uri=DWC.measurementRemarks, domain=None, range=Optional[str], mappings = [DWC["version/measurementRemarks-2009-04-24"]])

slots.resourceRelationshipID = Slot(uri=DWC.resourceRelationshipID, name="resourceRelationshipID", curie=DWC.curie('resourceRelationshipID'),
                      model_uri=DWC.resourceRelationshipID, domain=None, range=Optional[str], mappings = [DWC["version/resourceRelationshipID-2009-04-24"]])

slots.resourceID = Slot(uri=DWC.resourceID, name="resourceID", curie=DWC.curie('resourceID'),
                      model_uri=DWC.resourceID, domain=None, range=Optional[str], mappings = [DWC["version/resourceID-2009-04-24"]])

slots.relatedResourceID = Slot(uri=DWC.relatedResourceID, name="relatedResourceID", curie=DWC.curie('relatedResourceID'),
                      model_uri=DWC.relatedResourceID, domain=None, range=Optional[str], mappings = [DWC["version/relatedResourceID-2009-04-24"]])

slots.relationshipOfResource = Slot(uri=DWC.relationshipOfResource, name="relationshipOfResource", curie=DWC.curie('relationshipOfResource'),
                      model_uri=DWC.relationshipOfResource, domain=None, range=Optional[str], mappings = [DWC["version/relationshipOfResource-2009-04-24"]])

slots.relationshipAccordingTo = Slot(uri=DWC.relationshipAccordingTo, name="relationshipAccordingTo", curie=DWC.curie('relationshipAccordingTo'),
                      model_uri=DWC.relationshipAccordingTo, domain=None, range=Optional[str], mappings = [DWC["version/relationshipAccordingTo-2009-04-24"]])

slots.relationshipEstablishedDate = Slot(uri=DWC.relationshipEstablishedDate, name="relationshipEstablishedDate", curie=DWC.curie('relationshipEstablishedDate'),
                      model_uri=DWC.relationshipEstablishedDate, domain=None, range=Optional[str], mappings = [DWC["version/relationshipEstablishedDate-2009-04-24"]])

slots.relationshipRemarks = Slot(uri=DWC.relationshipRemarks, name="relationshipRemarks", curie=DWC.curie('relationshipRemarks'),
                      model_uri=DWC.relationshipRemarks, domain=None, range=Optional[str], mappings = [DWC["version/relationshipRemarks-2009-04-24"]])

slots.inDescribedPlace = Slot(uri=DWC.inDescribedPlace, name="inDescribedPlace", curie=DWC.curie('inDescribedPlace'),
                      model_uri=DWC.inDescribedPlace, domain=None, range=Optional[str])

slots.toTaxon = Slot(uri=DWC.toTaxon, name="toTaxon", curie=DWC.curie('toTaxon'),
                      model_uri=DWC.toTaxon, domain=None, range=Optional[str])

slots.inCollection = Slot(uri=DWC.inCollection, name="inCollection", curie=DWC.curie('inCollection'),
                      model_uri=DWC.inCollection, domain=None, range=Optional[str])

slots.earliestGeochronologicalEra = Slot(uri=DWC.earliestGeochronologicalEra, name="earliestGeochronologicalEra", curie=DWC.curie('earliestGeochronologicalEra'),
                      model_uri=DWC.earliestGeochronologicalEra, domain=None, range=Optional[str])

slots.fromLithostratigraphicUnit = Slot(uri=DWC.fromLithostratigraphicUnit, name="fromLithostratigraphicUnit", curie=DWC.curie('fromLithostratigraphicUnit'),
                      model_uri=DWC.fromLithostratigraphicUnit, domain=None, range=Optional[str])

slots.inDataset = Slot(uri=DWC.inDataset, name="inDataset", curie=DWC.curie('inDataset'),
                      model_uri=DWC.inDataset, domain=None, range=Optional[str])

slots.latestGeochronologicalEra = Slot(uri=DWC.latestGeochronologicalEra, name="latestGeochronologicalEra", curie=DWC.curie('latestGeochronologicalEra'),
                      model_uri=DWC.latestGeochronologicalEra, domain=None, range=Optional[str])

slots.Accepted_Name_Usage = Slot(uri=DWC.Accepted_Name_Usage, name="Accepted Name Usage", curie=DWC.curie('Accepted_Name_Usage'),
                      model_uri=DWC.Accepted_Name_Usage, domain=None, range=Optional[str], mappings = [DWC["version/acceptedScientificName-2009-07-06"]])

slots.Accepted_Name_Usage_ID = Slot(uri=DWC.Accepted_Name_Usage_ID, name="Accepted Name Usage ID", curie=DWC.curie('Accepted_Name_Usage_ID'),
                      model_uri=DWC.Accepted_Name_Usage_ID, domain=None, range=Optional[str], mappings = [DWC["version/acceptedTaxonID-2009-08-24"]])

slots.Accepted_Scientific_Name = Slot(uri=DWC.Accepted_Scientific_Name, name="Accepted Scientific Name", curie=DWC.curie('Accepted_Scientific_Name'),
                      model_uri=DWC.Accepted_Scientific_Name, domain=None, range=Optional[str], mappings = [DWC["version/acceptedTaxonName-2009-04-24"]])

slots.Accepted_Scientific_Name_ID = Slot(uri=DWC.Accepted_Scientific_Name_ID, name="Accepted Scientific Name ID", curie=DWC.curie('Accepted_Scientific_Name_ID'),
                      model_uri=DWC.Accepted_Scientific_Name_ID, domain=None, range=Optional[str], mappings = [DWC["version/acceptedTaxonNameID-2009-04-24"]])

slots.Accepted_Taxon = Slot(uri=DWC.Accepted_Taxon, name="Accepted Taxon", curie=DWC.curie('Accepted_Taxon'),
                      model_uri=DWC.Accepted_Taxon, domain=None, range=Optional[str])

slots.Accepted_Taxon_ID = Slot(uri=DWC.Accepted_Taxon_ID, name="Accepted Taxon ID", curie=DWC.curie('Accepted_Taxon_ID'),
                      model_uri=DWC.Accepted_Taxon_ID, domain=None, range=Optional[str], mappings = [DWC["version/acceptedScientificNameID-2009-07-06"]])

slots.Accepted_Taxon_Name = Slot(uri=DWC.Accepted_Taxon_Name, name="Accepted Taxon Name", curie=DWC.curie('Accepted_Taxon_Name'),
                      model_uri=DWC.Accepted_Taxon_Name, domain=None, range=Optional[str], mappings = [DWC["version/AcceptedTaxon-2008-11-19"]])

slots.Accepted_Taxon_Name_ID = Slot(uri=DWC.Accepted_Taxon_Name_ID, name="Accepted Taxon Name ID", curie=DWC.curie('Accepted_Taxon_Name_ID'),
                      model_uri=DWC.Accepted_Taxon_Name_ID, domain=None, range=Optional[str], mappings = [DWC["version/AcceptedTaxonID-2009-01-21"]])

slots.Access_Constraints = Slot(uri=DWC.Access_Constraints, name="Access Constraints", curie=DWC.curie('Access_Constraints'),
                      model_uri=DWC.Access_Constraints, domain=None, range=Optional[str])

slots.Accuracy = Slot(uri=DWC.Accuracy, name="Accuracy", curie=DWC.curie('Accuracy'),
                      model_uri=DWC.Accuracy, domain=None, range=Optional[str])

slots.Associated_Media = Slot(uri=DWC.Associated_Media, name="Associated Media", curie=DWC.curie('Associated_Media'),
                      model_uri=DWC.Associated_Media, domain=None, range=Optional[str], mappings = [DWC["version/associatedMedia-2009-04-24"]])

slots.Associated_Occurrences = Slot(uri=DWC.Associated_Occurrences, name="Associated Occurrences", curie=DWC.curie('Associated_Occurrences'),
                      model_uri=DWC.Associated_Occurrences, domain=None, range=Optional[str], mappings = [DWC["version/associatedOccurrences-2009-04-24"]])

slots.Associated_Organisms = Slot(uri=DWC.Associated_Organisms, name="Associated Organisms", curie=DWC.curie('Associated_Organisms'),
                      model_uri=DWC.Associated_Organisms, domain=None, range=Optional[str])

slots.Associated_References = Slot(uri=DWC.Associated_References, name="Associated References", curie=DWC.curie('Associated_References'),
                      model_uri=DWC.Associated_References, domain=None, range=Optional[str], mappings = [DWC["version/associatedReferences-2009-04-24"]])

slots.Associated_Sequences = Slot(uri=DWC.Associated_Sequences, name="Associated Sequences", curie=DWC.curie('Associated_Sequences'),
                      model_uri=DWC.Associated_Sequences, domain=None, range=Optional[str], mappings = [DWC["version/associatedSequences-2009-04-24"]])

slots.Associated_Taxa = Slot(uri=DWC.Associated_Taxa, name="Associated Taxa", curie=DWC.curie('Associated_Taxa'),
                      model_uri=DWC.Associated_Taxa, domain=None, range=Optional[str], mappings = [DWC["version/associatedTaxa-2009-04-24"]])

slots.Basionym = Slot(uri=DWC.Basionym, name="Basionym", curie=DWC.curie('Basionym'),
                      model_uri=DWC.Basionym, domain=None, range=Optional[str])

slots.Basionym_ID = Slot(uri=DWC.Basionym_ID, name="Basionym ID", curie=DWC.curie('Basionym_ID'),
                      model_uri=DWC.Basionym_ID, domain=None, range=Optional[str])

slots.Basis_of_Record = Slot(uri=DWC.Basis_of_Record, name="Basis of Record", curie=DWC.curie('Basis_of_Record'),
                      model_uri=DWC.Basis_of_Record, domain=None, range=Optional[str], mappings = [DWC["version/basisOfRecord-2009-12-07"]])

slots.Bed = Slot(uri=DWC.Bed, name="Bed", curie=DWC.curie('Bed'),
                      model_uri=DWC.Bed, domain=None, range=Optional[str])

slots.Behavior = Slot(uri=DWC.Behavior, name="Behavior", curie=DWC.curie('Behavior'),
                      model_uri=DWC.Behavior, domain=None, range=Optional[str])

slots.Binomial = Slot(uri=DWC.Binomial, name="Binomial", curie=DWC.curie('Binomial'),
                      model_uri=DWC.Binomial, domain=None, range=Optional[str])

slots.Catalog_Number = Slot(uri=DWC.Catalog_Number, name="Catalog Number", curie=DWC.curie('Catalog_Number'),
                      model_uri=DWC.Catalog_Number, domain=None, range=Optional[str])

slots.Catalog_Number_Numeric = Slot(uri=DWC.Catalog_Number_Numeric, name="Catalog Number Numeric", curie=DWC.curie('Catalog_Number_Numeric'),
                      model_uri=DWC.Catalog_Number_Numeric, domain=None, range=Optional[str])

slots.Class = Slot(uri=DWC.Class, name="Class", curie=DWC.curie('Class'),
                      model_uri=DWC.Class, domain=None, range=Optional[str])

slots.Collection_Code = Slot(uri=DWC.Collection_Code, name="Collection Code", curie=DWC.curie('Collection_Code'),
                      model_uri=DWC.Collection_Code, domain=None, range=Optional[str], mappings = [DWC["version/collectionCode-2009-08-24"]])

slots.Collection_ID = Slot(uri=DWC.Collection_ID, name="Collection ID", curie=DWC.curie('Collection_ID'),
                      model_uri=DWC.Collection_ID, domain=None, range=Optional[str], mappings = [DWC["version/collectionID-2009-04-24"]])

slots.Continent = Slot(uri=DWC.Continent, name="Continent", curie=DWC.curie('Continent'),
                      model_uri=DWC.Continent, domain=None, range=Optional[str])

slots.Coordinate_Precision = Slot(uri=DWC.Coordinate_Precision, name="Coordinate Precision", curie=DWC.curie('Coordinate_Precision'),
                      model_uri=DWC.Coordinate_Precision, domain=None, range=Optional[str])

slots.Coordinate_Uncertainty_In_Meters = Slot(uri=DWC.Coordinate_Uncertainty_In_Meters, name="Coordinate Uncertainty In Meters", curie=DWC.curie('Coordinate_Uncertainty_In_Meters'),
                      model_uri=DWC.Coordinate_Uncertainty_In_Meters, domain=None, range=Optional[str])

slots.Country = Slot(uri=DWC.Country, name="Country", curie=DWC.curie('Country'),
                      model_uri=DWC.Country, domain=None, range=Optional[str])

slots.Country_Code = Slot(uri=DWC.Country_Code, name="Country Code", curie=DWC.curie('Country_Code'),
                      model_uri=DWC.Country_Code, domain=None, range=Optional[str])

slots.County = Slot(uri=DWC.County, name="County", curie=DWC.curie('County'),
                      model_uri=DWC.County, domain=None, range=Optional[str])

slots.Data_Generalizations = Slot(uri=DWC.Data_Generalizations, name="Data Generalizations", curie=DWC.curie('Data_Generalizations'),
                      model_uri=DWC.Data_Generalizations, domain=None, range=Optional[str], mappings = [DWC["version/Generalizations-2008-11-19"]])

slots.Dataset_ID = Slot(uri=DWC.Dataset_ID, name="Dataset ID", curie=DWC.curie('Dataset_ID'),
                      model_uri=DWC.Dataset_ID, domain=None, range=Optional[str], mappings = [DWC["version/datasetID-2009-04-24"]])

slots.Dataset_Name = Slot(uri=DWC.Dataset_Name, name="Dataset Name", curie=DWC.curie('Dataset_Name'),
                      model_uri=DWC.Dataset_Name, domain=None, range=Optional[str])

slots.Date_Identified = Slot(uri=DWC.Date_Identified, name="Date Identified", curie=DWC.curie('Date_Identified'),
                      model_uri=DWC.Date_Identified, domain=None, range=Optional[str], mappings = [DWC["version/dateIdentified-2009-04-24"]])

slots.Day = Slot(uri=DWC.Day, name="Day", curie=DWC.curie('Day'),
                      model_uri=DWC.Day, domain=None, range=Optional[str])

slots.Decimal_Latitude = Slot(uri=DWC.Decimal_Latitude, name="Decimal Latitude", curie=DWC.curie('Decimal_Latitude'),
                      model_uri=DWC.Decimal_Latitude, domain=None, range=Optional[str])

slots.Decimal_Longitude = Slot(uri=DWC.Decimal_Longitude, name="Decimal Longitude", curie=DWC.curie('Decimal_Longitude'),
                      model_uri=DWC.Decimal_Longitude, domain=None, range=Optional[str])

slots.Disposition = Slot(uri=DWC.Disposition, name="Disposition", curie=DWC.curie('Disposition'),
                      model_uri=DWC.Disposition, domain=None, range=Optional[str])

slots.Dynamic_Properties = Slot(uri=DWC.Dynamic_Properties, name="Dynamic Properties", curie=DWC.curie('Dynamic_Properties'),
                      model_uri=DWC.Dynamic_Properties, domain=None, range=Optional[str], mappings = [DWC["version/dynamicProperties-2009-04-24"]])

slots.Earliest_Age_Or_Lowest_Stage = Slot(uri=DWC.Earliest_Age_Or_Lowest_Stage, name="Earliest Age Or Lowest Stage", curie=DWC.curie('Earliest_Age_Or_Lowest_Stage'),
                      model_uri=DWC.Earliest_Age_Or_Lowest_Stage, domain=None, range=Optional[str])

slots.Earliest_Date_Collected = Slot(uri=DWC.Earliest_Date_Collected, name="Earliest Date Collected", curie=DWC.curie('Earliest_Date_Collected'),
                      model_uri=DWC.Earliest_Date_Collected, domain=None, range=Optional[str])

slots.Earliest_Eon_Or_Lowest_Eonothem = Slot(uri=DWC.Earliest_Eon_Or_Lowest_Eonothem, name="Earliest Eon Or Lowest Eonothem", curie=DWC.curie('Earliest_Eon_Or_Lowest_Eonothem'),
                      model_uri=DWC.Earliest_Eon_Or_Lowest_Eonothem, domain=None, range=Optional[str])

slots.Earliest_Epoch_Or_Lowest_Series = Slot(uri=DWC.Earliest_Epoch_Or_Lowest_Series, name="Earliest Epoch Or Lowest Series", curie=DWC.curie('Earliest_Epoch_Or_Lowest_Series'),
                      model_uri=DWC.Earliest_Epoch_Or_Lowest_Series, domain=None, range=Optional[str])

slots.Earliest_Era_Or_Lowest_Erathem = Slot(uri=DWC.Earliest_Era_Or_Lowest_Erathem, name="Earliest Era Or Lowest Erathem", curie=DWC.curie('Earliest_Era_Or_Lowest_Erathem'),
                      model_uri=DWC.Earliest_Era_Or_Lowest_Erathem, domain=None, range=Optional[str])

slots.Earliest_Period_Or_Lowest_System = Slot(uri=DWC.Earliest_Period_Or_Lowest_System, name="Earliest Period Or Lowest System", curie=DWC.curie('Earliest_Period_Or_Lowest_System'),
                      model_uri=DWC.Earliest_Period_Or_Lowest_System, domain=None, range=Optional[str])

slots.End_Day_Of_Year = Slot(uri=DWC.End_Day_Of_Year, name="End Day Of Year", curie=DWC.curie('End_Day_Of_Year'),
                      model_uri=DWC.End_Day_Of_Year, domain=None, range=Optional[str])

slots.End_Time_of_Day = Slot(uri=DWC.End_Time_of_Day, name="End Time of Day", curie=DWC.curie('End_Time_of_Day'),
                      model_uri=DWC.End_Time_of_Day, domain=None, range=Optional[str])

slots.Establishment_Means = Slot(uri=DWC.Establishment_Means, name="Establishment Means", curie=DWC.curie('Establishment_Means'),
                      model_uri=DWC.Establishment_Means, domain=None, range=Optional[str])

slots.Event_Attribute_Accuracy = Slot(uri=DWC.Event_Attribute_Accuracy, name="Event Attribute Accuracy", curie=DWC.curie('Event_Attribute_Accuracy'),
                      model_uri=DWC.Event_Attribute_Accuracy, domain=None, range=Optional[str])

slots.Event_Attribute_Determined_By = Slot(uri=DWC.Event_Attribute_Determined_By, name="Event Attribute Determined By", curie=DWC.curie('Event_Attribute_Determined_By'),
                      model_uri=DWC.Event_Attribute_Determined_By, domain=None, range=Optional[str])

slots.Event_Attribute_Determined_Date = Slot(uri=DWC.Event_Attribute_Determined_Date, name="Event Attribute Determined Date", curie=DWC.curie('Event_Attribute_Determined_Date'),
                      model_uri=DWC.Event_Attribute_Determined_Date, domain=None, range=Optional[str])

slots.Event_Attribute_ID = Slot(uri=DWC.Event_Attribute_ID, name="Event Attribute ID", curie=DWC.curie('Event_Attribute_ID'),
                      model_uri=DWC.Event_Attribute_ID, domain=None, range=Optional[str])

slots.Event_Attribute_Remarks = Slot(uri=DWC.Event_Attribute_Remarks, name="Event Attribute Remarks", curie=DWC.curie('Event_Attribute_Remarks'),
                      model_uri=DWC.Event_Attribute_Remarks, domain=None, range=Optional[str])

slots.Event_Attributes = Slot(uri=DWC.Event_Attributes, name="Event Attributes", curie=DWC.curie('Event_Attributes'),
                      model_uri=DWC.Event_Attributes, domain=None, range=Optional[str])

slots.Event_Attribute_Type = Slot(uri=DWC.Event_Attribute_Type, name="Event Attribute Type", curie=DWC.curie('Event_Attribute_Type'),
                      model_uri=DWC.Event_Attribute_Type, domain=None, range=Optional[str])

slots.Event_Attribute_Unit = Slot(uri=DWC.Event_Attribute_Unit, name="Event Attribute Unit", curie=DWC.curie('Event_Attribute_Unit'),
                      model_uri=DWC.Event_Attribute_Unit, domain=None, range=Optional[str])

slots.Event_Attribute = Slot(uri=DWC.Event_Attribute, name="Event Attribute", curie=DWC.curie('Event_Attribute'),
                      model_uri=DWC.Event_Attribute, domain=None, range=Optional[str])

slots.Event_Date = Slot(uri=DWC.Event_Date, name="Event Date", curie=DWC.curie('Event_Date'),
                      model_uri=DWC.Event_Date, domain=None, range=Optional[str], mappings = [DWC["version/EarliestDateCollected-2008-11-19"], DWC["version/LatestDateCollected-2008-11-19"]])

slots.Event_ID = Slot(uri=DWC.Event_ID, name="Event ID", curie=DWC.curie('Event_ID'),
                      model_uri=DWC.Event_ID, domain=None, range=Optional[str], mappings = [DWC["version/SamplingEventID-2008-11-19"]])

slots.Event_Measurement_Accuracy = Slot(uri=DWC.Event_Measurement_Accuracy, name="Event Measurement Accuracy", curie=DWC.curie('Event_Measurement_Accuracy'),
                      model_uri=DWC.Event_Measurement_Accuracy, domain=None, range=Optional[str], mappings = [DWC["version/EventAttributeAccuracy-2009-01-18"]])

slots.Event_Measurement_Determined_By = Slot(uri=DWC.Event_Measurement_Determined_By, name="Event Measurement Determined By", curie=DWC.curie('Event_Measurement_Determined_By'),
                      model_uri=DWC.Event_Measurement_Determined_By, domain=None, range=Optional[str], mappings = [DWC["version/EventAttributeDeterminedBy-2009-01-23"]])

slots.Event_Measurement_Determined_Date = Slot(uri=DWC.Event_Measurement_Determined_Date, name="Event Measurement Determined Date", curie=DWC.curie('Event_Measurement_Determined_Date'),
                      model_uri=DWC.Event_Measurement_Determined_Date, domain=None, range=Optional[str], mappings = [DWC["version/EventAttributeDeterminedDate-2009-01-23"]])

slots.Event_Measurement_ID = Slot(uri=DWC.Event_Measurement_ID, name="Event Measurement ID", curie=DWC.curie('Event_Measurement_ID'),
                      model_uri=DWC.Event_Measurement_ID, domain=None, range=Optional[str], mappings = [DWC["version/EventAttributeID-2008-11-19"]])

slots.Event_Measurement_Remarks = Slot(uri=DWC.Event_Measurement_Remarks, name="Event Measurement Remarks", curie=DWC.curie('Event_Measurement_Remarks'),
                      model_uri=DWC.Event_Measurement_Remarks, domain=None, range=Optional[str])

slots.Event_Measurement_Type = Slot(uri=DWC.Event_Measurement_Type, name="Event Measurement Type", curie=DWC.curie('Event_Measurement_Type'),
                      model_uri=DWC.Event_Measurement_Type, domain=None, range=Optional[str], mappings = [DWC["version/EventAttributeType-2008-11-19"]])

slots.Event_Measurement_Unit = Slot(uri=DWC.Event_Measurement_Unit, name="Event Measurement Unit", curie=DWC.curie('Event_Measurement_Unit'),
                      model_uri=DWC.Event_Measurement_Unit, domain=None, range=Optional[str], mappings = [DWC["version/EventAttributeUnit-2008-11-19"]])

slots.Event_Measurement_Value = Slot(uri=DWC.Event_Measurement_Value, name="Event Measurement Value", curie=DWC.curie('Event_Measurement_Value'),
                      model_uri=DWC.Event_Measurement_Value, domain=None, range=Optional[str], mappings = [DWC["version/EventAttributeValue-2008-11-19"]])

slots.Event_Remarks = Slot(uri=DWC.Event_Remarks, name="Event Remarks", curie=DWC.curie('Event_Remarks'),
                      model_uri=DWC.Event_Remarks, domain=None, range=Optional[str])

slots.Event_Time = Slot(uri=DWC.Event_Time, name="Event Time", curie=DWC.curie('Event_Time'),
                      model_uri=DWC.Event_Time, domain=None, range=Optional[str], mappings = [DWC["version/StartTimeOfDay-2008-11-19"], DWC["version/EndTimeOfDay-2008-11-19"]])

slots.Family = Slot(uri=DWC.Family, name="Family", curie=DWC.curie('Family'),
                      model_uri=DWC.Family, domain=None, range=Optional[str])

slots.Field_Notes = Slot(uri=DWC.Field_Notes, name="Field Notes", curie=DWC.curie('Field_Notes'),
                      model_uri=DWC.Field_Notes, domain=None, range=Optional[str])

slots.Field_Number = Slot(uri=DWC.Field_Number, name="Field Number", curie=DWC.curie('Field_Number'),
                      model_uri=DWC.Field_Number, domain=None, range=Optional[str])

slots.Footprint_Spatial_Fit = Slot(uri=DWC.Footprint_Spatial_Fit, name="Footprint Spatial Fit", curie=DWC.curie('Footprint_Spatial_Fit'),
                      model_uri=DWC.Footprint_Spatial_Fit, domain=None, range=Optional[str])

slots.Footprint_SRS = Slot(uri=DWC.Footprint_SRS, name="Footprint SRS", curie=DWC.curie('Footprint_SRS'),
                      model_uri=DWC.Footprint_SRS, domain=None, range=Optional[str])

slots.Footprint_WKT = Slot(uri=DWC.Footprint_WKT, name="Footprint WKT", curie=DWC.curie('Footprint_WKT'),
                      model_uri=DWC.Footprint_WKT, domain=None, range=Optional[str])

slots.Formation = Slot(uri=DWC.Formation, name="Formation", curie=DWC.curie('Formation'),
                      model_uri=DWC.Formation, domain=None, range=Optional[str])

slots.Generalizations = Slot(uri=DWC.Generalizations, name="Generalizations", curie=DWC.curie('Generalizations'),
                      model_uri=DWC.Generalizations, domain=None, range=Optional[str])

slots.Genus = Slot(uri=DWC.Genus, name="Genus", curie=DWC.curie('Genus'),
                      model_uri=DWC.Genus, domain=None, range=Optional[str])

slots.Geodetic_Datum = Slot(uri=DWC.Geodetic_Datum, name="Geodetic Datum", curie=DWC.curie('Geodetic_Datum'),
                      model_uri=DWC.Geodetic_Datum, domain=None, range=Optional[str])

slots.Geological_Context_ID = Slot(uri=DWC.Geological_Context_ID, name="Geological Context ID", curie=DWC.curie('Geological_Context_ID'),
                      model_uri=DWC.Geological_Context_ID, domain=None, range=Optional[str])

slots.Georeferenced_By = Slot(uri=DWC.Georeferenced_By, name="Georeferenced By", curie=DWC.curie('Georeferenced_By'),
                      model_uri=DWC.Georeferenced_By, domain=None, range=Optional[str], mappings = [DWC["version/georeferencedBy-2009-04-24"]])

slots.Georeferenced_Date = Slot(uri=DWC.Georeferenced_Date, name="Georeferenced Date", curie=DWC.curie('Georeferenced_Date'),
                      model_uri=DWC.Georeferenced_Date, domain=None, range=Optional[str])

slots.Georeference_Protocol = Slot(uri=DWC.Georeference_Protocol, name="Georeference Protocol", curie=DWC.curie('Georeference_Protocol'),
                      model_uri=DWC.Georeference_Protocol, domain=None, range=Optional[str])

slots.Georeference_Remarks = Slot(uri=DWC.Georeference_Remarks, name="Georeference Remarks", curie=DWC.curie('Georeference_Remarks'),
                      model_uri=DWC.Georeference_Remarks, domain=None, range=Optional[str])

slots.Georeference_Sources = Slot(uri=DWC.Georeference_Sources, name="Georeference Sources", curie=DWC.curie('Georeference_Sources'),
                      model_uri=DWC.Georeference_Sources, domain=None, range=Optional[str], mappings = [DWC["version/georeferenceSources-2009-04-24"]])

slots.Georeference_Verification_Status = Slot(uri=DWC.Georeference_Verification_Status, name="Georeference Verification Status", curie=DWC.curie('Georeference_Verification_Status'),
                      model_uri=DWC.Georeference_Verification_Status, domain=None, range=Optional[str])

slots.Group = Slot(uri=DWC.Group, name="Group", curie=DWC.curie('Group'),
                      model_uri=DWC.Group, domain=None, range=Optional[str])

slots.Habitat = Slot(uri=DWC.Habitat, name="Habitat", curie=DWC.curie('Habitat'),
                      model_uri=DWC.Habitat, domain=None, range=Optional[str])

slots.Higher_Classification = Slot(uri=DWC.Higher_Classification, name="Higher Classification", curie=DWC.curie('Higher_Classification'),
                      model_uri=DWC.Higher_Classification, domain=None, range=Optional[str], mappings = [DWC["version/higherClassification-2009-08-24"]])

slots.Higher_Geography = Slot(uri=DWC.Higher_Geography, name="Higher Geography", curie=DWC.curie('Higher_Geography'),
                      model_uri=DWC.Higher_Geography, domain=None, range=Optional[str], mappings = [DWC["version/higherGeography-2009-04-24"]])

slots.Higher_Geography_ID = Slot(uri=DWC.Higher_Geography_ID, name="Higher Geography ID", curie=DWC.curie('Higher_Geography_ID'),
                      model_uri=DWC.Higher_Geography_ID, domain=None, range=Optional[str])

slots.Higher_Taxon = Slot(uri=DWC.Higher_Taxon, name="Higher Taxon", curie=DWC.curie('Higher_Taxon'),
                      model_uri=DWC.Higher_Taxon, domain=None, range=Optional[str])

slots.Higher_Taxon_Concept_ID = Slot(uri=DWC.Higher_Taxon_Concept_ID, name="Higher Taxon Concept ID", curie=DWC.curie('Higher_Taxon_Concept_ID'),
                      model_uri=DWC.Higher_Taxon_Concept_ID, domain=None, range=Optional[str])

slots.Higher_Taxon_ID = Slot(uri=DWC.Higher_Taxon_ID, name="Higher Taxon ID", curie=DWC.curie('Higher_Taxon_ID'),
                      model_uri=DWC.Higher_Taxon_ID, domain=None, range=Optional[str])

slots.Higher_Taxon_Name = Slot(uri=DWC.Higher_Taxon_Name, name="Higher Taxon Name", curie=DWC.curie('Higher_Taxon_Name'),
                      model_uri=DWC.Higher_Taxon_Name, domain=None, range=Optional[str])

slots.Higher_Taxon_Name_ID = Slot(uri=DWC.Higher_Taxon_Name_ID, name="Higher Taxon Name ID", curie=DWC.curie('Higher_Taxon_Name_ID'),
                      model_uri=DWC.Higher_Taxon_Name_ID, domain=None, range=Optional[str], mappings = [DWC["version/HigherTaxonID-2009-01-21"]])

slots.Highest_Biostratigraphic_Zone = Slot(uri=DWC.Highest_Biostratigraphic_Zone, name="Highest Biostratigraphic Zone", curie=DWC.curie('Highest_Biostratigraphic_Zone'),
                      model_uri=DWC.Highest_Biostratigraphic_Zone, domain=None, range=Optional[str])

slots.Identification_Attributes = Slot(uri=DWC.Identification_Attributes, name="Identification Attributes", curie=DWC.curie('Identification_Attributes'),
                      model_uri=DWC.Identification_Attributes, domain=None, range=Optional[str])

slots.Identification_ID = Slot(uri=DWC.Identification_ID, name="Identification ID", curie=DWC.curie('Identification_ID'),
                      model_uri=DWC.Identification_ID, domain=None, range=Optional[str])

slots.Identification_Qualifier = Slot(uri=DWC.Identification_Qualifier, name="Identification Qualifier", curie=DWC.curie('Identification_Qualifier'),
                      model_uri=DWC.Identification_Qualifier, domain=None, range=Optional[str])

slots.Identification_References = Slot(uri=DWC.Identification_References, name="Identification References", curie=DWC.curie('Identification_References'),
                      model_uri=DWC.Identification_References, domain=None, range=Optional[str], mappings = [DWC["version/identificationReferences-2009-04-24"]])

slots.Identification_Remarks = Slot(uri=DWC.Identification_Remarks, name="Identification Remarks", curie=DWC.curie('Identification_Remarks'),
                      model_uri=DWC.Identification_Remarks, domain=None, range=Optional[str])

slots.Identification_Verification_Status = Slot(uri=DWC.Identification_Verification_Status, name="Identification Verification Status", curie=DWC.curie('Identification_Verification_Status'),
                      model_uri=DWC.Identification_Verification_Status, domain=None, range=Optional[str])

slots.Identified_By = Slot(uri=DWC.Identified_By, name="Identified By", curie=DWC.curie('Identified_By'),
                      model_uri=DWC.Identified_By, domain=None, range=Optional[str], mappings = [DWC["version/identifiedBy-2009-08-24"]])

slots.Individual_Count = Slot(uri=DWC.Individual_Count, name="Individual Count", curie=DWC.curie('Individual_Count'),
                      model_uri=DWC.Individual_Count, domain=None, range=Optional[str])

slots.Individual_ID = Slot(uri=DWC.Individual_ID, name="Individual ID", curie=DWC.curie('Individual_ID'),
                      model_uri=DWC.Individual_ID, domain=None, range=Optional[str])

slots.Information_Withheld = Slot(uri=DWC.Information_Withheld, name="Information Withheld", curie=DWC.curie('Information_Withheld'),
                      model_uri=DWC.Information_Withheld, domain=None, range=Optional[str])

slots.Infraspecific_Epithet = Slot(uri=DWC.Infraspecific_Epithet, name="Infraspecific Epithet", curie=DWC.curie('Infraspecific_Epithet'),
                      model_uri=DWC.Infraspecific_Epithet, domain=None, range=Optional[str], mappings = [DWC["version/infraspecificEpithet-2009-04-24"]])

slots.Institution_Code = Slot(uri=DWC.Institution_Code, name="Institution Code", curie=DWC.curie('Institution_Code'),
                      model_uri=DWC.Institution_Code, domain=None, range=Optional[str], mappings = [DWC["version/institutionCode-2009-08-24"]])

slots.Institution_ID = Slot(uri=DWC.Institution_ID, name="Institution ID", curie=DWC.curie('Institution_ID'),
                      model_uri=DWC.Institution_ID, domain=None, range=Optional[str])

slots.Island = Slot(uri=DWC.Island, name="Island", curie=DWC.curie('Island'),
                      model_uri=DWC.Island, domain=None, range=Optional[str])

slots.Island_Group = Slot(uri=DWC.Island_Group, name="Island Group", curie=DWC.curie('Island_Group'),
                      model_uri=DWC.Island_Group, domain=None, range=Optional[str])

slots.Kingdom = Slot(uri=DWC.Kingdom, name="Kingdom", curie=DWC.curie('Kingdom'),
                      model_uri=DWC.Kingdom, domain=None, range=Optional[str])

slots.Latest_AgeOr_Highest_Stage = Slot(uri=DWC.Latest_AgeOr_Highest_Stage, name="Latest AgeOr Highest Stage", curie=DWC.curie('Latest_AgeOr_Highest_Stage'),
                      model_uri=DWC.Latest_AgeOr_Highest_Stage, domain=None, range=Optional[str])

slots.Latest_Date_Collected = Slot(uri=DWC.Latest_Date_Collected, name="Latest Date Collected", curie=DWC.curie('Latest_Date_Collected'),
                      model_uri=DWC.Latest_Date_Collected, domain=None, range=Optional[str])

slots.Latest_Eon_Or_Highest_Eonothem = Slot(uri=DWC.Latest_Eon_Or_Highest_Eonothem, name="Latest Eon Or Highest Eonothem", curie=DWC.curie('Latest_Eon_Or_Highest_Eonothem'),
                      model_uri=DWC.Latest_Eon_Or_Highest_Eonothem, domain=None, range=Optional[str], mappings = [DWC["version/LatestEonOrLowestEonothem-2005-07-03"]])

slots.Latest_Epoch_Or_Highest_Series = Slot(uri=DWC.Latest_Epoch_Or_Highest_Series, name="Latest Epoch Or Highest Series", curie=DWC.curie('Latest_Epoch_Or_Highest_Series'),
                      model_uri=DWC.Latest_Epoch_Or_Highest_Series, domain=None, range=Optional[str])

slots.Latest_Era_Or_Highest_Erathem = Slot(uri=DWC.Latest_Era_Or_Highest_Erathem, name="Latest Era Or Highest Erathem", curie=DWC.curie('Latest_Era_Or_Highest_Erathem'),
                      model_uri=DWC.Latest_Era_Or_Highest_Erathem, domain=None, range=Optional[str])

slots.Latest_Period_Or_Highest_System = Slot(uri=DWC.Latest_Period_Or_Highest_System, name="Latest Period Or Highest System", curie=DWC.curie('Latest_Period_Or_Highest_System'),
                      model_uri=DWC.Latest_Period_Or_Highest_System, domain=None, range=Optional[str])

slots.Life_Stage = Slot(uri=DWC.Life_Stage, name="Life Stage", curie=DWC.curie('Life_Stage'),
                      model_uri=DWC.Life_Stage, domain=None, range=Optional[str])

slots.Lithostratigraphic_Terms = Slot(uri=DWC.Lithostratigraphic_Terms, name="Lithostratigraphic Terms", curie=DWC.curie('Lithostratigraphic_Terms'),
                      model_uri=DWC.Lithostratigraphic_Terms, domain=None, range=Optional[str])

slots.Locality = Slot(uri=DWC.Locality, name="Locality", curie=DWC.curie('Locality'),
                      model_uri=DWC.Locality, domain=None, range=Optional[str])

slots.Location_According_To = Slot(uri=DWC.Location_According_To, name="Location According To", curie=DWC.curie('Location_According_To'),
                      model_uri=DWC.Location_According_To, domain=None, range=Optional[str])

slots.Location_Attributes = Slot(uri=DWC.Location_Attributes, name="Location Attributes", curie=DWC.curie('Location_Attributes'),
                      model_uri=DWC.Location_Attributes, domain=None, range=Optional[str])

slots.Location_ID = Slot(uri=DWC.Location_ID, name="Location ID", curie=DWC.curie('Location_ID'),
                      model_uri=DWC.Location_ID, domain=None, range=Optional[str], mappings = [DWC["version/SamplingLocationID-2008-11-19"]])

slots.Location_Remarks = Slot(uri=DWC.Location_Remarks, name="Location Remarks", curie=DWC.curie('Location_Remarks'),
                      model_uri=DWC.Location_Remarks, domain=None, range=Optional[str], mappings = [DWC["version/SamplingLocationRemarks-2009-01-18"]])

slots.Lowest_Biostratigraphic_Zone = Slot(uri=DWC.Lowest_Biostratigraphic_Zone, name="Lowest Biostratigraphic Zone", curie=DWC.curie('Lowest_Biostratigraphic_Zone'),
                      model_uri=DWC.Lowest_Biostratigraphic_Zone, domain=None, range=Optional[str])

slots.Material_Sample_ID = Slot(uri=DWC.Material_Sample_ID, name="Material Sample ID", curie=DWC.curie('Material_Sample_ID'),
                      model_uri=DWC.Material_Sample_ID, domain=None, range=Optional[str])

slots.Maximum_Depth_In_Meters = Slot(uri=DWC.Maximum_Depth_In_Meters, name="Maximum Depth In Meters", curie=DWC.curie('Maximum_Depth_In_Meters'),
                      model_uri=DWC.Maximum_Depth_In_Meters, domain=None, range=Optional[str])

slots.Maximum_Distance_Above_Surface_In_Meters = Slot(uri=DWC.Maximum_Distance_Above_Surface_In_Meters, name="Maximum Distance Above Surface In Meters", curie=DWC.curie('Maximum_Distance_Above_Surface_In_Meters'),
                      model_uri=DWC.Maximum_Distance_Above_Surface_In_Meters, domain=None, range=Optional[str])

slots.Maximum_Elevation_In_Meters = Slot(uri=DWC.Maximum_Elevation_In_Meters, name="Maximum Elevation In Meters", curie=DWC.curie('Maximum_Elevation_In_Meters'),
                      model_uri=DWC.Maximum_Elevation_In_Meters, domain=None, range=Optional[str])

slots.Measurement_Accuracy = Slot(uri=DWC.Measurement_Accuracy, name="Measurement Accuracy", curie=DWC.curie('Measurement_Accuracy'),
                      model_uri=DWC.Measurement_Accuracy, domain=None, range=Optional[str], mappings = [DWC["version/occurrenceMeasurementAccuracy-2009-04-24"], DWC["version/eventMeasurementAccuracy-2009-04-24"]])

slots.Measurement_Determined_By = Slot(uri=DWC.Measurement_Determined_By, name="Measurement Determined By", curie=DWC.curie('Measurement_Determined_By'),
                      model_uri=DWC.Measurement_Determined_By, domain=None, range=Optional[str], mappings = [DWC["version/measurementDeterminedBy-2009-04-24"]])

slots.Measurement_Determined_Date = Slot(uri=DWC.Measurement_Determined_Date, name="Measurement Determined Date", curie=DWC.curie('Measurement_Determined_Date'),
                      model_uri=DWC.Measurement_Determined_Date, domain=None, range=Optional[str], mappings = [DWC["version/occurrenceMeasurementDeterminedDate-2009-04-24"], DWC["version/eventMeasurementDeterminedDate-2009-04-24"]])

slots.Measurement_ID = Slot(uri=DWC.Measurement_ID, name="Measurement ID", curie=DWC.curie('Measurement_ID'),
                      model_uri=DWC.Measurement_ID, domain=None, range=Optional[str], mappings = [DWC["version/occurrenceMeasurementID-2009-04-24"], DWC["version/eventMeasurementID-2009-04-24"]])

slots.Measurement_Method = Slot(uri=DWC.Measurement_Method, name="Measurement Method", curie=DWC.curie('Measurement_Method'),
                      model_uri=DWC.Measurement_Method, domain=None, range=Optional[str])

slots.Measurement_Remarks = Slot(uri=DWC.Measurement_Remarks, name="Measurement Remarks", curie=DWC.curie('Measurement_Remarks'),
                      model_uri=DWC.Measurement_Remarks, domain=None, range=Optional[str], mappings = [DWC["version/occurrenceMeasurementRemarks-2009-04-24"], DWC["version/eventMeasurementRemarks-2009-04-24"]])

slots.Measurement_Type = Slot(uri=DWC.Measurement_Type, name="Measurement Type", curie=DWC.curie('Measurement_Type'),
                      model_uri=DWC.Measurement_Type, domain=None, range=Optional[str], mappings = [DWC["version/occurrenceMeasurementType-2009-04-24"], DWC["version/eventMeasurementType-2009-04-24"]])

slots.Measurement_Unit = Slot(uri=DWC.Measurement_Unit, name="Measurement Unit", curie=DWC.curie('Measurement_Unit'),
                      model_uri=DWC.Measurement_Unit, domain=None, range=Optional[str], mappings = [DWC["version/occurrenceMeasurementUnit-2009-04-24"], DWC["version/eventMeasurementUnit-2009-04-24"]])

slots.Measurement_Value = Slot(uri=DWC.Measurement_Value, name="Measurement Value", curie=DWC.curie('Measurement_Value'),
                      model_uri=DWC.Measurement_Value, domain=None, range=Optional[str], mappings = [DWC["version/occurrenceMeasurementValue-2009-04-24"], DWC["version/eventMeasurementValue-2009-04-24"]])

slots.Member = Slot(uri=DWC.Member, name="Member", curie=DWC.curie('Member'),
                      model_uri=DWC.Member, domain=None, range=Optional[str])

slots.Minimum_Depth_In_Meters = Slot(uri=DWC.Minimum_Depth_In_Meters, name="Minimum Depth In Meters", curie=DWC.curie('Minimum_Depth_In_Meters'),
                      model_uri=DWC.Minimum_Depth_In_Meters, domain=None, range=Optional[str])

slots.Minimum_Distance_Above_Surface_In_Meters = Slot(uri=DWC.Minimum_Distance_Above_Surface_In_Meters, name="Minimum Distance Above Surface In Meters", curie=DWC.curie('Minimum_Distance_Above_Surface_In_Meters'),
                      model_uri=DWC.Minimum_Distance_Above_Surface_In_Meters, domain=None, range=Optional[str])

slots.Minimum_Elevation_In_Meters = Slot(uri=DWC.Minimum_Elevation_In_Meters, name="Minimum Elevation In Meters", curie=DWC.curie('Minimum_Elevation_In_Meters'),
                      model_uri=DWC.Minimum_Elevation_In_Meters, domain=None, range=Optional[str])

slots.Month = Slot(uri=DWC.Month, name="Month", curie=DWC.curie('Month'),
                      model_uri=DWC.Month, domain=None, range=Optional[str])

slots.Municipality = Slot(uri=DWC.Municipality, name="Municipality", curie=DWC.curie('Municipality'),
                      model_uri=DWC.Municipality, domain=None, range=Optional[str])

slots.Name_According_To = Slot(uri=DWC.Name_According_To, name="Name According To", curie=DWC.curie('Name_According_To'),
                      model_uri=DWC.Name_According_To, domain=None, range=Optional[str], mappings = [DWC["version/taxonAccordingTo-2009-04-24"]])

slots.Name_According_To_ID = Slot(uri=DWC.Name_According_To_ID, name="Name According To ID", curie=DWC.curie('Name_According_To_ID'),
                      model_uri=DWC.Name_According_To_ID, domain=None, range=Optional[str])

slots.Name_Publication_ID = Slot(uri=DWC.Name_Publication_ID, name="Name Publication ID", curie=DWC.curie('Name_Publication_ID'),
                      model_uri=DWC.Name_Publication_ID, domain=None, range=Optional[str])

slots.Name_Published_In = Slot(uri=DWC.Name_Published_In, name="Name Published In", curie=DWC.curie('Name_Published_In'),
                      model_uri=DWC.Name_Published_In, domain=None, range=Optional[str], mappings = [DWC["version/namePublishedIn-2009-04-24"]])

slots.Name_Published_In_ID = Slot(uri=DWC.Name_Published_In_ID, name="Name Published In ID", curie=DWC.curie('Name_Published_In_ID'),
                      model_uri=DWC.Name_Published_In_ID, domain=None, range=Optional[str], mappings = [DWC["version/namePublicationID-2009-05-18"]])

slots.Name_Published_In_Year = Slot(uri=DWC.Name_Published_In_Year, name="Name Published In Year", curie=DWC.curie('Name_Published_In_Year'),
                      model_uri=DWC.Name_Published_In_Year, domain=None, range=Optional[str])

slots.Nomenclatural_Code = Slot(uri=DWC.Nomenclatural_Code, name="Nomenclatural Code", curie=DWC.curie('Nomenclatural_Code'),
                      model_uri=DWC.Nomenclatural_Code, domain=None, range=Optional[str], mappings = [DWC["version/nomenclaturalCode-2009-04-24"]])

slots.Nomenclatural_Status = Slot(uri=DWC.Nomenclatural_Status, name="Nomenclatural Status", curie=DWC.curie('Nomenclatural_Status'),
                      model_uri=DWC.Nomenclatural_Status, domain=None, range=Optional[str])

slots.Occurrence_Attributes = Slot(uri=DWC.Occurrence_Attributes, name="Occurrence Attributes", curie=DWC.curie('Occurrence_Attributes'),
                      model_uri=DWC.Occurrence_Attributes, domain=None, range=Optional[str])

slots.Occurrence_Details = Slot(uri=DWC.Occurrence_Details, name="Occurrence Details", curie=DWC.curie('Occurrence_Details'),
                      model_uri=DWC.Occurrence_Details, domain=None, range=Optional[str])

slots.Occurrence_ID = Slot(uri=DWC.Occurrence_ID, name="Occurrence ID", curie=DWC.curie('Occurrence_ID'),
                      model_uri=DWC.Occurrence_ID, domain=None, range=Optional[str])

slots.Occurrence_Measurement_Accuracy = Slot(uri=DWC.Occurrence_Measurement_Accuracy, name="Occurrence Measurement Accuracy", curie=DWC.curie('Occurrence_Measurement_Accuracy'),
                      model_uri=DWC.Occurrence_Measurement_Accuracy, domain=None, range=Optional[str], mappings = [DWC["version/SampleAttributeAccuracy-2009-01-18"]])

slots.Occurrence_Measurement_Determined_By = Slot(uri=DWC.Occurrence_Measurement_Determined_By, name="Occurrence Measurement Determined By", curie=DWC.curie('Occurrence_Measurement_Determined_By'),
                      model_uri=DWC.Occurrence_Measurement_Determined_By, domain=None, range=Optional[str], mappings = [DWC["version/SampleAttributeDeterminedBy-2009-01-23"]])

slots.Occurrence_Measurement_Determined_Date = Slot(uri=DWC.Occurrence_Measurement_Determined_Date, name="Occurrence Measurement Determined Date", curie=DWC.curie('Occurrence_Measurement_Determined_Date'),
                      model_uri=DWC.Occurrence_Measurement_Determined_Date, domain=None, range=Optional[str], mappings = [DWC["version/SampleAttributeDeterminedDate-2009-01-23"]])

slots.Occurrence_Measurement_ID = Slot(uri=DWC.Occurrence_Measurement_ID, name="Occurrence Measurement ID", curie=DWC.curie('Occurrence_Measurement_ID'),
                      model_uri=DWC.Occurrence_Measurement_ID, domain=None, range=Optional[str], mappings = [DWC["version/SampleAttributeID-2008-11-19"]])

slots.Occurrence_Measurement_Remarks = Slot(uri=DWC.Occurrence_Measurement_Remarks, name="Occurrence Measurement Remarks", curie=DWC.curie('Occurrence_Measurement_Remarks'),
                      model_uri=DWC.Occurrence_Measurement_Remarks, domain=None, range=Optional[str])

slots.Occurrence_Measurement_Type = Slot(uri=DWC.Occurrence_Measurement_Type, name="Occurrence Measurement Type", curie=DWC.curie('Occurrence_Measurement_Type'),
                      model_uri=DWC.Occurrence_Measurement_Type, domain=None, range=Optional[str], mappings = [DWC["version/SampleAttributeType-2008-11-19"]])

slots.Occurrence_Measurement_Unit = Slot(uri=DWC.Occurrence_Measurement_Unit, name="Occurrence Measurement Unit", curie=DWC.curie('Occurrence_Measurement_Unit'),
                      model_uri=DWC.Occurrence_Measurement_Unit, domain=None, range=Optional[str], mappings = [DWC["version/SampleAttributeUnit-2008-11-19"]])

slots.Occurrence_Measurement_Value = Slot(uri=DWC.Occurrence_Measurement_Value, name="Occurrence Measurement Value", curie=DWC.curie('Occurrence_Measurement_Value'),
                      model_uri=DWC.Occurrence_Measurement_Value, domain=None, range=Optional[str], mappings = [DWC["version/SampleAttributeValue-2008-11-19"]])

slots.Occurrence_Remarks = Slot(uri=DWC.Occurrence_Remarks, name="Occurrence Remarks", curie=DWC.curie('Occurrence_Remarks'),
                      model_uri=DWC.Occurrence_Remarks, domain=None, range=Optional[str], mappings = [DWC["version/SampleRemarks-2009-01-18"]])

slots.Occurrence_Status = Slot(uri=DWC.Occurrence_Status, name="Occurrence Status", curie=DWC.curie('Occurrence_Status'),
                      model_uri=DWC.Occurrence_Status, domain=None, range=Optional[str])

slots.Order = Slot(uri=DWC.Order, name="Order", curie=DWC.curie('Order'),
                      model_uri=DWC.Order, domain=None, range=Optional[str])

slots.Organism_ID = Slot(uri=DWC.Organism_ID, name="Organism ID", curie=DWC.curie('Organism_ID'),
                      model_uri=DWC.Organism_ID, domain=None, range=Optional[str], mappings = [DWC["version/individualID-2009-04-24"]])

slots.Organism_Name = Slot(uri=DWC.Organism_Name, name="Organism Name", curie=DWC.curie('Organism_Name'),
                      model_uri=DWC.Organism_Name, domain=None, range=Optional[str])

slots.Organism_Quantity = Slot(uri=DWC.Organism_Quantity, name="Organism Quantity", curie=DWC.curie('Organism_Quantity'),
                      model_uri=DWC.Organism_Quantity, domain=None, range=Optional[str])

slots.Organism_Quantity_Type = Slot(uri=DWC.Organism_Quantity_Type, name="Organism Quantity Type", curie=DWC.curie('Organism_Quantity_Type'),
                      model_uri=DWC.Organism_Quantity_Type, domain=None, range=Optional[str])

slots.Organism_Remarks = Slot(uri=DWC.Organism_Remarks, name="Organism Remarks", curie=DWC.curie('Organism_Remarks'),
                      model_uri=DWC.Organism_Remarks, domain=None, range=Optional[str])

slots.Organism_Scope = Slot(uri=DWC.Organism_Scope, name="Organism Scope", curie=DWC.curie('Organism_Scope'),
                      model_uri=DWC.Organism_Scope, domain=None, range=Optional[str])

slots.Original_Name_Usage = Slot(uri=DWC.Original_Name_Usage, name="Original Name Usage", curie=DWC.curie('Original_Name_Usage'),
                      model_uri=DWC.Original_Name_Usage, domain=None, range=Optional[str], mappings = [DWC["version/basionym-2009-04-24"]])

slots.Original_Name_Usage_ID = Slot(uri=DWC.Original_Name_Usage_ID, name="Original Name Usage ID", curie=DWC.curie('Original_Name_Usage_ID'),
                      model_uri=DWC.Original_Name_Usage_ID, domain=None, range=Optional[str], mappings = [DWC["version/basionymID-2009-04-24"]])

slots.Other_Catalog_Numbers = Slot(uri=DWC.Other_Catalog_Numbers, name="Other Catalog Numbers", curie=DWC.curie('Other_Catalog_Numbers'),
                      model_uri=DWC.Other_Catalog_Numbers, domain=None, range=Optional[str], mappings = [DWC["version/otherCatalogNumbers-2009-04-24"]])

slots.Owner_Institution_Code = Slot(uri=DWC.Owner_Institution_Code, name="Owner Institution Code", curie=DWC.curie('Owner_Institution_Code'),
                      model_uri=DWC.Owner_Institution_Code, domain=None, range=Optional[str])

slots.Parent_Event_ID = Slot(uri=DWC.Parent_Event_ID, name="Parent Event ID", curie=DWC.curie('Parent_Event_ID'),
                      model_uri=DWC.Parent_Event_ID, domain=None, range=Optional[str])

slots.Parent_Name_Usage = Slot(uri=DWC.Parent_Name_Usage, name="Parent Name Usage", curie=DWC.curie('Parent_Name_Usage'),
                      model_uri=DWC.Parent_Name_Usage, domain=None, range=Optional[str])

slots.Parent_Name_Usage_ID = Slot(uri=DWC.Parent_Name_Usage_ID, name="Parent Name Usage ID", curie=DWC.curie('Parent_Name_Usage_ID'),
                      model_uri=DWC.Parent_Name_Usage_ID, domain=None, range=Optional[str], mappings = [DWC["version/higherTaxonNameID-2009-04-24"]])

slots.Phylum = Slot(uri=DWC.Phylum, name="Phylum", curie=DWC.curie('Phylum'),
                      model_uri=DWC.Phylum, domain=None, range=Optional[str])

slots.Point_Radius_Spatial_Fit = Slot(uri=DWC.Point_Radius_Spatial_Fit, name="Point Radius Spatial Fit", curie=DWC.curie('Point_Radius_Spatial_Fit'),
                      model_uri=DWC.Point_Radius_Spatial_Fit, domain=None, range=Optional[str])

slots.Preparations = Slot(uri=DWC.Preparations, name="Preparations", curie=DWC.curie('Preparations'),
                      model_uri=DWC.Preparations, domain=None, range=Optional[str])

slots.Previous_Identifications = Slot(uri=DWC.Previous_Identifications, name="Previous Identifications", curie=DWC.curie('Previous_Identifications'),
                      model_uri=DWC.Previous_Identifications, domain=None, range=Optional[str], mappings = [DWC["version/previousIdentifications-2009-05-18"]])

slots.Recorded_By = Slot(uri=DWC.Recorded_By, name="Recorded By", curie=DWC.curie('Recorded_By'),
                      model_uri=DWC.Recorded_By, domain=None, range=Optional[str], mappings = [DWC["version/recordedBy-2009-04-24"]])

slots.Record_Number = Slot(uri=DWC.Record_Number, name="Record Number", curie=DWC.curie('Record_Number'),
                      model_uri=DWC.Record_Number, domain=None, range=Optional[str])

slots.Related_Basis_of_Record = Slot(uri=DWC.Related_Basis_of_Record, name="Related Basis of Record", curie=DWC.curie('Related_Basis_of_Record'),
                      model_uri=DWC.Related_Basis_of_Record, domain=None, range=Optional[str])

slots.Related_Resource_ID = Slot(uri=DWC.Related_Resource_ID, name="Related Resource ID", curie=DWC.curie('Related_Resource_ID'),
                      model_uri=DWC.Related_Resource_ID, domain=None, range=Optional[str])

slots.Related_Resource_Type = Slot(uri=DWC.Related_Resource_Type, name="Related Resource Type", curie=DWC.curie('Related_Resource_Type'),
                      model_uri=DWC.Related_Resource_Type, domain=None, range=Optional[str])

slots.Relationship_According_To = Slot(uri=DWC.Relationship_According_To, name="Relationship According To", curie=DWC.curie('Relationship_According_To'),
                      model_uri=DWC.Relationship_According_To, domain=None, range=Optional[str])

slots.Relationship_Established_Date = Slot(uri=DWC.Relationship_Established_Date, name="Relationship Established Date", curie=DWC.curie('Relationship_Established_Date'),
                      model_uri=DWC.Relationship_Established_Date, domain=None, range=Optional[str])

slots.Relationship_Of_Resource = Slot(uri=DWC.Relationship_Of_Resource, name="Relationship Of Resource", curie=DWC.curie('Relationship_Of_Resource'),
                      model_uri=DWC.Relationship_Of_Resource, domain=None, range=Optional[str])

slots.Relationship_Remarks = Slot(uri=DWC.Relationship_Remarks, name="Relationship Remarks", curie=DWC.curie('Relationship_Remarks'),
                      model_uri=DWC.Relationship_Remarks, domain=None, range=Optional[str])

slots.Reproductive_Condition = Slot(uri=DWC.Reproductive_Condition, name="Reproductive Condition", curie=DWC.curie('Reproductive_Condition'),
                      model_uri=DWC.Reproductive_Condition, domain=None, range=Optional[str])

slots.Resource_ID = Slot(uri=DWC.Resource_ID, name="Resource ID", curie=DWC.curie('Resource_ID'),
                      model_uri=DWC.Resource_ID, domain=None, range=Optional[str])

slots.Resource_Relationship_ID = Slot(uri=DWC.Resource_Relationship_ID, name="Resource Relationship ID", curie=DWC.curie('Resource_Relationship_ID'),
                      model_uri=DWC.Resource_Relationship_ID, domain=None, range=Optional[str])

slots.Sample_Attribute_Accuracy = Slot(uri=DWC.Sample_Attribute_Accuracy, name="Sample Attribute Accuracy", curie=DWC.curie('Sample_Attribute_Accuracy'),
                      model_uri=DWC.Sample_Attribute_Accuracy, domain=None, range=Optional[str])

slots.Sample_Attribute_Determined_By = Slot(uri=DWC.Sample_Attribute_Determined_By, name="Sample Attribute Determined By", curie=DWC.curie('Sample_Attribute_Determined_By'),
                      model_uri=DWC.Sample_Attribute_Determined_By, domain=None, range=Optional[str])

slots.Sample_Attribute_Determined_Date = Slot(uri=DWC.Sample_Attribute_Determined_Date, name="Sample Attribute Determined Date", curie=DWC.curie('Sample_Attribute_Determined_Date'),
                      model_uri=DWC.Sample_Attribute_Determined_Date, domain=None, range=Optional[str])

slots.Sample_Attribute_Remarks = Slot(uri=DWC.Sample_Attribute_Remarks, name="Sample Attribute Remarks", curie=DWC.curie('Sample_Attribute_Remarks'),
                      model_uri=DWC.Sample_Attribute_Remarks, domain=None, range=Optional[str])

slots.Sample_Attribute_Unit = Slot(uri=DWC.Sample_Attribute_Unit, name="Sample Attribute Unit", curie=DWC.curie('Sample_Attribute_Unit'),
                      model_uri=DWC.Sample_Attribute_Unit, domain=None, range=Optional[str])

slots.Sample_Attribute_Value = Slot(uri=DWC.Sample_Attribute_Value, name="Sample Attribute Value", curie=DWC.curie('Sample_Attribute_Value'),
                      model_uri=DWC.Sample_Attribute_Value, domain=None, range=Optional[str])

slots.Sample_Remarks = Slot(uri=DWC.Sample_Remarks, name="Sample Remarks", curie=DWC.curie('Sample_Remarks'),
                      model_uri=DWC.Sample_Remarks, domain=None, range=Optional[str])

slots.Sample_Size_Unit = Slot(uri=DWC.Sample_Size_Unit, name="Sample Size Unit", curie=DWC.curie('Sample_Size_Unit'),
                      model_uri=DWC.Sample_Size_Unit, domain=None, range=Optional[str])

slots.Sample_Size_Value = Slot(uri=DWC.Sample_Size_Value, name="Sample Size Value", curie=DWC.curie('Sample_Size_Value'),
                      model_uri=DWC.Sample_Size_Value, domain=None, range=Optional[str])

slots.Sample_Attribute_ID = Slot(uri=DWC.Sample_Attribute_ID, name="Sample Attribute ID", curie=DWC.curie('Sample_Attribute_ID'),
                      model_uri=DWC.Sample_Attribute_ID, domain=None, range=Optional[str])

slots.Sample_Attribute_Type = Slot(uri=DWC.Sample_Attribute_Type, name="Sample Attribute Type", curie=DWC.curie('Sample_Attribute_Type'),
                      model_uri=DWC.Sample_Attribute_Type, domain=None, range=Optional[str], mappings = [DWC["version/EventAttributeType-2008-11-19"], DWC["version/SampleAttributeType-2008-11-19"]])

slots.Sampling_Effort = Slot(uri=DWC.Sampling_Effort, name="Sampling Effort", curie=DWC.curie('Sampling_Effort'),
                      model_uri=DWC.Sampling_Effort, domain=None, range=Optional[str])

slots.Sampling_Event_Attributes = Slot(uri=DWC.Sampling_Event_Attributes, name="Sampling Event Attributes", curie=DWC.curie('Sampling_Event_Attributes'),
                      model_uri=DWC.Sampling_Event_Attributes, domain=None, range=Optional[str])

slots.Sampling_Event_ID = Slot(uri=DWC.Sampling_Event_ID, name="Sampling Event ID", curie=DWC.curie('Sampling_Event_ID'),
                      model_uri=DWC.Sampling_Event_ID, domain=None, range=Optional[str])

slots.Sampling_Event_Remarks = Slot(uri=DWC.Sampling_Event_Remarks, name="Sampling Event Remarks", curie=DWC.curie('Sampling_Event_Remarks'),
                      model_uri=DWC.Sampling_Event_Remarks, domain=None, range=Optional[str])

slots.Sampling_Location_ID = Slot(uri=DWC.Sampling_Location_ID, name="Sampling Location ID", curie=DWC.curie('Sampling_Location_ID'),
                      model_uri=DWC.Sampling_Location_ID, domain=None, range=Optional[str])

slots.Sampling_Location_Remarks = Slot(uri=DWC.Sampling_Location_Remarks, name="Sampling Location Remarks", curie=DWC.curie('Sampling_Location_Remarks'),
                      model_uri=DWC.Sampling_Location_Remarks, domain=None, range=Optional[str])

slots.Sampling_Protocol = Slot(uri=DWC.Sampling_Protocol, name="Sampling Protocol", curie=DWC.curie('Sampling_Protocol'),
                      model_uri=DWC.Sampling_Protocol, domain=None, range=Optional[str])

slots.Scientific_Name = Slot(uri=DWC.Scientific_Name, name="Scientific Name", curie=DWC.curie('Scientific_Name'),
                      model_uri=DWC.Scientific_Name, domain=None, range=Optional[str], mappings = [DWC["version/scientificName-2009-04-24"]])

slots.Scientific_Name_Authorship = Slot(uri=DWC.Scientific_Name_Authorship, name="Scientific Name Authorship", curie=DWC.curie('Scientific_Name_Authorship'),
                      model_uri=DWC.Scientific_Name_Authorship, domain=None, range=Optional[str])

slots.Scientific_Name_ID = Slot(uri=DWC.Scientific_Name_ID, name="Scientific Name ID", curie=DWC.curie('Scientific_Name_ID'),
                      model_uri=DWC.Scientific_Name_ID, domain=None, range=Optional[str], mappings = [DWC["version/TaxonNameID-2009-04-24"]])

slots.Scientific_Name_Rank = Slot(uri=DWC.Scientific_Name_Rank, name="Scientific Name Rank", curie=DWC.curie('Scientific_Name_Rank'),
                      model_uri=DWC.Scientific_Name_Rank, domain=None, range=Optional[str], mappings = [DWC["version/taxonRank-2009-04-24"]])

slots.Sex = Slot(uri=DWC.Sex, name="Sex", curie=DWC.curie('Sex'),
                      model_uri=DWC.Sex, domain=None, range=Optional[str])

slots.Specific_Epithet = Slot(uri=DWC.Specific_Epithet, name="Specific Epithet", curie=DWC.curie('Specific_Epithet'),
                      model_uri=DWC.Specific_Epithet, domain=None, range=Optional[str])

slots.Start_Day_Of_Year = Slot(uri=DWC.Start_Day_Of_Year, name="Start Day Of Year", curie=DWC.curie('Start_Day_Of_Year'),
                      model_uri=DWC.Start_Day_Of_Year, domain=None, range=Optional[str])

slots.Start_Time_of_Day = Slot(uri=DWC.Start_Time_of_Day, name="Start Time of Day", curie=DWC.curie('Start_Time_of_Day'),
                      model_uri=DWC.Start_Time_of_Day, domain=None, range=Optional[str])

slots.State_Province = Slot(uri=DWC.State_Province, name="State Province", curie=DWC.curie('State_Province'),
                      model_uri=DWC.State_Province, domain=None, range=Optional[str])

slots.Subgenus = Slot(uri=DWC.Subgenus, name="Subgenus", curie=DWC.curie('Subgenus'),
                      model_uri=DWC.Subgenus, domain=None, range=Optional[str], mappings = [DWC["version/subgenus-2009-04-24"]])

slots.Taxon_According_To = Slot(uri=DWC.Taxon_According_To, name="Taxon According To", curie=DWC.curie('Taxon_According_To'),
                      model_uri=DWC.Taxon_According_To, domain=None, range=Optional[str])

slots.Taxon_Attributes = Slot(uri=DWC.Taxon_Attributes, name="Taxon Attributes", curie=DWC.curie('Taxon_Attributes'),
                      model_uri=DWC.Taxon_Attributes, domain=None, range=Optional[str])

slots.Taxon_Concept_ID = Slot(uri=DWC.Taxon_Concept_ID, name="Taxon Concept ID", curie=DWC.curie('Taxon_Concept_ID'),
                      model_uri=DWC.Taxon_Concept_ID, domain=None, range=Optional[str], mappings = [DWC["version/taxonConceptID-2009-04-24"]])

slots.Taxon_ID = Slot(uri=DWC.Taxon_ID, name="Taxon ID", curie=DWC.curie('Taxon_ID'),
                      model_uri=DWC.Taxon_ID, domain=None, range=Optional[str], mappings = [DWC["version/scientificNameID-2009-07-06"]])

slots.Taxon_Name_ID = Slot(uri=DWC.Taxon_Name_ID, name="Taxon Name ID", curie=DWC.curie('Taxon_Name_ID'),
                      model_uri=DWC.Taxon_Name_ID, domain=None, range=Optional[str], mappings = [DWC["version/TaxonID-2008-11-19"]])

slots.Taxonomic_Status = Slot(uri=DWC.Taxonomic_Status, name="Taxonomic Status", curie=DWC.curie('Taxonomic_Status'),
                      model_uri=DWC.Taxonomic_Status, domain=None, range=Optional[str])

slots.Taxon_Rank = Slot(uri=DWC.Taxon_Rank, name="Taxon Rank", curie=DWC.curie('Taxon_Rank'),
                      model_uri=DWC.Taxon_Rank, domain=None, range=Optional[str], mappings = [DWC["version/scientificNameRank-2009-07-06"]])

slots.Taxon_Remarks = Slot(uri=DWC.Taxon_Remarks, name="Taxon Remarks", curie=DWC.curie('Taxon_Remarks'),
                      model_uri=DWC.Taxon_Remarks, domain=None, range=Optional[str], mappings = [DWC["version/taxonRemarks-2009-04-24"]])

slots.Type_Status = Slot(uri=DWC.Type_Status, name="Type Status", curie=DWC.curie('Type_Status'),
                      model_uri=DWC.Type_Status, domain=None, range=Optional[str], mappings = [DWC["version/typeStatus-2009-04-24"]])

slots.Verbatim_Coordinates = Slot(uri=DWC.Verbatim_Coordinates, name="Verbatim Coordinates", curie=DWC.curie('Verbatim_Coordinates'),
                      model_uri=DWC.Verbatim_Coordinates, domain=None, range=Optional[str])

slots.Verbatim_Coordinate_System = Slot(uri=DWC.Verbatim_Coordinate_System, name="Verbatim Coordinate System", curie=DWC.curie('Verbatim_Coordinate_System'),
                      model_uri=DWC.Verbatim_Coordinate_System, domain=None, range=Optional[str])

slots.Verbatim_Depth = Slot(uri=DWC.Verbatim_Depth, name="Verbatim Depth", curie=DWC.curie('Verbatim_Depth'),
                      model_uri=DWC.Verbatim_Depth, domain=None, range=Optional[str])

slots.Verbatim_Elevation = Slot(uri=DWC.Verbatim_Elevation, name="Verbatim Elevation", curie=DWC.curie('Verbatim_Elevation'),
                      model_uri=DWC.Verbatim_Elevation, domain=None, range=Optional[str])

slots.Verbatim_EventDate = Slot(uri=DWC.Verbatim_EventDate, name="Verbatim EventDate", curie=DWC.curie('Verbatim_EventDate'),
                      model_uri=DWC.Verbatim_EventDate, domain=None, range=Optional[str])

slots.Verbatim_Latitude = Slot(uri=DWC.Verbatim_Latitude, name="Verbatim Latitude", curie=DWC.curie('Verbatim_Latitude'),
                      model_uri=DWC.Verbatim_Latitude, domain=None, range=Optional[str])

slots.Verbatim_Locality = Slot(uri=DWC.Verbatim_Locality, name="Verbatim Locality", curie=DWC.curie('Verbatim_Locality'),
                      model_uri=DWC.Verbatim_Locality, domain=None, range=Optional[str])

slots.Verbatim_Longitude = Slot(uri=DWC.Verbatim_Longitude, name="Verbatim Longitude", curie=DWC.curie('Verbatim_Longitude'),
                      model_uri=DWC.Verbatim_Longitude, domain=None, range=Optional[str])

slots.Verbatim_Scientific_Name_Rank = Slot(uri=DWC.Verbatim_Scientific_Name_Rank, name="Verbatim Scientific Name Rank", curie=DWC.curie('Verbatim_Scientific_Name_Rank'),
                      model_uri=DWC.Verbatim_Scientific_Name_Rank, domain=None, range=Optional[str])

slots.Verbatim_SRS = Slot(uri=DWC.Verbatim_SRS, name="Verbatim SRS", curie=DWC.curie('Verbatim_SRS'),
                      model_uri=DWC.Verbatim_SRS, domain=None, range=Optional[str])

slots.Verbatim_Taxon_Rank = Slot(uri=DWC.Verbatim_Taxon_Rank, name="Verbatim Taxon Rank", curie=DWC.curie('Verbatim_Taxon_Rank'),
                      model_uri=DWC.Verbatim_Taxon_Rank, domain=None, range=Optional[str], mappings = [DWC["version/verbatimScientificNameRank-2009-07-06"]])

slots.Vernacular_Name = Slot(uri=DWC.Vernacular_Name, name="Vernacular Name", curie=DWC.curie('Vernacular_Name'),
                      model_uri=DWC.Vernacular_Name, domain=None, range=Optional[str])

slots.Water_Body = Slot(uri=DWC.Water_Body, name="Water Body", curie=DWC.curie('Water_Body'),
                      model_uri=DWC.Water_Body, domain=None, range=Optional[str])

slots.Year = Slot(uri=DWC.Year, name="Year", curie=DWC.curie('Year'),
                      model_uri=DWC.Year, domain=None, range=Optional[str])

slots.CatalogNumberNumeric = Slot(uri=DWC.CatalogNumberNumeric, name="CatalogNumberNumeric", curie=DWC.curie('CatalogNumberNumeric'),
                      model_uri=DWC.CatalogNumberNumeric, domain=None, range=Optional[str])

slots.CollectorNumber = Slot(uri=DWC.CollectorNumber, name="CollectorNumber", curie=DWC.curie('CollectorNumber'),
                      model_uri=DWC.CollectorNumber, domain=None, range=Optional[str])

slots.DateIdentified = Slot(uri=DWC.DateIdentified, name="DateIdentified", curie=DWC.curie('DateIdentified'),
                      model_uri=DWC.DateIdentified, domain=None, range=Optional[str])

slots.FieldNotes = Slot(uri=DWC.FieldNotes, name="FieldNotes", curie=DWC.curie('FieldNotes'),
                      model_uri=DWC.FieldNotes, domain=None, range=Optional[str])

slots.FieldNumber = Slot(uri=DWC.FieldNumber, name="FieldNumber", curie=DWC.curie('FieldNumber'),
                      model_uri=DWC.FieldNumber, domain=None, range=Optional[str])

slots.GenBankNumber = Slot(uri=DWC.GenBankNumber, name="GenBankNumber", curie=DWC.curie('GenBankNumber'),
                      model_uri=DWC.GenBankNumber, domain=None, range=Optional[str])

slots.IdentifiedBy = Slot(uri=DWC.IdentifiedBy, name="IdentifiedBy", curie=DWC.curie('IdentifiedBy'),
                      model_uri=DWC.IdentifiedBy, domain=None, range=Optional[str])

slots.IndividualCount = Slot(uri=DWC.IndividualCount, name="IndividualCount", curie=DWC.curie('IndividualCount'),
                      model_uri=DWC.IndividualCount, domain=None, range=Optional[str])

slots.OtherCatalogNumbers = Slot(uri=DWC.OtherCatalogNumbers, name="OtherCatalogNumbers", curie=DWC.curie('OtherCatalogNumbers'),
                      model_uri=DWC.OtherCatalogNumbers, domain=None, range=Optional[str])

slots.RelatedCatalogedItems = Slot(uri=DWC.RelatedCatalogedItems, name="RelatedCatalogedItems", curie=DWC.curie('RelatedCatalogedItems'),
                      model_uri=DWC.RelatedCatalogedItems, domain=None, range=Optional[str])

slots.TypeStatus = Slot(uri=DWC.TypeStatus, name="TypeStatus", curie=DWC.curie('TypeStatus'),
                      model_uri=DWC.TypeStatus, domain=None, range=Optional[str])

slots.VerbatimCollectingDate = Slot(uri=DWC.VerbatimCollectingDate, name="VerbatimCollectingDate", curie=DWC.curie('VerbatimCollectingDate'),
                      model_uri=DWC.VerbatimCollectingDate, domain=None, range=Optional[str])

slots.VerbatimDepth = Slot(uri=DWC.VerbatimDepth, name="VerbatimDepth", curie=DWC.curie('VerbatimDepth'),
                      model_uri=DWC.VerbatimDepth, domain=None, range=Optional[str])

slots.VerbatimElevation = Slot(uri=DWC.VerbatimElevation, name="VerbatimElevation", curie=DWC.curie('VerbatimElevation'),
                      model_uri=DWC.VerbatimElevation, domain=None, range=Optional[str])

slots.AgeClass = Slot(uri=DWC.AgeClass, name="AgeClass", curie=DWC.curie('AgeClass'),
                      model_uri=DWC.AgeClass, domain=None, range=Optional[str])

slots.BasisOfRecord = Slot(uri=DWC.BasisOfRecord, name="BasisOfRecord", curie=DWC.curie('BasisOfRecord'),
                      model_uri=DWC.BasisOfRecord, domain=None, range=Optional[str])

slots.BoundingBox = Slot(uri=DWC.BoundingBox, name="BoundingBox", curie=DWC.curie('BoundingBox'),
                      model_uri=DWC.BoundingBox, domain=None, range=Optional[str])

slots.CatalogNumber = Slot(uri=DWC.CatalogNumber, name="CatalogNumber", curie=DWC.curie('CatalogNumber'),
                      model_uri=DWC.CatalogNumber, domain=None, range=Optional[str])

slots.CatalogNumberText = Slot(uri=DWC.CatalogNumberText, name="CatalogNumberText", curie=DWC.curie('CatalogNumberText'),
                      model_uri=DWC.CatalogNumberText, domain=None, range=Optional[str])

slots.CollectionCode = Slot(uri=DWC.CollectionCode, name="CollectionCode", curie=DWC.curie('CollectionCode'),
                      model_uri=DWC.CollectionCode, domain=None, range=Optional[str])

slots.Collector = Slot(uri=DWC.Collector, name="Collector", curie=DWC.curie('Collector'),
                      model_uri=DWC.Collector, domain=None, range=Optional[str])

slots.ContinentOcean = Slot(uri=DWC.ContinentOcean, name="ContinentOcean", curie=DWC.curie('ContinentOcean'),
                      model_uri=DWC.ContinentOcean, domain=None, range=Optional[str])

slots.CoordinatePrecision = Slot(uri=DWC.CoordinatePrecision, name="CoordinatePrecision", curie=DWC.curie('CoordinatePrecision'),
                      model_uri=DWC.CoordinatePrecision, domain=None, range=Optional[str])

slots.CoordinateUncertaintyInMeters = Slot(uri=DWC.CoordinateUncertaintyInMeters, name="CoordinateUncertaintyInMeters", curie=DWC.curie('CoordinateUncertaintyInMeters'),
                      model_uri=DWC.CoordinateUncertaintyInMeters, domain=None, range=Optional[str])

slots.DateLastModified = Slot(uri=DWC.DateLastModified, name="DateLastModified", curie=DWC.curie('DateLastModified'),
                      model_uri=DWC.DateLastModified, domain=None, range=Optional[str])

slots.DayCollected = Slot(uri=DWC.DayCollected, name="DayCollected", curie=DWC.curie('DayCollected'),
                      model_uri=DWC.DayCollected, domain=None, range=Optional[str])

slots.DayIdentified = Slot(uri=DWC.DayIdentified, name="DayIdentified", curie=DWC.curie('DayIdentified'),
                      model_uri=DWC.DayIdentified, domain=None, range=Optional[str])

slots.DecimalLatitude = Slot(uri=DWC.DecimalLatitude, name="DecimalLatitude", curie=DWC.curie('DecimalLatitude'),
                      model_uri=DWC.DecimalLatitude, domain=None, range=Optional[str])

slots.DecimalLongitude = Slot(uri=DWC.DecimalLongitude, name="DecimalLongitude", curie=DWC.curie('DecimalLongitude'),
                      model_uri=DWC.DecimalLongitude, domain=None, range=Optional[str])

slots.GenBankNum = Slot(uri=DWC.GenBankNum, name="GenBankNum", curie=DWC.curie('GenBankNum'),
                      model_uri=DWC.GenBankNum, domain=None, range=Optional[str])

slots.GeorefMethod = Slot(uri=DWC.GeorefMethod, name="GeorefMethod", curie=DWC.curie('GeorefMethod'),
                      model_uri=DWC.GeorefMethod, domain=None, range=Optional[str])

slots.HigherGeography = Slot(uri=DWC.HigherGeography, name="HigherGeography", curie=DWC.curie('HigherGeography'),
                      model_uri=DWC.HigherGeography, domain=None, range=Optional[str])

slots.HigherTaxon = Slot(uri=DWC.HigherTaxon, name="HigherTaxon", curie=DWC.curie('HigherTaxon'),
                      model_uri=DWC.HigherTaxon, domain=None, range=Optional[str])

slots.HorizontalDatum = Slot(uri=DWC.HorizontalDatum, name="HorizontalDatum", curie=DWC.curie('HorizontalDatum'),
                      model_uri=DWC.HorizontalDatum, domain=None, range=Optional[str])

slots.IdentificationModifier = Slot(uri=DWC.IdentificationModifier, name="IdentificationModifier", curie=DWC.curie('IdentificationModifier'),
                      model_uri=DWC.IdentificationModifier, domain=None, range=Optional[str])

slots.InstitutionCode = Slot(uri=DWC.InstitutionCode, name="InstitutionCode", curie=DWC.curie('InstitutionCode'),
                      model_uri=DWC.InstitutionCode, domain=None, range=Optional[str])

slots.IslandGroup = Slot(uri=DWC.IslandGroup, name="IslandGroup", curie=DWC.curie('IslandGroup'),
                      model_uri=DWC.IslandGroup, domain=None, range=Optional[str])

slots.JulianDay = Slot(uri=DWC.JulianDay, name="JulianDay", curie=DWC.curie('JulianDay'),
                      model_uri=DWC.JulianDay, domain=None, range=Optional[str])

slots.Latitude = Slot(uri=DWC.Latitude, name="Latitude", curie=DWC.curie('Latitude'),
                      model_uri=DWC.Latitude, domain=None, range=Optional[str])

slots.LatLongComments = Slot(uri=DWC.LatLongComments, name="LatLongComments", curie=DWC.curie('LatLongComments'),
                      model_uri=DWC.LatLongComments, domain=None, range=Optional[str])

slots.Longitude = Slot(uri=DWC.Longitude, name="Longitude", curie=DWC.curie('Longitude'),
                      model_uri=DWC.Longitude, domain=None, range=Optional[str])

slots.MaximumDepth = Slot(uri=DWC.MaximumDepth, name="MaximumDepth", curie=DWC.curie('MaximumDepth'),
                      model_uri=DWC.MaximumDepth, domain=None, range=Optional[str])

slots.MaximumDepthInMeters = Slot(uri=DWC.MaximumDepthInMeters, name="MaximumDepthInMeters", curie=DWC.curie('MaximumDepthInMeters'),
                      model_uri=DWC.MaximumDepthInMeters, domain=None, range=Optional[str])

slots.MaximumElevation = Slot(uri=DWC.MaximumElevation, name="MaximumElevation", curie=DWC.curie('MaximumElevation'),
                      model_uri=DWC.MaximumElevation, domain=None, range=Optional[str])

slots.MaximumElevationInMeters = Slot(uri=DWC.MaximumElevationInMeters, name="MaximumElevationInMeters", curie=DWC.curie('MaximumElevationInMeters'),
                      model_uri=DWC.MaximumElevationInMeters, domain=None, range=Optional[str])

slots.MinimumDepth = Slot(uri=DWC.MinimumDepth, name="MinimumDepth", curie=DWC.curie('MinimumDepth'),
                      model_uri=DWC.MinimumDepth, domain=None, range=Optional[str])

slots.MinimumDepthInMeters = Slot(uri=DWC.MinimumDepthInMeters, name="MinimumDepthInMeters", curie=DWC.curie('MinimumDepthInMeters'),
                      model_uri=DWC.MinimumDepthInMeters, domain=None, range=Optional[str])

slots.MinimumElevation = Slot(uri=DWC.MinimumElevation, name="MinimumElevation", curie=DWC.curie('MinimumElevation'),
                      model_uri=DWC.MinimumElevation, domain=None, range=Optional[str])

slots.MinimumElevationInMeters = Slot(uri=DWC.MinimumElevationInMeters, name="MinimumElevationInMeters", curie=DWC.curie('MinimumElevationInMeters'),
                      model_uri=DWC.MinimumElevationInMeters, domain=None, range=Optional[str])

slots.MonthCollected = Slot(uri=DWC.MonthCollected, name="MonthCollected", curie=DWC.curie('MonthCollected'),
                      model_uri=DWC.MonthCollected, domain=None, range=Optional[str])

slots.MonthIdentified = Slot(uri=DWC.MonthIdentified, name="MonthIdentified", curie=DWC.curie('MonthIdentified'),
                      model_uri=DWC.MonthIdentified, domain=None, range=Optional[str])

slots.Notes = Slot(uri=DWC.Notes, name="Notes", curie=DWC.curie('Notes'),
                      model_uri=DWC.Notes, domain=None, range=Optional[str])

slots.OriginalCoordinateSystem = Slot(uri=DWC.OriginalCoordinateSystem, name="OriginalCoordinateSystem", curie=DWC.curie('OriginalCoordinateSystem'),
                      model_uri=DWC.OriginalCoordinateSystem, domain=None, range=Optional[str])

slots.PreparationType = Slot(uri=DWC.PreparationType, name="PreparationType", curie=DWC.curie('PreparationType'),
                      model_uri=DWC.PreparationType, domain=None, range=Optional[str])

slots.PreviousCatalogNumber = Slot(uri=DWC.PreviousCatalogNumber, name="PreviousCatalogNumber", curie=DWC.curie('PreviousCatalogNumber'),
                      model_uri=DWC.PreviousCatalogNumber, domain=None, range=Optional[str])

slots.RelatedCatalogItem = Slot(uri=DWC.RelatedCatalogItem, name="RelatedCatalogItem", curie=DWC.curie('RelatedCatalogItem'),
                      model_uri=DWC.RelatedCatalogItem, domain=None, range=Optional[str])

slots.RelationshipType = Slot(uri=DWC.RelationshipType, name="RelationshipType", curie=DWC.curie('RelationshipType'),
                      model_uri=DWC.RelationshipType, domain=None, range=Optional[str])

slots.Remarks = Slot(uri=DWC.Remarks, name="Remarks", curie=DWC.curie('Remarks'),
                      model_uri=DWC.Remarks, domain=None, range=Optional[str])

slots.ScientificName = Slot(uri=DWC.ScientificName, name="ScientificName", curie=DWC.curie('ScientificName'),
                      model_uri=DWC.ScientificName, domain=None, range=Optional[str])

slots.ScientificNameAuthor = Slot(uri=DWC.ScientificNameAuthor, name="ScientificNameAuthor", curie=DWC.curie('ScientificNameAuthor'),
                      model_uri=DWC.ScientificNameAuthor, domain=None, range=Optional[str])

slots.Species = Slot(uri=DWC.Species, name="Species", curie=DWC.curie('Species'),
                      model_uri=DWC.Species, domain=None, range=Optional[str])

slots.StateProvince = Slot(uri=DWC.StateProvince, name="StateProvince", curie=DWC.curie('StateProvince'),
                      model_uri=DWC.StateProvince, domain=None, range=Optional[str])

slots.Subspecies = Slot(uri=DWC.Subspecies, name="Subspecies", curie=DWC.curie('Subspecies'),
                      model_uri=DWC.Subspecies, domain=None, range=Optional[str])

slots.TimeCollected = Slot(uri=DWC.TimeCollected, name="TimeCollected", curie=DWC.curie('TimeCollected'),
                      model_uri=DWC.TimeCollected, domain=None, range=Optional[str])

slots.TimeOfDay = Slot(uri=DWC.TimeOfDay, name="TimeOfDay", curie=DWC.curie('TimeOfDay'),
                      model_uri=DWC.TimeOfDay, domain=None, range=Optional[str])

slots.Tissues = Slot(uri=DWC.Tissues, name="Tissues", curie=DWC.curie('Tissues'),
                      model_uri=DWC.Tissues, domain=None, range=Optional[str])

slots.VerbatimLatitude = Slot(uri=DWC.VerbatimLatitude, name="VerbatimLatitude", curie=DWC.curie('VerbatimLatitude'),
                      model_uri=DWC.VerbatimLatitude, domain=None, range=Optional[str])

slots.VerbatimLongitude = Slot(uri=DWC.VerbatimLongitude, name="VerbatimLongitude", curie=DWC.curie('VerbatimLongitude'),
                      model_uri=DWC.VerbatimLongitude, domain=None, range=Optional[str])

slots.YearCollected = Slot(uri=DWC.YearCollected, name="YearCollected", curie=DWC.curie('YearCollected'),
                      model_uri=DWC.YearCollected, domain=None, range=Optional[str])

slots.YearIdentified = Slot(uri=DWC.YearIdentified, name="YearIdentified", curie=DWC.curie('YearIdentified'),
                      model_uri=DWC.YearIdentified, domain=None, range=Optional[str])

slots.EarliestAgeOrLowestStage = Slot(uri=DWC.EarliestAgeOrLowestStage, name="EarliestAgeOrLowestStage", curie=DWC.curie('EarliestAgeOrLowestStage'),
                      model_uri=DWC.EarliestAgeOrLowestStage, domain=None, range=Optional[str])

slots.EarliestEonOrLowestEonothem = Slot(uri=DWC.EarliestEonOrLowestEonothem, name="EarliestEonOrLowestEonothem", curie=DWC.curie('EarliestEonOrLowestEonothem'),
                      model_uri=DWC.EarliestEonOrLowestEonothem, domain=None, range=Optional[str])

slots.EarliestEpochOrLowestSeries = Slot(uri=DWC.EarliestEpochOrLowestSeries, name="EarliestEpochOrLowestSeries", curie=DWC.curie('EarliestEpochOrLowestSeries'),
                      model_uri=DWC.EarliestEpochOrLowestSeries, domain=None, range=Optional[str])

slots.EarliestEraOrLowestErathem = Slot(uri=DWC.EarliestEraOrLowestErathem, name="EarliestEraOrLowestErathem", curie=DWC.curie('EarliestEraOrLowestErathem'),
                      model_uri=DWC.EarliestEraOrLowestErathem, domain=None, range=Optional[str])

slots.EarliestPeriodOrLowestSystem = Slot(uri=DWC.EarliestPeriodOrLowestSystem, name="EarliestPeriodOrLowestSystem", curie=DWC.curie('EarliestPeriodOrLowestSystem'),
                      model_uri=DWC.EarliestPeriodOrLowestSystem, domain=None, range=Optional[str])

slots.HighestBiostratigraphicZone = Slot(uri=DWC.HighestBiostratigraphicZone, name="HighestBiostratigraphicZone", curie=DWC.curie('HighestBiostratigraphicZone'),
                      model_uri=DWC.HighestBiostratigraphicZone, domain=None, range=Optional[str])

slots.LatestAgeOrHighestStage = Slot(uri=DWC.LatestAgeOrHighestStage, name="LatestAgeOrHighestStage", curie=DWC.curie('LatestAgeOrHighestStage'),
                      model_uri=DWC.LatestAgeOrHighestStage, domain=None, range=Optional[str])

slots.LatestEonOrHighestEonothem = Slot(uri=DWC.LatestEonOrHighestEonothem, name="LatestEonOrHighestEonothem", curie=DWC.curie('LatestEonOrHighestEonothem'),
                      model_uri=DWC.LatestEonOrHighestEonothem, domain=None, range=Optional[str])

slots.LatestEpochOrHighestSeries = Slot(uri=DWC.LatestEpochOrHighestSeries, name="LatestEpochOrHighestSeries", curie=DWC.curie('LatestEpochOrHighestSeries'),
                      model_uri=DWC.LatestEpochOrHighestSeries, domain=None, range=Optional[str])

slots.LatestEraOrHighestErathem = Slot(uri=DWC.LatestEraOrHighestErathem, name="LatestEraOrHighestErathem", curie=DWC.curie('LatestEraOrHighestErathem'),
                      model_uri=DWC.LatestEraOrHighestErathem, domain=None, range=Optional[str])

slots.LatestPeriodOrHighestSystem = Slot(uri=DWC.LatestPeriodOrHighestSystem, name="LatestPeriodOrHighestSystem", curie=DWC.curie('LatestPeriodOrHighestSystem'),
                      model_uri=DWC.LatestPeriodOrHighestSystem, domain=None, range=Optional[str])

slots.LithostratigraphicTerms = Slot(uri=DWC.LithostratigraphicTerms, name="LithostratigraphicTerms", curie=DWC.curie('LithostratigraphicTerms'),
                      model_uri=DWC.LithostratigraphicTerms, domain=None, range=Optional[str])

slots.LowestBiostratigraphicZone = Slot(uri=DWC.LowestBiostratigraphicZone, name="LowestBiostratigraphicZone", curie=DWC.curie('LowestBiostratigraphicZone'),
                      model_uri=DWC.LowestBiostratigraphicZone, domain=None, range=Optional[str])

slots.source_mat_id = Slot(uri=DWC.source_mat_id, name="source_mat_id", curie=DWC.curie('source_mat_id'),
                      model_uri=DWC.source_mat_id, domain=None, range=Optional[str])

slots.Attributes = Slot(uri=DWC.Attributes, name="Attributes", curie=DWC.curie('Attributes'),
                      model_uri=DWC.Attributes, domain=None, range=Optional[str])

slots.AuthorYearOfScientificName = Slot(uri=DWC.AuthorYearOfScientificName, name="AuthorYearOfScientificName", curie=DWC.curie('AuthorYearOfScientificName'),
                      model_uri=DWC.AuthorYearOfScientificName, domain=None, range=Optional[str])

slots.CollectingMethod = Slot(uri=DWC.CollectingMethod, name="CollectingMethod", curie=DWC.curie('CollectingMethod'),
                      model_uri=DWC.CollectingMethod, domain=None, range=Optional[str])

slots.DayOfYear = Slot(uri=DWC.DayOfYear, name="DayOfYear", curie=DWC.curie('DayOfYear'),
                      model_uri=DWC.DayOfYear, domain=None, range=Optional[str])

slots.EarliestDateCollected = Slot(uri=DWC.EarliestDateCollected, name="EarliestDateCollected", curie=DWC.curie('EarliestDateCollected'),
                      model_uri=DWC.EarliestDateCollected, domain=None, range=Optional[str])

slots.GlobalUniqueIdentifier = Slot(uri=DWC.GlobalUniqueIdentifier, name="GlobalUniqueIdentifier", curie=DWC.curie('GlobalUniqueIdentifier'),
                      model_uri=DWC.GlobalUniqueIdentifier, domain=None, range=Optional[str])

slots.IdentificationQualifier = Slot(uri=DWC.IdentificationQualifier, name="IdentificationQualifier", curie=DWC.curie('IdentificationQualifier'),
                      model_uri=DWC.IdentificationQualifier, domain=None, range=Optional[str])

slots.ImageURL = Slot(uri=DWC.ImageURL, name="ImageURL", curie=DWC.curie('ImageURL'),
                      model_uri=DWC.ImageURL, domain=None, range=Optional[str])

slots.InformationWithheld = Slot(uri=DWC.InformationWithheld, name="InformationWithheld", curie=DWC.curie('InformationWithheld'),
                      model_uri=DWC.InformationWithheld, domain=None, range=Optional[str])

slots.InfraspecificEpithet = Slot(uri=DWC.InfraspecificEpithet, name="InfraspecificEpithet", curie=DWC.curie('InfraspecificEpithet'),
                      model_uri=DWC.InfraspecificEpithet, domain=None, range=Optional[str])

slots.InfraspecificRank = Slot(uri=DWC.InfraspecificRank, name="InfraspecificRank", curie=DWC.curie('InfraspecificRank'),
                      model_uri=DWC.InfraspecificRank, domain=None, range=Optional[str])

slots.LatestDateCollected = Slot(uri=DWC.LatestDateCollected, name="LatestDateCollected", curie=DWC.curie('LatestDateCollected'),
                      model_uri=DWC.LatestDateCollected, domain=None, range=Optional[str])

slots.LifeStage = Slot(uri=DWC.LifeStage, name="LifeStage", curie=DWC.curie('LifeStage'),
                      model_uri=DWC.LifeStage, domain=None, range=Optional[str])

slots.NomenclaturalCode = Slot(uri=DWC.NomenclaturalCode, name="NomenclaturalCode", curie=DWC.curie('NomenclaturalCode'),
                      model_uri=DWC.NomenclaturalCode, domain=None, range=Optional[str])

slots.RelatedInformation = Slot(uri=DWC.RelatedInformation, name="RelatedInformation", curie=DWC.curie('RelatedInformation'),
                      model_uri=DWC.RelatedInformation, domain=None, range=Optional[str])

slots.SpecificEpithet = Slot(uri=DWC.SpecificEpithet, name="SpecificEpithet", curie=DWC.curie('SpecificEpithet'),
                      model_uri=DWC.SpecificEpithet, domain=None, range=Optional[str])

slots.ValidDistributionFlag = Slot(uri=DWC.ValidDistributionFlag, name="ValidDistributionFlag", curie=DWC.curie('ValidDistributionFlag'),
                      model_uri=DWC.ValidDistributionFlag, domain=None, range=Optional[str])

slots.WaterBody = Slot(uri=DWC.WaterBody, name="WaterBody", curie=DWC.curie('WaterBody'),
                      model_uri=DWC.WaterBody, domain=None, range=Optional[str])

slots.FootprintSpatialFit = Slot(uri=DWC.FootprintSpatialFit, name="FootprintSpatialFit", curie=DWC.curie('FootprintSpatialFit'),
                      model_uri=DWC.FootprintSpatialFit, domain=None, range=Optional[str])

slots.FootprintWKT = Slot(uri=DWC.FootprintWKT, name="FootprintWKT", curie=DWC.curie('FootprintWKT'),
                      model_uri=DWC.FootprintWKT, domain=None, range=Optional[str])

slots.GeodeticDatum = Slot(uri=DWC.GeodeticDatum, name="GeodeticDatum", curie=DWC.curie('GeodeticDatum'),
                      model_uri=DWC.GeodeticDatum, domain=None, range=Optional[str])

slots.GeoreferenceProtocol = Slot(uri=DWC.GeoreferenceProtocol, name="GeoreferenceProtocol", curie=DWC.curie('GeoreferenceProtocol'),
                      model_uri=DWC.GeoreferenceProtocol, domain=None, range=Optional[str])

slots.GeoreferenceRemarks = Slot(uri=DWC.GeoreferenceRemarks, name="GeoreferenceRemarks", curie=DWC.curie('GeoreferenceRemarks'),
                      model_uri=DWC.GeoreferenceRemarks, domain=None, range=Optional[str])

slots.GeoreferenceSources = Slot(uri=DWC.GeoreferenceSources, name="GeoreferenceSources", curie=DWC.curie('GeoreferenceSources'),
                      model_uri=DWC.GeoreferenceSources, domain=None, range=Optional[str])

slots.GeoreferenceVerificationStatus = Slot(uri=DWC.GeoreferenceVerificationStatus, name="GeoreferenceVerificationStatus", curie=DWC.curie('GeoreferenceVerificationStatus'),
                      model_uri=DWC.GeoreferenceVerificationStatus, domain=None, range=Optional[str])

slots.PointRadiusSpatialFit = Slot(uri=DWC.PointRadiusSpatialFit, name="PointRadiusSpatialFit", curie=DWC.curie('PointRadiusSpatialFit'),
                      model_uri=DWC.PointRadiusSpatialFit, domain=None, range=Optional[str])

slots.VerbatimCoordinates = Slot(uri=DWC.VerbatimCoordinates, name="VerbatimCoordinates", curie=DWC.curie('VerbatimCoordinates'),
                      model_uri=DWC.VerbatimCoordinates, domain=None, range=Optional[str])

slots.VerbatimCoordinateSystem = Slot(uri=DWC.VerbatimCoordinateSystem, name="VerbatimCoordinateSystem", curie=DWC.curie('VerbatimCoordinateSystem'),
                      model_uri=DWC.VerbatimCoordinateSystem, domain=None, range=Optional[str])
