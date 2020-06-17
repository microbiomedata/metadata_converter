
# Type: TSW_5min




URI: [neon:TSW5min](https://data.neonscience.org/TSW5min)


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

### Inherited from TAAT_1min:

 * [rangeQAQCRpt](rangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realisitc value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [persistenceQAQCRpt](persistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [stepQAQCRpt](stepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [nullQAQCRpt](nullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [gapQAQCRpt](gapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [consistencyQAQCRpt](consistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [spikeQAQCRpt](spikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [alphaQAQCRpt](alphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [betaQAQCRpt](betaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [flowQAQCRpt](flowQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the flow rate flag, which indicates whether the sensor is adequately aspirated, detailed in NEON.DOC.000646 and NEON.DOC.000654 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
    * inherited from: None
 * [tempAveQAQCRpt](tempAveQAQCRpt.md)  <sub>OPT</sub>
    * Description: Quality assurance and quality control report for the averaging flag (0=average of all three platinum resistor thermometers (PRTs); 1,2, 4, and 7=median of the three PRTs; 3,5, and 6=only two PRTs were used to compute the average), detailed in NEON.DOC.000654
    * range: [String](types/String.md)
    * inherited from: None
 * [validCalQAQCRpt](validCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)

### Inherited from TAAT_30min:

 * [rangeFailQM](rangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [rangePassQM](rangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [rangeNAQM](rangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [persistenceFailQM](persistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [persistencePassQM](persistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [persistenceNAQM](persistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [stepFailQM](stepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [stepPassQM](stepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [stepNAQM](stepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [nullFailQM](nullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [nullPassQM](nullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [nullNAQM](nullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gapFailQM](gapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gapPassQM](gapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gapNAQM](gapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [spikeFailQM](spikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [spikePassQM](spikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [spikeNAQM](spikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [consistencyFailQM](consistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [consistencyPassQM](consistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [consistencyNAQM](consistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [flowFailQM](flowFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the flow rate test over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [flowPassQM](flowPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the flow rate test over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [flowNAQM](flowNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the flow rate test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [alphaQM](alphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [betaQM](betaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [finalQF](finalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [tempTripleMean](tempTripleMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of triple aspirated air temperature
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempTripleMinimum](tempTripleMinimum.md)  <sub>OPT</sub>
    * Description: Minimum triple aspirated air temperature
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempTripleMaximum](tempTripleMaximum.md)  <sub>OPT</sub>
    * Description: Maximum triple aspirated air temperature
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempTripleVariance](tempTripleVariance.md)  <sub>OPT</sub>
    * Description: Variance in triple aspirated air temperature
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempTripleNumPts](tempTripleNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of triple aspirated air temperature
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempTripleExpUncert](tempTripleExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for triple aspirated air temperature
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempTripleStdErMean](tempTripleStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for triple aspirated air temperature
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempAve0QM](tempAve0QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the averaging flag was set to 0 over the averaging period, as a percent and detailed in NEON.DOC.000654
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempAve1QM](tempAve1QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the averaging flag was set to 1 over the averaging period, as a percent and detailed in NEON.DOC.000654
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempAve2QM](tempAve2QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the averaging flag was set to 2 over the averaging period, as a percent and detailed in NEON.DOC.000654
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempAve3QM](tempAve3QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the averaging flag was set to 3 over the averaging period, as a percent and detailed in NEON.DOC.000654
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempAve4QM](tempAve4QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the averaging flag was set to 4 over the averaging period, as a percent and detailed in NEON.DOC.000654
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempAve5QM](tempAve5QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the averaging flag was set to 5 over the averaging period, as a percent and detailed in NEON.DOC.000654
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempAve6QM](tempAve6QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the averaging flag was set to 6 over the averaging period, as a percent and detailed in NEON.DOC.000654
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempAve7QM](tempAve7QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the averaging flag was set to 7 over the averaging period, as a percent and detailed in NEON.DOC.000654
    * range: [Double](types/Double.md)
    * inherited from: None
 * [finalQFSciRvw](finalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)

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

### Inherited from TSW_30min:

 * [surfWaterTempExpUncert](surfWaterTempExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for temperature of surface water in degrees celsius
    * range: [Double](types/Double.md)
 * [surfWaterTempMean](surfWaterTempMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of temperature of surface water in degrees celsius
    * range: [Double](types/Double.md)
 * [surfWaterTempMinimum](surfWaterTempMinimum.md)  <sub>OPT</sub>
    * Description: Minimum temperature of surface water in degrees celsius
    * range: [Double](types/Double.md)
 * [surfWaterTempMaximum](surfWaterTempMaximum.md)  <sub>OPT</sub>
    * Description: Maximum temperature of surface water in degrees celsius
    * range: [Double](types/Double.md)
 * [surfWaterTempVariance](surfWaterTempVariance.md)  <sub>OPT</sub>
    * Description: Variance in temperature of surface water in degrees celsius
    * range: [Double](types/Double.md)
 * [surfWaterTempNumPts](surfWaterTempNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of temperature of surface water in degrees celsius
    * range: [Double](types/Double.md)
 * [surfWaterTempStdErMean](surfWaterTempStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for temperature of surface water in degrees celsius
    * range: [Double](types/Double.md)

### Inherited from dpsd_60_minutes:

 * [PM15Median](PM15Median.md)  <sub>OPT</sub>
    * Description: Median particulate matter 15
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15Minimum](PM15Minimum.md)  <sub>OPT</sub>
    * Description: Minimum particulate matter 15
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15Maximum](PM15Maximum.md)  <sub>OPT</sub>
    * Description: Maximum particulate matter 15
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15NumPts](PM15NumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the Median particulate matter 15
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15MAD](PM15MAD.md)  <sub>OPT</sub>
    * Description: Median Absolute Deviation (from the median) for particulate matter 15
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15rangeFailQM](PM15rangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15rangePassQM](PM15rangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15rangeNAQM](PM15rangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for particulate matter 15 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15persistenceFailQM](PM15persistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15persistencePassQM](PM15persistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15persistenceNAQM](PM15persistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for particulate matter 15 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15stepFailQM](PM15stepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15stepPassQM](PM15stepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15stepNAQM](PM15stepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for particulate matter 15 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15nullFailQM](PM15nullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15nullPassQM](PM15nullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15nullNAQM](PM15nullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for particulate matter 15 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15gapFailQM](PM15gapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15gapPassQM](PM15gapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15gapNAQM](PM15gapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for particulate matter 15 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15spikeFailQM](PM15spikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15spikePassQM](PM15spikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15spikeNAQM](PM15spikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for particulate matter 15 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15consistencyFailQM](PM15consistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15consistencyPassQM](PM15consistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for particulate matter 15 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15consistencyNAQM](PM15consistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for particulate matter 15 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15alphaQM](PM15alphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for particulate matter 15 over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15betaQM](PM15betaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for particulate matter 15 over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15finalQF](PM15finalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the PM15 data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM10Median](PM10Median.md)  <sub>OPT</sub>
    * Description: Median particulate matter 10
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10Minimum](PM10Minimum.md)  <sub>OPT</sub>
    * Description: Minimum particulate matter 10
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10Maximum](PM10Maximum.md)  <sub>OPT</sub>
    * Description: Maximum particulate matter 10
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10NumPts](PM10NumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the Median particulate matter 10
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10MAD](PM10MAD.md)  <sub>OPT</sub>
    * Description: Median Absolute Deviation (from the median) for particulate matter 10
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10rangeFailQM](PM10rangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10rangePassQM](PM10rangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10rangeNAQM](PM10rangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for particulate matter 10 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10persistenceFailQM](PM10persistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10persistencePassQM](PM10persistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10persistenceNAQM](PM10persistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for particulate matter 10 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10stepFailQM](PM10stepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10stepPassQM](PM10stepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10stepNAQM](PM10stepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for particulate matter 10 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10nullFailQM](PM10nullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10nullPassQM](PM10nullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10nullNAQM](PM10nullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for particulate matter 10 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10gapFailQM](PM10gapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10gapPassQM](PM10gapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10gapNAQM](PM10gapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for particulate matter 10 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10spikeFailQM](PM10spikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10spikePassQM](PM10spikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10spikeNAQM](PM10spikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for particulate matter 10 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10consistencyFailQM](PM10consistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10consistencyPassQM](PM10consistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for particulate matter 10 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10consistencyNAQM](PM10consistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for particulate matter 10 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10alphaQM](PM10alphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for particulate matter 10 over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10betaQM](PM10betaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for particulate matter 10 over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10finalQF](PM10finalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the PM10 data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM4Median](PM4Median.md)  <sub>OPT</sub>
    * Description: Median particulate matter 4
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4Minimum](PM4Minimum.md)  <sub>OPT</sub>
    * Description: Minimum particulate matter 4
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4Maximum](PM4Maximum.md)  <sub>OPT</sub>
    * Description: Maximum particulate matter 4
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4NumPts](PM4NumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the Median particulate matter 4
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4MAD](PM4MAD.md)  <sub>OPT</sub>
    * Description: Median Absolute Deviation (from the median) for particulate matter 4
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4rangeFailQM](PM4rangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4rangePassQM](PM4rangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4rangeNAQM](PM4rangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for particulate matter 4 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4persistenceFailQM](PM4persistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4persistencePassQM](PM4persistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4persistenceNAQM](PM4persistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for particulate matter 4 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4stepFailQM](PM4stepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4stepPassQM](PM4stepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4stepNAQM](PM4stepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for particulate matter 4 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4nullFailQM](PM4nullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4nullPassQM](PM4nullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4nullNAQM](PM4nullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for particulate matter 4 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4gapFailQM](PM4gapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4gapPassQM](PM4gapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4gapNAQM](PM4gapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for particulate matter 4 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4spikeFailQM](PM4spikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4spikePassQM](PM4spikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4spikeNAQM](PM4spikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for particulate matter 4 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4consistencyFailQM](PM4consistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4consistencyPassQM](PM4consistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for particulate matter 4 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4consistencyNAQM](PM4consistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for particulate matter 4 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4alphaQM](PM4alphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for particulate matter 4 over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4betaQM](PM4betaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for particulate matter 4 over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4finalQF](PM4finalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the PM4 data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM2.5Median](PM2.5Median.md)  <sub>OPT</sub>
    * Description: Median particulate matter 2.5
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5Minimum](PM2.5Minimum.md)  <sub>OPT</sub>
    * Description: Minimum particulate matter 2.5
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5Maximum](PM2.5Maximum.md)  <sub>OPT</sub>
    * Description: Maximum particulate matter 2.5
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5NumPts](PM2.5NumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the Median particulate matter 2.5
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5MAD](PM2.5MAD.md)  <sub>OPT</sub>
    * Description: Median Absolute Deviation (from the median) for particulate matter 2.5
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5rangeFailQM](PM2.5rangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5rangePassQM](PM2.5rangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5rangeNAQM](PM2.5rangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for particulate matter 2.5 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5persistenceFailQM](PM2.5persistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5persistencePassQM](PM2.5persistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5persistenceNAQM](PM2.5persistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for particulate matter 2.5 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5stepFailQM](PM2.5stepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5stepPassQM](PM2.5stepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5stepNAQM](PM2.5stepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for particulate matter 2.5 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5nullFailQM](PM2.5nullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5nullPassQM](PM2.5nullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5nullNAQM](PM2.5nullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for particulate matter 2.5 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5gapFailQM](PM2.5gapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5gapPassQM](PM2.5gapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5gapNAQM](PM2.5gapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for particulate matter 2.5 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5spikeFailQM](PM2.5spikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5spikePassQM](PM2.5spikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5spikeNAQM](PM2.5spikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for particulate matter 2.5 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5consistencyFailQM](PM2.5consistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5consistencyPassQM](PM2.5consistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for particulate matter 2.5 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5consistencyNAQM](PM2.5consistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for particulate matter 2.5 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5alphaQM](PM2.5alphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for particulate matter 2.5 over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5betaQM](PM2.5betaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for particulate matter 2.5 over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5finalQF](PM2.5finalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the PM2.5 data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM1Median](PM1Median.md)  <sub>OPT</sub>
    * Description: Median particulate matter 1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1Minimum](PM1Minimum.md)  <sub>OPT</sub>
    * Description: Minimum particulate matter 1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1Maximum](PM1Maximum.md)  <sub>OPT</sub>
    * Description: Maximum particulate matter 1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1NumPts](PM1NumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the Median particulate matter 1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1MAD](PM1MAD.md)  <sub>OPT</sub>
    * Description: Median Absolute Deviation (from the median) for particulate matter 1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1rangeFailQM](PM1rangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1rangePassQM](PM1rangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1rangeNAQM](PM1rangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for particulate matter 1 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1persistenceFailQM](PM1persistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1persistencePassQM](PM1persistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1persistenceNAQM](PM1persistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for particulate matter 1 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1stepFailQM](PM1stepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1stepPassQM](PM1stepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1stepNAQM](PM1stepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for particulate matter 1 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1nullFailQM](PM1nullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1nullPassQM](PM1nullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1nullNAQM](PM1nullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for particulate matter 1 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1gapFailQM](PM1gapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1gapPassQM](PM1gapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1gapNAQM](PM1gapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for particulate matter 1 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1spikeFailQM](PM1spikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1spikePassQM](PM1spikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1spikeNAQM](PM1spikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for particulate matter 1 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1consistencyFailQM](PM1consistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1consistencyPassQM](PM1consistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for particulate matter 1 over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1consistencyNAQM](PM1consistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for particulate matter 1 could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1alphaQM](PM1alphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for particulate matter 1 over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1betaQM](PM1betaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for particulate matter 1 over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1finalQF](PM1finalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the PM1 data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM15sub50RHMedian](PM15sub50RHMedian.md)  <sub>OPT</sub>
    * Description: Median of particulate matter 15 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHMinimum](PM15sub50RHMinimum.md)  <sub>OPT</sub>
    * Description: Minimum particulate matter 15 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHMaximum](PM15sub50RHMaximum.md)  <sub>OPT</sub>
    * Description: Maximum particulate matter 15 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHNumPts](PM15sub50RHNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the Median of particulate matter 15 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHMAD](PM15sub50RHMAD.md)  <sub>OPT</sub>
    * Description: Median Absolute Deviation (from the median) for particulate matter 15 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHrangeFailQM](PM15sub50RHrangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHrangePassQM](PM15sub50RHrangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHrangeNAQM](PM15sub50RHrangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for PM15 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHpersistenceFailQM](PM15sub50RHpersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHpersistencePassQM](PM15sub50RHpersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHpersistenceNAQM](PM15sub50RHpersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for PM15 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHstepFailQM](PM15sub50RHstepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHstepPassQM](PM15sub50RHstepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHstepNAQM](PM15sub50RHstepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for PM15 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHnullFailQM](PM15sub50RHnullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHnullPassQM](PM15sub50RHnullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHnullNAQM](PM15sub50RHnullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for PM15 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHgapFailQM](PM15sub50RHgapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHgapPassQM](PM15sub50RHgapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHgapNAQM](PM15sub50RHgapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for PM15 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHspikeFailQM](PM15sub50RHspikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHspikePassQM](PM15sub50RHspikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHspikeNAQM](PM15sub50RHspikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for PM15 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHconsistencyFailQM](PM15sub50RHconsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHconsistencyPassQM](PM15sub50RHconsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for PM15 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHconsistencyNAQM](PM15sub50RHconsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for PM15 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHalphaQM](PM15sub50RHalphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for PM15 at RH <50% over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHbetaQM](PM15sub50RHbetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for PM15 at RH <50% over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM15sub50RHfinalQF](PM15sub50RHfinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the PM15 at RH <50% data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM10sub50RHMedian](PM10sub50RHMedian.md)  <sub>OPT</sub>
    * Description: Median of particulate matter 10 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHMinimum](PM10sub50RHMinimum.md)  <sub>OPT</sub>
    * Description: Minimum particulate matter 10 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHMaximum](PM10sub50RHMaximum.md)  <sub>OPT</sub>
    * Description: Maximum particulate matter 10 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHNumPts](PM10sub50RHNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the Median of particulate matter 10 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHMAD](PM10sub50RHMAD.md)  <sub>OPT</sub>
    * Description: Median Absolute Deviation (from the median) for particulate matter 10 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHrangeFailQM](PM10sub50RHrangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHrangePassQM](PM10sub50RHrangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHrangeNAQM](PM10sub50RHrangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for PM10 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHpersistenceFailQM](PM10sub50RHpersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHpersistencePassQM](PM10sub50RHpersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHpersistenceNAQM](PM10sub50RHpersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for PM10 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHstepFailQM](PM10sub50RHstepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHstepPassQM](PM10sub50RHstepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHstepNAQM](PM10sub50RHstepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for PM10 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHnullFailQM](PM10sub50RHnullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHnullPassQM](PM10sub50RHnullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHnullNAQM](PM10sub50RHnullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for PM10 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHgapFailQM](PM10sub50RHgapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHgapPassQM](PM10sub50RHgapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHgapNAQM](PM10sub50RHgapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for PM10 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHspikeFailQM](PM10sub50RHspikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHspikePassQM](PM10sub50RHspikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHspikeNAQM](PM10sub50RHspikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for PM10 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHconsistencyFailQM](PM10sub50RHconsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHconsistencyPassQM](PM10sub50RHconsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for PM10 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHconsistencyNAQM](PM10sub50RHconsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for PM10 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHalphaQM](PM10sub50RHalphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for PM10 at RH <50% over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHbetaQM](PM10sub50RHbetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for PM10 at RH <50% over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM10sub50RHfinalQF](PM10sub50RHfinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the PM10 at RH <50% data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM4sub50RHMedian](PM4sub50RHMedian.md)  <sub>OPT</sub>
    * Description: Median of particulate matter 4 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHMinimum](PM4sub50RHMinimum.md)  <sub>OPT</sub>
    * Description: Minimum particulate matter 4 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHMaximum](PM4sub50RHMaximum.md)  <sub>OPT</sub>
    * Description: Maximum particulate matter 4 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHNumPts](PM4sub50RHNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the Median of particulate matter 4 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHMAD](PM4sub50RHMAD.md)  <sub>OPT</sub>
    * Description: Median Absolute Deviation (from the median) for particulate matter 4 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHrangeFailQM](PM4sub50RHrangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHrangePassQM](PM4sub50RHrangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHrangeNAQM](PM4sub50RHrangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for PM4 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHpersistenceFailQM](PM4sub50RHpersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHpersistencePassQM](PM4sub50RHpersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHpersistenceNAQM](PM4sub50RHpersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for PM4 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHstepFailQM](PM4sub50RHstepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHstepPassQM](PM4sub50RHstepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHstepNAQM](PM4sub50RHstepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for PM4 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHnullFailQM](PM4sub50RHnullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHnullPassQM](PM4sub50RHnullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHnullNAQM](PM4sub50RHnullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for PM4 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHgapFailQM](PM4sub50RHgapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHgapPassQM](PM4sub50RHgapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHgapNAQM](PM4sub50RHgapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for PM4 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHspikeFailQM](PM4sub50RHspikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHspikePassQM](PM4sub50RHspikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHspikeNAQM](PM4sub50RHspikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for PM4 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHconsistencyFailQM](PM4sub50RHconsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHconsistencyPassQM](PM4sub50RHconsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for PM4 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHconsistencyNAQM](PM4sub50RHconsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for PM4 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHalphaQM](PM4sub50RHalphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for PM4 at RH <50% over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHbetaQM](PM4sub50RHbetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for PM4 at RH <50% over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM4sub50RHfinalQF](PM4sub50RHfinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the PM4 at RH <50% data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM2.5sub50RHMedian](PM2.5sub50RHMedian.md)  <sub>OPT</sub>
    * Description: Median of particulate matter 2.5 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHMinimum](PM2.5sub50RHMinimum.md)  <sub>OPT</sub>
    * Description: Minimum particulate matter 2.5 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHMaximum](PM2.5sub50RHMaximum.md)  <sub>OPT</sub>
    * Description: Maximum particulate matter 2.5 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHNumPts](PM2.5sub50RHNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the Median of particulate matter 2.5 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHMAD](PM2.5sub50RHMAD.md)  <sub>OPT</sub>
    * Description: Median Absolute Deviation (from the median) for particulate matter 2.5 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHrangeFailQM](PM2.5sub50RHrangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHrangePassQM](PM2.5sub50RHrangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHrangeNAQM](PM2.5sub50RHrangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for PM2.5 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHpersistenceFailQM](PM2.5sub50RHpersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHpersistencePassQM](PM2.5sub50RHpersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHpersistenceNAQM](PM2.5sub50RHpersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for PM2.5 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHstepFailQM](PM2.5sub50RHstepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHstepPassQM](PM2.5sub50RHstepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHstepNAQM](PM2.5sub50RHstepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for PM2.5 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHnullFailQM](PM2.5sub50RHnullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHnullPassQM](PM2.5sub50RHnullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHnullNAQM](PM2.5sub50RHnullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for PM2.5 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHgapFailQM](PM2.5sub50RHgapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHgapPassQM](PM2.5sub50RHgapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHgapNAQM](PM2.5sub50RHgapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for PM2.5 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHspikeFailQM](PM2.5sub50RHspikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHspikePassQM](PM2.5sub50RHspikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHspikeNAQM](PM2.5sub50RHspikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for PM2.5 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHconsistencyFailQM](PM2.5sub50RHconsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHconsistencyPassQM](PM2.5sub50RHconsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for PM2.5 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHconsistencyNAQM](PM2.5sub50RHconsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for PM2.5 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHalphaQM](PM2.5sub50RHalphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for PM2.5 at RH <50% over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHbetaQM](PM2.5sub50RHbetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for PM2.5 at RH <50% over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM2.5sub50RHfinalQF](PM2.5sub50RHfinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the PM2.5 at RH <50% data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM1sub50RHMedian](PM1sub50RHMedian.md)  <sub>OPT</sub>
    * Description: Median of particulate matter 1 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHMinimum](PM1sub50RHMinimum.md)  <sub>OPT</sub>
    * Description: Minimum particulate matter 1 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHMaximum](PM1sub50RHMaximum.md)  <sub>OPT</sub>
    * Description: Maximum particulate matter 1 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHNumPts](PM1sub50RHNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the Median of particulate matter 1 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHMAD](PM1sub50RHMAD.md)  <sub>OPT</sub>
    * Description: Median Absolute Deviation (from the median) for particulate matter 1 measured at <50% relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHrangeFailQM](PM1sub50RHrangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHrangePassQM](PM1sub50RHrangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHrangeNAQM](PM1sub50RHrangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test for PM1 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHpersistenceFailQM](PM1sub50RHpersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHpersistencePassQM](PM1sub50RHpersistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHpersistenceNAQM](PM1sub50RHpersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test for PM1 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHstepFailQM](PM1sub50RHstepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHstepPassQM](PM1sub50RHstepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHstepNAQM](PM1sub50RHstepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test for PM1 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHnullFailQM](PM1sub50RHnullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHnullPassQM](PM1sub50RHnullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHnullNAQM](PM1sub50RHnullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test for PM1 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHgapFailQM](PM1sub50RHgapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHgapPassQM](PM1sub50RHgapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHgapNAQM](PM1sub50RHgapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test for PM1 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHspikeFailQM](PM1sub50RHspikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHspikePassQM](PM1sub50RHspikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHspikeNAQM](PM1sub50RHspikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test for PM1 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHconsistencyFailQM](PM1sub50RHconsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHconsistencyPassQM](PM1sub50RHconsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test for PM1 at RH <50% over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHconsistencyNAQM](PM1sub50RHconsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test for PM1 at RH <50% could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHalphaQM](PM1sub50RHalphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag for PM1 at RH <50% over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHbetaQM](PM1sub50RHbetaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag for PM1 at RH <50% over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
    * inherited from: None
 * [PM1sub50RHfinalQF](PM1sub50RHfinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the PM1 at RH <50% data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [sensorFlowRateFailQM](sensorFlowRateFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the sensor flow rate test over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sensorFlowRatePassQM](sensorFlowRatePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the sensor flow rate test over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sensorFlowRateNAQM](sensorFlowRateNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the sensor flow rate test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [assemblyFlowRateFailQM](assemblyFlowRateFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the assembly flow rate test over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [assemblyFlowRatePassQM](assemblyFlowRatePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the assembly flow rate test over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [assemblyFlowRateNAQM](assemblyFlowRateNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the assembly flow rate test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [measurementValidityFailQM](measurementValidityFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the measurement validity test over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [measurementValidityPassQM](measurementValidityPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the measurement validity test over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [measurementValidityNAQM](measurementValidityNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the measurement validity test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
    * inherited from: None
 * [validCalFailQM](validCalFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [validCalNAQM](validCalNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [validCalPassQM](validCalPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [PM15finalQFSciRvw](PM15finalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Particulate matter 15 quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM10finalQFSciRvw](PM10finalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Particulate matter 10 quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM10sub50RHfinalQFSciRvw](PM10sub50RHfinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: PM10 at RH <50% quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM15sub50RHfinalQFSciRvw](PM15sub50RHfinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: PM15 at RH <50% quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM1finalQFSciRvw](PM1finalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Particulate matter 1 quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM1sub50RHfinalQFSciRvw](PM1sub50RHfinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: PM1 at RH <50% quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM2.5finalQFSciRvw](PM2.5finalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Particulate matter 2.5 quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM2.5sub50RHfinalQFSciRvw](PM2.5sub50RHfinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: PM2.5 at RH <50% quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM4finalQFSciRvw](PM4finalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Particulate matter 4 quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [PM4sub50RHfinalQFSciRvw](PM4sub50RHfinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: PM4 at RH <50% quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:TSW_5min |
| **In Subsets:** | | DP1.20053.001 |

