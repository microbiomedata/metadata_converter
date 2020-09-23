
# Type: profSndAux_L0prime




URI: [neon:ProfSndAuxL0prime](https://data.neonscience.org/ProfSndAuxL0prime)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ProfSndAuxL0prime&#124;valvCmd1:integer%20%3F;valvCmd2:integer%20%3F;valvCmd3:integer%20%3F;valvCmd4:integer%20%3F;measTypeCrdH2O:integer%20%3F;measTypeCrdCO2:integer%20%3F;qfValvIrga:integer%20%3F;measTypeIrga:integer%20%3F])

## Attributes


### Own

 * [measTypeCrdCO2](measTypeCrdCO2.md)  <sub>OPT</sub>
    * Description: Measurement type for PICARRO G2131-I cavity ring down isotopic analyzer (i.e., sampling or validation)
    * range: [Integer](types/Integer.md)
 * [measTypeCrdH2O](measTypeCrdH2O.md)  <sub>OPT</sub>
    * Description: Measurement type for PICARRO L2130-I cavity ring down isotopic analyzer (i.e., sampling or validation)
    * range: [Integer](types/Integer.md)
 * [measTypeIrga](measTypeIrga.md)  <sub>OPT</sub>
    * Description: Measurement type for LI-COR LI840A IRGA (i.e., sampling or validation or calibration)
    * range: [Integer](types/Integer.md)
 * [qfValvIrga](qfValvIrga.md)  <sub>OPT</sub>
    * Description: Flag indicates whether the system fails because IRGA vent valve is open (1=fail, 0=pass, -1=NA (i.e, could not be run)
    * range: [Integer](types/Integer.md)
 * [valvCmd1](valvCmd1.md)  <sub>OPT</sub>
    * Description: Solenoid valve 1 command (0 = close, 1 = open)
    * range: [Integer](types/Integer.md)
 * [valvCmd2](valvCmd2.md)  <sub>OPT</sub>
    * Description: Solenoid valve 2 command (0 = close, 1 = open)
    * range: [Integer](types/Integer.md)
 * [valvCmd3](valvCmd3.md)  <sub>OPT</sub>
    * Description: Solenoid valve 3 command (0 = close, 1 = open)
    * range: [Integer](types/Integer.md)
 * [valvCmd4](valvCmd4.md)  <sub>OPT</sub>
    * Description: Solenoid valve 4 command (0 = close, 1 = open)
    * range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:profSndAux_L0prime |
| **In Subsets:** | | IP0.00114.001 |

