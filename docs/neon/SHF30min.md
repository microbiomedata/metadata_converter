
# Type: SHF_30min




URI: [neon:SHF30min](https://data.neonscience.org/SHF30min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [SHFCalHeaterFailQM](SHFCalHeaterFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the calibration heater was on over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [SHFCalHeaterNAQM](SHFCalHeaterNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the calibration heater status was unknown over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [SHFCalHeaterOffMetric](SHFCalHeaterOffMetric.md)  <sub>OPT</sub>
    * Description: A metric that summarizes when the calibration heater was off over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [SHFCalHeaterOnMetric](SHFCalHeaterOnMetric.md)  <sub>OPT</sub>
    * Description: A metric that summarizes when the calibration heater was on over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [SHFCalHeaterPassQM](SHFCalHeaterPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the calibration heater was off over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [SHFCalHeaterQF](SHFCalHeaterQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether the calibration heater turned on correctly as described in the sensor specific algorithm theoretical basis document  (ATBD) (1=calibration heater failed to turn on, 0=calibration heater turned on correctly, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [SHFCalPeriodFlag](SHFCalPeriodFlag.md)  <sub>OPT</sub>
    * Description: Calibration period flag indicating when the sensor is operated under calibration period as described in the sensor specific algorithm theoretical basis document  (ATBD), (1=calibration period, 0=normal operating condition)
    * range: [Double](types/Double.md)
 * [SHFCalPeriodOffMetric](SHFCalPeriodOffMetric.md)  <sub>OPT</sub>
    * Description: A metric that summarizes when the sensor is operated under normal conditions over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [SHFCalPeriodOnMetric](SHFCalPeriodOnMetric.md)  <sub>OPT</sub>
    * Description: A metric that summarizes when the sensor is operated during a calibration period over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [SHFExpUncert](SHFExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for soil heat flux
    * range: [Double](types/Double.md)
 * [SHFInSituCorFailQM](SHFInSituCorFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when an error occur during the self-calibration process to determine the in situ correction factor over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [SHFInSituCorNAQM](SHFInSituCorNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when  the self-calibration process to determine the in situ correction factor was unknown over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [SHFInSituCorPassQM](SHFInSituCorPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when no error occur during the self-calibration process to determine the in situ correction factor over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [SHFInSituCorQF](SHFInSituCorQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether an error occur during the self-calibration process to determine the in situ correction factor as described in the sensor specific algorithm theoretical basis document  (ATBD) (1=error is detected, 0=no error, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [SHFMaximum](SHFMaximum.md)  <sub>OPT</sub>
    * Description: Maximum soil heat flux
    * range: [Double](types/Double.md)
 * [SHFMean](SHFMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of soil heat flux
    * range: [Double](types/Double.md)
 * [SHFMinimum](SHFMinimum.md)  <sub>OPT</sub>
    * Description: Minimum soil heat flux
    * range: [Double](types/Double.md)
 * [SHFNumPts](SHFNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of soil heat flux
    * range: [Double](types/Double.md)
 * [SHFStdErMean](SHFStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for soil heat flux
    * range: [Double](types/Double.md)
 * [SHFVariance](SHFVariance.md)  <sub>OPT</sub>
    * Description: Variance in soil heat flux
    * range: [Double](types/Double.md)

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

### Inherited from SHF:

 * [SHFVoltage](SHFVoltage.md)  <sub>OPT</sub>
    * Description: Soil heat flux sensor voltage	
    * range: [Double](types/Double.md)
    * inherited from: None
 * [SHFCalHeaterFlag](SHFCalHeaterFlag.md)  <sub>OPT</sub>
    * Description: Calibration heater flag indicating whether the heater was operational to perform a self-calibration (0 = off, 1 = on)	
    * range: [Double](types/Double.md)
 * [curVoltage](curVoltage.md)  <sub>OPT</sub>
    * Description: Voltage across the current sensing resistor	
    * range: [Double](types/Double.md)
    * inherited from: None

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:SHF_30min |

