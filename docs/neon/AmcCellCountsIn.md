
# Type: amc_cellCounts_in




URI: [neon:AmcCellCountsIn](https://data.neonscience.org/AmcCellCountsIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AmcCellCountsIn&#124;uid:string%20%3F;remarks:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;laboratoryName:string%20%3F;deprecatedVialID:string%20%3F;testedDate:time%20%3F;testProtocolVersion:string%20%3F;locationID:string%20%3F;analyzedBy:string%20%3F;filterSize:double%20%3F;cellCountSampleID:string%20%3F;sampleCondition:string%20%3F;cellCountSampleFate:string%20%3F;cellCountSampleCode:string%20%3F;externalLabDataQF:string%20%3F;batchID:string%20%3F;reviewedBy:string%20%3F;qaqcStatus:string%20%3F;analysisMagnification:string%20%3F;analysisVolume:double%20%3F;batchReferenceCount:string%20%3F;cellCountMethod:string%20%3F;enumerationDifference:double%20%3F;numberOfFieldsAnalyzed:string%20%3F;rawMicrobialAbundance:string%20%3F;totalCellCount:string%20%3F;dilutionFactor:double%20%3F;qcAnalyzedBy:string%20%3F])

## Attributes


### Own

 * [analysisMagnification](analysisMagnification.md)  <sub>OPT</sub>
    * Description: Magnification used during analysis
    * range: [String](types/String.md)
 * [analysisVolume](analysisVolume.md)  <sub>OPT</sub>
    * Description: Volume in milliliters of sample analyzed
    * range: [Double](types/Double.md)
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
 * [batchID](batchID.md)  <sub>OPT</sub>
    * Description: Identifier for batch or analytical run
    * range: [String](types/String.md)
 * [batchReferenceCount](batchReferenceCount.md)  <sub>OPT</sub>
    * Description: Automated count of reference image for the batch
    * range: [String](types/String.md)
 * [cellCountMethod](cellCountMethod.md)  <sub>OPT</sub>
    * Description: Enumeration method used for microbial cell count
    * range: [String](types/String.md)
 * [cellCountSampleCode](cellCountSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a cell count sample
    * range: [String](types/String.md)
 * [cellCountSampleFate](cellCountSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a cell count sample
    * range: [String](types/String.md)
 * [cellCountSampleID](cellCountSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for the cell count sample
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [deprecatedVialID](deprecatedVialID.md)  <sub>OPT</sub>
    * Description: Identifier on vial label, if different from standard ID
    * range: [String](types/String.md)
 * [dilutionFactor](dilutionFactor.md)  <sub>OPT</sub>
    * Description: The factor by which the sample was diluted prior to analysis
    * range: [Double](types/Double.md)
 * [enumerationDifference](enumerationDifference.md)  <sub>OPT</sub>
    * Description: Percent difference in enumeration between the original sample and the quality checked sample
    * range: [Double](types/Double.md)
 * [externalLabDataQF](externalLabDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for external lab data
    * range: [String](types/String.md)
 * [filterSize](filterSize.md)  <sub>OPT</sub>
    * Description: Filter diameter
    * range: [Double](types/Double.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [numberOfFieldsAnalyzed](numberOfFieldsAnalyzed.md)  <sub>OPT</sub>
    * Description: Number of fields analyzed for microbial cell count
    * range: [String](types/String.md)
 * [qaqcStatus](qaqcStatus.md)  <sub>OPT</sub>
    * Description: Status of internal QAQC
    * range: [String](types/String.md)
 * [qcAnalyzedBy](qcAnalyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample for quality control
    * range: [String](types/String.md)
 * [rawMicrobialAbundance](rawMicrobialAbundance.md)  <sub>OPT</sub>
    * Description: Raw microbial abundance, not corrected for preservative volume
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [reviewedBy](reviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed the data prior to submission
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [testProtocolVersion](testProtocolVersion.md)  <sub>OPT</sub>
    * Description: The protocol version used to test the sample
    * range: [String](types/String.md)
 * [testedDate](testedDate.md)  <sub>OPT</sub>
    * Description: Date test was conducted
    * range: [Time](types/Time.md)
 * [totalCellCount](totalCellCount.md)  <sub>OPT</sub>
    * Description: Total number of cells counted in the analysis
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:amc_cellCounts_in |

