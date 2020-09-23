
# Type: ptx_qualityCheck_in




URI: [neon:PtxQualityCheckIn](https://data.neonscience.org/PtxQualityCheckIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PtxQualityCheckIn&#124;uid:string%20%3F;remarks:string%20%3F;scientificName:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;individualCount:string%20%3F;morphospeciesID:string%20%3F;identifiedBy:string%20%3F;identifiedDate:time%20%3F;stationID:string%20%3F;startDate:time%20%3F;laboratoryName:string%20%3F;qcPercentSimilarity:double%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;taxonAbbreviation:string%20%3F;enumerationDifference:double%20%3F;qcIdentifiedBy:string%20%3F;qcIndividualCount:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [enumerationDifference](enumerationDifference.md)  <sub>OPT</sub>
    * Description: Percent difference in enumeration between the original sample and the quality checked sample
    * range: [Double](types/Double.md)
 * [identifiedBy](identifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who identified the specimen
    * range: [String](types/String.md)
 * [identifiedDate](identifiedDate.md)  <sub>OPT</sub>
    * Description: Date on which the sample, individual, or specimen was identified
    * range: [Time](types/Time.md)
 * [individualCount](individualCount.md)  <sub>OPT</sub>
    * Description: Number of individuals of the same type
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [morphospeciesID](morphospeciesID.md)  <sub>OPT</sub>
    * Description: Identifier for morphospecies
    * range: [String](types/String.md)
 * [qcIdentifiedBy](qcIdentifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who quality checked the specimen
    * range: [String](types/String.md)
 * [qcIndividualCount](qcIndividualCount.md)  <sub>OPT</sub>
    * Description: Number of individuals of the same type in the quality checked sample
    * range: [String](types/String.md)
 * [qcPercentSimilarity](qcPercentSimilarity.md)  <sub>OPT</sub>
    * Description: Percent similarity of original taxonomy report and QC taxonomy report (identification + count)
    * range: [Double](types/Double.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
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
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [taxonAbbreviation](taxonAbbreviation.md)  <sub>OPT</sub>
    * Description: The abbreviation for the taxon
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:ptx_qualityCheck_in |

