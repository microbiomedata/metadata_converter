
# Type: dpm_sensor_in




URI: [neon:DpmSensorIn](https://data.neonscience.org/DpmSensorIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [baroPressParticulateMass](baroPressParticulateMass.md)  <sub>OPT</sub>
    * Description: Barometric pressure measurements for proper pressure compensation to ensure constant flow rate	
    * range: [Double](types/Double.md)
 * [corrAirVolume](corrAirVolume.md)  <sub>OPT</sub>
    * Description: Accumulated sample air volume, corrected to standard conditions of temperature and pressure of 298 K (25 degrees C) and 101.3 kPa (760mm Hg)
    * range: [Double](types/Double.md)
 * [flowRate](flowRate.md)  <sub>OPT</sub>
    * Description: Flow rate in cubic meters per hour
    * range: [Double](types/Double.md)
 * [uncorrAirVolume](uncorrAirVolume.md)  <sub>OPT</sub>
    * Description: Accumulated sample air volume, uncorrected 
    * range: [Double](types/Double.md)

### Inherited from RH_L0prime:

 * [sensorTemp](sensorTemp.md)  <sub>OPT</sub>
    * Description: Temperature of sensor
    * range: [Double](types/Double.md)
 * [RH](RH.md)  <sub>OPT</sub>
    * Description: Relative humidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [dewPoint](dewPoint.md)  <sub>OPT</sub>
    * Description: Dew point temperature
    * range: [Double](types/Double.md)
    * inherited from: None
 * [RHStatus](RHStatus.md)  <sub>OPT</sub>
    * Description: Status of the relative humidity sensor
    * range: [Double](types/Double.md)
    * inherited from: None
 * [qfHeat](qfHeat.md)  <sub>OPT</sub>
    * Description: Heater quality flag (L0 prime processing ATBD)
    * range: [Integer](types/Integer.md)
    * inherited from: None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:dpm_sensor_in |
| **In Subsets:** | | DP0.00101.001 |

