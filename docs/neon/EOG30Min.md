
# Type: EOG_30_min




URI: [neon:EOG30Min](https://data.neonscience.org/EOG30Min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[EOG30Min&#124;startDateTime:time%20%3F;endDateTime:time%20%3F;groundwaterElevExpUncert:double%20%3F;groundwaterElevMean:double%20%3F;groundwaterElevMinimum:double%20%3F;groundwaterElevMaximum:double%20%3F;groundwaterElevVariance:double%20%3F;groundwaterElevNumPts:double%20%3F;groundwaterElevStdErMean:double%20%3F;gWatElevRangeFailQM:double%20%3F;gWatElevRangePassQM:double%20%3F;gWatElevRangeNAQM:double%20%3F;gWatElevPersistenceFailQM:double%20%3F;gWatElevPersistencePassQM:double%20%3F;gWatElevPersistenceNAQM:double%20%3F;gWatElevStepFailQM:double%20%3F;gWatElevStepPassQM:double%20%3F;gWatElevStepNAQM:double%20%3F;gWatElevNullFailQM:double%20%3F;gWatElevNullPassQM:double%20%3F;gWatElevNullNAQM:double%20%3F;gWatElevGapFailQM:double%20%3F;gWatElevGapPassQM:double%20%3F;gWatElevGapNAQM:double%20%3F;gWatElevSpikeFailQM:double%20%3F;gWatElevSpikePassQM:double%20%3F;gWatElevSpikeNAQM:double%20%3F;gWatElevConsistencyFailQM:double%20%3F;gWatElevConsistencyPassQM:double%20%3F;gWatElevConsistencyNAQM:double%20%3F;gWatElevAlphaQM:double%20%3F;gWatElevBetaQM:double%20%3F;gWatElevFinalQF:string%20%3F;validCalFailQM:double%20%3F;validCalNAQM:double%20%3F;validCalPassQM:double%20%3F;gWatElevFinalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [gWatElevAlphaQM](gWatElevAlphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for groundwater elevation over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [gWatElevBetaQM](gWatElevBetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for groundwater elevation over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [gWatElevConsistencyFailQM](gWatElevConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevConsistencyNAQM](gWatElevConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevConsistencyPassQM](gWatElevConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevFinalQF](gWatElevFinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether groundwater elevation data has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [gWatElevFinalQFSciRvw](gWatElevFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Groundwater elevation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [gWatElevGapFailQM](gWatElevGapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevGapNAQM](gWatElevGapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevGapPassQM](gWatElevGapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevNullFailQM](gWatElevNullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevNullNAQM](gWatElevNullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevNullPassQM](gWatElevNullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevPersistenceFailQM](gWatElevPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the persistence test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevPersistenceNAQM](gWatElevPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevPersistencePassQM](gWatElevPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevRangeFailQM](gWatElevRangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevRangeNAQM](gWatElevRangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevRangePassQM](gWatElevRangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevSpikeFailQM](gWatElevSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevSpikeNAQM](gWatElevSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevSpikePassQM](gWatElevSpikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevStepFailQM](gWatElevStepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevStepNAQM](gWatElevStepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatElevStepPassQM](gWatElevStepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [groundwaterElevExpUncert](groundwaterElevExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for elevation of groundwater
    * range: [Double](types/Double.md)
 * [groundwaterElevMaximum](groundwaterElevMaximum.md)  <sub>OPT</sub>
    * Description: Maximum elevation of groundwater
    * range: [Double](types/Double.md)
 * [groundwaterElevMean](groundwaterElevMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of elevation of groundwater
    * range: [Double](types/Double.md)
 * [groundwaterElevMinimum](groundwaterElevMinimum.md)  <sub>OPT</sub>
    * Description: Minimum elevation of groundwater
    * range: [Double](types/Double.md)
 * [groundwaterElevNumPts](groundwaterElevNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of elevation of groundwater
    * range: [Double](types/Double.md)
 * [groundwaterElevStdErMean](groundwaterElevStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for elevation of groundwater
    * range: [Double](types/Double.md)
 * [groundwaterElevVariance](groundwaterElevVariance.md)  <sub>OPT</sub>
    * Description: Variance in elevation of groundwater
    * range: [Double](types/Double.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
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
| **Mappings:** | | neon:EOG_30_min |

