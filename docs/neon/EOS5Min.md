
# Type: EOS_5_min




URI: [neon:EOS5Min](https://data.neonscience.org/EOS5Min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[EOS5Min&#124;startDateTime:time%20%3F;endDateTime:time%20%3F;surfacewaterElevMean:double%20%3F;surfacewaterElevMinimum:double%20%3F;surfacewaterElevMaximum:double%20%3F;surfacewaterElevVariance:double%20%3F;surfacewaterElevNumPts:double%20%3F;surfacewaterElevExpUncert:double%20%3F;surfacewaterElevStdErMean:double%20%3F;sWatElevRangeFailQM:double%20%3F;sWatElevRangePassQM:double%20%3F;sWatElevRangeNAQM:double%20%3F;sWatElevPersistenceFailQM:double%20%3F;sWatElevPersistencePassQM:double%20%3F;sWatElevPersistenceNAQM:double%20%3F;sWatElevStepFailQM:double%20%3F;sWatElevStepPassQM:double%20%3F;sWatElevStepNAQM:double%20%3F;sWatElevNullFailQM:double%20%3F;sWatElevNullPassQM:double%20%3F;sWatElevNullNAQM:double%20%3F;sWatElevGapFailQM:double%20%3F;sWatElevGapPassQM:double%20%3F;sWatElevGapNAQM:double%20%3F;sWatElevSpikeFailQM:double%20%3F;sWatElevSpikePassQM:double%20%3F;sWatElevSpikeNAQM:double%20%3F;sWatElevConsistencyFailQM:double%20%3F;sWatElevConsistencyPassQM:double%20%3F;sWatElevConsistencyNAQM:double%20%3F;sWatElevAlphaQM:double%20%3F;sWatElevBetaQM:double%20%3F;sWatElevFinalQF:string%20%3F;validCalFailQM:double%20%3F;validCalNAQM:double%20%3F;validCalPassQM:double%20%3F;tempRHValidCalQAQCRpt:string%20%3F;sWatElevFinalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [sWatElevAlphaQM](sWatElevAlphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for elevation of surfacewater over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [sWatElevBetaQM](sWatElevBetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for elevation of surfacewater over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [sWatElevConsistencyFailQM](sWatElevConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevConsistencyNAQM](sWatElevConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevConsistencyPassQM](sWatElevConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevFinalQF](sWatElevFinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether elevation of surfacewater has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [sWatElevFinalQFSciRvw](sWatElevFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Suface water elevation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [sWatElevGapFailQM](sWatElevGapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevGapNAQM](sWatElevGapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevGapPassQM](sWatElevGapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevNullFailQM](sWatElevNullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevNullNAQM](sWatElevNullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevNullPassQM](sWatElevNullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevPersistenceFailQM](sWatElevPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the persistence test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevPersistenceNAQM](sWatElevPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevPersistencePassQM](sWatElevPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevRangeFailQM](sWatElevRangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevRangeNAQM](sWatElevRangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevRangePassQM](sWatElevRangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevSpikeFailQM](sWatElevSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevSpikeNAQM](sWatElevSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevSpikePassQM](sWatElevSpikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevStepFailQM](sWatElevStepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevStepNAQM](sWatElevStepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for elevation of surfacewater could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sWatElevStepPassQM](sWatElevStepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for elevation of surfacewater over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
 * [surfacewaterElevExpUncert](surfacewaterElevExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for elevation of surfacewater
    * range: [Double](types/Double.md)
 * [surfacewaterElevMaximum](surfacewaterElevMaximum.md)  <sub>OPT</sub>
    * Description: Maximum elevation of surfacewater
    * range: [Double](types/Double.md)
 * [surfacewaterElevMean](surfacewaterElevMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of elevation of surfacewater
    * range: [Double](types/Double.md)
 * [surfacewaterElevMinimum](surfacewaterElevMinimum.md)  <sub>OPT</sub>
    * Description: Minimum elevation of surfacewater
    * range: [Double](types/Double.md)
 * [surfacewaterElevNumPts](surfacewaterElevNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of elevation of surfacewater
    * range: [Double](types/Double.md)
 * [surfacewaterElevStdErMean](surfacewaterElevStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for elevation of surfacewater
    * range: [Double](types/Double.md)
 * [surfacewaterElevVariance](surfacewaterElevVariance.md)  <sub>OPT</sub>
    * Description: Variance in elevation of surfacewater
    * range: [Double](types/Double.md)
 * [tempRHValidCalQAQCRpt](tempRHValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Temperature measures by RH sensor QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [validCalFailQM](validCalFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [validCalNAQM](validCalNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [validCalPassQM](validCalPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:EOS_5_min |
| **In Subsets:** | | DP1.20016.001 |

