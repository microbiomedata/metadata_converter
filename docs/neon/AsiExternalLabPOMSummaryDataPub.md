
# Type: asi_externalLabPOMSummaryData_pub




URI: [neon:AsiExternalLabPOMSummaryDataPub](https://data.neonscience.org/AsiExternalLabPOMSummaryDataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AsiExternalLabPOMSummaryDataPub&#124;uid:string%20%3F;sampleType:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;analyte:string%20%3F;instrument:string%20%3F;method:string%20%3F;labSpecificStartDate:time%20%3F;labSpecificEndDate:time%20%3F;testMethod:string%20%3F;analyteAccuracy:double%20%3F;analyteStandardDeviation:double%20%3F;qaReferenceID:string%20%3F;standardReferenceKnownValue:double%20%3F;standardReferenceMeasuredMean:double%20%3F])

## Attributes


### Own

 * [analyte](analyte.md)  <sub>OPT</sub>
    * Description: Analyte or parameter measured
    * range: [String](types/String.md)
 * [analyteAccuracy](analyteAccuracy.md)  <sub>OPT</sub>
    * Description: Long-term average accuracy, e.g. the absolute difference between observed and known values of the analyte, based on analysis of quality assurance reference materials or standards treated as unknowns
    * range: [Double](types/Double.md)
 * [analyteStandardDeviation](analyteStandardDeviation.md)  <sub>OPT</sub>
    * Description: Long-term average standard deviation values of the analyte, based on analysis of quality assurance reference materials or standards treated as unknowns
    * range: [Double](types/Double.md)
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
 * [method](method.md)  <sub>OPT</sub>
    * Description: Published method used for analysis
    * range: [String](types/String.md)
 * [qaReferenceID](qaReferenceID.md)  <sub>OPT</sub>
    * Description: Identifier for quality assurance reference material or standard
    * range: [String](types/String.md)
 * [sampleType](sampleType.md)  <sub>OPT</sub>
    * Description: Type of sample
    * range: [String](types/String.md)
 * [standardReferenceKnownValue](standardReferenceKnownValue.md)  <sub>OPT</sub>
    * Description: The known value for QA reference material, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [standardReferenceMeasuredMean](standardReferenceMeasuredMean.md)  <sub>OPT</sub>
    * Description: Long-term average of the measured value for QA reference material, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [testMethod](testMethod.md)  <sub>OPT</sub>
    * Description: Method used to conduct test
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:asi_externalLabPOMSummaryData_pub |

