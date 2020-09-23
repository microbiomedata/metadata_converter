
# Type: zoo_perTaxon_in




URI: [neon:ZooPerTaxonIn](https://data.neonscience.org/ZooPerTaxonIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ZooPerTaxonIn&#124;uid:string%20%3F;identificationReferences:string%20%3F;identificationQualifier:string%20%3F;scientificName:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;targetTaxaPresent:string%20%3F;individualCount:string%20%3F;morphospeciesID:string%20%3F;identifiedBy:string%20%3F;identifiedDate:time%20%3F;subsampleType:string%20%3F;startDate:time%20%3F;laboratoryName:string%20%3F;internalLabID:string%20%3F;internalLabName:string%20%3F;identificationRemarks:string%20%3F;testProtocolVersion:string%20%3F;locationID:string%20%3F;kingdom:string%20%3F;phylum:string%20%3F;class:string%20%3F;order:string%20%3F;family:string%20%3F;subfamily:string%20%3F;genus:string%20%3F;subgenus:string%20%3F;specificEpithet:string%20%3F;infraspecificEpithet:string%20%3F;tribe:string%20%3F;taxonDatabaseName:string%20%3F;taxonDatabaseID:string%20%3F;distinctTaxon:string%20%3F;qcChecked:string%20%3F;indeterminateSpecies:string%20%3F;notSubsampled:string%20%3F;subphylum:string%20%3F;subclass:string%20%3F;infraclass:string%20%3F;superorder:string%20%3F;suborder:string%20%3F;infraorder:string%20%3F;superfamily:string%20%3F;subtribe:string%20%3F;subkingdom:string%20%3F;infrakingdom:string%20%3F;superclass:string%20%3F;subspecies:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;referencePhotoID:string%20%3F;sampleCondition:string%20%3F;nauplii:string%20%3F;zooMinimumLength:double%20%3F;zooMaximumLength:double%20%3F;zooMeanLength:double%20%3F;zooWidth:double%20%3F;zooSubsampleVolume:double%20%3F;superphylum:string%20%3F;infraphylum:string%20%3F;adjCountPerBottle:double%20%3F;referencePhotoCode:string%20%3F;zooVolumePerBottle:double%20%3F;qcEnumerationDifference:double%20%3F;qcTaxonomicDifference:double%20%3F])

## Attributes


### Own

 * [adjCountPerBottle](adjCountPerBottle.md)  <sub>OPT</sub>
    * Description: Count of individuals of the given taxon, multiplied to the volume per bottle to account for lab subsampling
    * range: [Double](types/Double.md)
 * [class](class.md)  <sub>OPT</sub>
    * Description: The scientific name of the class in which the taxon is classified
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [distinctTaxon](distinctTaxon.md)  <sub>OPT</sub>
    * Description: Taxon is known to be distinct within the sample, used for species richness metrics
    * range: [String](types/String.md)
 * [family](family.md)  <sub>OPT</sub>
    * Description: The scientific name of the family in which the taxon is classified
    * range: [String](types/String.md)
 * [genus](genus.md)  <sub>OPT</sub>
    * Description: The scientific name of the genus in which the organism is classified
    * range: [String](types/String.md)
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
 * [identificationReferences](identificationReferences.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) used to derive the specific taxon concept; including field guide editions, books, or versions of NEON keys used
    * range: [String](types/String.md)
 * [identificationRemarks](identificationRemarks.md)  <sub>OPT</sub>
    * Description: Comments or notes about the identification
    * range: [String](types/String.md)
 * [identifiedBy](identifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who identified the specimen
    * range: [String](types/String.md)
 * [identifiedDate](identifiedDate.md)  <sub>OPT</sub>
    * Description: Date on which the sample, individual, or specimen was identified
    * range: [Time](types/Time.md)
 * [indeterminateSpecies](indeterminateSpecies.md)  <sub>OPT</sub>
    * Description: Sample contains specimen(s) not well-described in the literature, not all taxa for a group are included in the literature, or observed characters are such that they do not fit described taxa. See accompanying identificationRemarks
    * range: [String](types/String.md)
 * [individualCount](individualCount.md)  <sub>OPT</sub>
    * Description: Number of individuals of the same type
    * range: [String](types/String.md)
 * [infraclass](infraclass.md)  <sub>OPT</sub>
    * Description: The scientific name of the infraclass in which the taxon is classified
    * range: [String](types/String.md)
 * [infrakingdom](infrakingdom.md)  <sub>OPT</sub>
    * Description: The scientific name of the infrakingdom in which the taxon is classified
    * range: [String](types/String.md)
 * [infraorder](infraorder.md)  <sub>OPT</sub>
    * Description: The scientific name of the infraorder in which the taxon is classified
    * range: [String](types/String.md)
 * [infraphylum](infraphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the infraphylum in which the taxon is classified
    * range: [String](types/String.md)
 * [infraspecificEpithet](infraspecificEpithet.md)  <sub>OPT</sub>
    * Description: The infraspecific epithet (scientific name below the rank of species) of the scientific name applied to the taxon
    * range: [String](types/String.md)
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
 * [internalLabName](internalLabName.md)  <sub>OPT</sub>
    * Description: Name of internal laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [kingdom](kingdom.md)  <sub>OPT</sub>
    * Description: The scientific name of the kingdom in which the taxon is classified
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [morphospeciesID](morphospeciesID.md)  <sub>OPT</sub>
    * Description: Identifier for morphospecies
    * range: [String](types/String.md)
 * [nauplii](nauplii.md)  <sub>OPT</sub>
    * Description: Indication of whether the zooplankton specimen is nauplii
    * range: [String](types/String.md)
 * [notSubsampled](notSubsampled.md)  <sub>OPT</sub>
    * Description: Subsampling was not performed (for example, due to relative taxon abundance or rareness within a sample)
    * range: [String](types/String.md)
 * [order](order.md)  <sub>OPT</sub>
    * Description: The scientific name of the order in which the taxon is classified
    * range: [String](types/String.md)
 * [phylum](phylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the phylum or division in which the taxon is classified
    * range: [String](types/String.md)
 * [qcChecked](qcChecked.md)  <sub>OPT</sub>
    * Description: Whether or not QC procedure was performed
    * range: [String](types/String.md)
 * [qcEnumerationDifference](qcEnumerationDifference.md)  <sub>OPT</sub>
    * Description: Percent difference in enumeration (PDE) between the first taxonomist and the second taxonomist for the same sample
    * range: [Double](types/Double.md)
 * [qcTaxonomicDifference](qcTaxonomicDifference.md)  <sub>OPT</sub>
    * Description: Percent taxonomic difference (PTD) between the first taxonomist and the second taxonomist for the same sample
    * range: [Double](types/Double.md)
 * [referencePhotoCode](referencePhotoCode.md)  <sub>OPT</sub>
    * Description: Barcode of a reference photo
    * range: [String](types/String.md)
 * [referencePhotoID](referencePhotoID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the photo associated with the reference collection
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
    * range: [String](types/String.md)
 * [specificEpithet](specificEpithet.md)  <sub>OPT</sub>
    * Description: The specific epithet (second part of the species name) of the scientific name applied to the taxon
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [subclass](subclass.md)  <sub>OPT</sub>
    * Description: The scientific name of the subclass in which the taxon is classified
    * range: [String](types/String.md)
 * [subfamily](subfamily.md)  <sub>OPT</sub>
    * Description: The scientific name of the subfamily in which the organism is classified
    * range: [String](types/String.md)
 * [subgenus](subgenus.md)  <sub>OPT</sub>
    * Description: The scientific name of the subgenus in which the taxon is classified. Values should include the genus to avoid homonym confusion
    * range: [String](types/String.md)
 * [subkingdom](subkingdom.md)  <sub>OPT</sub>
    * Description: The scientific name of the subkingdom in which the taxon is classified
    * range: [String](types/String.md)
 * [suborder](suborder.md)  <sub>OPT</sub>
    * Description: The scientific name of the suborder in which the taxon is classified
    * range: [String](types/String.md)
 * [subphylum](subphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the subphylum in which the taxon is classified
    * range: [String](types/String.md)
 * [subsampleType](subsampleType.md)  <sub>OPT</sub>
    * Description: Indicates type of subsample generated
    * range: [String](types/String.md)
 * [subspecies](subspecies.md)  <sub>OPT</sub>
    * Description: The subspecies (infraspecific name below the rank of infraspecific epithet) of the scientific name applied to the taxon
    * range: [String](types/String.md)
 * [subtribe](subtribe.md)  <sub>OPT</sub>
    * Description: The scientific name of the subtribe in which the taxon is classified
    * range: [String](types/String.md)
 * [superclass](superclass.md)  <sub>OPT</sub>
    * Description: The scientific name of the superclass in which the taxon is classified
    * range: [String](types/String.md)
 * [superfamily](superfamily.md)  <sub>OPT</sub>
    * Description: The scientific name of the superfamily in which the taxon is classified
    * range: [String](types/String.md)
 * [superorder](superorder.md)  <sub>OPT</sub>
    * Description: The scientific name of the superorder in which the taxon is classified
    * range: [String](types/String.md)
 * [superphylum](superphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the superphylum in which the taxon is classified
    * range: [String](types/String.md)
 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [taxonDatabaseID](taxonDatabaseID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the taxon within the database
    * range: [String](types/String.md)
 * [taxonDatabaseName](taxonDatabaseName.md)  <sub>OPT</sub>
    * Description: Name of the taxonomic database
    * range: [String](types/String.md)
 * [testProtocolVersion](testProtocolVersion.md)  <sub>OPT</sub>
    * Description: The protocol version used to test the sample
    * range: [String](types/String.md)
 * [tribe](tribe.md)  <sub>OPT</sub>
    * Description: The scientific name of the tribe in which the taxon is classified
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [zooMaximumLength](zooMaximumLength.md)  <sub>OPT</sub>
    * Description: Maximum length of individuals in zooplankton taxonomic group subsample
    * range: [Double](types/Double.md)
 * [zooMeanLength](zooMeanLength.md)  <sub>OPT</sub>
    * Description: Mean length of individuals in zooplankton taxonomic group subsample
    * range: [Double](types/Double.md)
 * [zooMinimumLength](zooMinimumLength.md)  <sub>OPT</sub>
    * Description: Minimum length of individuals in zooplankton taxonomic group subsample
    * range: [Double](types/Double.md)
 * [zooSubsampleVolume](zooSubsampleVolume.md)  <sub>OPT</sub>
    * Description: Volume of zooplankton subsample analyzed
    * range: [Double](types/Double.md)
 * [zooVolumePerBottle](zooVolumePerBottle.md)  <sub>OPT</sub>
    * Description: Volume of zooplankton subsample per bottle
    * range: [Double](types/Double.md)
 * [zooWidth](zooWidth.md)  <sub>OPT</sub>
    * Description: Mean width of individuals in zooplankton taxonomic group subsample
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:zoo_perTaxon_in |

