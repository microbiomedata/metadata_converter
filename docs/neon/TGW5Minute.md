
# Type: TGW_5_minute




URI: [neon:TGW5Minute](https://data.neonscience.org/TGW5Minute)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [groundwaterTemp](groundwaterTemp.md)  <sub>OPT</sub>
    * Description: Temperature in groundwater
    * range: [Double](types/Double.md)
 * [groundwaterTempConsistencyQF](groundwaterTempConsistencyQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the consistency test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempGapQF](groundwaterTempGapQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the gap test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempNullQF](groundwaterTempNullQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the null test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempPersistenceQF](groundwaterTempPersistenceQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the persistence test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempRangeQF](groundwaterTempRangeQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the range test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempSpikeQF](groundwaterTempSpikeQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the spike test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempStepQF](groundwaterTempStepQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the step test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)

### Inherited from SCGW_5_minute:

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [groundwaterSpecCond](groundwaterSpecCond.md)  <sub>OPT</sub>
    * Description: Specific conductivity in groundwater in microsiemens per centimeter
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterSpecCondExpUncert](groundwaterSpecCondExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for Specific Conductivity in groundwater in degrees celsius
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterSpecCondRangeQF](groundwaterSpecCondRangeQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the range test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondPersistQF](groundwaterSpecCondPersistQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the persistence test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondStepQF](groundwaterSpecCondStepQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the step test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondNullQF](groundwaterSpecCondNullQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the null test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondGapQF](groundwaterSpecCondGapQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the gap test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondConsistQF](groundwaterSpecCondConsistQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the consistency test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondSpikeQF](groundwaterSpecCondSpikeQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the spike test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [validCalQF](validCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [sciRvwQF](sciRvwQF.md)  <sub>OPT</sub>
    * Description: Stand-alone quality flag (does not interact with final quality flag) indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)

### Inherited from TGW_30_minute:

 * [groundwaterTempExpUncert](groundwaterTempExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterTempMean](groundwaterTempMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterTempMinimum](groundwaterTempMinimum.md)  <sub>OPT</sub>
    * Description: Minimum temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterTempMaximum](groundwaterTempMaximum.md)  <sub>OPT</sub>
    * Description: Maximum temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterTempVariance](groundwaterTempVariance.md)  <sub>OPT</sub>
    * Description: Variance in temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterTempNumPts](groundwaterTempNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterTempStdErMean](groundwaterTempStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempRangeFailQM](gWatTempRangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempRangePassQM](gWatTempRangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempRangeNAQM](gWatTempRangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempPersistenceFailQM](gWatTempPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the persistence test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempPersistencePassQM](gWatTempPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempPersistenceNAQM](gWatTempPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempStepFailQM](gWatTempStepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempStepPassQM](gWatTempStepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempStepNAQM](gWatTempStepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempNullFailQM](gWatTempNullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempNullPassQM](gWatTempNullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempNullNAQM](gWatTempNullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempGapFailQM](gWatTempGapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempGapPassQM](gWatTempGapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempGapNAQM](gWatTempGapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempSpikeFailQM](gWatTempSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempSpikePassQM](gWatTempSpikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempSpikeNAQM](gWatTempSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempConsistencyFailQM](gWatTempConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempConsistencyPassQM](gWatTempConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for groundwater temperature over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempConsistencyNAQM](gWatTempConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for groundwater temperature could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempAlphaQM](gWatTempAlphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for groundwater temperature over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempBetaQM](gWatTempBetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for groundwater temperature over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatTempFinalQF](gWatTempFinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the groundwater temperature data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [gWatTempFinalQFSciRvw](gWatTempFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Groundwater temperature quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from TSD_1_min:

 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
 * [thermistorDepth](thermistorDepth.md)  <sub>OPT</sub>
    * Description: Depth of the temperature sensor (thermistor) from water surface in lakes and rivers
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tsdWaterTemp](tsdWaterTemp.md)  <sub>OPT</sub>
    * Description: Temperature of surface water at specific depths in lakes and rivers
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tsdWaterTempConsistQF](tsdWaterTempConsistQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the consistency test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempExpUncert](tsdWaterTempExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for tsdWaterTemp
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tsdWaterTempGapQF](tsdWaterTempGapQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the gap test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempNullQF](tsdWaterTempNullQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the null test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempRangeQF](tsdWaterTempRangeQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the range test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempSpikeQF](tsdWaterTempSpikeQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the spike test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempStepQF](tsdWaterTempStepQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the step test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempValidCalQF](tsdWaterTempValidCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:TGW_5_minute |
| **In Subsets:** | | DP1.20217.001 |

