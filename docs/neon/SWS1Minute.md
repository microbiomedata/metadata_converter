
# Type: SWS_1_minute




URI: [neon:SWS1Minute](https://data.neonscience.org/SWS1Minute)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [VSICAlphaQAQCRpt](VSICAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICBetaQAQCRpt](VSICBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICConsistencyQAQCRpt](VSICConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICGapQAQCRpt](VSICGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [VSICNullQAQCRpt](VSICNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICPersistenceQAQCRpt](VSICPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICRangeQAQCRpt](VSICRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICSpikeQAQCRpt](VSICSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICStepQAQCRpt](VSICStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSICValidCalQAQCRpt](VSICValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content QAQC report for the valid calibration check, which indicates whether the normalization cal is within the valid date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run)) and NEON.DOC.000007
    * range: [String](types/String.md)
 * [VSWCAlphaQAQCRpt](VSWCAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCBetaQAQCRpt](VSWCBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCConsistencyQAQCRpt](VSWCConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCGapQAQCRpt](VSWCGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [VSWCNullQAQCRpt](VSWCNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCPersistenceQAQCRpt](VSWCPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCRangeQAQCRpt](VSWCRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCSpikeQAQCRpt](VSWCSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCStepQAQCRpt](VSWCStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [VSWCValidCalQAQCRpt](VSWCValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content QAQC report for the valid calibration check, which indicates whether the normalization cal is within the valid date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run)) and NEON.DOC.000007
    * range: [String](types/String.md)
 * [calQAQCRpt](calQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the calibration test, which indicates  the type of calibration coefficients used in the data product calculations, detailed in NEON.DOC.000007 (1=manufacturer default, 0=NEON site- and depth-specific, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [tempQAQCRpt](tempQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the temperature test, which indicates  whether the temperature is high enough to make meaningful measurements, detailed in NEON.DOC.000007 (1=fail, 0=pass, -1=NA (i.e., could not be run))
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

### Inherited from SWS_30_minute:

 * [VSWCMean](VSWCMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCMinimum](VSWCMinimum.md)  <sub>OPT</sub>
    * Description: Minimum volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCMaximum](VSWCMaximum.md)  <sub>OPT</sub>
    * Description: Maximum volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCVariance](VSWCVariance.md)  <sub>OPT</sub>
    * Description: Variance in volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCNumPts](VSWCNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCExpUncert](VSWCExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCStdErMean](VSWCStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for volumetric soil water content
    * range: [Double](types/Double.md)
 * [VSWCRangeFailQM](VSWCRangeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCRangePassQM](VSWCRangePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCRangeNAQM](VSWCRangeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCPersistenceFailQM](VSWCPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCPersistencePassQM](VSWCPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCPersistenceNAQM](VSWCPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCStepFailQM](VSWCStepFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCStepPassQM](VSWCStepPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCStepNAQM](VSWCStepNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCNullFailQM](VSWCNullFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCNullPassQM](VSWCNullPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCNullNAQM](VSWCNullNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCGapFailQM](VSWCGapFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCGapPassQM](VSWCGapPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCGapNAQM](VSWCGapNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCSpikeFailQM](VSWCSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCSpikePassQM](VSWCSpikePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCSpikeNAQM](VSWCSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCConsistencyFailQM](VSWCConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCConsistencyPassQM](VSWCConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCConsistencyNAQM](VSWCConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSWCAlphaQM](VSWCAlphaQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [VSWCBetaQM](VSWCBetaQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [VSWCFinalQF](VSWCFinalQF.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [VSICMean](VSICMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICMinimum](VSICMinimum.md)  <sub>OPT</sub>
    * Description: Minimum volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICMaximum](VSICMaximum.md)  <sub>OPT</sub>
    * Description: Maximum volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICVariance](VSICVariance.md)  <sub>OPT</sub>
    * Description: Variance in volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICNumPts](VSICNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICExpUncert](VSICExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICStdErMean](VSICStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for volumetric soil ion content
    * range: [Double](types/Double.md)
 * [VSICRangeFailQM](VSICRangeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICRangePassQM](VSICRangePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICRangeNAQM](VSICRangeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICPersistenceFailQM](VSICPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICPersistencePassQM](VSICPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICPersistenceNAQM](VSICPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICStepFailQM](VSICStepFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICStepPassQM](VSICStepPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICStepNAQM](VSICStepNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICNullFailQM](VSICNullFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICNullPassQM](VSICNullPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICNullNAQM](VSICNullNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICGapFailQM](VSICGapFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICGapPassQM](VSICGapPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICGapNAQM](VSICGapNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICSpikeFailQM](VSICSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICSpikePassQM](VSICSpikePassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICSpikeNAQM](VSICSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICConsistencyFailQM](VSICConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICConsistencyPassQM](VSICConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICConsistencyNAQM](VSICConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICAlphaQM](VSICAlphaQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [VSICBetaQM](VSICBetaQM.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [VSICFinalQF](VSICFinalQF.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [tempFailQM](tempFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the temperature test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempPassQM](tempPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the temperature test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [tempNAQM](tempNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the temperature test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [calDefaultQM](calDefaultQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the occurrence of manufacturer default calibration coefficient outcomes of the calibration test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [calNEONQM](calNEONQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the occurrence of NEON site- and depth-specific calibration coefficient outcomes of the calibration test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [calNAQM](calNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the calibration test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [VSICFinalQFSciRvw](VSICFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Volumetric soil ion content quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
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
 * [VSWCFinalQFSciRvw](VSWCFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Volumetric soil water content quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
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
| **Mappings:** | | neon:SWS_1_minute |
| **In Subsets:** | | DP1.00094.001 |

