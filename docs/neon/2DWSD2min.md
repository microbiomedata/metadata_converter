
# Type: 2DWSD_2min




URI: [neon:2DWSD2min](https://data.neonscience.org/2DWSD2min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[2DWSD2min&#124;windSpeedMean:double%20%3F;windSpeedMinimum:double%20%3F;windSpeedMaximum:double%20%3F;windSpeedVariance:double%20%3F;windSpeedNumPts:double%20%3F;windSpeedExpUncert:double%20%3F;windSpeedStdErMean:double%20%3F;windSpeedRangeQAQCRpt:string%20%3F;windSpeedPersistenceQAQCRpt:string%20%3F;windSpeedStepQAQCRpt:string%20%3F;windSpeedNullQAQCRpt:string%20%3F;windSpeedGapQAQCRpt:string%20%3F;windSpeedConsistencyQAQCRpt:string%20%3F;windSpeedSpikeQAQCRpt:string%20%3F;windSpeedAlphaQAQCRpt:string%20%3F;windSpeedBetaQAQCRpt:string%20%3F;windSpeedRangeFailQM:double%20%3F;windSpeedRangePassQM:double%20%3F;windSpeedRangeNAQM:double%20%3F;windSpeedPersistenceFailQM:double%20%3F;windSpeedPersistencePassQM:double%20%3F;windSpeedPersistenceNAQM:double%20%3F;windSpeedStepFailQM:double%20%3F;windSpeedStepPassQM:double%20%3F;windSpeedStepNAQM:double%20%3F;windSpeedNullFailQM:double%20%3F;windSpeedNullPassQM:double%20%3F;windSpeedNullNAQM:double%20%3F;windSpeedGapFailQM:double%20%3F;windSpeedGapPassQM:double%20%3F;windSpeedGapNAQM:double%20%3F;windSpeedSpikeFailQM:double%20%3F;windSpeedSpikePassQM:double%20%3F;windSpeedSpikeNAQM:double%20%3F;windSpeedConsistencyFailQM:double%20%3F;windSpeedConsistencyPassQM:double%20%3F;windSpeedConsistencyNAQM:double%20%3F;windSpeedAlphaQM:double%20%3F;windSpeedBetaQM:double%20%3F;windSpeedFinalQF:string%20%3F;windDirMean:double%20%3F;windDirVariance:double%20%3F;windDirNumPts:double%20%3F;windDirExpUncert:double%20%3F;windDirStdErMean:double%20%3F;windDirRangeQAQCRpt:string%20%3F;windDirPersistenceQAQCRpt:string%20%3F;windDirStepQAQCRpt:string%20%3F;windDirNullQAQCRpt:string%20%3F;windDirGapQAQCRpt:string%20%3F;windDirConsistencyQAQCRpt:string%20%3F;windDirSpikeQAQCRpt:string%20%3F;windDirAlphaQAQCRpt:string%20%3F;windDirBetaQAQCRpt:string%20%3F;windDirRangeFailQM:double%20%3F;windDirRangePassQM:double%20%3F;windDirRangeNAQM:double%20%3F;windDirPersistenceFailQM:double%20%3F;windDirPersistencePassQM:double%20%3F;windDirPersistenceNAQM:double%20%3F;windDirStepFailQM:double%20%3F;windDirStepPassQM:double%20%3F;windDirStepNAQM:double%20%3F;windDirNullFailQM:double%20%3F;windDirNullPassQM:double%20%3F;windDirNullNAQM:double%20%3F;windDirGapFailQM:double%20%3F;windDirGapPassQM:double%20%3F;windDirGapNAQM:double%20%3F;windDirSpikeFailQM:double%20%3F;windDirSpikePassQM:double%20%3F;windDirSpikeNAQM:double%20%3F;windDirConsistencyFailQM:double%20%3F;windDirConsistencyPassQM:double%20%3F;windDirConsistencyNAQM:double%20%3F;windDirAlphaQM:double%20%3F;windDirBetaQM:double%20%3F;windDirFinalQF:string%20%3F;windDirDistortedFlowQAQCRpt:string%20%3F;windDirDistortedFlowFailQM:double%20%3F;windDirDistortedFlowPassQM:double%20%3F;windDirDistortedFlowNAQM:double%20%3F;windSpeedSensorErrorQAQCRpt:string%20%3F;windSpeedSensorErrorFailQM:double%20%3F;windSpeedSensorErrorPassQM:double%20%3F;windSpeedSensorErrorNAQM:double%20%3F;windSpeedCalmWindQF:integer%20%3F;windDirSensorErrorQAQCRpt:string%20%3F;windDirSensorErrorFailQM:double%20%3F;windDirSensorErrorPassQM:double%20%3F;windDirSensorErrorNAQM:double%20%3F;windDirCalmWindQF:integer%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;windDirValidCalFailQM:double%20%3F;windDirValidCalNAQM:double%20%3F;windDirValidCalPassQM:double%20%3F;windDirValidCalQAQCRpt:string%20%3F;windSpeedValidCalFailQM:double%20%3F;windSpeedValidCalNAQM:double%20%3F;windSpeedValidCalPassQM:double%20%3F;windSpeedValidCalQAQCRpt:string%20%3F;windDirFinalQFSciRvw:string%20%3F;windSpeedFinalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
 * [windDirAlphaQAQCRpt](windDirAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windDirAlphaQM](windDirAlphaQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [windDirBetaQAQCRpt](windDirBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
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
 * [windDirConsistencyQAQCRpt](windDirConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windDirDistortedFlowFailQM](windDirDistortedFlowFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the distorted flow test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirDistortedFlowNAQM](windDirDistortedFlowNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the distorted flow test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirDistortedFlowPassQM](windDirDistortedFlowPassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the distorted flow test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirDistortedFlowQAQCRpt](windDirDistortedFlowQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction quality assurance and quality control report for distorted flow, which indicates whether or not a wind measurement has been influenced by obstacles upstream of the sensor, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
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
 * [windDirGapQAQCRpt](windDirGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
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
 * [windDirNullQAQCRpt](windDirNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
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
 * [windDirPersistenceQAQCRpt](windDirPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windDirRangeFailQM](windDirRangeFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirRangeNAQM](windDirRangeNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirRangePassQM](windDirRangePassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirRangeQAQCRpt](windDirRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windDirSensorErrorFailQM](windDirSensorErrorFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the sensor error test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSensorErrorNAQM](windDirSensorErrorNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the sensor error test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSensorErrorPassQM](windDirSensorErrorPassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the sensor error test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSensorErrorQAQCRpt](windDirSensorErrorQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction quality assurance and quality control report for sensor errors, which indicates whether or not the sensor was reporting an error, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windDirSpikeFailQM](windDirSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSpikeNAQM](windDirSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSpikePassQM](windDirSpikePassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirSpikeQAQCRpt](windDirSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
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
 * [windDirStepQAQCRpt](windDirStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windDirValidCalFailQM](windDirValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirValidCalNAQM](windDirValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirValidCalPassQM](windDirValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Wind direction quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windDirValidCalQAQCRpt](windDirValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind direction QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windDirVariance](windDirVariance.md)  <sub>OPT</sub>
    * Description: Variance in wind direction
    * range: [Double](types/Double.md)
 * [windSpeedAlphaQAQCRpt](windSpeedAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind speed quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windSpeedAlphaQM](windSpeedAlphaQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [windSpeedBetaQAQCRpt](windSpeedBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind speed quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
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
 * [windSpeedConsistencyQAQCRpt](windSpeedConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind speed quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
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
 * [windSpeedGapQAQCRpt](windSpeedGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind speed quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
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
 * [windSpeedNullQAQCRpt](windSpeedNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind speed quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
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
 * [windSpeedPersistenceQAQCRpt](windSpeedPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind speed quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windSpeedRangeFailQM](windSpeedRangeFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedRangeNAQM](windSpeedRangeNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedRangePassQM](windSpeedRangePassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedRangeQAQCRpt](windSpeedRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind speed quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windSpeedSensorErrorFailQM](windSpeedSensorErrorFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the sensor error test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSensorErrorNAQM](windSpeedSensorErrorNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the sensor error test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSensorErrorPassQM](windSpeedSensorErrorPassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the sensor error test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSensorErrorQAQCRpt](windSpeedSensorErrorQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind speed quality assurance and quality control report for sensor errors, which indicates whether or not the sensor was reporting an error, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windSpeedSpikeFailQM](windSpeedSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSpikeNAQM](windSpeedSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSpikePassQM](windSpeedSpikePassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedSpikeQAQCRpt](windSpeedSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind speed quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
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
 * [windSpeedStepQAQCRpt](windSpeedStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind speed quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windSpeedValidCalFailQM](windSpeedValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedValidCalNAQM](windSpeedValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedValidCalPassQM](windSpeedValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Wind speed quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [windSpeedValidCalQAQCRpt](windSpeedValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Wind speed QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [windSpeedVariance](windSpeedVariance.md)  <sub>OPT</sub>
    * Description: Variance in wind speed
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:2DWSD_2min |
| **In Subsets:** | | DP1.00001.001 |

