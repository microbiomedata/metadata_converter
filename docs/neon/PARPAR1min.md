
# Type: PARPAR_1min




URI: [neon:PARPAR1min](https://data.neonscience.org/PARPAR1min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [PARAlphaQAQCRpt](PARAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARBetaQAQCRpt](PARBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARConsistencyQAQCRpt](PARConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARFinalQFSciRvw](PARFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [PARGapQAQCRpt](PARGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [PARNullQAQCRpt](PARNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARPersistenceQAQCRpt](PARPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARRangeQAQCRpt](PARRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARSpikeQAQCRpt](PARSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARStepQAQCRpt](PARStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARValidCalQAQCRpt](PARValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outPARAlphaQAQCRpt](outPARAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outPARBetaQAQCRpt](outPARBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outPARConsistencyQAQCRpt](outPARConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outPARGapQAQCRpt](outPARGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [outPARNullQAQCRpt](outPARNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outPARPersistenceQAQCRpt](outPARPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outPARRangeQAQCRpt](outPARRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realisitc value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outPARSpikeQAQCRpt](outPARSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outPARStepQAQCRpt](outPARStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outPARValidCalQAQCRpt](outPARValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)

### Inherited from PARPAR_30min:

 * [PARMean](PARMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARMinimum](PARMinimum.md)  <sub>OPT</sub>
    * Description: Minimum photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARMaximum](PARMaximum.md)  <sub>OPT</sub>
    * Description: Maximum photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARVariance](PARVariance.md)  <sub>OPT</sub>
    * Description: Variance in photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARNumPts](PARNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARExpUncert](PARExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARStdErMean](PARStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARRangeFailQM](PARRangeFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARRangePassQM](PARRangePassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARRangeNAQM](PARRangeNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARPersistenceFailQM](PARPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARPersistencePassQM](PARPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARPersistenceNAQM](PARPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARStepFailQM](PARStepFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARStepPassQM](PARStepPassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARStepNAQM](PARStepNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARNullFailQM](PARNullFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARNullPassQM](PARNullPassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARNullNAQM](PARNullNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARGapFailQM](PARGapFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARGapPassQM](PARGapPassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARGapNAQM](PARGapNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARSpikeFailQM](PARSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARSpikePassQM](PARSpikePassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARSpikeNAQM](PARSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARConsistencyFailQM](PARConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARConsistencyPassQM](PARConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARConsistencyNAQM](PARConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARAlphaQM](PARAlphaQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [PARBetaQM](PARBetaQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [PARFinalQF](PARFinalQF.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [outPARMean](outPARMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of outgoing photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [outPARMinimum](outPARMinimum.md)  <sub>OPT</sub>
    * Description: Minimum outgoing photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [outPARMaximum](outPARMaximum.md)  <sub>OPT</sub>
    * Description: Maximum outgoing photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [outPARVariance](outPARVariance.md)  <sub>OPT</sub>
    * Description: Variance in outgoing photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [outPARNumPts](outPARNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of outgoing photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [outPARExpUncert](outPARExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for outgoing photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [outPARStdErMean](outPARStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for outgoing photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [outPARRangeFailQM](outPARRangeFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARRangePassQM](outPARRangePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARRangeNAQM](outPARRangeNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing photosynthetically active radiation quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARPersistenceFailQM](outPARPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARPersistencePassQM](outPARPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARPersistenceNAQM](outPARPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARStepFailQM](outPARStepFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARStepPassQM](outPARStepPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARStepNAQM](outPARStepNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARNullFailQM](outPARNullFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARNullPassQM](outPARNullPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARNullNAQM](outPARNullNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARGapFailQM](outPARGapFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARGapPassQM](outPARGapPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARGapNAQM](outPARGapNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARSpikeFailQM](outPARSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARSpikePassQM](outPARSpikePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARSpikeNAQM](outPARSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARConsistencyFailQM](outPARConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARConsistencyPassQM](outPARConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARConsistencyNAQM](outPARConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARAlphaQM](outPARAlphaQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [outPARBetaQM](outPARBetaQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [outPARFinalQF](outPARFinalQF.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [PARValidCalPassQM](PARValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARValidCalNAQM](PARValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARValidCalFailQM](PARValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARValidCalPassQM](outPARValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARValidCalNAQM](outPARValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARValidCalFailQM](outPARValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outPARFinalQFSciRvw](outPARFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Outgoing PAR quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)

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
| **Mappings:** | | neon:PARPAR_1min |
| **In Subsets:** | | DP1.00024.001 |

