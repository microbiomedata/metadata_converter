
# Type: mos_identification_in




URI: [neon:MosIdentificationIn](https://data.neonscience.org/MosIdentificationIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MosIdentificationIn&#124;uid:string%20%3F;plotID:string%20%3F;identificationReferences:string%20%3F;remarks:string%20%3F;identificationQualifier:string%20%3F;sex:string%20%3F;scientificName:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;targetTaxaPresent:string%20%3F;individualCount:string%20%3F;identifiedBy:string%20%3F;identifiedDate:time%20%3F;subsampleID:string%20%3F;laboratoryName:string%20%3F;archiveID:string%20%3F;sampleCompromised:string%20%3F;testingID:string%20%3F;individualIDList:string%20%3F;identificationRemarks:string%20%3F;dataQF:string%20%3F;testingIDCode:string%20%3F;testingIDFate:string%20%3F;subsampleCode:string%20%3F;subsampleFate:string%20%3F;archiveFate:string%20%3F;archiveIDCode:string%20%3F;individualCode:string%20%3F;individualFate:string%20%3F])

## Attributes


### Own

 * [archiveFate](archiveFate.md)  <sub>OPT</sub>
    * Description: Fate of the Archive sample
    * range: [String](types/String.md)
 * [archiveID](archiveID.md)  <sub>OPT</sub>
    * Description: Identifier for the archive sample
    * range: [String](types/String.md)
 * [archiveIDCode](archiveIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of the Archive sample
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
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
 * [individualCode](individualCode.md)  <sub>OPT</sub>
    * Description: Barcode of an individual
    * range: [String](types/String.md)
 * [individualCount](individualCount.md)  <sub>OPT</sub>
    * Description: Number of individuals of the same type
    * range: [String](types/String.md)
 * [individualFate](individualFate.md)  <sub>OPT</sub>
    * Description: Fate of a tagged individual
    * range: [String](types/String.md)
 * [individualIDList](individualIDList.md)  <sub>OPT</sub>
    * Description: List of individualIDs
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleCompromised](sampleCompromised.md)  <sub>OPT</sub>
    * Description: Indicator of compromised sample integrity; 'other' requires further specification in remarks
    * range: [String](types/String.md)
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [sex](sex.md)  <sub>OPT</sub>
    * Description: M for male, F for female, U for unknown
    * range: [String](types/String.md)
 * [subsampleCode](subsampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a subsample
    * range: [String](types/String.md)
 * [subsampleFate](subsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a subsample
    * range: [String](types/String.md)
 * [subsampleID](subsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with each subsample per sampleID
    * range: [String](types/String.md)
 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [testingID](testingID.md)  <sub>OPT</sub>
    * Description: Identifier for the group of specimens for testing
    * range: [String](types/String.md)
 * [testingIDCode](testingIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of a test sample
    * range: [String](types/String.md)
 * [testingIDFate](testingIDFate.md)  <sub>OPT</sub>
    * Description: Fate of a test sample
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mos_identification_in |

