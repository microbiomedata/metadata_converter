
# Type: SCO2C_30_minute




URI: [neon:SCO2C30Minute](https://data.neonscience.org/SCO2C30Minute)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SCO2C30Minute&#124;rangeFailQM:double%20%3F;rangePassQM:double%20%3F;rangeNAQM:double%20%3F;persistenceFailQM:double%20%3F;persistencePassQM:double%20%3F;persistenceNAQM:double%20%3F;stepFailQM:double%20%3F;stepPassQM:double%20%3F;stepNAQM:double%20%3F;nullFailQM:double%20%3F;nullPassQM:double%20%3F;nullNAQM:double%20%3F;gapFailQM:double%20%3F;gapPassQM:double%20%3F;gapNAQM:double%20%3F;spikeFailQM:double%20%3F;spikePassQM:double%20%3F;spikeNAQM:double%20%3F;consistencyFailQM:double%20%3F;consistencyPassQM:double%20%3F;consistencyNAQM:double%20%3F;alphaQM:double%20%3F;betaQM:double%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;soilCO2concentrationMean:double%20%3F;soilCO2concentrationMinimum:double%20%3F;soilCO2concentrationMaximum:double%20%3F;soilCO2concentrationVariance:double%20%3F;soilCO2concentrationNumPts:double%20%3F;soilCO2concentrationExpUncert:double%20%3F;soilCO2concentrationStdErMean:double%20%3F;warmUpInstallationFailQM:double%20%3F;warmUpInstallationPassQM:double%20%3F;warmUpInstallationNAQM:double%20%3F;sensorErrorStatusFailQM:double%20%3F;sensorErrorStatusPassQM:double%20%3F;sensorErrorStatusNAQM:double%20%3F;temperatureSCO2FailQM:double%20%3F;temperatureSCO2PassQM:double%20%3F;temperatureSCO2NAQM:double%20%3F;pressureRangeFailQM:double%20%3F;pressureRangePassQM:double%20%3F;pressureRangeNAQM:double%20%3F;soilCO2FinalQF:string%20%3F;validCalFailQM:double%20%3F;validCalNAQM:double%20%3F;validCalPassQM:double%20%3F;finalQFSciRvw:string%20%3F])

## Attributes


### Own

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
 * [pressureRangeFailQM](pressureRangeFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the pressure range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [pressureRangeNAQM](pressureRangeNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the pressure range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [pressureRangePassQM](pressureRangePassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the pressure range test over the averaging period, as a percent
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
 * [sensorErrorStatusFailQM](sensorErrorStatusFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the sensor error status test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sensorErrorStatusNAQM](sensorErrorStatusNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the sensor error status test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [sensorErrorStatusPassQM](sensorErrorStatusPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the sensor error status test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [soilCO2FinalQF](soilCO2FinalQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether a soil CO2 data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [soilCO2concentrationExpUncert](soilCO2concentrationExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for Soil CO2 concentration adjusted for temperature, pressure, oxygen, and humidity conditions
    * range: [Double](types/Double.md)
 * [soilCO2concentrationMaximum](soilCO2concentrationMaximum.md)  <sub>OPT</sub>
    * Description: Maximum Soil CO2 concentration adjusted for temperature, pressure, oxygen, and humidity conditions
    * range: [Double](types/Double.md)
 * [soilCO2concentrationMean](soilCO2concentrationMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of Soil CO2 concentration adjusted for temperature, pressure, oxygen, and humidity conditions
    * range: [Double](types/Double.md)
 * [soilCO2concentrationMinimum](soilCO2concentrationMinimum.md)  <sub>OPT</sub>
    * Description: Minimum Soil CO2 concentration adjusted for temperature, pressure, oxygen, and humidity conditions
    * range: [Double](types/Double.md)
 * [soilCO2concentrationNumPts](soilCO2concentrationNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of Soil CO2 concentration adjusted for temperature, pressure, oxygen, and humidity conditions
    * range: [Double](types/Double.md)
 * [soilCO2concentrationStdErMean](soilCO2concentrationStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for Soil CO2 concentration adjusted for temperature, pressure, oxygen, and humidity conditions
    * range: [Double](types/Double.md)
 * [soilCO2concentrationVariance](soilCO2concentrationVariance.md)  <sub>OPT</sub>
    * Description: Variance in Soil CO2 concentration adjusted for temperature, pressure, oxygen, and humidity conditions
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
 * [temperatureSCO2FailQM](temperatureSCO2FailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the SCO2 temperature test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [temperatureSCO2NAQM](temperatureSCO2NAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the SCO2 temperature test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [temperatureSCO2PassQM](temperatureSCO2PassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the SCO2 temperature test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [validCalFailQM](validCalFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [validCalNAQM](validCalNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [validCalPassQM](validCalPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [warmUpInstallationFailQM](warmUpInstallationFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the failed outcomes of the warm-up and installation test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [warmUpInstallationNAQM](warmUpInstallationNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when the warm-up and installation test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [warmUpInstallationPassQM](warmUpInstallationPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes the passed outcomes of the warm-up and installation test over the averaging period, as a percent
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:SCO2C_30_minute |

