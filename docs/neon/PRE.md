
# Type: PRE




URI: [neon:PRE](https://data.neonscience.org/PRE)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PRE&#124;secPrecipBucketTips:integer%20%3F;TFPrecipBucketTips:integer%20%3F;strainGauge1Stability:integer%20%3F;strainGauge1Temp:double%20%3F;strainGauge1FreqRaw:double%20%3F;strainGauge1Weight:double%20%3F;totalGaugeWeight:double%20%3F;totalPrecipDepth:double%20%3F;inletTemp:double%20%3F;internalTemp:double%20%3F;precipAccumulationRate:double%20%3F;strainGauge1FreqComp:double%20%3F;orificeHeaterFlag:integer%20%3F;strainGauge2Stability:integer%20%3F;strainGauge3Stability:integer%20%3F;strainGauge2Temp:double%20%3F;strainGauge3Temp:double%20%3F;strainGauge2FreqRaw:double%20%3F;strainGauge3FreqRaw:double%20%3F;strainGauge2Weight:double%20%3F;strainGauge3Weight:double%20%3F;strainGauge2FreqComp:double%20%3F;strainGauge3FreqComp:double%20%3F;heaterMonitor:double%20%3F])

## Attributes


### Own

 * [TFPrecipBucketTips](TFPrecipBucketTips.md)  <sub>OPT</sub>
    * Description: Indicator of throughfall precipitation bucket tips
    * range: [Integer](types/Integer.md)
 * [heaterMonitor](heaterMonitor.md)  <sub>OPT</sub>
    * Description: Heater sensed current which is reported in voltage using a scale factor of 4.6A/V
    * range: [Double](types/Double.md)
 * [inletTemp](inletTemp.md)  <sub>OPT</sub>
    * Description: The inlet orifice temperature, which is monitored to control orifice heater operation for the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [internalTemp](internalTemp.md)  <sub>OPT</sub>
    * Description: Ambient temperature inside the sensor, which is monitored to control orifice heater operation for the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [orificeHeaterFlag](orificeHeaterFlag.md)  <sub>OPT</sub>
    * Description: Heater flag indicating the number of orifice heaters that were operational for a measurement period, (i.e., 000 = off, 100 = one on, 110 = two on, and 111 = all three on)
    * range: [Integer](types/Integer.md)
 * [precipAccumulationRate](precipAccumulationRate.md)  <sub>OPT</sub>
    * Description: Accumulation of precipitation calculated by internal calculations of the 3 strain gauges in the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [secPrecipBucketTips](secPrecipBucketTips.md)  <sub>OPT</sub>
    * Description: Indicator of secondary precipitation bucket tip
    * range: [Integer](types/Integer.md)
 * [strainGauge1FreqComp](strainGauge1FreqComp.md)  <sub>OPT</sub>
    * Description: The temperature compensated frequency reported by strain gauge 1 in the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [strainGauge1FreqRaw](strainGauge1FreqRaw.md)  <sub>OPT</sub>
    * Description: The raw frequency reported by strain gauge 1 in the primary precipitation sensor (i.e., uncompensated for temperature)
    * range: [Double](types/Double.md)
 * [strainGauge1Stability](strainGauge1Stability.md)  <sub>OPT</sub>
    * Description: Stability flag indicating if strain gauge 1 in the primary precipitation sensor is reporting a stable frequency (1 = stable, 0 = unstable, -1 = sensor failure)
    * range: [Integer](types/Integer.md)
 * [strainGauge1Temp](strainGauge1Temp.md)  <sub>OPT</sub>
    * Description: Strain gauge 1 transducer temperature in the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [strainGauge1Weight](strainGauge1Weight.md)  <sub>OPT</sub>
    * Description: The weight reported by strain gauge 1 in the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [strainGauge2FreqComp](strainGauge2FreqComp.md)  <sub>OPT</sub>
    * Description: The temperature compensated frequency reported by strain gauge 2 in the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [strainGauge2FreqRaw](strainGauge2FreqRaw.md)  <sub>OPT</sub>
    * Description: The raw frequency reported by strain gauge 2 in the primary precipitation sensor (i.e., uncompensated for temperature)
    * range: [Double](types/Double.md)
 * [strainGauge2Stability](strainGauge2Stability.md)  <sub>OPT</sub>
    * Description: Stability flag indicating if strain gauge 2 in the primary precipitation sensor is reporting a stable frequency (1 = stable, 0 = unstable, -1 = sensor failure)
    * range: [Integer](types/Integer.md)
 * [strainGauge2Temp](strainGauge2Temp.md)  <sub>OPT</sub>
    * Description: Strain gauge 2 transducer temperature in the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [strainGauge2Weight](strainGauge2Weight.md)  <sub>OPT</sub>
    * Description: The weight reported by strain gauge 2 in the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [strainGauge3FreqComp](strainGauge3FreqComp.md)  <sub>OPT</sub>
    * Description: The temperature compensated frequency reported by strain gauge 3 in the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [strainGauge3FreqRaw](strainGauge3FreqRaw.md)  <sub>OPT</sub>
    * Description: The raw frequency reported by strain gauge 3 in the primary precipitation sensor (i.e., uncompensated for temperature)
    * range: [Double](types/Double.md)
 * [strainGauge3Stability](strainGauge3Stability.md)  <sub>OPT</sub>
    * Description: Stability flag indicating if strain gauge 3 in the primary precipitation sensor is reporting a stable frequency (1 = stable, 0 = unstable, -1 = sensor failure)
    * range: [Integer](types/Integer.md)
 * [strainGauge3Temp](strainGauge3Temp.md)  <sub>OPT</sub>
    * Description: Strain gauge 3 transducer temperature in the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [strainGauge3Weight](strainGauge3Weight.md)  <sub>OPT</sub>
    * Description: The weight reported by strain gauge 3 in the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [totalGaugeWeight](totalGaugeWeight.md)  <sub>OPT</sub>
    * Description: The combined weight from the 3 strain gauges in the primary precipitation sensor
    * range: [Double](types/Double.md)
 * [totalPrecipDepth](totalPrecipDepth.md)  <sub>OPT</sub>
    * Description: The total depth reported by the internal calculations of the 3 strain gauges in the primary precipitation sensor
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:PRE |
| **In Subsets:** | | DP0.00006.001 |

