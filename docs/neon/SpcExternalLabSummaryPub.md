
# Type: spc_externalLabSummary_pub




URI: [neon:SpcExternalLabSummaryPub](https://data.neonscience.org/SpcExternalLabSummaryPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SpcExternalLabSummaryPub&#124;uid:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;analyte:string%20%3F;method:string%20%3F;methodDetectionLimit:double%20%3F;analyteUnits:string%20%3F;labSpecificStartDate:time%20%3F;labSpecificEndDate:time%20%3F;dataQF:string%20%3F;analyteAccuracy:double%20%3F;analyteStandardDeviation:double%20%3F;qaReferenceID:string%20%3F;analyteKnownValue:double%20%3F;methodPub:string%20%3F])

## Attributes


### Own

 * [analyte](analyte.md)  <sub>OPT</sub>
    * Description: Analyte or parameter measured
    * range: [String](types/String.md)
 * [analyteAccuracy](analyteAccuracy.md)  <sub>OPT</sub>
    * Description: Long-term average accuracy, e.g. the absolute difference between observed and known values of the analyte, based on analysis of quality assurance reference materials or standards treated as unknowns
    * range: [Double](types/Double.md)
 * [analyteKnownValue](analyteKnownValue.md)  <sub>OPT</sub>
    * Description: The known value of a given analyte for a quality assurance reference material or standard, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [analyteStandardDeviation](analyteStandardDeviation.md)  <sub>OPT</sub>
    * Description: Long-term average standard deviation values of the analyte, based on analysis of quality assurance reference materials or standards treated as unknowns
    * range: [Double](types/Double.md)
 * [analyteUnits](analyteUnits.md)  <sub>OPT</sub>
    * Description: Associated units of measure for analyte
    * range: [String](types/String.md)
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
 * [method](method.md)  <sub>OPT</sub>
    * Description: Published method used for analysis
    * range: [String](types/String.md)
 * [methodDetectionLimit](methodDetectionLimit.md)  <sub>OPT</sub>
    * Description: Detection limit for method used
    * range: [Double](types/Double.md)
 * [methodPub](methodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the method used
    * range: [String](types/String.md)
 * [qaReferenceID](qaReferenceID.md)  <sub>OPT</sub>
    * Description: Identifier for quality assurance reference material or standard
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:spc_externalLabSummary_pub |

