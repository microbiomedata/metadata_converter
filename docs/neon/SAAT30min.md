
# Type: SAAT_30min




URI: [neon:SAAT30min](https://data.neonscience.org/SAAT30min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SAAT30min&#124;tempSingleMean:double%20%3F;tempSingleMinimum:double%20%3F;tempSingleMaximum:double%20%3F;tempSingleVariance:double%20%3F;tempSingleNumPts:double%20%3F;tempSingleExpUncert:double%20%3F;tempSingleStdErMean:double%20%3F;rangeFailQM:double%20%3F;rangePassQM:double%20%3F;rangeNAQM:double%20%3F;persistenceFailQM:double%20%3F;persistencePassQM:double%20%3F;persistenceNAQM:double%20%3F;stepFailQM:double%20%3F;stepPassQM:double%20%3F;stepNAQM:double%20%3F;nullFailQM:double%20%3F;nullPassQM:double%20%3F;nullNAQM:double%20%3F;gapFailQM:double%20%3F;gapPassQM:double%20%3F;gapNAQM:double%20%3F;spikeFailQM:double%20%3F;spikePassQM:double%20%3F;spikeNAQM:double%20%3F;consistencyFailQM:double%20%3F;consistencyPassQM:double%20%3F;consistencyNAQM:double%20%3F;flowFailQM:double%20%3F;flowPassQM:double%20%3F;flowNAQM:double%20%3F;heaterFailQM:double%20%3F;heaterPassQM:double%20%3F;heaterNAQM:double%20%3F;alphaQM:double%20%3F;betaQM:double%20%3F;finalQF:string%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;validCalFailQM:double%20%3F;validCalNAQM:double%20%3F;validCalPassQM:double%20%3F;finalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [alphaQM](alphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [betaQM](betaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [consistencyFailQM](consistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [consistencyNAQM](consistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [consistencyPassQM](consistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [finalQF](finalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [finalQFSciRvw](finalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [flowFailQM](flowFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the flow rate test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [flowNAQM](flowNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the flow rate test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [flowPassQM](flowPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the flow rate test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gapFailQM](gapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gapNAQM](gapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gapPassQM](gapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [heaterFailQM](heaterFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the heater was on over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [heaterNAQM](heaterNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the heater status was unknown over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [heaterPassQM](heaterPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the heater was off over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [nullFailQM](nullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [nullNAQM](nullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [nullPassQM](nullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [persistenceFailQM](persistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [persistenceNAQM](persistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [persistencePassQM](persistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [rangeFailQM](rangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [rangeNAQM](rangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [rangePassQM](rangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [spikeFailQM](spikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [spikeNAQM](spikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [spikePassQM](spikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
 * [stepFailQM](stepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [stepNAQM](stepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [stepPassQM](stepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempSingleExpUncert](tempSingleExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for single aspirated air temperature
    * range: [Double](types/Double.md)
 * [tempSingleMaximum](tempSingleMaximum.md)  <sub>OPT</sub>
    * Description: Maximum single aspirated air temperature
    * range: [Double](types/Double.md)
 * [tempSingleMean](tempSingleMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of single aspirated air temperature
    * range: [Double](types/Double.md)
 * [tempSingleMinimum](tempSingleMinimum.md)  <sub>OPT</sub>
    * Description: Minimum single aspirated air temperature
    * range: [Double](types/Double.md)
 * [tempSingleNumPts](tempSingleNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of single aspirated air temperature
    * range: [Double](types/Double.md)
 * [tempSingleStdErMean](tempSingleStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for single aspirated air temperature
    * range: [Double](types/Double.md)
 * [tempSingleVariance](tempSingleVariance.md)  <sub>OPT</sub>
    * Description: Variance in single aspirated air temperature
    * range: [Double](types/Double.md)
 * [validCalFailQM](validCalFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [validCalNAQM](validCalNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [validCalPassQM](validCalPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:SAAT_30min |

