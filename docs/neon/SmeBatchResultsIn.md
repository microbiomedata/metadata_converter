
# Type: sme_batchResults_in




URI: [neon:SmeBatchResultsIn](https://data.neonscience.org/SmeBatchResultsIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SmeBatchResultsIn&#124;uid:string%20%3F;processedDate:time%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;analyteUnits:string%20%3F;dataQF:string%20%3F;batchID:string%20%3F;analyteKnownValue:double%20%3F;analyteObservedValue:double%20%3F;analysisStandardID:string%20%3F;lipidID:string%20%3F;lotNumber:string%20%3F;extractEffStdID:string%20%3F;extractEffStdUnits:string%20%3F;analyteStandardQF:string%20%3F])

## Attributes


### Own

 * [analysisStandardID](analysisStandardID.md)  <sub>OPT</sub>
    * Description: Manufacturer and catalog number of analytical standard
    * range: [String](types/String.md)
 * [analyteKnownValue](analyteKnownValue.md)  <sub>OPT</sub>
    * Description: The known value of a given analyte for a quality assurance reference material or standard, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [analyteObservedValue](analyteObservedValue.md)  <sub>OPT</sub>
    * Description: The measured value of a given analyte for a standard reference material, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [analyteStandardQF](analyteStandardQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the analyte standard/s
    * range: [String](types/String.md)
 * [analyteUnits](analyteUnits.md)  <sub>OPT</sub>
    * Description: Associated units of measure for analyte
    * range: [String](types/String.md)
 * [batchID](batchID.md)  <sub>OPT</sub>
    * Description: Identifier for batch or analytical run
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [extractEffStdID](extractEffStdID.md)  <sub>OPT</sub>
    * Description: Identifier of lipid standard used for measuring extraction efficiency
    * range: [String](types/String.md)
 * [extractEffStdUnits](extractEffStdUnits.md)  <sub>OPT</sub>
    * Description: Associated units of measure for extraction efficiency standard
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [lipidID](lipidID.md)  <sub>OPT</sub>
    * Description: Identifier of lipid standard used for quality assurance testing
    * range: [String](types/String.md)
 * [lotNumber](lotNumber.md)  <sub>OPT</sub>
    * Description: Lot number for standard
    * range: [String](types/String.md)
 * [processedDate](processedDate.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event
    * range: [Time](types/Time.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sme_batchResults_in |

