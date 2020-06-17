
# Type: EOG_5_min




URI: [neon:EOG5Min](https://data.neonscience.org/EOG5Min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [groundwaterElev](groundwaterElev.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater
    * range: [Double](types/Double.md)
 * [groundwaterElevConsistQF](groundwaterElevConsistQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the consistency test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevGapQF](groundwaterElevGapQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the gap test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevNullQF](groundwaterElevNullQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the null test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevPersistQF](groundwaterElevPersistQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the persistence test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevRangeQF](groundwaterElevRangeQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the range test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevSpikeQF](groundwaterElevSpikeQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the spike test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevStepQF](groundwaterElevStepQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the step test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)

### Inherited from EOG_30_min:

 * [groundwaterElevExpUncert](groundwaterElevExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for elevation of groundwater
    * range: [Double](types/Double.md)
 * [groundwaterElevMean](groundwaterElevMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of elevation of groundwater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterElevMinimum](groundwaterElevMinimum.md)  <sub>OPT</sub>
    * Description: Minimum elevation of groundwater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterElevMaximum](groundwaterElevMaximum.md)  <sub>OPT</sub>
    * Description: Maximum elevation of groundwater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterElevVariance](groundwaterElevVariance.md)  <sub>OPT</sub>
    * Description: Variance in elevation of groundwater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterElevNumPts](groundwaterElevNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of elevation of groundwater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterElevStdErMean](groundwaterElevStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for elevation of groundwater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevRangeFailQM](gWatElevRangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevRangePassQM](gWatElevRangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevRangeNAQM](gWatElevRangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevPersistenceFailQM](gWatElevPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the persistence test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevPersistencePassQM](gWatElevPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevPersistenceNAQM](gWatElevPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevStepFailQM](gWatElevStepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevStepPassQM](gWatElevStepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevStepNAQM](gWatElevStepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevNullFailQM](gWatElevNullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevNullPassQM](gWatElevNullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevNullNAQM](gWatElevNullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevGapFailQM](gWatElevGapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevGapPassQM](gWatElevGapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevGapNAQM](gWatElevGapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevSpikeFailQM](gWatElevSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevSpikePassQM](gWatElevSpikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevSpikeNAQM](gWatElevSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevConsistencyFailQM](gWatElevConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevConsistencyPassQM](gWatElevConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for groundwater elevation over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevConsistencyNAQM](gWatElevConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for groundwater elevation could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevAlphaQM](gWatElevAlphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for groundwater elevation over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevBetaQM](gWatElevBetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for groundwater elevation over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gWatElevFinalQF](gWatElevFinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether groundwater elevation data has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [gWatElevFinalQFSciRvw](gWatElevFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Groundwater elevation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None

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
| **Mappings:** | | neon:EOG_5_min |
| **In Subsets:** | | DP1.20100.001 |

