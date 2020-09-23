
# Type: fsh_bulkCount_in




URI: [neon:FshBulkCountIn](https://data.neonscience.org/FshBulkCountIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[FshBulkCountIn&#124;uid:string%20%3F;identificationReferences:string%20%3F;remarks:string%20%3F;taxonID:string%20%3F;identificationQualifier:string%20%3F;eventID:string%20%3F;morphospeciesID:string%20%3F;identifiedBy:string%20%3F;morphospeciesIDRemarks:string%20%3F;locationID:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;actualOrEstimated:string%20%3F;bulkFishCount:string%20%3F;bulkMortality:string%20%3F;passEndTime:time%20%3F;passNumber:string%20%3F;passStartTime:time%20%3F])

## Attributes


### Own

 * [actualOrEstimated](actualOrEstimated.md)  <sub>OPT</sub>
    * Description: Indication of whether the count is actual or estimated
    * range: [String](types/String.md)
 * [bulkFishCount](bulkFishCount.md)  <sub>OPT</sub>
    * Description: The number of fish counted during bulk processing
    * range: [String](types/String.md)
 * [bulkMortality](bulkMortality.md)  <sub>OPT</sub>
    * Description: The number of specimens found dead in bulk processing
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
 * [identificationReferences](identificationReferences.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) used to derive the specific taxon concept; including field guide editions, books, or versions of NEON keys used
    * range: [String](types/String.md)
 * [identifiedBy](identifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who identified the specimen
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [morphospeciesID](morphospeciesID.md)  <sub>OPT</sub>
    * Description: Identifier for morphospecies
    * range: [String](types/String.md)
 * [morphospeciesIDRemarks](morphospeciesIDRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes about the morphospecies; free text comments accompanying the record
    * range: [String](types/String.md)
 * [passEndTime](passEndTime.md)  <sub>OPT</sub>
    * Description: The end time of the pass
    * range: [Time](types/Time.md)
 * [passNumber](passNumber.md)  <sub>OPT</sub>
    * Description: Number of the sampling pass within a reach
    * range: [String](types/String.md)
 * [passStartTime](passStartTime.md)  <sub>OPT</sub>
    * Description: The start time of the pass
    * range: [Time](types/Time.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:fsh_bulkCount_in |

