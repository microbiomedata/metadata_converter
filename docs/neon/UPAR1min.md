
# Type: uPAR_1min




URI: [neon:UPAR1min](https://data.neonscience.org/UPAR1min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[UPAR1min&#124;startDateTime:time%20%3F;endDateTime:time%20%3F;outuPARAlphaQAQCRpt:string%20%3F;outuPARAlphaQM:double%20%3F;outuPARBetaQAQCRpt:string%20%3F;outuPARBetaQM:double%20%3F;outuPARConsistencyFailQM:double%20%3F;outuPARConsistencyNAQM:double%20%3F;outuPARConsistencyPassQM:double%20%3F;outuPARConsistencyQAQCRpt:string%20%3F;outuPARExpUncert:double%20%3F;outuPARFinalQF:string%20%3F;outuPARGapFailQM:double%20%3F;outuPARGapNAQM:double%20%3F;outuPARGapPassQM:double%20%3F;outuPARGapQAQCRpt:string%20%3F;outuPARMaximum:double%20%3F;outuPARMean:double%20%3F;outuPARMinimum:double%20%3F;outuPARNullFailQM:double%20%3F;outuPARNullNAQM:double%20%3F;outuPARNullPassQM:double%20%3F;outuPARNullQAQCRpt:string%20%3F;outuPARNumPts:integer%20%3F;outuPARPersistenceFailQM:double%20%3F;outuPARPersistenceNAQM:double%20%3F;outuPARPersistencePassQM:double%20%3F;outuPARPersistenceQAQCRpt:string%20%3F;outuPARRangeFailQM:double%20%3F;outuPARRangeNAQM:double%20%3F;outuPARRangePassQM:double%20%3F;outuPARRangeQAQCRpt:string%20%3F;outuPARSpikeFailQM:double%20%3F;outuPARSpikeNAQM:double%20%3F;outuPARSpikePassQM:double%20%3F;outuPARSpikeQAQCRpt:string%20%3F;outuPARStdErMean:double%20%3F;outuPARStepFailQM:double%20%3F;outuPARStepNAQM:double%20%3F;outuPARStepPassQM:double%20%3F;outuPARStepQAQCRpt:string%20%3F;outuPARValidCalFailQM:double%20%3F;outuPARValidCalNAQM:double%20%3F;outuPARValidCalPassQM:double%20%3F;outuPARValidCalQAQCRpt:string%20%3F;outuPARVariance:double%20%3F;uPARAlphaQAQCRpt:string%20%3F;uPARAlphaQM:double%20%3F;uPARBetaQAQCRpt:string%20%3F;uPARBetaQM:double%20%3F;uPARConsistencyFailQM:double%20%3F;uPARConsistencyNAQM:double%20%3F;uPARConsistencyPassQM:double%20%3F;uPARConsistencyQAQCRpt:string%20%3F;uPARExpUncert:double%20%3F;uPARFinalQF:string%20%3F;uPARGapFailQM:double%20%3F;uPARGapNAQM:double%20%3F;uPARGapPassQM:double%20%3F;uPARGapQAQCRpt:string%20%3F;uPARMaximum:double%20%3F;uPARMean:double%20%3F;uPARMinimum:double%20%3F;uPARNullFailQM:double%20%3F;uPARNullNAQM:double%20%3F;uPARNullPassQM:double%20%3F;uPARNullQAQCRpt:string%20%3F;uPARNumPts:integer%20%3F;uPARPersistenceFailQM:double%20%3F;uPARPersistenceNAQM:double%20%3F;uPARPersistencePassQM:double%20%3F;uPARPersistenceQAQCRpt:string%20%3F;uPARRangeFailQM:double%20%3F;uPARRangeNAQM:double%20%3F;uPARRangePassQM:double%20%3F;uPARRangeQAQCRpt:string%20%3F;uPARSpikeFailQM:double%20%3F;uPARSpikeNAQM:double%20%3F;uPARSpikePassQM:double%20%3F;uPARSpikeQAQCRpt:string%20%3F;uPARStdErMean:double%20%3F;uPARStepFailQM:double%20%3F;uPARStepNAQM:double%20%3F;uPARStepPassQM:double%20%3F;uPARStepQAQCRpt:string%20%3F;uPARValidCalFailQM:double%20%3F;uPARValidCalNAQM:double%20%3F;uPARValidCalPassQM:double%20%3F;uPARValidCalQAQCRpt:string%20%3F;uPARVariance:double%20%3F;outuPARFinalQFSciRvw:string%20%3F;uPARFinalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [outuPARAlphaQAQCRpt](outuPARAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outuPARAlphaQM](outuPARAlphaQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [outuPARBetaQAQCRpt](outuPARBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface QAQC report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outuPARBetaQM](outuPARBetaQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [outuPARConsistencyFailQM](outuPARConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARConsistencyNAQM](outuPARConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARConsistencyPassQM](outuPARConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARConsistencyQAQCRpt](outuPARConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outuPARExpUncert](outuPARExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for outgoing PAR below water surface
    * range: [Double](types/Double.md)
 * [outuPARFinalQF](outuPARFinalQF.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [outuPARFinalQFSciRvw](outuPARFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [outuPARGapFailQM](outuPARGapFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARGapNAQM](outuPARGapNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARGapPassQM](outuPARGapPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARGapQAQCRpt](outuPARGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [outuPARMaximum](outuPARMaximum.md)  <sub>OPT</sub>
    * Description: Maximum outgoing PAR below water surface
    * range: [Double](types/Double.md)
 * [outuPARMean](outuPARMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of outgoing PAR below water surface
    * range: [Double](types/Double.md)
 * [outuPARMinimum](outuPARMinimum.md)  <sub>OPT</sub>
    * Description: Minimum outgoing PAR below water surface
    * range: [Double](types/Double.md)
 * [outuPARNullFailQM](outuPARNullFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARNullNAQM](outuPARNullNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARNullPassQM](outuPARNullPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARNullQAQCRpt](outuPARNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outuPARNumPts](outuPARNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of outgoing PAR below water surface
    * range: [Integer](types/Integer.md)
 * [outuPARPersistenceFailQM](outuPARPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARPersistenceNAQM](outuPARPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARPersistencePassQM](outuPARPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARPersistenceQAQCRpt](outuPARPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface QAQC report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outuPARRangeFailQM](outuPARRangeFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARRangeNAQM](outuPARRangeNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARRangePassQM](outuPARRangePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARRangeQAQCRpt](outuPARRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realisitc value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outuPARSpikeFailQM](outuPARSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARSpikeNAQM](outuPARSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARSpikePassQM](outuPARSpikePassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARSpikeQAQCRpt](outuPARSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outuPARStdErMean](outuPARStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for outgoing PAR below water surface
    * range: [Double](types/Double.md)
 * [outuPARStepFailQM](outuPARStepFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARStepNAQM](outuPARStepNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARStepPassQM](outuPARStepPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARStepQAQCRpt](outuPARStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outuPARValidCalFailQM](outuPARValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARValidCalNAQM](outuPARValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARValidCalPassQM](outuPARValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [outuPARValidCalQAQCRpt](outuPARValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Outgoing PAR below water surface QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [outuPARVariance](outuPARVariance.md)  <sub>OPT</sub>
    * Description: Variance in outgoing PAR below water surface
    * range: [Double](types/Double.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
 * [uPARAlphaQAQCRpt](uPARAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the null test for PM15 at RH <50%, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [uPARAlphaQM](uPARAlphaQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [uPARBetaQAQCRpt](uPARBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [uPARBetaQM](uPARBetaQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [uPARConsistencyFailQM](uPARConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARConsistencyNAQM](uPARConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARConsistencyPassQM](uPARConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARConsistencyQAQCRpt](uPARConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [uPARExpUncert](uPARExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for PAR below water surface
    * range: [Double](types/Double.md)
 * [uPARFinalQF](uPARFinalQF.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [uPARFinalQFSciRvw](uPARFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [uPARGapFailQM](uPARGapFailQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARGapNAQM](uPARGapNAQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARGapPassQM](uPARGapPassQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARGapQAQCRpt](uPARGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [uPARMaximum](uPARMaximum.md)  <sub>OPT</sub>
    * Description: Maximum PAR below water surface
    * range: [Double](types/Double.md)
 * [uPARMean](uPARMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of PAR below water surface
    * range: [Double](types/Double.md)
 * [uPARMinimum](uPARMinimum.md)  <sub>OPT</sub>
    * Description: Minimum PAR below water surface
    * range: [Double](types/Double.md)
 * [uPARNullFailQM](uPARNullFailQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARNullNAQM](uPARNullNAQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARNullPassQM](uPARNullPassQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARNullQAQCRpt](uPARNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run)
    * range: [String](types/String.md)
 * [uPARNumPts](uPARNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of PAR below water surface
    * range: [Integer](types/Integer.md)
 * [uPARPersistenceFailQM](uPARPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARPersistenceNAQM](uPARPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARPersistencePassQM](uPARPersistencePassQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARPersistenceQAQCRpt](uPARPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: PAR below water surface QAQC report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [uPARRangeFailQM](uPARRangeFailQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARRangeNAQM](uPARRangeNAQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARRangePassQM](uPARRangePassQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARRangeQAQCRpt](uPARRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run)
    * range: [String](types/String.md)
 * [uPARSpikeFailQM](uPARSpikeFailQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARSpikeNAQM](uPARSpikeNAQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARSpikePassQM](uPARSpikePassQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARSpikeQAQCRpt](uPARSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [uPARStdErMean](uPARStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for PAR below water surface
    * range: [Double](types/Double.md)
 * [uPARStepFailQM](uPARStepFailQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARStepNAQM](uPARStepNAQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARStepPassQM](uPARStepPassQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARStepQAQCRpt](uPARStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [uPARValidCalFailQM](uPARValidCalFailQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARValidCalNAQM](uPARValidCalNAQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARValidCalPassQM](uPARValidCalPassQM.md)  <sub>OPT</sub>
    * Description: PAR below water surface quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [uPARValidCalQAQCRpt](uPARValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: PAR below water surface QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [uPARVariance](uPARVariance.md)  <sub>OPT</sub>
    * Description: Variance in PAR below water surface
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:uPAR_1min |
| **In Subsets:** | | DP1.20261.001 |

