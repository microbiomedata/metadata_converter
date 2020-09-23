
# Type: PARWS_1min




URI: [neon:PARWS1min](https://data.neonscience.org/PARWS1min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PARWS1min&#124;PARMean:double%20%3F;PARMinimum:double%20%3F;PARMaximum:double%20%3F;PARVariance:double%20%3F;PARNumPts:double%20%3F;PARExpUncert:double%20%3F;PARStdErMean:double%20%3F;PARRangeQAQCRpt:string%20%3F;PARPersistenceQAQCRpt:string%20%3F;PARStepQAQCRpt:string%20%3F;PARNullQAQCRpt:string%20%3F;PARGapQAQCRpt:string%20%3F;PARSpikeQAQCRpt:string%20%3F;PARAlphaQAQCRpt:string%20%3F;PARBetaQAQCRpt:string%20%3F;PARRangeFailQM:double%20%3F;PARRangePassQM:double%20%3F;PARRangeNAQM:double%20%3F;PARPersistenceFailQM:double%20%3F;PARPersistencePassQM:double%20%3F;PARPersistenceNAQM:double%20%3F;PARStepFailQM:double%20%3F;PARStepPassQM:double%20%3F;PARStepNAQM:double%20%3F;PARNullFailQM:double%20%3F;PARNullPassQM:double%20%3F;PARNullNAQM:double%20%3F;PARGapFailQM:double%20%3F;PARGapPassQM:double%20%3F;PARGapNAQM:double%20%3F;PARSpikeFailQM:double%20%3F;PARSpikePassQM:double%20%3F;PARSpikeNAQM:double%20%3F;PARAlphaQM:double%20%3F;PARBetaQM:double%20%3F;PARFinalQF:string%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;PARValidCalQAQCRpt:string%20%3F;PARValidCalPassQM:double%20%3F;PARValidCalNAQM:double%20%3F;PARValidCalFailQM:double%20%3F;PARFinalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [PARAlphaQAQCRpt](PARAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARAlphaQM](PARAlphaQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [PARBetaQAQCRpt](PARBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARBetaQM](PARBetaQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [PARExpUncert](PARExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARFinalQF](PARFinalQF.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [PARFinalQFSciRvw](PARFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [PARGapFailQM](PARGapFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARGapNAQM](PARGapNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARGapPassQM](PARGapPassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARGapQAQCRpt](PARGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [PARMaximum](PARMaximum.md)  <sub>OPT</sub>
    * Description: Maximum photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARMean](PARMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARMinimum](PARMinimum.md)  <sub>OPT</sub>
    * Description: Minimum photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARNullFailQM](PARNullFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARNullNAQM](PARNullNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARNullPassQM](PARNullPassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARNullQAQCRpt](PARNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARNumPts](PARNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARPersistenceFailQM](PARPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARPersistenceNAQM](PARPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARPersistencePassQM](PARPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARPersistenceQAQCRpt](PARPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARRangeFailQM](PARRangeFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARRangeNAQM](PARRangeNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARRangePassQM](PARRangePassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARRangeQAQCRpt](PARRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARSpikeFailQM](PARSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARSpikeNAQM](PARSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARSpikePassQM](PARSpikePassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARSpikeQAQCRpt](PARSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARStdErMean](PARStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [PARStepFailQM](PARStepFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARStepNAQM](PARStepNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARStepPassQM](PARStepPassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARStepQAQCRpt](PARStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARValidCalFailQM](PARValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARValidCalNAQM](PARValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARValidCalPassQM](PARValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PARValidCalQAQCRpt](PARValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Photosynthetically active radiation QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [PARVariance](PARVariance.md)  <sub>OPT</sub>
    * Description: Variance in photosynthetically active radiation
    * range: [Double](types/Double.md)
 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:PARWS_1min |
| **In Subsets:** | | DP1.20042.001 |

