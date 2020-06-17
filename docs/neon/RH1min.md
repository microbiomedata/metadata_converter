
# Type: RH_1min




URI: [neon:RH1min](https://data.neonscience.org/RH1min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [RHAlphaQAQCRpt](RHAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Relative humidity quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [RHBetaQAQCRpt](RHBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Relative humidity quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [RHConsistencyQAQCRpt](RHConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Relative humidity quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [RHGapQAQCRpt](RHGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Relative humidity quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [RHNullQAQCRpt](RHNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Relative humidity quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [RHPersistenceQAQCRpt](RHPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Relative humidity quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [RHRangeQAQCRpt](RHRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Relative humidity quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [RHSensorErrorQAQCRpt](RHSensorErrorQAQCRpt.md)  <sub>OPT</sub>
    * Description: Relative humidity quality assurance and quality control report for the sensor error flag, which indicates whether a sensor error occurred, detailed in NEON.DOC.000850 and NEON.DOC.000851 (1=error is detected, 0=no error, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [RHSpikeQAQCRpt](RHSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Relative humidity quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [RHStepQAQCRpt](RHStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Relative humidity quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [RHValidCalQAQCRpt](RHValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Relative humidity QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [dewTempAlphaQAQCRpt](dewTempAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [dewTempBetaQAQCRpt](dewTempBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [dewTempConsistencyQAQCRpt](dewTempConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [dewTempGapQAQCRpt](dewTempGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [dewTempNullQAQCRpt](dewTempNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [dewTempPersistenceQAQCRpt](dewTempPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [dewTempRangeQAQCRpt](dewTempRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [dewTempSpikeQAQCRpt](dewTempSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [dewTempStepQAQCRpt](dewTempStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [dewTempValidCalQAQCRpt](dewTempValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [tempRHAlphaQAQCRpt](tempRHAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [tempRHBetaQAQCRpt](tempRHBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [tempRHConsistencyQAQCRpt](tempRHConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [tempRHGapQAQCRpt](tempRHGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [tempRHNullQAQCRpt](tempRHNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [tempRHPersistenceQAQCRpt](tempRHPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [tempRHRangeQAQCRpt](tempRHRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [tempRHSpikeQAQCRpt](tempRHSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [tempRHStepQAQCRpt](tempRHStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)

### Inherited from EOS_30_min:

 * [surfacewaterElevMean](surfacewaterElevMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of elevation of surfacewater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [surfacewaterElevMinimum](surfacewaterElevMinimum.md)  <sub>OPT</sub>
    * Description: Minimum elevation of surfacewater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [surfacewaterElevMaximum](surfacewaterElevMaximum.md)  <sub>OPT</sub>
    * Description: Maximum elevation of surfacewater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [surfacewaterElevVariance](surfacewaterElevVariance.md)  <sub>OPT</sub>
    * Description: Variance in elevation of surfacewater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [surfacewaterElevNumPts](surfacewaterElevNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of elevation of surfacewater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [surfacewaterElevExpUncert](surfacewaterElevExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for elevation of surfacewater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [surfacewaterElevStdErMean](surfacewaterElevStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for elevation of surfacewater
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevRangeFailQM](sWatElevRangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevRangePassQM](sWatElevRangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevRangeNAQM](sWatElevRangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevPersistenceFailQM](sWatElevPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the persistence test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevPersistencePassQM](sWatElevPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevPersistenceNAQM](sWatElevPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevStepFailQM](sWatElevStepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevStepPassQM](sWatElevStepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevStepNAQM](sWatElevStepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevNullFailQM](sWatElevNullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevNullPassQM](sWatElevNullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevNullNAQM](sWatElevNullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevGapFailQM](sWatElevGapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevGapPassQM](sWatElevGapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevGapNAQM](sWatElevGapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevSpikeFailQM](sWatElevSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevSpikePassQM](sWatElevSpikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevSpikeNAQM](sWatElevSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevConsistencyFailQM](sWatElevConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevConsistencyPassQM](sWatElevConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevConsistencyNAQM](sWatElevConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevAlphaQM](sWatElevAlphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for elevation of surfacewater over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevBetaQM](sWatElevBetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for elevation of surfacewater over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sWatElevFinalQF](sWatElevFinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether elevation of surfacewater has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [tempRHValidCalQAQCRpt](tempRHValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [sWatElevFinalQFSciRvw](sWatElevFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Suface water elevation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from RH_30min:

 * [RHMean](RHMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of relative humidity
    * range: [Double](types/Double.md)
 * [RHMinimum](RHMinimum.md)  <sub>OPT</sub>
    * Description: Minimum relative humidity
    * range: [Double](types/Double.md)
 * [RHMaximum](RHMaximum.md)  <sub>OPT</sub>
    * Description: Maximum relative humidity
    * range: [Double](types/Double.md)
 * [RHVariance](RHVariance.md)  <sub>OPT</sub>
    * Description: Variance in relative humidity
    * range: [Double](types/Double.md)
 * [RHNumPts](RHNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of relative humidity
    * range: [Double](types/Double.md)
 * [RHExpUncert](RHExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for relative humidity
    * range: [Double](types/Double.md)
 * [RHStdErMean](RHStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for relative humidity
    * range: [Double](types/Double.md)
 * [RHRangeFailQM](RHRangeFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHRangePassQM](RHRangePassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHRangeNAQM](RHRangeNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHPersistenceFailQM](RHPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHPersistencePassQM](RHPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHPersistenceNAQM](RHPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHStepFailQM](RHStepFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHStepPassQM](RHStepPassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHStepNAQM](RHStepNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHNullFailQM](RHNullFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHNullPassQM](RHNullPassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHNullNAQM](RHNullNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHGapFailQM](RHGapFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHGapPassQM](RHGapPassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHGapNAQM](RHGapNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHSpikeFailQM](RHSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHSpikePassQM](RHSpikePassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHSpikeNAQM](RHSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHConsistencyFailQM](RHConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHConsistencyPassQM](RHConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHConsistencyNAQM](RHConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHAlphaQM](RHAlphaQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [RHBetaQM](RHBetaQM.md)  <sub>OPT</sub>
    * Description: Relative humidity quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [RHFinalQF](RHFinalQF.md)  <sub>OPT</sub>
    * Description: Relative humidity quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [tempRHMean](tempRHMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHMinimum](tempRHMinimum.md)  <sub>OPT</sub>
    * Description: Minimum temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHMaximum](tempRHMaximum.md)  <sub>OPT</sub>
    * Description: Maximum temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHVariance](tempRHVariance.md)  <sub>OPT</sub>
    * Description: Variance in temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHNumPts](tempRHNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHExpUncert](tempRHExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHStdErMean](tempRHStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for temperature measures by RH sensor
    * range: [Double](types/Double.md)
 * [tempRHRangeFailQM](tempRHRangeFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHRangePassQM](tempRHRangePassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHRangeNAQM](tempRHRangeNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHPersistenceFailQM](tempRHPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHPersistencePassQM](tempRHPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHPersistenceNAQM](tempRHPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHStepFailQM](tempRHStepFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHStepPassQM](tempRHStepPassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHStepNAQM](tempRHStepNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHNullFailQM](tempRHNullFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHNullPassQM](tempRHNullPassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHNullNAQM](tempRHNullNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHGapFailQM](tempRHGapFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHGapPassQM](tempRHGapPassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHGapNAQM](tempRHGapNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHSpikeFailQM](tempRHSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHSpikePassQM](tempRHSpikePassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHSpikeNAQM](tempRHSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHConsistencyFailQM](tempRHConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHConsistencyPassQM](tempRHConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHConsistencyNAQM](tempRHConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHAlphaQM](tempRHAlphaQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [tempRHBetaQM](tempRHBetaQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [tempRHFinalQF](tempRHFinalQF.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [dewTempMean](dewTempMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempMinimum](dewTempMinimum.md)  <sub>OPT</sub>
    * Description: Minimum dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempMaximum](dewTempMaximum.md)  <sub>OPT</sub>
    * Description: Maximum dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempVariance](dewTempVariance.md)  <sub>OPT</sub>
    * Description: Variance in dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempNumPts](dewTempNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempExpUncert](dewTempExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempStdErMean](dewTempStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for dew or frost point temperature
    * range: [Double](types/Double.md)
 * [dewTempRangeFailQM](dewTempRangeFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempRangePassQM](dewTempRangePassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempRangeNAQM](dewTempRangeNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempPersistenceFailQM](dewTempPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempPersistencePassQM](dewTempPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempPersistenceNAQM](dewTempPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempStepFailQM](dewTempStepFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempStepPassQM](dewTempStepPassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempStepNAQM](dewTempStepNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempNullFailQM](dewTempNullFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempNullPassQM](dewTempNullPassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempNullNAQM](dewTempNullNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempGapFailQM](dewTempGapFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempGapPassQM](dewTempGapPassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempGapNAQM](dewTempGapNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempSpikeFailQM](dewTempSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempSpikePassQM](dewTempSpikePassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempSpikeNAQM](dewTempSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempConsistencyFailQM](dewTempConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempConsistencyPassQM](dewTempConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempConsistencyNAQM](dewTempConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempAlphaQM](dewTempAlphaQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [dewTempBetaQM](dewTempBetaQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [dewTempFinalQF](dewTempFinalQF.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [RHSensorErrorFailQM](RHSensorErrorFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the sensor error occurred over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHSensorErrorPassQM](RHSensorErrorPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the sensor error was not occurred  over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [RHSensorErrorNAQM](RHSensorErrorNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the sensor error was unknown over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempFinalQFSciRvw](dewTempFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [RHFinalQFSciRvw](RHFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Relative humidity quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [tempRHFinalQFSciRvw](tempRHFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [dewTempValidCalFailQM](dewTempValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempValidCalNAQM](dewTempValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [dewTempValidCalPassQM](dewTempValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Dew or frost point temperature quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
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
 * [tempRHValidCalFailQM](tempRHValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHValidCalNAQM](tempRHValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempRHValidCalPassQM](tempRHValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
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
| **Mappings:** | | neon:RH_1min |
| **In Subsets:** | | DP1.00098.001 |

