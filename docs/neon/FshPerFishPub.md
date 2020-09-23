
# Type: fsh_perFish_pub




URI: [neon:FshPerFishPub](https://data.neonscience.org/FshPerFishPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[FshPerFishPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;identificationReferences:string%20%3F;remarks:string%20%3F;taxonID:string%20%3F;identificationQualifier:string%20%3F;voucherSampleID:string%20%3F;eventID:string%20%3F;scientificName:string%20%3F;taxonRank:string%20%3F;morphospeciesID:string%20%3F;identifiedBy:string%20%3F;morphospeciesIDRemarks:string%20%3F;dataQF:string%20%3F;dnaSampleID:string%20%3F;dnaSampleCode:string%20%3F;namedLocation:string%20%3F;voucherSampleCode:string%20%3F;delt:string%20%3F;fishLifeStage:string%20%3F;fishTotalLength:double%20%3F;fishWeight:double%20%3F;efInjury:string%20%3F;efMortality:string%20%3F;passEndTime:time%20%3F;passNumber:string%20%3F;passStartTime:time%20%3F;sampleTypeCollected:string%20%3F;specimenNumber:string%20%3F])

## Attributes


### Own

 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [delt](delt.md)  <sub>OPT</sub>
    * Description: Indication of any deformities, eroded fins, lesions/parasites, tumors
    * range: [String](types/String.md)
 * [dnaSampleCode](dnaSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a DNA sample
    * range: [String](types/String.md)
 * [dnaSampleID](dnaSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for DNA sample
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [efInjury](efInjury.md)  <sub>OPT</sub>
    * Description: Indication of injury from the electrofishing equipment (burn marks, bent spine, hemorrhage)
    * range: [String](types/String.md)
 * [efMortality](efMortality.md)  <sub>OPT</sub>
    * Description: Indication of mortality from the electrofishing equipment
    * range: [String](types/String.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fishLifeStage](fishLifeStage.md)  <sub>OPT</sub>
    * Description: Indication of the life stage of the fish
    * range: [String](types/String.md)
 * [fishTotalLength](fishTotalLength.md)  <sub>OPT</sub>
    * Description: Length of the specimen
    * range: [Double](types/Double.md)
 * [fishWeight](fishWeight.md)  <sub>OPT</sub>
    * Description: Live weight as measured in the field
    * range: [Double](types/Double.md)
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
 * [identificationReferences](identificationReferences.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) used to derive the specific taxon concept; including field guide editions, books, or versions of NEON keys used
    * range: [String](types/String.md)
 * [identifiedBy](identifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who identified the specimen
    * range: [String](types/String.md)
 * [morphospeciesID](morphospeciesID.md)  <sub>OPT</sub>
    * Description: Identifier for morphospecies
    * range: [String](types/String.md)
 * [morphospeciesIDRemarks](morphospeciesIDRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes about the morphospecies; free text comments accompanying the record
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
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
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleTypeCollected](sampleTypeCollected.md)  <sub>OPT</sub>
    * Description: Type of sample collected
    * range: [String](types/String.md)
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [specimenNumber](specimenNumber.md)  <sub>OPT</sub>
    * Description: Number of the specimen
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [taxonRank](taxonRank.md)  <sub>OPT</sub>
    * Description: The lowest level taxonomic rank that can be determined for the individual or specimen
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [voucherSampleCode](voucherSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a voucher sample
    * range: [String](types/String.md)
 * [voucherSampleID](voucherSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the voucher sample
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:fsh_perFish_pub |

