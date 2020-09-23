
# Type: cfc_chlorophyllParameters_pub




URI: [neon:CfcChlorophyllParametersPub](https://data.neonscience.org/CfcChlorophyllParametersPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[CfcChlorophyllParametersPub&#124;uid:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;analyte:string%20%3F;labSpecificStartDate:time%20%3F;labSpecificEndDate:time%20%3F;testMethod:string%20%3F;dataQF:string%20%3F;chlCarotEquationInput:string%20%3F;chlCarotExtinctionCoefficient:double%20%3F;ecReference:string%20%3F])

## Attributes


### Own

 * [analyte](analyte.md)  <sub>OPT</sub>
    * Description: Analyte or parameter measured
    * range: [String](types/String.md)
 * [chlCarotEquationInput](chlCarotEquationInput.md)  <sub>OPT</sub>
    * Description: Equation input for calculating chlorophyll or carotenoid content
    * range: [String](types/String.md)
 * [chlCarotExtinctionCoefficient](chlCarotExtinctionCoefficient.md)  <sub>OPT</sub>
    * Description: Parameter used for calculating chlorophyll or carotenoid content
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [ecReference](ecReference.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) for the extinction coefficients
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
| **Mappings:** | | neon:cfc_chlorophyllParameters_pub |

