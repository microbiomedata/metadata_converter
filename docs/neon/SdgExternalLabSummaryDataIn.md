
# Type: sdg_externalLabSummaryData_in




URI: [neon:SdgExternalLabSummaryDataIn](https://data.neonscience.org/SdgExternalLabSummaryDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SdgExternalLabSummaryDataIn&#124;uid:string%20%3F;remarks:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;analyte:string%20%3F;instrument:string%20%3F;method:string%20%3F;methodDetectionLimit:double%20%3F;precision:double%20%3F;measurementUncertainty:double%20%3F;labSpecificStartDate:time%20%3F;labSpecificEndDate:time%20%3F;dataQF:string%20%3F;measurementUncertaintyUnits:string%20%3F;methodDetectionLimitUnits:string%20%3F;precisionUnits:string%20%3F])

## Attributes


### Own

 * [analyte](analyte.md)  <sub>OPT</sub>
    * Description: Analyte or parameter measured
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
 * [measurementUncertainty](measurementUncertainty.md)  <sub>OPT</sub>
    * Description: Parameter, associated with the result of a measurement, that characterizes the dispersion of the values that could reasonably be attributed to the measurant
    * range: [Double](types/Double.md)
 * [measurementUncertaintyUnits](measurementUncertaintyUnits.md)  <sub>OPT</sub>
    * Description: Units of measurement uncertainty
    * range: [String](types/String.md)
 * [method](method.md)  <sub>OPT</sub>
    * Description: Published method used for analysis
    * range: [String](types/String.md)
 * [methodDetectionLimit](methodDetectionLimit.md)  <sub>OPT</sub>
    * Description: Detection limit for method used
    * range: [Double](types/Double.md)
 * [methodDetectionLimitUnits](methodDetectionLimitUnits.md)  <sub>OPT</sub>
    * Description: Units of detection limit for method used
    * range: [String](types/String.md)
 * [precision](precision.md)  <sub>OPT</sub>
    * Description: Closeness of agreement between indications or measured quantity values obtained by replicate measurements on the same or similar objects under specified conditions
    * range: [Double](types/Double.md)
 * [precisionUnits](precisionUnits.md)  <sub>OPT</sub>
    * Description: Units of reported precision
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
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
| **Mappings:** | | neon:sdg_externalLabSummaryData_in |

