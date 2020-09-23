
# Type: SWS_1_minute




URI: [neon:SWS1Minute](https://data.neonscience.org/SWS1Minute)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SWS1Minute&#124;VSWCMean:double%20%3F;VSWCMinimum:double%20%3F;VSWCMaximum:double%20%3F;VSWCVariance:double%20%3F;VSWCNumPts:double%20%3F;VSWCExpUncert:double%20%3F;VSWCStdErMean:double%20%3F;VSWCRangeQAQCRpt:string%20%3F;VSWCPersistenceQAQCRpt:string%20%3F;VSWCStepQAQCRpt:string%20%3F;VSWCNullQAQCRpt:string%20%3F;VSWCGapQAQCRpt:string%20%3F;VSWCConsistencyQAQCRpt:string%20%3F;VSWCSpikeQAQCRpt:string%20%3F;VSWCAlphaQAQCRpt:string%20%3F;VSWCBetaQAQCRpt:string%20%3F;VSWCRangeFailQM:double%20%3F;VSWCRangePassQM:double%20%3F;VSWCRangeNAQM:double%20%3F;VSWCPersistenceFailQM:double%20%3F;VSWCPersistencePassQM:double%20%3F;VSWCPersistenceNAQM:double%20%3F;VSWCStepFailQM:double%20%3F;VSWCStepPassQM:double%20%3F;VSWCStepNAQM:double%20%3F;VSWCNullFailQM:double%20%3F;VSWCNullPassQM:double%20%3F;VSWCNullNAQM:double%20%3F;VSWCGapFailQM:double%20%3F;VSWCGapPassQM:double%20%3F;VSWCGapNAQM:double%20%3F;VSWCSpikeFailQM:double%20%3F;VSWCSpikePassQM:double%20%3F;VSWCSpikeNAQM:double%20%3F;VSWCConsistencyFailQM:double%20%3F;VSWCConsistencyPassQM:double%20%3F;VSWCConsistencyNAQM:double%20%3F;VSWCAlphaQM:double%20%3F;VSWCBetaQM:double%20%3F;VSWCFinalQF:string%20%3F;VSICMean:double%20%3F;VSICMinimum:double%20%3F;VSICMaximum:double%20%3F;VSICVariance:double%20%3F;VSICNumPts:double%20%3F;VSICExpUncert:double%20%3F;VSICStdErMean:double%20%3F;VSICRangeQAQCRpt:string%20%3F;VSICPersistenceQAQCRpt:string%20%3F;VSICStepQAQCRpt:string%20%3F;VSICNullQAQCRpt:string%20%3F;VSICGapQAQCRpt:string%20%3F;VSICConsistencyQAQCRpt:string%20%3F;VSICSpikeQAQCRpt:string%20%3F;VSICAlphaQAQCRpt:string%20%3F;VSICBetaQAQCRpt:string%20%3F;VSICRangeFailQM:double%20%3F;VSICRangePassQM:double%20%3F;VSICRangeNAQM:double%20%3F;VSICPersistenceFailQM:double%20%3F;VSICPersistencePassQM:double%20%3F;VSICPersistenceNAQM:double%20%3F;VSICStepFailQM:double%20%3F;VSICStepPassQM:double%20%3F;VSICStepNAQM:double%20%3F;VSICNullFailQM:double%20%3F;VSICNullPassQM:double%20%3F;VSICNullNAQM:double%20%3F;VSICGapFailQM:double%20%3F;VSICGapPassQM:double%20%3F;VSICGapNAQM:double%20%3F;VSICSpikeFailQM:double%20%3F;VSICSpikePassQM:double%20%3F;VSICSpikeNAQM:double%20%3F;VSICConsistencyFailQM:double%20%3F;VSICConsistencyPassQM:double%20%3F;VSICConsistencyNAQM:double%20%3F;VSICAlphaQM:double%20%3F;VSICBetaQM:double%20%3F;VSICFinalQF:string%20%3F;tempQAQCRpt:string%20%3F;tempFailQM:double%20%3F;tempPassQM:double%20%3F;tempNAQM:double%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;calQAQCRpt:string%20%3F;calDefaultQM:double%20%3F;calNEONQM:double%20%3F;calNAQM:double%20%3F;VSICFinalQFSciRvw:string%20%3F;VSICValidCalFailQM:double%20%3F;VSICValidCalNAQM:double%20%3F;VSICValidCalPassQM:double%20%3F;VSICValidCalQAQCRpt:string%20%3F;VSWCFinalQFSciRvw:string%20%3F;VSWCValidCalFailQM:double%20%3F;VSWCValidCalNAQM:double%20%3F;VSWCValidCalPassQM:double%20%3F;VSWCValidCalQAQCRpt:string%20%3F])

## Attributes


### Own

 * [VSICAlphaQAQCRpt](VSICAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICAlphaQM](VSICAlphaQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [VSICBetaQAQCRpt](VSICBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICBetaQM](VSICBetaQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [VSICConsistencyFailQM](VSICConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICConsistencyNAQM](VSICConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICConsistencyPassQM](VSICConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICConsistencyQAQCRpt](VSICConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICExpUncert](VSICExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICFinalQF](VSICFinalQF.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [VSICFinalQFSciRvw](VSICFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [VSICGapFailQM](VSICGapFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICGapNAQM](VSICGapNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICGapPassQM](VSICGapPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICGapQAQCRpt](VSICGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [VSICMaximum](VSICMaximum.md)  <sub>OPT</sub>
    * Description: Maximum volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICMean](VSICMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICMinimum](VSICMinimum.md)  <sub>OPT</sub>
    * Description: Minimum volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICNullFailQM](VSICNullFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICNullNAQM](VSICNullNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICNullPassQM](VSICNullPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICNullQAQCRpt](VSICNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICNumPts](VSICNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICPersistenceFailQM](VSICPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICPersistenceNAQM](VSICPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICPersistencePassQM](VSICPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICPersistenceQAQCRpt](VSICPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICRangeFailQM](VSICRangeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICRangeNAQM](VSICRangeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICRangePassQM](VSICRangePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICRangeQAQCRpt](VSICRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICSpikeFailQM](VSICSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICSpikeNAQM](VSICSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICSpikePassQM](VSICSpikePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICSpikeQAQCRpt](VSICSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICStdErMean](VSICStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICStepFailQM](VSICStepFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICStepNAQM](VSICStepNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICStepPassQM](VSICStepPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICStepQAQCRpt](VSICStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICValidCalFailQM](VSICValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICValidCalNAQM](VSICValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICValidCalPassQM](VSICValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICValidCalQAQCRpt](VSICValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content QAQC report for the valid calibration check, which indicates whether the normalization cal is within the valid date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run)) and NEON.DOC.000007
    * range: [String](types/String.md)
 * [VSICVariance](VSICVariance.md)  <sub>OPT</sub>
    * Description: Variance in volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSWCAlphaQAQCRpt](VSWCAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCAlphaQM](VSWCAlphaQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [VSWCBetaQAQCRpt](VSWCBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCBetaQM](VSWCBetaQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [VSWCConsistencyFailQM](VSWCConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCConsistencyNAQM](VSWCConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCConsistencyPassQM](VSWCConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCConsistencyQAQCRpt](VSWCConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCExpUncert](VSWCExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCFinalQF](VSWCFinalQF.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [VSWCFinalQFSciRvw](VSWCFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [VSWCGapFailQM](VSWCGapFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCGapNAQM](VSWCGapNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCGapPassQM](VSWCGapPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCGapQAQCRpt](VSWCGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [VSWCMaximum](VSWCMaximum.md)  <sub>OPT</sub>
    * Description: Maximum volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCMean](VSWCMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCMinimum](VSWCMinimum.md)  <sub>OPT</sub>
    * Description: Minimum volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCNullFailQM](VSWCNullFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCNullNAQM](VSWCNullNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCNullPassQM](VSWCNullPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCNullQAQCRpt](VSWCNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCNumPts](VSWCNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCPersistenceFailQM](VSWCPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCPersistenceNAQM](VSWCPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCPersistencePassQM](VSWCPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCPersistenceQAQCRpt](VSWCPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCRangeFailQM](VSWCRangeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCRangeNAQM](VSWCRangeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCRangePassQM](VSWCRangePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCRangeQAQCRpt](VSWCRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCSpikeFailQM](VSWCSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCSpikeNAQM](VSWCSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCSpikePassQM](VSWCSpikePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCSpikeQAQCRpt](VSWCSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCStdErMean](VSWCStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCStepFailQM](VSWCStepFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCStepNAQM](VSWCStepNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCStepPassQM](VSWCStepPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCStepQAQCRpt](VSWCStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCValidCalFailQM](VSWCValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCValidCalNAQM](VSWCValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCValidCalPassQM](VSWCValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCValidCalQAQCRpt](VSWCValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content QAQC report for the valid calibration check, which indicates whether the normalization cal is within the valid date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run)) and NEON.DOC.000007
    * range: [String](types/String.md)
 * [VSWCVariance](VSWCVariance.md)  <sub>OPT</sub>
    * Description: Variance in volumetric soil water content
    * range: [Double](types/Double.md)
 * [calDefaultQM](calDefaultQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the occurrence of manufacturer default calibration coefficient outcomes of the calibration test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [calNAQM](calNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the calibration test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [calNEONQM](calNEONQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the occurrence of NEON site- and depth-specific calibration coefficient outcomes of the calibration test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [calQAQCRpt](calQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the calibration test, which indicates  the type of calibration coefficients used in the data product calculations, detailed in NEON.DOC.000007 (1=manufacturer default, 0=NEON site- and depth-specific, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
 * [tempFailQM](tempFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the temperature test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempNAQM](tempNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the temperature test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempPassQM](tempPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the temperature test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempQAQCRpt](tempQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the temperature test, which indicates  whether the temperature is high enough to make meaningful measurements, detailed in NEON.DOC.000007 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:SWS_1_minute |
| **In Subsets:** | | DP1.00094.001 |

