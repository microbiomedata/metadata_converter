
# Type: PRIPRE_5min




URI: [neon:PRIPRE5min](https://data.neonscience.org/PRIPRE5min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PRIPRE5min&#124;priPrecipBulk:double%20%3F;priPrecipExpUncert:double%20%3F;priPrecipNullQF:integer%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;wire1StabilityPassQM:double%20%3F;wire1StabilitySearchQM:double%20%3F;wire1StabilityFailQM:double%20%3F;wire2StabilityPassQM:double%20%3F;wire2StabilitySearchQM:double%20%3F;wire2StabilityFailQM:double%20%3F;wire3StabilityPassQM:double%20%3F;wire3StabilitySearchQM:double%20%3F;wire3StabilityFailQM:double%20%3F;inletHeaters1QM:double%20%3F;inletHeaters2QM:double%20%3F;inletHeaters3QM:double%20%3F;priorDepthQF:string%20%3F;unstableQF:string%20%3F;lowDepthQF:string%20%3F;exDeltaQF:string%20%3F;missingWireInfoQF:string%20%3F;gaugeNoiseQF:string%20%3F;wireNoiseQF:string%20%3F;overflowQF:string%20%3F;heaterErrorQF:string%20%3F;priPrecipFinalQF:string%20%3F;wire1StabilityNAQM:double%20%3F;wire2StabilityNAQM:double%20%3F;wire3StabilityNAQM:double%20%3F;inletHeatersNAQM:double%20%3F;priPrecipFinalQFSciRvw:string%20%3F;priPrecipValidCalQF:integer%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [exDeltaQF](exDeltaQF.md)  <sub>OPT</sub>
    * Description: Quality flag that indicates whether the depth change for any of the strain gauges was too extreme (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [gaugeNoiseQF](gaugeNoiseQF.md)  <sub>OPT</sub>
    * Description: Quality flag that indicates there was too much variability among the strain gauge measurements and precipitation was set to zero for a time interval (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [heaterErrorQF](heaterErrorQF.md)  <sub>OPT</sub>
    * Description: Quality flag that indicates whether the heaters were malfunctioning (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [inletHeaters1QM](inletHeaters1QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when one of the inlet heaters was on over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [inletHeaters2QM](inletHeaters2QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when two of the inlet heaters were on over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [inletHeaters3QM](inletHeaters3QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when all three of the inlet heaters were on over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [inletHeatersNAQM](inletHeatersNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when no heater information was available over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [lowDepthQF](lowDepthQF.md)  <sub>OPT</sub>
    * Description: Quality flag that that indicates whether one or more of the depth measurements from the strain gauges were too low, which is typically a sign of a broken strain gauge (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [missingWireInfoQF](missingWireInfoQF.md)  <sub>OPT</sub>
    * Description: Quality flag that indicates when measurements are invalid from two or more strain gauges and precipitation could not be calculated (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [overflowQF](overflowQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating the gauge was overflowing and precipitation could not be calculated (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [priPrecipBulk](priPrecipBulk.md)  <sub>OPT</sub>
    * Description: Bulk primary precipitation
    * range: [Double](types/Double.md)
 * [priPrecipExpUncert](priPrecipExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for primary precipitation
    * range: [Double](types/Double.md)
 * [priPrecipFinalQF](priPrecipFinalQF.md)  <sub>OPT</sub>
    * Description: Primary precipitation quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.000898 (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [priPrecipFinalQFSciRvw](priPrecipFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Primary precipitation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [priPrecipNullQF](priPrecipNullQF.md)  <sub>OPT</sub>
    * Description: Primary precipitation quality flag for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [priPrecipValidCalQF](priPrecipValidCalQF.md)  <sub>OPT</sub>
    * Description: Primary precipitation quality flag for the valid calibration check detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [priorDepthQF](priorDepthQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating whether or not precipitation could calculated because the previous depth measurements were missing from two or more of the strain gauges (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:PRIPRE_5min |
| **In Subsets:** | | DP1.00006.001 |

