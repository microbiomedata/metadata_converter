
# Type: sdrc_posteriorParameters_pub




URI: [neon:SdrcPosteriorParametersPub](https://data.neonscience.org/SdrcPosteriorParametersPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SdrcPosteriorParametersPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;curveID:string%20%3F;controlNumber:integer%20%3F;maxPostActivationStage:double%20%3F;maxPostCoefficient:double%20%3F;maxPostExponent:double%20%3F;maxPostGamma1:double%20%3F;maxPostGamma2:double%20%3F;maxPostZeroFlowOffset:double%20%3F;stdDevActivationStage:double%20%3F;stdDevCoefficient:double%20%3F;stdDevExponent:double%20%3F;stdDevGamma1:double%20%3F;stdDevGamma2:double%20%3F;stdDevZeroFlowOffset:double%20%3F;curveEndDate:time%20%3F;curveStartDate:time%20%3F])

## Attributes


### Own

 * [controlNumber](controlNumber.md)  <sub>OPT</sub>
    * Description: Numeric designation for the control number
    * range: [Integer](types/Integer.md)
 * [curveEndDate](curveEndDate.md)  <sub>OPT</sub>
    * Description: End date for the curve
    * range: [Time](types/Time.md)
 * [curveID](curveID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the curve fit to gauge and discharge measurements
    * range: [String](types/String.md)
 * [curveStartDate](curveStartDate.md)  <sub>OPT</sub>
    * Description: Start date for the curve
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [maxPostActivationStage](maxPostActivationStage.md)  <sub>OPT</sub>
    * Description: Maximum posterior probability estimate of activation stage for a control (k in equations)
    * range: [Double](types/Double.md)
 * [maxPostCoefficient](maxPostCoefficient.md)  <sub>OPT</sub>
    * Description: Maximum posterior probability estimate of coefficient for a control (a in equations)
    * range: [Double](types/Double.md)
 * [maxPostExponent](maxPostExponent.md)  <sub>OPT</sub>
    * Description: Maximum posterior probability estimate of exponent for a control (c in equations)
    * range: [Double](types/Double.md)
 * [maxPostGamma1](maxPostGamma1.md)  <sub>OPT</sub>
    * Description: Maximum posterior probability estimate of gamma1 for remnant error of a rating curve (intercept in equations)
    * range: [Double](types/Double.md)
 * [maxPostGamma2](maxPostGamma2.md)  <sub>OPT</sub>
    * Description: Maximum posterior probability estimate of gamma2 for remnant error of a rating curve (slope in equations)
    * range: [Double](types/Double.md)
 * [maxPostZeroFlowOffset](maxPostZeroFlowOffset.md)  <sub>OPT</sub>
    * Description: Maximum posterior probability estimate of zero flow offset for a rating curve (b in equations)
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stdDevActivationStage](stdDevActivationStage.md)  <sub>OPT</sub>
    * Description: Standard deviation of maximum posterior probability estimate of activation stage for a control (k in equations)
    * range: [Double](types/Double.md)
 * [stdDevCoefficient](stdDevCoefficient.md)  <sub>OPT</sub>
    * Description: Standard deviation of maximum posterior probability estimate of coefficient for a control (a in equations)
    * range: [Double](types/Double.md)
 * [stdDevExponent](stdDevExponent.md)  <sub>OPT</sub>
    * Description: Standard deviation of maximum posterior probability estimate of exponent for a control (c in equations)
    * range: [Double](types/Double.md)
 * [stdDevGamma1](stdDevGamma1.md)  <sub>OPT</sub>
    * Description: Standard deviation of maximum posterior probability estimate of gamma1 for remnant error of a rating curve (intercept in equations)
    * range: [Double](types/Double.md)
 * [stdDevGamma2](stdDevGamma2.md)  <sub>OPT</sub>
    * Description: Standard deviation of maximum posterior probability estimate of gamma2 for remnant error of a rating curve (slope in equations)
    * range: [Double](types/Double.md)
 * [stdDevZeroFlowOffset](stdDevZeroFlowOffset.md)  <sub>OPT</sub>
    * Description: Standard deviation of maximum posterior probability estimate of zero flow offset for a rating curve (b in equations)
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sdrc_posteriorParameters_pub |

