
# Type: hutEnv_L0prime




URI: [neon:HutEnvL0prime](https://data.neonscience.org/HutEnvL0prime)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[HutEnvL0prime&#124;tempHut:double%20%3F;RHHut:double%20%3F;baroPresHut:double%20%3F;H2OMixRatioHut:double%20%3F;qfTemp:string%20%3F;qfRh:integer%20%3F])

## Attributes


### Own

 * [H2OMixRatioHut](H2OMixRatioHut.md)  <sub>OPT</sub>
    * Description: Mixing ratio of water vapor (H2O) in the instrument hut
    * range: [Double](types/Double.md)
 * [RHHut](RHHut.md)  <sub>OPT</sub>
    * Description: Humidity in the instrument hut
    * range: [Double](types/Double.md)
 * [baroPresHut](baroPresHut.md)  <sub>OPT</sub>
    * Description: Barometric pressure in the instrument hut
    * range: [Double](types/Double.md)
 * [qfRh](qfRh.md)  <sub>OPT</sub>
    * Description: Flag indicates whether the temperature is outside the acceptable rangle (1=fail, 0=pass, -1=NA (i.e, could not be run))
    * range: [Integer](types/Integer.md)
 * [qfTemp](qfTemp.md)  <sub>OPT</sub>
    * Description: qfTemp
    * range: [String](types/String.md)
 * [tempHut](tempHut.md)  <sub>OPT</sub>
    * Description: Temperature in the instrument hut
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:hutEnv_L0prime |
| **In Subsets:** | | IP0.00104.001 |

