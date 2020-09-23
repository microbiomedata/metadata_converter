
# Type: SCGW_30_minute




URI: [neon:SCGW30Minute](https://data.neonscience.org/SCGW30Minute)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SCGW30Minute&#124;startDateTime:time%20%3F;endDateTime:time%20%3F;groundwaterSpecCondExpUncert:double%20%3F;groundwaterSpecCondMean:double%20%3F;groundwaterSpecCondMinimum:double%20%3F;groundwaterSpecCondMaximum:double%20%3F;groundwaterSpecCondVariance:double%20%3F;groundwaterSpecCondNumPts:double%20%3F;groundwaterSpecCondStdErMean:double%20%3F;gWatSCondRangeFailQM:double%20%3F;gWatSCondRangePassQM:double%20%3F;gWatSCondRangeNAQM:double%20%3F;gWatSCondPersistenceFailQM:double%20%3F;gWatSCondPersistencePassQM:double%20%3F;gWatSCondPersistenceNAQM:double%20%3F;gWatSCondStepFailQM:double%20%3F;gWatSCondStepPassQM:double%20%3F;gWatSCondStepNAQM:double%20%3F;gWatSCondNullFailQM:double%20%3F;gWatSCondNullPassQM:double%20%3F;gWatSCondNullNAQM:double%20%3F;gWatSCondGapFailQM:double%20%3F;gWatSCondGapPassQM:double%20%3F;gWatSCondGapNAQM:double%20%3F;gWatSCondSpikeFailQM:double%20%3F;gWatSCondSpikePassQM:double%20%3F;gWatSCondSpikeNAQM:double%20%3F;gWatSCondConsistencyFailQM:double%20%3F;gWatSCondConsistencyPassQM:double%20%3F;gWatSCondConsistencyNAQM:double%20%3F;gWatSCondAlphaQM:double%20%3F;gWatSCondBetaQM:double%20%3F;gWatSCondFinalQF:string%20%3F;validCalFailQM:double%20%3F;validCalNAQM:double%20%3F;validCalPassQM:double%20%3F;gWatSCondFinalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [gWatSCondAlphaQM](gWatSCondAlphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for groundwater specific conductivity over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [gWatSCondBetaQM](gWatSCondBetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for groundwater specific conductivity over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [gWatSCondConsistencyFailQM](gWatSCondConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondConsistencyNAQM](gWatSCondConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for groundwater specific conductivity could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondConsistencyPassQM](gWatSCondConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondFinalQF](gWatSCondFinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether groundwater specific conductivity data has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [gWatSCondFinalQFSciRvw](gWatSCondFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Groundwater specific conductivity quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [gWatSCondGapFailQM](gWatSCondGapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondGapNAQM](gWatSCondGapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for groundwater specific conductivity could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondGapPassQM](gWatSCondGapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondNullFailQM](gWatSCondNullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondNullNAQM](gWatSCondNullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for groundwater specific conductivity could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondNullPassQM](gWatSCondNullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondPersistenceFailQM](gWatSCondPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the persistence test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondPersistenceNAQM](gWatSCondPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for groundwater specific conductivity could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondPersistencePassQM](gWatSCondPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondRangeFailQM](gWatSCondRangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondRangeNAQM](gWatSCondRangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for groundwater specific conductivity could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondRangePassQM](gWatSCondRangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondSpikeFailQM](gWatSCondSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondSpikeNAQM](gWatSCondSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for groundwater specific conductivity could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondSpikePassQM](gWatSCondSpikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondStepFailQM](gWatSCondStepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondStepNAQM](gWatSCondStepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for groundwater specific conductivity could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatSCondStepPassQM](gWatSCondStepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for groundwater specific conductivity over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [groundwaterSpecCondExpUncert](groundwaterSpecCondExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for Specific Conductivity in groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterSpecCondMaximum](groundwaterSpecCondMaximum.md)  <sub>OPT</sub>
    * Description: Maximum Specific Conductivity in groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterSpecCondMean](groundwaterSpecCondMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of Specific Conductivity in groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterSpecCondMinimum](groundwaterSpecCondMinimum.md)  <sub>OPT</sub>
    * Description: Minimum Specific Conductivity in groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterSpecCondNumPts](groundwaterSpecCondNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of Specific Conductivity in groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterSpecCondStdErMean](groundwaterSpecCondStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for Specific Conductivity in groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterSpecCondVariance](groundwaterSpecCondVariance.md)  <sub>OPT</sub>
    * Description: Variance in Specific Conductivity in groundwater in degrees celsius
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
| **Mappings:** | | neon:SCGW_30_minute |
| **In Subsets:** | | DP1.20015.001 |

