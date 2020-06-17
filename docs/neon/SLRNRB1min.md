
# Type: SLRNRB_1min




URI: [neon:SLRNRB1min](https://data.neonscience.org/SLRNRB1min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


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

### Inherited from SLRNR_1min:

 * [heaterQAQCRpt](heaterQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the heater flag, which indicates whether the heater was operational as described in the sensor specific algorithm theoretical basis document (ATBD) (1=on, 0=off, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inSWRangeQAQCRpt](inSWRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inSWPersistenceQAQCRpt](inSWPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inSWStepQAQCRpt](inSWStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inSWNullQAQCRpt](inSWNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inSWGapQAQCRpt](inSWGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [inSWConsistencyQAQCRpt](inSWConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inSWSpikeQAQCRpt](inSWSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inSWAlphaQAQCRpt](inSWAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inSWBetaQAQCRpt](inSWBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outSWRangeQAQCRpt](outSWRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outSWPersistenceQAQCRpt](outSWPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outSWStepQAQCRpt](outSWStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outSWNullQAQCRpt](outSWNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outSWGapQAQCRpt](outSWGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [outSWConsistencyQAQCRpt](outSWConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outSWSpikeQAQCRpt](outSWSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outSWAlphaQAQCRpt](outSWAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outSWBetaQAQCRpt](outSWBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inLWRangeQAQCRpt](inLWRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inLWPersistenceQAQCRpt](inLWPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inLWStepQAQCRpt](inLWStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inLWNullQAQCRpt](inLWNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inLWGapQAQCRpt](inLWGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [inLWConsistencyQAQCRpt](inLWConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inLWSpikeQAQCRpt](inLWSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inLWAlphaQAQCRpt](inLWAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inLWBetaQAQCRpt](inLWBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outLWRangeQAQCRpt](outLWRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outLWPersistenceQAQCRpt](outLWPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outLWStepQAQCRpt](outLWStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outLWNullQAQCRpt](outLWNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outLWGapQAQCRpt](outLWGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [outLWConsistencyQAQCRpt](outLWConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outLWSpikeQAQCRpt](outLWSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outLWAlphaQAQCRpt](outLWAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outLWBetaQAQCRpt](outLWBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inLWValidCalQAQCRpt](inLWValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [inSWValidCalQAQCRpt](inSWValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outLWValidCalQAQCRpt](outLWValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outSWValidCalQAQCRpt](outSWValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)

### Inherited from SLRNR_30min:

 * [heaterFailQM](heaterFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the heater was on over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [heaterPassQM](heaterPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the heater was off over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [heaterNAQM](heaterNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the heater status was unknown over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWMean](inSWMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of incoming shortwave radiation
    * range: [Double](types/Double.md)
 * [inSWMinimum](inSWMinimum.md)  <sub>OPT</sub>
    * Description: Minimum incoming shortwave radiation
    * range: [Double](types/Double.md)
 * [inSWMaximum](inSWMaximum.md)  <sub>OPT</sub>
    * Description: Maximum incoming shortwave radiation
    * range: [Double](types/Double.md)
 * [inSWVariance](inSWVariance.md)  <sub>OPT</sub>
    * Description: Variance in incoming shortwave radiation
    * range: [Double](types/Double.md)
 * [inSWNumPts](inSWNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of incoming shortwave radiation
    * range: [Double](types/Double.md)
 * [inSWExpUncert](inSWExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for incoming shortwave radiation
    * range: [Double](types/Double.md)
 * [inSWStdErMean](inSWStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for incoming shortwave radiation
    * range: [Double](types/Double.md)
 * [inSWRangeFailQM](inSWRangeFailQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWRangePassQM](inSWRangePassQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWRangeNAQM](inSWRangeNAQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWPersistenceFailQM](inSWPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWPersistencePassQM](inSWPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWPersistenceNAQM](inSWPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWStepFailQM](inSWStepFailQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWStepPassQM](inSWStepPassQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWStepNAQM](inSWStepNAQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWNullFailQM](inSWNullFailQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWNullPassQM](inSWNullPassQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWNullNAQM](inSWNullNAQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWGapFailQM](inSWGapFailQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWGapPassQM](inSWGapPassQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWGapNAQM](inSWGapNAQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWSpikeFailQM](inSWSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWSpikePassQM](inSWSpikePassQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWSpikeNAQM](inSWSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWConsistencyFailQM](inSWConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWConsistencyPassQM](inSWConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWConsistencyNAQM](inSWConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWAlphaQM](inSWAlphaQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [inSWBetaQM](inSWBetaQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [inSWFinalQF](inSWFinalQF.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [outSWMean](outSWMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of outgoing shortwave radiation
    * range: [Double](types/Double.md)
 * [outSWMinimum](outSWMinimum.md)  <sub>OPT</sub>
    * Description: Minimum outgoing shortwave radiation
    * range: [Double](types/Double.md)
 * [outSWMaximum](outSWMaximum.md)  <sub>OPT</sub>
    * Description: Maximum outgoing shortwave radiation
    * range: [Double](types/Double.md)
 * [outSWVariance](outSWVariance.md)  <sub>OPT</sub>
    * Description: Variance in outgoing shortwave radiation
    * range: [Double](types/Double.md)
 * [outSWNumPts](outSWNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of outgoing shortwave radiation
    * range: [Double](types/Double.md)
 * [outSWExpUncert](outSWExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for outgoing shortwave radiation
    * range: [Double](types/Double.md)
 * [outSWStdErMean](outSWStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for outgoing shortwave radiation
    * range: [Double](types/Double.md)
 * [outSWRangeFailQM](outSWRangeFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWRangePassQM](outSWRangePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWRangeNAQM](outSWRangeNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWPersistenceFailQM](outSWPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWPersistencePassQM](outSWPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWPersistenceNAQM](outSWPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWStepFailQM](outSWStepFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWStepPassQM](outSWStepPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWStepNAQM](outSWStepNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWNullFailQM](outSWNullFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWNullPassQM](outSWNullPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWNullNAQM](outSWNullNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWGapFailQM](outSWGapFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWGapPassQM](outSWGapPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWGapNAQM](outSWGapNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWSpikeFailQM](outSWSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWSpikePassQM](outSWSpikePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWSpikeNAQM](outSWSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWConsistencyFailQM](outSWConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWConsistencyPassQM](outSWConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWConsistencyNAQM](outSWConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWAlphaQM](outSWAlphaQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [outSWBetaQM](outSWBetaQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [outSWFinalQF](outSWFinalQF.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [inLWMean](inLWMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of incoming longwave radiation
    * range: [Double](types/Double.md)
 * [inLWMinimum](inLWMinimum.md)  <sub>OPT</sub>
    * Description: Minimum incoming longwave radiation
    * range: [Double](types/Double.md)
 * [inLWMaximum](inLWMaximum.md)  <sub>OPT</sub>
    * Description: Maximum incoming longwave radiation
    * range: [Double](types/Double.md)
 * [inLWVariance](inLWVariance.md)  <sub>OPT</sub>
    * Description: Variance in incoming longwave radiation
    * range: [Double](types/Double.md)
 * [inLWNumPts](inLWNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of incoming longwave radiation
    * range: [Double](types/Double.md)
 * [inLWExpUncert](inLWExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for incoming longwave radiation
    * range: [Double](types/Double.md)
 * [inLWStdErMean](inLWStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for incoming longwave radiation
    * range: [Double](types/Double.md)
 * [inLWRangeFailQM](inLWRangeFailQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWRangePassQM](inLWRangePassQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWRangeNAQM](inLWRangeNAQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWPersistenceFailQM](inLWPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWPersistencePassQM](inLWPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWPersistenceNAQM](inLWPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWStepFailQM](inLWStepFailQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWStepPassQM](inLWStepPassQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWStepNAQM](inLWStepNAQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWNullFailQM](inLWNullFailQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWNullPassQM](inLWNullPassQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWNullNAQM](inLWNullNAQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWGapFailQM](inLWGapFailQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWGapPassQM](inLWGapPassQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWGapNAQM](inLWGapNAQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWSpikeFailQM](inLWSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWSpikePassQM](inLWSpikePassQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWSpikeNAQM](inLWSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWConsistencyFailQM](inLWConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWConsistencyPassQM](inLWConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWConsistencyNAQM](inLWConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWAlphaQM](inLWAlphaQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [inLWBetaQM](inLWBetaQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [inLWFinalQF](inLWFinalQF.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation  quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [outLWMean](outLWMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of outgoing longwave radiation
    * range: [Double](types/Double.md)
 * [outLWMinimum](outLWMinimum.md)  <sub>OPT</sub>
    * Description: Minimum outgoing longwave radiation
    * range: [Double](types/Double.md)
 * [outLWMaximum](outLWMaximum.md)  <sub>OPT</sub>
    * Description: Maximum outgoing longwave radiation
    * range: [Double](types/Double.md)
 * [outLWVariance](outLWVariance.md)  <sub>OPT</sub>
    * Description: Variance in outgoing longwave radiation
    * range: [Double](types/Double.md)
 * [outLWNumPts](outLWNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of outgoing longwave radiation
    * range: [Double](types/Double.md)
 * [outLWExpUncert](outLWExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for outgoing longwave radiation
    * range: [Double](types/Double.md)
 * [outLWStdErMean](outLWStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for outgoing longwave radiation
    * range: [Double](types/Double.md)
 * [outLWRangeFailQM](outLWRangeFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWRangePassQM](outLWRangePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWRangeNAQM](outLWRangeNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWPersistenceFailQM](outLWPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWPersistencePassQM](outLWPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWPersistenceNAQM](outLWPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWStepFailQM](outLWStepFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWStepPassQM](outLWStepPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWStepNAQM](outLWStepNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWNullFailQM](outLWNullFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWNullPassQM](outLWNullPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWNullNAQM](outLWNullNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWGapFailQM](outLWGapFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWGapPassQM](outLWGapPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWGapNAQM](outLWGapNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWSpikeFailQM](outLWSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWSpikePassQM](outLWSpikePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWSpikeNAQM](outLWSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWConsistencyFailQM](outLWConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWConsistencyPassQM](outLWConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWConsistencyNAQM](outLWConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWAlphaQM](outLWAlphaQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [outLWBetaQM](outLWBetaQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation  quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [outLWFinalQF](outLWFinalQF.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [inLWFinalQFSciRvw](inLWFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [inSWFinalQFSciRvw](inSWFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [outLWFinalQFSciRvw](outLWFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [outSWFinalQFSciRvw](outSWFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [inLWValidCalFailQM](inLWValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWValidCalNAQM](inLWValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inLWValidCalPassQM](inLWValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Incoming longwave radiation quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWValidCalFailQM](inSWValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWValidCalNAQM](inSWValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [inSWValidCalPassQM](inSWValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Incoming shortwave radiation quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWValidCalFailQM](outLWValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWValidCalNAQM](outLWValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outLWValidCalPassQM](outLWValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing longwave radiation quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWValidCalFailQM](outSWValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWValidCalNAQM](outSWValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outSWValidCalPassQM](outSWValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing shortwave radiation quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)

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
| **Mappings:** | | neon:SLRNRB_1min |
| **In Subsets:** | | DP1.20032.001 |

