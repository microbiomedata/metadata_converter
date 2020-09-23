
# Type: alg_biovolumes_in




URI: [neon:AlgBiovolumesIn](https://data.neonscience.org/AlgBiovolumesIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AlgBiovolumesIn&#124;uid:string%20%3F;identificationReferences:string%20%3F;remarks:string%20%3F;scientificName:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;labSpecificStartDate:time%20%3F;labSpecificEndDate:time%20%3F;taxonDatabaseName:string%20%3F;taxonDatabaseID:string%20%3F;dataQF:string%20%3F;biovolumeMean:double%20%3F;biovolumeFormula:string%20%3F;biovolumeSpecimenNumber:string%20%3F;taxonAbbreviation:string%20%3F;biovolumeSD:double%20%3F])

## Attributes


### Own

 * [biovolumeFormula](biovolumeFormula.md)  <sub>OPT</sub>
    * Description: Formula used to calculate biovolume of cells of the same taxon
    * range: [String](types/String.md)
 * [biovolumeMean](biovolumeMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean biovolume of cells of the same taxon
    * range: [Double](types/Double.md)
 * [biovolumeSD](biovolumeSD.md)  <sub>OPT</sub>
    * Description: Standard deviation in biovolume across cells of the same taxon
    * range: [Double](types/Double.md)
 * [biovolumeSpecimenNumber](biovolumeSpecimenNumber.md)  <sub>OPT</sub>
    * Description: Number of specimens measured for biovolume
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [identificationReferences](identificationReferences.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) used to derive the specific taxon concept; including field guide editions, books, or versions of NEON keys used
    * range: [String](types/String.md)
 * [labSpecificEndDate](labSpecificEndDate.md)  <sub>OPT</sub>
    * Description: Date a specific analyte, instrument, and associated method detection limit combination ended
    * range: [Time](types/Time.md)
 * [labSpecificStartDate](labSpecificStartDate.md)  <sub>OPT</sub>
    * Description: Date a specific analyte, instrument, and associated method detection limit combination started
    * range: [Time](types/Time.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [taxonAbbreviation](taxonAbbreviation.md)  <sub>OPT</sub>
    * Description: The abbreviation for the taxon
    * range: [String](types/String.md)
 * [taxonDatabaseID](taxonDatabaseID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the taxon within the database
    * range: [String](types/String.md)
 * [taxonDatabaseName](taxonDatabaseName.md)  <sub>OPT</sub>
    * Description: Name of the taxonomic database
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:alg_biovolumes_in |

