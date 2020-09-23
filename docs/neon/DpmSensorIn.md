
# Type: dpm_sensor_in




URI: [neon:DpmSensorIn](https://data.neonscience.org/DpmSensorIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DpmSensorIn&#124;sensorTemp:double%20%3F;baroPressParticulateMass:double%20%3F;flowRate:double%20%3F;corrAirVolume:double%20%3F;uncorrAirVolume:double%20%3F])

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
 * [sensorTemp](sensorTemp.md)  <sub>OPT</sub>
    * Description: Temperature of sensor
    * range: [Double](types/Double.md)
 * [uncorrAirVolume](uncorrAirVolume.md)  <sub>OPT</sub>
    * Description: Accumulated sample air volume, uncorrected 
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:dpm_sensor_in |
| **In Subsets:** | | DP0.00101.001 |

