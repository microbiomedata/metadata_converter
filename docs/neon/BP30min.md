
# Type: BP_30min




URI: [neon:BP30min](https://data.neonscience.org/BP30min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [corPres](corPres.md)  <sub>OPT</sub>
    * Description: Mean station pressure corrected to sea level
    * range: [Double](types/Double.md)
 * [corPresDewPtQF](corPresDewPtQF.md)  <sub>OPT</sub>
    * Description: Corrected pressure quality flag that assesses whether dew point measurements for correcting pressure were available (0=yes, 1=no)
    * range: [String](types/String.md)
 * [corPresExpUncert](corPresExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for pressure corrected to sea level
    * range: [Double](types/Double.md)
 * [corPresFinalQF](corPresFinalQF.md)  <sub>OPT</sub>
    * Description: Pressure corrected to sea level quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.000653 and NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [corPresFinalQFSciRvw](corPresFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Pressure corrected to sea level quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [corPresTempQF](corPresTempQF.md)  <sub>OPT</sub>
    * Description: Corrected pressure quality flag that assesses whether temperature measurements for correcting pressure were available (0=yes, 1=no)
    * range: [String](types/String.md)
 * [staPresAlphaQM](staPresAlphaQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [staPresBetaQM](staPresBetaQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [staPresConsistencyFailQM](staPresConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresConsistencyNAQM](staPresConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresConsistencyPassQM](staPresConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresExpUncert](staPresExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for station pressure
    * range: [Double](types/Double.md)
 * [staPresFinalQF](staPresFinalQF.md)  <sub>OPT</sub>
    * Description: Station pressure quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [staPresFinalQFSciRvw](staPresFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Station pressure quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [staPresGapFailQM](staPresGapFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresGapNAQM](staPresGapNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresGapPassQM](staPresGapPassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresMaximum](staPresMaximum.md)  <sub>OPT</sub>
    * Description: Maximum station pressure
    * range: [Double](types/Double.md)
 * [staPresMean](staPresMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of station pressure
    * range: [Double](types/Double.md)
 * [staPresMinimum](staPresMinimum.md)  <sub>OPT</sub>
    * Description: Minimum station pressure
    * range: [Double](types/Double.md)
 * [staPresNullFailQM](staPresNullFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresNullNAQM](staPresNullNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresNullPassQM](staPresNullPassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresNumPts](staPresNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of station pressure
    * range: [Double](types/Double.md)
 * [staPresPersistenceFailQM](staPresPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresPersistenceNAQM](staPresPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresPersistencePassQM](staPresPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresRangeFailQM](staPresRangeFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresRangeNAQM](staPresRangeNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresRangePassQM](staPresRangePassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresSpikeFailQM](staPresSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresSpikeNAQM](staPresSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresSpikePassQM](staPresSpikePassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresStdErMean](staPresStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for station pressure
    * range: [Double](types/Double.md)
 * [staPresStepFailQM](staPresStepFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresStepNAQM](staPresStepNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresStepPassQM](staPresStepPassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresValidCalFailQM](staPresValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresValidCalNAQM](staPresValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresValidCalPassQM](staPresValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresVariance](staPresVariance.md)  <sub>OPT</sub>
    * Description: Variance in station pressure
    * range: [Double](types/Double.md)

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
    * inherited from: None
 * [sciRvwQF](sciRvwQF.md)  <sub>OPT</sub>
    * Description: Stand-alone quality flag (does not interact with final quality flag) indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
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
| **Mappings:** | | neon:BP_30min |

