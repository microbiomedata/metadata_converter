
# Type: sme_labSummary_in




URI: [neon:SmeLabSummaryIn](https://data.neonscience.org/SmeLabSummaryIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SmeLabSummaryIn&#124;uid:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;instrument:string%20%3F;labSpecificStartDate:time%20%3F;labSpecificEndDate:time%20%3F;testProtocolVersion:string%20%3F;dataQF:string%20%3F;analyteAccuracy:double%20%3F;analyteStandardDeviation:double%20%3F;reviewedBy:string%20%3F;analyteKnownValue:double%20%3F;analysisStandardID:string%20%3F;lipidID:string%20%3F;analyteAccuracyUnits:string%20%3F;analyteKnownValueUnits:string%20%3F;analyteStandardDeviationUnits:string%20%3F])

## Attributes


### Own

 * [analysisStandardID](analysisStandardID.md)  <sub>OPT</sub>
    * Description: Manufacturer and catalog number of analytical standard
    * range: [String](types/String.md)
 * [analyteAccuracy](analyteAccuracy.md)  <sub>OPT</sub>
    * Description: Long-term average accuracy, e.g. the absolute difference between observed and known values of the analyte, based on analysis of quality assurance reference materials or standards treated as unknowns
    * range: [Double](types/Double.md)
 * [analyteAccuracyUnits](analyteAccuracyUnits.md)  <sub>OPT</sub>
    * Description: Associated units of measure for analyte accuracy
    * range: [String](types/String.md)
 * [analyteKnownValue](analyteKnownValue.md)  <sub>OPT</sub>
    * Description: The known value of a given analyte for a quality assurance reference material or standard, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [analyteKnownValueUnits](analyteKnownValueUnits.md)  <sub>OPT</sub>
    * Description: Associated units of measure for analyte known value
    * range: [String](types/String.md)
 * [analyteStandardDeviation](analyteStandardDeviation.md)  <sub>OPT</sub>
    * Description: Long-term average standard deviation values of the analyte, based on analysis of quality assurance reference materials or standards treated as unknowns
    * range: [Double](types/Double.md)
 * [analyteStandardDeviationUnits](analyteStandardDeviationUnits.md)  <sub>OPT</sub>
    * Description: Associated units of measure for analyte standard deviation
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
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
 * [lipidID](lipidID.md)  <sub>OPT</sub>
    * Description: Identifier of lipid standard used for quality assurance testing
    * range: [String](types/String.md)
 * [reviewedBy](reviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed the data prior to submission
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [testProtocolVersion](testProtocolVersion.md)  <sub>OPT</sub>
    * Description: The protocol version used to test the sample
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sme_labSummary_in |

