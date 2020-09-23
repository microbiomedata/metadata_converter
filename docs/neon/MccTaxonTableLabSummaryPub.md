
# Type: mcc_taxonTableLabSummary_pub




URI: [neon:MccTaxonTableLabSummaryPub](https://data.neonscience.org/MccTaxonTableLabSummaryPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MccTaxonTableLabSummaryPub&#124;uid:string%20%3F;remarks:string%20%3F;recordedBy:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;labSpecificStartDate:time%20%3F;labSpecificEndDate:time%20%3F;testMethod:string%20%3F;dataQF:string%20%3F;targetTaxonGroup:string%20%3F;alignmentMethod:string%20%3F;analysisCodeFileName:string%20%3F;analysisProgram:string%20%3F;analysisProgramVersion:string%20%3F;chimeraMethod:string%20%3F;clusterMethod:string%20%3F;clusterSimilarity:double%20%3F;referenceDatabase:string%20%3F;referenceDatabaseVersion:string%20%3F;sequenceMatchMethod:string%20%3F;sequenceMatchThresholdValue:double%20%3F;sequenceMatchValueDescription:string%20%3F])

## Attributes


### Own

 * [alignmentMethod](alignmentMethod.md)  <sub>OPT</sub>
    * Description: Method used to align sequences
    * range: [String](types/String.md)
 * [analysisCodeFileName](analysisCodeFileName.md)  <sub>OPT</sub>
    * Description: File name of code used for data analysis
    * range: [String](types/String.md)
 * [analysisProgram](analysisProgram.md)  <sub>OPT</sub>
    * Description: Program or software used to analyze sequences for taxonomic identification
    * range: [String](types/String.md)
 * [analysisProgramVersion](analysisProgramVersion.md)  <sub>OPT</sub>
    * Description: The unique name and numbering combination assigned to the analysis program
    * range: [String](types/String.md)
 * [chimeraMethod](chimeraMethod.md)  <sub>OPT</sub>
    * Description: Method used to remove chimeras from sequences
    * range: [String](types/String.md)
 * [clusterMethod](clusterMethod.md)  <sub>OPT</sub>
    * Description: Method used to cluster sequences
    * range: [String](types/String.md)
 * [clusterSimilarity](clusterSimilarity.md)  <sub>OPT</sub>
    * Description: Similarity threshold for sequence clusters
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [labSpecificEndDate](labSpecificEndDate.md)  <sub>OPT</sub>
    * Description: Date a specific analyte, instrument, and associated method detection limit combination ended
    * range: [Time](types/Time.md)
 * [labSpecificStartDate](labSpecificStartDate.md)  <sub>OPT</sub>
    * Description: Date a specific analyte, instrument, and associated method detection limit combination started
    * range: [Time](types/Time.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [referenceDatabase](referenceDatabase.md)  <sub>OPT</sub>
    * Description: Reference database used for taxonomic identification
    * range: [String](types/String.md)
 * [referenceDatabaseVersion](referenceDatabaseVersion.md)  <sub>OPT</sub>
    * Description: The unique name and numbering combination assigned to the reference database
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sequenceMatchMethod](sequenceMatchMethod.md)  <sub>OPT</sub>
    * Description: Method and/or algorithm used to evaluate the similarity between a query and reference sequence
    * range: [String](types/String.md)
 * [sequenceMatchThresholdValue](sequenceMatchThresholdValue.md)  <sub>OPT</sub>
    * Description: Threshold value for considering a query and a reference sequence a match
    * range: [Double](types/Double.md)
 * [sequenceMatchValueDescription](sequenceMatchValueDescription.md)  <sub>OPT</sub>
    * Description: Description of the metric used to evaluate if a query and a reference sequence are a match
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [targetTaxonGroup](targetTaxonGroup.md)  <sub>OPT</sub>
    * Description: Taxonomic group targeted
    * range: [String](types/String.md)
 * [testMethod](testMethod.md)  <sub>OPT</sub>
    * Description: Method used to conduct test
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mcc_taxonTableLabSummary_pub |

