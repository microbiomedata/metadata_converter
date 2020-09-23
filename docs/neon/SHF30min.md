
# Type: SHF_30min




URI: [neon:SHF30min](https://data.neonscience.org/SHF30min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SHF30min&#124;rangeFailQM:double%20%3F;rangePassQM:double%20%3F;rangeNAQM:double%20%3F;persistenceFailQM:double%20%3F;persistencePassQM:double%20%3F;persistenceNAQM:double%20%3F;stepFailQM:double%20%3F;stepPassQM:double%20%3F;stepNAQM:double%20%3F;nullFailQM:double%20%3F;nullPassQM:double%20%3F;nullNAQM:double%20%3F;gapFailQM:double%20%3F;gapPassQM:double%20%3F;gapNAQM:double%20%3F;spikeFailQM:double%20%3F;spikePassQM:double%20%3F;spikeNAQM:double%20%3F;consistencyFailQM:double%20%3F;consistencyPassQM:double%20%3F;consistencyNAQM:double%20%3F;alphaQM:double%20%3F;betaQM:double%20%3F;finalQF:string%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;SHFCalHeaterFlag:double%20%3F;SHFMean:double%20%3F;SHFMinimum:double%20%3F;SHFMaximum:double%20%3F;SHFVariance:double%20%3F;SHFNumPts:double%20%3F;SHFExpUncert:double%20%3F;SHFStdErMean:double%20%3F;SHFCalHeaterQF:integer%20%3F;SHFCalPeriodFlag:double%20%3F;SHFInSituCorQF:integer%20%3F;SHFCalHeaterOnMetric:double%20%3F;SHFCalHeaterOffMetric:double%20%3F;SHFCalHeaterFailQM:double%20%3F;SHFCalHeaterPassQM:double%20%3F;SHFCalHeaterNAQM:double%20%3F;SHFCalPeriodOnMetric:double%20%3F;SHFCalPeriodOffMetric:double%20%3F;SHFInSituCorFailQM:double%20%3F;SHFInSituCorPassQM:double%20%3F;SHFInSituCorNAQM:double%20%3F;finalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [SHFCalHeaterFailQM](SHFCalHeaterFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the calibration heater was on over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [SHFCalHeaterFlag](SHFCalHeaterFlag.md)  <sub>OPT</sub>
    * Description: Calibration heater flag indicating whether the heater was operational to perform a self-calibration (0 = off, 1 = on)	
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
 * [alphaQM](alphaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [betaQM](betaQM.md)  <sub>OPT</sub>
    * Description: Quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [consistencyFailQM](consistencyFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [consistencyNAQM](consistencyNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [consistencyPassQM](consistencyPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [finalQF](finalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [finalQFSciRvw](finalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [gapFailQM](gapFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gapNAQM](gapNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [gapPassQM](gapPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [nullFailQM](nullFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [nullNAQM](nullNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [nullPassQM](nullPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [persistenceFailQM](persistenceFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [persistenceNAQM](persistenceNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [persistencePassQM](persistencePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [rangeFailQM](rangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [rangeNAQM](rangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [rangePassQM](rangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [spikeFailQM](spikeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [spikeNAQM](spikeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [spikePassQM](spikePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
 * [stepFailQM](stepFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [stepNAQM](stepNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [stepPassQM](stepPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:SHF_30min |

