
# Type: PRIPRE_5min




URI: [neon:PRIPRE5min](https://data.neonscience.org/PRIPRE5min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [exDeltaQF](exDeltaQF.md)  <sub>OPT</sub>
    * Description: Quality flag that indicates whether the depth change for any of the strain gauges was too extreme (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [gaugeNoiseQF](gaugeNoiseQF.md)  <sub>OPT</sub>
    * Description: Quality flag that indicates there was too much variability among the strain gauge measurements and precipitation was set to zero for a time interval (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [heaterErrorQF](heaterErrorQF.md)  <sub>OPT</sub>
    * Description: Quality flag that indicates whether the heaters were malfunctioning (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [lowDepthQF](lowDepthQF.md)  <sub>OPT</sub>
    * Description: Quality flag that that indicates whether one or more of the depth measurements from the strain gauges were too low, which is typically a sign of a broken strain gauge (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [missingWireInfoQF](missingWireInfoQF.md)  <sub>OPT</sub>
    * Description: Quality flag that indicates when measurements are invalid from two or more strain gauges and precipitation could not be calculated (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [overflowQF](overflowQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating the gauge was overflowing and precipitation could not be calculated (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [priPrecipValidCalQF](priPrecipValidCalQF.md)  <sub>OPT</sub>
    * Description: Primary precipitation quality flag for the valid calibration check detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [priorDepthQF](priorDepthQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether or not precipitation could calculated because the previous depth measurements were missing from two or more of the strain gauges (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [unstableQF](unstableQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether or not two or more strain gauges were stable to allow for precipitation to be calculated, (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [wire1StabilityFailQM](wire1StabilityFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 1 stability failed over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wire1StabilityNAQM](wire1StabilityNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 1 stability information was not available  over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wire1StabilityPassQM](wire1StabilityPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 1 stability passed over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wire1StabilitySearchQM](wire1StabilitySearchQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 1 was searching for stability over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wire2StabilityFailQM](wire2StabilityFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 2 stability failed over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wire2StabilityNAQM](wire2StabilityNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 2 stability information was not available  over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wire2StabilityPassQM](wire2StabilityPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 2 stability passed over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wire2StabilitySearchQM](wire2StabilitySearchQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 2 was searching for stability over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wire3StabilityFailQM](wire3StabilityFailQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 3 stability failed over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wire3StabilityNAQM](wire3StabilityNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 3 stability information was not available  over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wire3StabilityPassQM](wire3StabilityPassQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 3 stability passed over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wire3StabilitySearchQM](wire3StabilitySearchQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when strain gauge 3 was searching for stability over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [wireNoiseQF](wireNoiseQF.md)  <sub>OPT</sub>
    * Description: Quality flag that indicates whether one or more of the strain gauge's depth change was negative, resulting in setting precipitation to zero for a time interval (0 = pass, 1 = fail)
    * range: [String](types/String.md)

### Inherited from PRIPRE_30min:

 * [priPrecipBulk](priPrecipBulk.md)  <sub>OPT</sub>
    * Description: Bulk primary precipitation
    * range: [Double](types/Double.md)
 * [priPrecipExpUncert](priPrecipExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for primary precipitation
    * range: [Double](types/Double.md)
 * [priPrecipNullQF](priPrecipNullQF.md)  <sub>OPT</sub>
    * Description: Primary precipitation quality flag for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [inletHeaters1QM](inletHeaters1QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when one of the inlet heaters was on over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [inletHeaters2QM](inletHeaters2QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when two of the inlet heaters were on over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [inletHeaters3QM](inletHeaters3QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when all three of the inlet heaters were on over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [priPrecipFinalQF](priPrecipFinalQF.md)  <sub>OPT</sub>
    * Description: Primary precipitation quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.000898 (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [priPrecipNumPts](priPrecipNumPts.md)  <sub>OPT</sub>
    * Description: Number of five-minute bulk precipitation values that were used to compute the 30-minute bulk precipitation value
    * range: [Double](types/Double.md)
    * inherited from: None
 * [inletHeatersNAQM](inletHeatersNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when no heater information was available over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [priPrecipFinalQFSciRvw](priPrecipFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Primary precipitation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
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
| **Mappings:** | | neon:PRIPRE_5min |
| **In Subsets:** | | DP1.00006.001 |

