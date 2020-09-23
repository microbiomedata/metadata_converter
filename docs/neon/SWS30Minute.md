
# Type: SWS_30_minute




URI: [neon:SWS30Minute](https://data.neonscience.org/SWS30Minute)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SWS30Minute&#124;VSWCMean:double%20%3F;VSWCMinimum:double%20%3F;VSWCMaximum:double%20%3F;VSWCVariance:double%20%3F;VSWCNumPts:double%20%3F;VSWCExpUncert:double%20%3F;VSWCStdErMean:double%20%3F;VSWCRangeFailQM:double%20%3F;VSWCRangePassQM:double%20%3F;VSWCRangeNAQM:double%20%3F;VSWCPersistenceFailQM:double%20%3F;VSWCPersistencePassQM:double%20%3F;VSWCPersistenceNAQM:double%20%3F;VSWCStepFailQM:double%20%3F;VSWCStepPassQM:double%20%3F;VSWCStepNAQM:double%20%3F;VSWCNullFailQM:double%20%3F;VSWCNullPassQM:double%20%3F;VSWCNullNAQM:double%20%3F;VSWCGapFailQM:double%20%3F;VSWCGapPassQM:double%20%3F;VSWCGapNAQM:double%20%3F;VSWCSpikeFailQM:double%20%3F;VSWCSpikePassQM:double%20%3F;VSWCSpikeNAQM:double%20%3F;VSWCConsistencyFailQM:double%20%3F;VSWCConsistencyPassQM:double%20%3F;VSWCConsistencyNAQM:double%20%3F;VSWCAlphaQM:double%20%3F;VSWCBetaQM:double%20%3F;VSWCFinalQF:string%20%3F;VSICMean:double%20%3F;VSICMinimum:double%20%3F;VSICMaximum:double%20%3F;VSICVariance:double%20%3F;VSICNumPts:double%20%3F;VSICExpUncert:double%20%3F;VSICStdErMean:double%20%3F;VSICRangeFailQM:double%20%3F;VSICRangePassQM:double%20%3F;VSICRangeNAQM:double%20%3F;VSICPersistenceFailQM:double%20%3F;VSICPersistencePassQM:double%20%3F;VSICPersistenceNAQM:double%20%3F;VSICStepFailQM:double%20%3F;VSICStepPassQM:double%20%3F;VSICStepNAQM:double%20%3F;VSICNullFailQM:double%20%3F;VSICNullPassQM:double%20%3F;VSICNullNAQM:double%20%3F;VSICGapFailQM:double%20%3F;VSICGapPassQM:double%20%3F;VSICGapNAQM:double%20%3F;VSICSpikeFailQM:double%20%3F;VSICSpikePassQM:double%20%3F;VSICSpikeNAQM:double%20%3F;VSICConsistencyFailQM:double%20%3F;VSICConsistencyPassQM:double%20%3F;VSICConsistencyNAQM:double%20%3F;VSICAlphaQM:double%20%3F;VSICBetaQM:double%20%3F;VSICFinalQF:string%20%3F;tempFailQM:double%20%3F;tempPassQM:double%20%3F;tempNAQM:double%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;calDefaultQM:double%20%3F;calNEONQM:double%20%3F;calNAQM:double%20%3F;VSICFinalQFSciRvw:string%20%3F;VSICValidCalFailQM:double%20%3F;VSICValidCalNAQM:double%20%3F;VSICValidCalPassQM:double%20%3F;VSWCFinalQFSciRvw:string%20%3F;VSWCValidCalFailQM:double%20%3F;VSWCValidCalNAQM:double%20%3F;VSWCValidCalPassQM:double%20%3F])

## Attributes


### Own

 * [VSICAlphaQM](VSICAlphaQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
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
 * [VSICRangeFailQM](VSICRangeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICRangeNAQM](VSICRangeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICRangePassQM](VSICRangePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICSpikeFailQM](VSICSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICSpikeNAQM](VSICSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICSpikePassQM](VSICSpikePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
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
 * [VSICValidCalFailQM](VSICValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICValidCalNAQM](VSICValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICValidCalPassQM](VSICValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICVariance](VSICVariance.md)  <sub>OPT</sub>
    * Description: Variance in volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSWCAlphaQM](VSWCAlphaQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
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
 * [VSWCRangeFailQM](VSWCRangeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCRangeNAQM](VSWCRangeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCRangePassQM](VSWCRangePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCSpikeFailQM](VSWCSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCSpikeNAQM](VSWCSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCSpikePassQM](VSWCSpikePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
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
 * [VSWCValidCalFailQM](VSWCValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCValidCalNAQM](VSWCValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCValidCalPassQM](VSWCValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:SWS_30_minute |

