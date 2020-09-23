
# Type: TSD_30_min




URI: [neon:TSD30Min](https://data.neonscience.org/TSD30Min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TSD30Min&#124;startDateTime:time%20%3F;endDateTime:time%20%3F;thermistorDepth:double%20%3F;tsdWaterTempAlphaQM:double%20%3F;tsdWaterTempBetaQM:double%20%3F;tsdWaterTempConsistencyFailQM:double%20%3F;tsdWaterTempConsistencyNAQM:double%20%3F;tsdWaterTempConsistencyPassQM:double%20%3F;tsdWaterTempExpUncert:double%20%3F;tsdWaterTempFinalQF:string%20%3F;tsdWaterTempGapFailQM:double%20%3F;tsdWaterTempGapNAQM:double%20%3F;tsdWaterTempGapPassQM:double%20%3F;tsdWaterTempMaximum:double%20%3F;tsdWaterTempMean:double%20%3F;tsdWaterTempMinimum:double%20%3F;tsdWaterTempNullFailQM:double%20%3F;tsdWaterTempNullNAQM:double%20%3F;tsdWaterTempNullPassQM:double%20%3F;tsdWaterTempNumPts:string%20%3F;tsdWaterTempRangeFailQM:double%20%3F;tsdWaterTempRangeNAQM:double%20%3F;tsdWaterTempRangePassQM:double%20%3F;tsdWaterTempSpikeFailQM:double%20%3F;tsdWaterTempSpikeNAQM:double%20%3F;tsdWaterTempSpikePassQM:double%20%3F;tsdWaterTempStdErMean:double%20%3F;tsdWaterTempStepFailQM:double%20%3F;tsdWaterTempStepNAQM:double%20%3F;tsdWaterTempStepPassQM:double%20%3F;tsdWaterTempValidCalFailQM:double%20%3F;tsdWaterTempValidCalNAQM:double%20%3F;tsdWaterTempValidCalPassQM:double%20%3F;tsdWaterTempVariance:double%20%3F;tsdWaterTempFinalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
 * [thermistorDepth](thermistorDepth.md)  <sub>OPT</sub>
    * Description: Depth of the temperature sensor (thermistor) from water surface in lakes and rivers
    * range: [Double](types/Double.md)
 * [tsdWaterTempAlphaQM](tsdWaterTempAlphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp detailing the outcomes of the alpha quality flag over the averaging period as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [tsdWaterTempBetaQM](tsdWaterTempBetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp detailing the outcomes of the beta quality flag over the averaging period as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [tsdWaterTempConsistencyFailQM](tsdWaterTempConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the failed outcomes of the consistency test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempConsistencyNAQM](tsdWaterTempConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes when the consistency test could not be run over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempConsistencyPassQM](tsdWaterTempConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the passed outcomes of the consistency test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempExpUncert](tsdWaterTempExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for tsdWaterTemp
    * range: [Double](types/Double.md)
 * [tsdWaterTempFinalQF](tsdWaterTempFinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether for tsdWaterTemp has passed or failed an overall assessment of its quality detailed in NEON.DOC.001113 (1=fail 0=pass)
    * range: [String](types/String.md)
 * [tsdWaterTempFinalQFSciRvw](tsdWaterTempFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether for tsdWaterTemp has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [tsdWaterTempGapFailQM](tsdWaterTempGapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the failed outcomes of the gap test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempGapNAQM](tsdWaterTempGapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes when the gap test could not be run over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempGapPassQM](tsdWaterTempGapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the passed outcomes of the gap test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempMaximum](tsdWaterTempMaximum.md)  <sub>OPT</sub>
    * Description: Maximum temperature of tsdWaterTemp
    * range: [Double](types/Double.md)
 * [tsdWaterTempMean](tsdWaterTempMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of tsdWaterTemp
    * range: [Double](types/Double.md)
 * [tsdWaterTempMinimum](tsdWaterTempMinimum.md)  <sub>OPT</sub>
    * Description: Minimum temperature of tsdWaterTemp
    * range: [Double](types/Double.md)
 * [tsdWaterTempNullFailQM](tsdWaterTempNullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the failed outcomes of the null test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempNullNAQM](tsdWaterTempNullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes when the null test could not be run over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempNullPassQM](tsdWaterTempNullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the passed outcomes of the null test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempNumPts](tsdWaterTempNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of tsdWaterTemp
    * range: [String](types/String.md)
 * [tsdWaterTempRangeFailQM](tsdWaterTempRangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the failed outcomes of the range test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempRangeNAQM](tsdWaterTempRangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes when the range test could not be run over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempRangePassQM](tsdWaterTempRangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the passed outcomes of the range test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempSpikeFailQM](tsdWaterTempSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the failed outcomes of the spike test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempSpikeNAQM](tsdWaterTempSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes when the spike test could not be run over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempSpikePassQM](tsdWaterTempSpikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the passed outcomes of the spike test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempStdErMean](tsdWaterTempStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for tsdWaterTemp
    * range: [Double](types/Double.md)
 * [tsdWaterTempStepFailQM](tsdWaterTempStepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the failed outcomes of the step test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempStepNAQM](tsdWaterTempStepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes when the step test could not be run over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempStepPassQM](tsdWaterTempStepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the passed outcomes of the step test over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempValidCalFailQM](tsdWaterTempValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the failed outcomes of the valid calibration check over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempValidCalNAQM](tsdWaterTempValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes when the valid calibration check could not be run over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempValidCalPassQM](tsdWaterTempValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric for tsdWaterTemp that summarizes the passed outcomes of the valid calibration check over the averaging period as a percent
    * range: [Double](types/Double.md)
 * [tsdWaterTempVariance](tsdWaterTempVariance.md)  <sub>OPT</sub>
    * Description: Variance in temperature of tsdWaterTemp
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:TSD_30_min |
| **In Subsets:** | | DP1.20264.001 |

