
# Type: BP_30min




URI: [neon:BP30min](https://data.neonscience.org/BP30min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BP30min&#124;staPresMean:double%20%3F;staPresMinimum:double%20%3F;staPresMaximum:double%20%3F;staPresVariance:double%20%3F;staPresNumPts:double%20%3F;staPresExpUncert:double%20%3F;staPresStdErMean:double%20%3F;staPresRangeFailQM:double%20%3F;staPresRangePassQM:double%20%3F;staPresRangeNAQM:double%20%3F;staPresPersistenceFailQM:double%20%3F;staPresPersistencePassQM:double%20%3F;staPresPersistenceNAQM:double%20%3F;staPresStepFailQM:double%20%3F;staPresStepPassQM:double%20%3F;staPresStepNAQM:double%20%3F;staPresNullFailQM:double%20%3F;staPresNullPassQM:double%20%3F;staPresNullNAQM:double%20%3F;staPresGapFailQM:double%20%3F;staPresGapPassQM:double%20%3F;staPresGapNAQM:double%20%3F;staPresSpikeFailQM:double%20%3F;staPresSpikePassQM:double%20%3F;staPresSpikeNAQM:double%20%3F;staPresConsistencyFailQM:double%20%3F;staPresConsistencyPassQM:double%20%3F;staPresConsistencyNAQM:double%20%3F;staPresAlphaQM:double%20%3F;staPresBetaQM:double%20%3F;staPresFinalQF:string%20%3F;corPres:double%20%3F;corPresExpUncert:double%20%3F;corPresFinalQF:string%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;corPresTempQF:string%20%3F;corPresDewPtQF:string%20%3F;staPresValidCalFailQM:double%20%3F;staPresValidCalNAQM:double%20%3F;staPresValidCalPassQM:double%20%3F;corPresFinalQFSciRvw:string%20%3F;staPresFinalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [corPres](corPres.md)  <sub>OPT</sub>
    * Description: Mean station pressure corrected to sea level
    * range: [Double](types/Double.md)
 * [corPresDewPtQF](corPresDewPtQF.md)  <sub>OPT</sub>
    * Description: Corrected pressure quality flag that assesses whether dew point measurements for correcting pressure were available (0=yes, 1=no)
    * range: [String](types/String.md)
 * [corPresExpUncert](corPresExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for pressure corrected to sea level
    * range: [Double](types/Double.md)
 * [corPresFinalQF](corPresFinalQF.md)  <sub>OPT</sub>
    * Description: Pressure corrected to sea level quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.000653 and NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [corPresFinalQFSciRvw](corPresFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Pressure corrected to sea level quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [corPresTempQF](corPresTempQF.md)  <sub>OPT</sub>
    * Description: Corrected pressure quality flag that assesses whether temperature measurements for correcting pressure were available (0=yes, 1=no)
    * range: [String](types/String.md)
 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [staPresAlphaQM](staPresAlphaQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [staPresBetaQM](staPresBetaQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [staPresConsistencyFailQM](staPresConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresConsistencyNAQM](staPresConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresConsistencyPassQM](staPresConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresExpUncert](staPresExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for station pressure
    * range: [Double](types/Double.md)
 * [staPresFinalQF](staPresFinalQF.md)  <sub>OPT</sub>
    * Description: Station pressure quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [staPresFinalQFSciRvw](staPresFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Station pressure quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [staPresGapFailQM](staPresGapFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresGapNAQM](staPresGapNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresGapPassQM](staPresGapPassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresMaximum](staPresMaximum.md)  <sub>OPT</sub>
    * Description: Maximum station pressure
    * range: [Double](types/Double.md)
 * [staPresMean](staPresMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of station pressure
    * range: [Double](types/Double.md)
 * [staPresMinimum](staPresMinimum.md)  <sub>OPT</sub>
    * Description: Minimum station pressure
    * range: [Double](types/Double.md)
 * [staPresNullFailQM](staPresNullFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresNullNAQM](staPresNullNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresNullPassQM](staPresNullPassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresNumPts](staPresNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of station pressure
    * range: [Double](types/Double.md)
 * [staPresPersistenceFailQM](staPresPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresPersistenceNAQM](staPresPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresPersistencePassQM](staPresPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresRangeFailQM](staPresRangeFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresRangeNAQM](staPresRangeNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresRangePassQM](staPresRangePassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresSpikeFailQM](staPresSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresSpikeNAQM](staPresSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresSpikePassQM](staPresSpikePassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresStdErMean](staPresStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for station pressure
    * range: [Double](types/Double.md)
 * [staPresStepFailQM](staPresStepFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresStepNAQM](staPresStepNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresStepPassQM](staPresStepPassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresValidCalFailQM](staPresValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresValidCalNAQM](staPresValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresValidCalPassQM](staPresValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Station pressure quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [staPresVariance](staPresVariance.md)  <sub>OPT</sub>
    * Description: Variance in station pressure
    * range: [Double](types/Double.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:BP_30min |

