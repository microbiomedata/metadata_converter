
# Type: sdrc_sampledParameters_pub




URI: [neon:SdrcSampledParametersPub](https://data.neonscience.org/SdrcSampledParametersPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SdrcSampledParametersPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;curveID:string%20%3F;controlNumber:integer%20%3F;spagActivationStage:double%20%3F;spagCoefficient:double%20%3F;spagExponent:double%20%3F;spagGamma1:double%20%3F;spagGamma2:double%20%3F;spagLogPost:double%20%3F;spagZeroFlowOffset:double%20%3F;curveEndDate:time%20%3F;curveStartDate:time%20%3F;parameterNumber:integer%20%3F])

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
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [parameterNumber](parameterNumber.md)  <sub>OPT</sub>
    * Description: Numeric designation for the set of sampled parameters
    * range: [Integer](types/Integer.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [spagActivationStage](spagActivationStage.md)  <sub>OPT</sub>
    * Description: Activation stage for a control for a spaghetti (k in equations)
    * range: [Double](types/Double.md)
 * [spagCoefficient](spagCoefficient.md)  <sub>OPT</sub>
    * Description: Coefficient for a control for a spaghetti (a in equations)
    * range: [Double](types/Double.md)
 * [spagExponent](spagExponent.md)  <sub>OPT</sub>
    * Description: Exponent for a control for a spaghetti (c in equations)
    * range: [Double](types/Double.md)
 * [spagGamma1](spagGamma1.md)  <sub>OPT</sub>
    * Description: Gamma1 for remnant error of a rating curve for a spaghetti (intercept in equations)
    * range: [Double](types/Double.md)
 * [spagGamma2](spagGamma2.md)  <sub>OPT</sub>
    * Description: Gamma2 for remnant error of a rating curve for a spaghetti (slope in equations)
    * range: [Double](types/Double.md)
 * [spagLogPost](spagLogPost.md)  <sub>OPT</sub>
    * Description: Posterior probability estimate of spaghetti
    * range: [Double](types/Double.md)
 * [spagZeroFlowOffset](spagZeroFlowOffset.md)  <sub>OPT</sub>
    * Description: Zero flow offset for a rating curve for a spaghetti (b in equations)
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sdrc_sampledParameters_pub |

