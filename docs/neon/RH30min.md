
# Type: RH_30min




URI: [neon:RH30min](https://data.neonscience.org/RH30min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [RHAlphaQM](RHAlphaQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [RHBetaQM](RHBetaQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [RHConsistencyFailQM](RHConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHConsistencyNAQM](RHConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHConsistencyPassQM](RHConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHExpUncert](RHExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for relative humidity
    * range: [Double](types/Double.md)
 * [RHFinalQF](RHFinalQF.md)  <sub>OPT</sub>
    * Description: Relative humidity quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [RHFinalQFSciRvw](RHFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Relative humidity quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [RHGapFailQM](RHGapFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHGapNAQM](RHGapNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHGapPassQM](RHGapPassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHMaximum](RHMaximum.md)  <sub>OPT</sub>
    * Description: Maximum relative humidity
    * range: [Double](types/Double.md)
 * [RHMean](RHMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of relative humidity
    * range: [Double](types/Double.md)
 * [RHMinimum](RHMinimum.md)  <sub>OPT</sub>
    * Description: Minimum relative humidity
    * range: [Double](types/Double.md)
 * [RHNullFailQM](RHNullFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHNullNAQM](RHNullNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHNullPassQM](RHNullPassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHNumPts](RHNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of relative humidity
    * range: [Double](types/Double.md)
 * [RHPersistenceFailQM](RHPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHPersistenceNAQM](RHPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHPersistencePassQM](RHPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHRangeFailQM](RHRangeFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHRangeNAQM](RHRangeNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHRangePassQM](RHRangePassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHSensorErrorFailQM](RHSensorErrorFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the sensor error occurred over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHSensorErrorNAQM](RHSensorErrorNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the sensor error was unknown over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHSensorErrorPassQM](RHSensorErrorPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the sensor error was not occurred  over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHSpikeFailQM](RHSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHSpikeNAQM](RHSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHSpikePassQM](RHSpikePassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHStdErMean](RHStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for relative humidity
    * range: [Double](types/Double.md)
 * [RHStepFailQM](RHStepFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHStepNAQM](RHStepNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHStepPassQM](RHStepPassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHValidCalFailQM](RHValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHValidCalNAQM](RHValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHValidCalPassQM](RHValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHVariance](RHVariance.md)  <sub>OPT</sub>
    * Description: Variance in relative humidity
    * range: [Double](types/Double.md)
 * [dewTempAlphaQM](dewTempAlphaQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [dewTempBetaQM](dewTempBetaQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [dewTempConsistencyFailQM](dewTempConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempConsistencyNAQM](dewTempConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempConsistencyPassQM](dewTempConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempExpUncert](dewTempExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempFinalQF](dewTempFinalQF.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [dewTempFinalQFSciRvw](dewTempFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [dewTempGapFailQM](dewTempGapFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempGapNAQM](dewTempGapNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempGapPassQM](dewTempGapPassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempMaximum](dewTempMaximum.md)  <sub>OPT</sub>
    * Description: Maximum dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempMean](dewTempMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempMinimum](dewTempMinimum.md)  <sub>OPT</sub>
    * Description: Minimum dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempNullFailQM](dewTempNullFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempNullNAQM](dewTempNullNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempNullPassQM](dewTempNullPassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempNumPts](dewTempNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempPersistenceFailQM](dewTempPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempPersistenceNAQM](dewTempPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempPersistencePassQM](dewTempPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempRangeFailQM](dewTempRangeFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempRangeNAQM](dewTempRangeNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempRangePassQM](dewTempRangePassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempSpikeFailQM](dewTempSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempSpikeNAQM](dewTempSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempSpikePassQM](dewTempSpikePassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempStdErMean](dewTempStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempStepFailQM](dewTempStepFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempStepNAQM](dewTempStepNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempStepPassQM](dewTempStepPassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempValidCalFailQM](dewTempValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempValidCalNAQM](dewTempValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempValidCalPassQM](dewTempValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempVariance](dewTempVariance.md)  <sub>OPT</sub>
    * Description: Variance in dew or frost point temperature
    * range: [Double](types/Double.md)
 * [tempRHAlphaQM](tempRHAlphaQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [tempRHBetaQM](tempRHBetaQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [tempRHConsistencyFailQM](tempRHConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHConsistencyNAQM](tempRHConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHConsistencyPassQM](tempRHConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHExpUncert](tempRHExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHFinalQF](tempRHFinalQF.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [tempRHFinalQFSciRvw](tempRHFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [tempRHGapFailQM](tempRHGapFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHGapNAQM](tempRHGapNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHGapPassQM](tempRHGapPassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHMaximum](tempRHMaximum.md)  <sub>OPT</sub>
    * Description: Maximum temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHMean](tempRHMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHMinimum](tempRHMinimum.md)  <sub>OPT</sub>
    * Description: Minimum temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHNullFailQM](tempRHNullFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHNullNAQM](tempRHNullNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHNullPassQM](tempRHNullPassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHNumPts](tempRHNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHPersistenceFailQM](tempRHPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHPersistenceNAQM](tempRHPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHPersistencePassQM](tempRHPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHRangeFailQM](tempRHRangeFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHRangeNAQM](tempRHRangeNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHRangePassQM](tempRHRangePassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHSpikeFailQM](tempRHSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHSpikeNAQM](tempRHSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHSpikePassQM](tempRHSpikePassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHStdErMean](tempRHStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHStepFailQM](tempRHStepFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHStepNAQM](tempRHStepNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHStepPassQM](tempRHStepPassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHValidCalFailQM](tempRHValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHValidCalNAQM](tempRHValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHValidCalPassQM](tempRHValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHVariance](tempRHVariance.md)  <sub>OPT</sub>
    * Description: Variance in temperature measures by RH sensor
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
| **Mappings:** | | neon:RH_30min |

