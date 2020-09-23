
# Type: TGW_30_minute




URI: [neon:TGW30Minute](https://data.neonscience.org/TGW30Minute)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TGW30Minute&#124;startDateTime:time%20%3F;endDateTime:time%20%3F;groundwaterTempExpUncert:double%20%3F;groundwaterTempMean:double%20%3F;groundwaterTempMinimum:double%20%3F;groundwaterTempMaximum:double%20%3F;groundwaterTempVariance:double%20%3F;groundwaterTempNumPts:double%20%3F;groundwaterTempStdErMean:double%20%3F;gWatTempRangeFailQM:double%20%3F;gWatTempRangePassQM:double%20%3F;gWatTempRangeNAQM:double%20%3F;gWatTempPersistenceFailQM:double%20%3F;gWatTempPersistencePassQM:double%20%3F;gWatTempPersistenceNAQM:double%20%3F;gWatTempStepFailQM:double%20%3F;gWatTempStepPassQM:double%20%3F;gWatTempStepNAQM:double%20%3F;gWatTempNullFailQM:double%20%3F;gWatTempNullPassQM:double%20%3F;gWatTempNullNAQM:double%20%3F;gWatTempGapFailQM:double%20%3F;gWatTempGapPassQM:double%20%3F;gWatTempGapNAQM:double%20%3F;gWatTempSpikeFailQM:double%20%3F;gWatTempSpikePassQM:double%20%3F;gWatTempSpikeNAQM:double%20%3F;gWatTempConsistencyFailQM:double%20%3F;gWatTempConsistencyPassQM:double%20%3F;gWatTempConsistencyNAQM:double%20%3F;gWatTempAlphaQM:double%20%3F;gWatTempBetaQM:double%20%3F;gWatTempFinalQF:string%20%3F;validCalFailQM:double%20%3F;validCalNAQM:double%20%3F;validCalPassQM:double%20%3F;gWatTempFinalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [gWatTempAlphaQM](gWatTempAlphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for groundwater temperature over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [gWatTempBetaQM](gWatTempBetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for groundwater temperature over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [gWatTempConsistencyFailQM](gWatTempConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempConsistencyNAQM](gWatTempConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempConsistencyPassQM](gWatTempConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempFinalQF](gWatTempFinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the groundwater temperature data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [gWatTempFinalQFSciRvw](gWatTempFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Groundwater temperature quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [gWatTempGapFailQM](gWatTempGapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempGapNAQM](gWatTempGapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempGapPassQM](gWatTempGapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempNullFailQM](gWatTempNullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempNullNAQM](gWatTempNullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempNullPassQM](gWatTempNullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempPersistenceFailQM](gWatTempPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the persistence test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempPersistenceNAQM](gWatTempPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempPersistencePassQM](gWatTempPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempRangeFailQM](gWatTempRangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempRangeNAQM](gWatTempRangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempRangePassQM](gWatTempRangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempSpikeFailQM](gWatTempSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempSpikeNAQM](gWatTempSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempSpikePassQM](gWatTempSpikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempStepFailQM](gWatTempStepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempStepNAQM](gWatTempStepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gWatTempStepPassQM](gWatTempStepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [groundwaterTempExpUncert](groundwaterTempExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterTempMaximum](groundwaterTempMaximum.md)  <sub>OPT</sub>
    * Description: Maximum temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterTempMean](groundwaterTempMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterTempMinimum](groundwaterTempMinimum.md)  <sub>OPT</sub>
    * Description: Minimum temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterTempNumPts](groundwaterTempNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterTempStdErMean](groundwaterTempStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterTempVariance](groundwaterTempVariance.md)  <sub>OPT</sub>
    * Description: Variance in temperature of groundwater in degrees celsius
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
| **Mappings:** | | neon:TGW_30_minute |

