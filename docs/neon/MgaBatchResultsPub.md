
# Type: mga_batchResults_pub




URI: [neon:MgaBatchResultsPub](https://data.neonscience.org/MgaBatchResultsPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MgaBatchResultsPub&#124;uid:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;dataQF:string%20%3F;batchID:string%20%3F;calCurveIntercept:double%20%3F;calCurveRsquared:double%20%3F;calCurveSlope:double%20%3F;linearDynamicRangeLower:double%20%3F;linearDynamicRangeUpper:double%20%3F;lodCqVar:double%20%3F;negControl1Result:string%20%3F;negControl2Result:string%20%3F;negControl3Result:string%20%3F;negControl4Result:string%20%3F;negControl5Result:string%20%3F;noTemplateControlCq:integer%20%3F;pcrEfficiency:double%20%3F;pcrEfficiencyConfInt:double%20%3F;standardDescription:string%20%3F])

## Attributes


### Own

 * [batchID](batchID.md)  <sub>OPT</sub>
    * Description: Identifier for batch or analytical run
    * range: [String](types/String.md)
 * [calCurveIntercept](calCurveIntercept.md)  <sub>OPT</sub>
    * Description: y-intercept of assay calibration curve for the quantification cycle versus log10 of the template concentration
    * range: [Double](types/Double.md)
 * [calCurveRsquared](calCurveRsquared.md)  <sub>OPT</sub>
    * Description: R-squared value for calibration curve
    * range: [Double](types/Double.md)
 * [calCurveSlope](calCurveSlope.md)  <sub>OPT</sub>
    * Description: Slope of assay calibration curve for the quantification cycle versus log10 of the template concentration
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [linearDynamicRangeLower](linearDynamicRangeLower.md)  <sub>OPT</sub>
    * Description: The lower range of gene copy number in which the threshold cycle versus the dilution factor fits a straight line on a base-10 semi-logarithmic graph
    * range: [Double](types/Double.md)
 * [linearDynamicRangeUpper](linearDynamicRangeUpper.md)  <sub>OPT</sub>
    * Description: The upper range of gene copy number in which the threshold cycle versus the dilution factor fits a straight line on a base-10 semi-logarithmic graph
    * range: [Double](types/Double.md)
 * [lodCqVar](lodCqVar.md)  <sub>OPT</sub>
    * Description: Variability in quantification cycle threshold at the limit of detection
    * range: [Double](types/Double.md)
 * [negControl1Result](negControl1Result.md)  <sub>OPT</sub>
    * Description: Result for negative control sample 1
    * range: [String](types/String.md)
 * [negControl2Result](negControl2Result.md)  <sub>OPT</sub>
    * Description: Result for negative control sample 2
    * range: [String](types/String.md)
 * [negControl3Result](negControl3Result.md)  <sub>OPT</sub>
    * Description: Result for negative control sample 3
    * range: [String](types/String.md)
 * [negControl4Result](negControl4Result.md)  <sub>OPT</sub>
    * Description: Result for negative control sample 4
    * range: [String](types/String.md)
 * [negControl5Result](negControl5Result.md)  <sub>OPT</sub>
    * Description: Result for negative control sample 5
    * range: [String](types/String.md)
 * [noTemplateControlCq](noTemplateControlCq.md)  <sub>OPT</sub>
    * Description: Quantification or threshold cycle number for no template control
    * range: [Integer](types/Integer.md)
 * [pcrEfficiency](pcrEfficiency.md)  <sub>OPT</sub>
    * Description: Efficiency of PCR reaction
    * range: [Double](types/Double.md)
 * [pcrEfficiencyConfInt](pcrEfficiencyConfInt.md)  <sub>OPT</sub>
    * Description: Confidence interval for PCR efficiency
    * range: [Double](types/Double.md)
 * [standardDescription](standardDescription.md)  <sub>OPT</sub>
    * Description: Description of assay standard used
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
| **Mappings:** | | neon:mga_batchResults_pub |

