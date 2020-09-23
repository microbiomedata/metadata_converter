
# Type: mga_labSummary_pub




URI: [neon:MgaLabSummaryPub](https://data.neonscience.org/MgaLabSummaryPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MgaLabSummaryPub&#124;uid:string%20%3F;recordedBy:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;instrument:string%20%3F;labSpecificStartDate:time%20%3F;labSpecificEndDate:time%20%3F;dataQF:string%20%3F;ampliconLength:string%20%3F;bufferComposition:string%20%3F;bufferID:string%20%3F;cqMethod:string%20%3F;dNTPConcentration:double%20%3F;forwardPrimer:string%20%3F;detectionLimit:double%20%3F;mgConcentration:double%20%3F;multiplexStatus:string%20%3F;polymeraseType:string%20%3F;polymeraseUnitNumber:double%20%3F;primerConcentration:double%20%3F;primerSpecificity:double%20%3F;probeConcentration:double%20%3F;qPCRAnalysisProgram:string%20%3F;qpcrDetectionMethod:string%20%3F;qpcrMethod:string%20%3F;reactionVolume:double%20%3F;reversePrimer:string%20%3F;targetTaxonGroup:string%20%3F])

## Attributes


### Own

 * [ampliconLength](ampliconLength.md)  <sub>OPT</sub>
    * Description: Length of amplicon
    * range: [String](types/String.md)
 * [bufferComposition](bufferComposition.md)  <sub>OPT</sub>
    * Description: Contents of buffer solution
    * range: [String](types/String.md)
 * [bufferID](bufferID.md)  <sub>OPT</sub>
    * Description: Identity and manufacturer of buffer or kit
    * range: [String](types/String.md)
 * [cqMethod](cqMethod.md)  <sub>OPT</sub>
    * Description: Method used to determine the quantification cycle
    * range: [String](types/String.md)
 * [dNTPConcentration](dNTPConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of deoxynucleoside triphosphates used in sample assay
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [detectionLimit](detectionLimit.md)  <sub>OPT</sub>
    * Description: Lowest concentration of target gene copies measured consistently in replicate assays
    * range: [Double](types/Double.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [forwardPrimer](forwardPrimer.md)  <sub>OPT</sub>
    * Description: DNA sequence of forward primer
    * range: [String](types/String.md)
 * [instrument](instrument.md)  <sub>OPT</sub>
    * Description: Type of instrument used for the analysis
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
 * [mgConcentration](mgConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of magnesium used in sample assay
    * range: [Double](types/Double.md)
 * [multiplexStatus](multiplexStatus.md)  <sub>OPT</sub>
    * Description: Whether multiple genes are targeted in a single PCR reaction
    * range: [String](types/String.md)
 * [polymeraseType](polymeraseType.md)  <sub>OPT</sub>
    * Description: Type of DNA polymerase used in sample assay
    * range: [String](types/String.md)
 * [polymeraseUnitNumber](polymeraseUnitNumber.md)  <sub>OPT</sub>
    * Description: Number of units of DNA polymerase used in sample assay
    * range: [Double](types/Double.md)
 * [primerConcentration](primerConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of primers used in sample assay
    * range: [Double](types/Double.md)
 * [primerSpecificity](primerSpecificity.md)  <sub>OPT</sub>
    * Description: Specificity of primer for target taxa based on BLAST or similar analysis
    * range: [Double](types/Double.md)
 * [probeConcentration](probeConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of probe used in sample assays
    * range: [Double](types/Double.md)
 * [qPCRAnalysisProgram](qPCRAnalysisProgram.md)  <sub>OPT</sub>
    * Description: Name, version and manufacturer of qPCR analysis software
    * range: [String](types/String.md)
 * [qpcrDetectionMethod](qpcrDetectionMethod.md)  <sub>OPT</sub>
    * Description: Method used for amplicon detection in qPCR assay
    * range: [String](types/String.md)
 * [qpcrMethod](qpcrMethod.md)  <sub>OPT</sub>
    * Description: Protocol used for qPCR reaction setup and themocycling conditions
    * range: [String](types/String.md)
 * [reactionVolume](reactionVolume.md)  <sub>OPT</sub>
    * Description: Volume of reaction
    * range: [Double](types/Double.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [reversePrimer](reversePrimer.md)  <sub>OPT</sub>
    * Description: DNA sequence of reverse primer
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [targetTaxonGroup](targetTaxonGroup.md)  <sub>OPT</sub>
    * Description: Taxonomic group targeted
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mga_labSummary_pub |

