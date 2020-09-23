
# Type: profMfcVali_L0prime




URI: [neon:ProfMfcValiL0prime](https://data.neonscience.org/ProfMfcValiL0prime)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ProfMfcValiL0prime&#124;presAtm:double%20%3F;temp:double%20%3F;frt:double%20%3F;frt0:double%20%3F;frtSet0:double%20%3F;qfFrt0:integer%20%3F])

## Attributes


### Own

 * [frt](frt.md)  <sub>OPT</sub>
    * Description: Flow rate (frt) at site temperature and pressure, synonymous with volumetric flow rate
    * range: [Double](types/Double.md)
 * [frt0](frt0.md)  <sub>OPT</sub>
    * Description: Flow rate (frt) at National Institute of Standards and Technology standard conditions (0, which are  293.15 K, 101.325 kPa), synonymous with mass flow rate
    * range: [Double](types/Double.md)
 * [frtSet0](frtSet0.md)  <sub>OPT</sub>
    * Description: Flow rate (frt) set point (Set) at National Institute of Standards and Technology standard conditions (0, which are 293.15 K, 101.325 kPa), synonymous with mass flow rate set point
    * range: [Double](types/Double.md)
 * [presAtm](presAtm.md)  <sub>OPT</sub>
    * Description: Pressure (pres), measured as atmospheric (Atm) pressure, synonymous with absolute pressure or total pressure (at sea level the standard atmospheric pressure is 101.325 kPa)
    * range: [Double](types/Double.md)
 * [qfFrt0](qfFrt0.md)  <sub>OPT</sub>
    * Description: Flag indicates whether the gas flow rate is within the acceptable tolerance (1=fail, 0=pass, -1=NA (i.e, could not be run))
    * range: [Integer](types/Integer.md)
 * [temp](temp.md)  <sub>OPT</sub>
    * Description: Temperature (temp)
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:profMfcVali_L0prime |
| **In Subsets:** | | IP0.00107.001 |

