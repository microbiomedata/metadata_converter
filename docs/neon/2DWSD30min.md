
# Type: 2DWSD_30min




URI: [neon:2DWSD30min](https://data.neonscience.org/2DWSD30min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[2DWSD30min&#124;windSpeedMean:double%20%3F;windSpeedMinimum:double%20%3F;windSpeedMaximum:double%20%3F;windSpeedVariance:double%20%3F;windSpeedNumPts:double%20%3F;windSpeedExpUncert:double%20%3F;windSpeedStdErMean:double%20%3F;windSpeedRangeFailQM:double%20%3F;windSpeedRangePassQM:double%20%3F;windSpeedRangeNAQM:double%20%3F;windSpeedPersistenceFailQM:double%20%3F;windSpeedPersistencePassQM:double%20%3F;windSpeedPersistenceNAQM:double%20%3F;windSpeedStepFailQM:double%20%3F;windSpeedStepPassQM:double%20%3F;windSpeedStepNAQM:double%20%3F;windSpeedNullFailQM:double%20%3F;windSpeedNullPassQM:double%20%3F;windSpeedNullNAQM:double%20%3F;windSpeedGapFailQM:double%20%3F;windSpeedGapPassQM:double%20%3F;windSpeedGapNAQM:double%20%3F;windSpeedSpikeFailQM:double%20%3F;windSpeedSpikePassQM:double%20%3F;windSpeedSpikeNAQM:double%20%3F;windSpeedConsistencyFailQM:double%20%3F;windSpeedConsistencyPassQM:double%20%3F;windSpeedConsistencyNAQM:double%20%3F;windSpeedAlphaQM:double%20%3F;windSpeedBetaQM:double%20%3F;windSpeedFinalQF:string%20%3F;windDirMean:double%20%3F;windDirVariance:double%20%3F;windDirNumPts:double%20%3F;windDirExpUncert:double%20%3F;windDirStdErMean:double%20%3F;windDirRangeFailQM:double%20%3F;windDirRangePassQM:double%20%3F;windDirRangeNAQM:double%20%3F;windDirPersistenceFailQM:double%20%3F;windDirPersistencePassQM:double%20%3F;windDirPersistenceNAQM:double%20%3F;windDirStepFailQM:double%20%3F;windDirStepPassQM:double%20%3F;windDirStepNAQM:double%20%3F;windDirNullFailQM:double%20%3F;windDirNullPassQM:double%20%3F;windDirNullNAQM:double%20%3F;windDirGapFailQM:double%20%3F;windDirGapPassQM:double%20%3F;windDirGapNAQM:double%20%3F;windDirSpikeFailQM:double%20%3F;windDirSpikePassQM:double%20%3F;windDirSpikeNAQM:double%20%3F;windDirConsistencyFailQM:double%20%3F;windDirConsistencyPassQM:double%20%3F;windDirConsistencyNAQM:double%20%3F;windDirAlphaQM:double%20%3F;windDirBetaQM:double%20%3F;windDirFinalQF:string%20%3F;windDirDistortedFlowFailQM:double%20%3F;windDirDistortedFlowPassQM:double%20%3F;windDirDistortedFlowNAQM:double%20%3F;windSpeedSensorErrorFailQM:double%20%3F;windSpeedSensorErrorPassQM:double%20%3F;windSpeedSensorErrorNAQM:double%20%3F;windSpeedCalmWindQF:integer%20%3F;windDirSensorErrorFailQM:double%20%3F;windDirSensorErrorPassQM:double%20%3F;windDirSensorErrorNAQM:double%20%3F;windDirCalmWindQF:integer%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;windDirValidCalFailQM:double%20%3F;windDirValidCalNAQM:double%20%3F;windDirValidCalPassQM:double%20%3F;windSpeedValidCalFailQM:double%20%3F;windSpeedValidCalNAQM:double%20%3F;windSpeedValidCalPassQM:double%20%3F;windDirFinalQFSciRvw:string%20%3F;windSpeedFinalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
 * [windDirAlphaQM](windDirAlphaQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [windDirBetaQM](windDirBetaQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [windDirCalmWindQF](windDirCalmWindQF.md)  <sub>OPT</sub>
    * Description: Wind direction quality flag for the calm wind test, as detailed in NEON.DOC.000780 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [windDirConsistencyFailQM](windDirConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirConsistencyNAQM](windDirConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirConsistencyPassQM](windDirConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirDistortedFlowFailQM](windDirDistortedFlowFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the distorted flow test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirDistortedFlowNAQM](windDirDistortedFlowNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the distorted flow test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirDistortedFlowPassQM](windDirDistortedFlowPassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the distorted flow test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirExpUncert](windDirExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for wind direction
    * range: [Double](types/Double.md)
 * [windDirFinalQF](windDirFinalQF.md)  <sub>OPT</sub>
    * Description: Wind direction quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [windDirFinalQFSciRvw](windDirFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Wind direction quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [windDirGapFailQM](windDirGapFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirGapNAQM](windDirGapNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirGapPassQM](windDirGapPassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirMean](windDirMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of wind direction
    * range: [Double](types/Double.md)
 * [windDirNullFailQM](windDirNullFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirNullNAQM](windDirNullNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirNullPassQM](windDirNullPassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirNumPts](windDirNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of wind direction
    * range: [Double](types/Double.md)
 * [windDirPersistenceFailQM](windDirPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirPersistenceNAQM](windDirPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirPersistencePassQM](windDirPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirRangeFailQM](windDirRangeFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirRangeNAQM](windDirRangeNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirRangePassQM](windDirRangePassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSensorErrorFailQM](windDirSensorErrorFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the sensor error test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSensorErrorNAQM](windDirSensorErrorNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the sensor error test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSensorErrorPassQM](windDirSensorErrorPassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the sensor error test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSpikeFailQM](windDirSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSpikeNAQM](windDirSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSpikePassQM](windDirSpikePassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirStdErMean](windDirStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for wind direction
    * range: [Double](types/Double.md)
 * [windDirStepFailQM](windDirStepFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirStepNAQM](windDirStepNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirStepPassQM](windDirStepPassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirValidCalFailQM](windDirValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirValidCalNAQM](windDirValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirValidCalPassQM](windDirValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirVariance](windDirVariance.md)  <sub>OPT</sub>
    * Description: Variance in wind direction
    * range: [Double](types/Double.md)
 * [windSpeedAlphaQM](windSpeedAlphaQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [windSpeedBetaQM](windSpeedBetaQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [windSpeedCalmWindQF](windSpeedCalmWindQF.md)  <sub>OPT</sub>
    * Description: Wind speed quality flag for the calm wind test, as detailed in NEON.DOC.000780 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [windSpeedConsistencyFailQM](windSpeedConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedConsistencyNAQM](windSpeedConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedConsistencyPassQM](windSpeedConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedExpUncert](windSpeedExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for wind speed
    * range: [Double](types/Double.md)
 * [windSpeedFinalQF](windSpeedFinalQF.md)  <sub>OPT</sub>
    * Description: Wind speed quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [windSpeedFinalQFSciRvw](windSpeedFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Wind speed quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [windSpeedGapFailQM](windSpeedGapFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedGapNAQM](windSpeedGapNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedGapPassQM](windSpeedGapPassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedMaximum](windSpeedMaximum.md)  <sub>OPT</sub>
    * Description: Maximum wind speed
    * range: [Double](types/Double.md)
 * [windSpeedMean](windSpeedMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of wind speed
    * range: [Double](types/Double.md)
 * [windSpeedMinimum](windSpeedMinimum.md)  <sub>OPT</sub>
    * Description: Minimum wind speed
    * range: [Double](types/Double.md)
 * [windSpeedNullFailQM](windSpeedNullFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedNullNAQM](windSpeedNullNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedNullPassQM](windSpeedNullPassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedNumPts](windSpeedNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of wind speed
    * range: [Double](types/Double.md)
 * [windSpeedPersistenceFailQM](windSpeedPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedPersistenceNAQM](windSpeedPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedPersistencePassQM](windSpeedPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedRangeFailQM](windSpeedRangeFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedRangeNAQM](windSpeedRangeNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedRangePassQM](windSpeedRangePassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSensorErrorFailQM](windSpeedSensorErrorFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the sensor error test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSensorErrorNAQM](windSpeedSensorErrorNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the sensor error test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSensorErrorPassQM](windSpeedSensorErrorPassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the sensor error test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSpikeFailQM](windSpeedSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSpikeNAQM](windSpeedSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSpikePassQM](windSpeedSpikePassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedStdErMean](windSpeedStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for wind speed
    * range: [Double](types/Double.md)
 * [windSpeedStepFailQM](windSpeedStepFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedStepNAQM](windSpeedStepNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedStepPassQM](windSpeedStepPassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedValidCalFailQM](windSpeedValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedValidCalNAQM](windSpeedValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedValidCalPassQM](windSpeedValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedVariance](windSpeedVariance.md)  <sub>OPT</sub>
    * Description: Variance in wind speed
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:2DWSD_30min |

