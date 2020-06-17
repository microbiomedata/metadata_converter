
# Type: profSnd_L0prime




URI: [neon:ProfSndL0prime](https://data.neonscience.org/ProfSndL0prime)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [injNum](injNum.md)  <sub>OPT</sub>
    * Description: injNum
    * range: [String](types/String.md)
 * [lvlCrdCO2](lvlCrdCO2.md)  <sub>OPT</sub>
    * Description: Measurement location (measurement level 1, measurement level 2, etc) that air is pulled from for the measurements by PICARRO G2131-I analyzer
    * range: [Integer](types/Integer.md)
 * [lvlCrdH2O](lvlCrdH2O.md)  <sub>OPT</sub>
    * Description: Measurement location (measurement level 1, measurement level 2, etc) that air is pulled from for the measurements by PICARRO L2130-I analyzer
    * range: [Integer](types/Integer.md)
 * [lvlIrga](lvlIrga.md)  <sub>OPT</sub>
    * Description: Measurement location (measurement level 1, measurement level 2, etc) that air is pulled from for the measurements by LI-COR LI840A IRGA
    * range: [Integer](types/Integer.md)
 * [typeGas](typeGas.md)  <sub>OPT</sub>
    * Description: The type of reference standard gas that is used for validation.
    * range: [String](types/String.md)
 * [typeGasCrdH2O](typeGasCrdH2O.md)  <sub>OPT</sub>
    * Description: The zero air gas status for crdH2O during L2130-I validation
    * range: [Integer](types/Integer.md)
 * [typeH2o](typeH2o.md)  <sub>OPT</sub>
    * Description: typeH2o
    * range: [String](types/String.md)
 * [valvStat1](valvStat1.md)  <sub>OPT</sub>
    * Description: Solenoid valve 1 status (0 = close, 1 = open)
    * range: [Integer](types/Integer.md)

### Inherited from profSnd:

 * [valvCmd5](valvCmd5.md)  <sub>OPT</sub>
    * Description: Solenoid valve 5 command (0 = close, 1 = open)
    * range: [Integer](types/Integer.md)
 * [valvCmd6](valvCmd6.md)  <sub>OPT</sub>
    * Description: Solenoid valve 6 command (0 = close, 1 = open)
    * range: [Integer](types/Integer.md)
 * [valvCmd7](valvCmd7.md)  <sub>OPT</sub>
    * Description: Solenoid valve 7 command (0 = close, 1 = open)
    * range: [Integer](types/Integer.md)
 * [valvCmd8](valvCmd8.md)  <sub>OPT</sub>
    * Description: Solenoid valve 8 command (0 = close, 1 = open)
    * range: [Integer](types/Integer.md)

### Inherited from profSndAux_L0prime:

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
 * [measTypeCrdH2O](measTypeCrdH2O.md)  <sub>OPT</sub>
    * Description: Measurement type for PICARRO L2130-I cavity ring down isotopic analyzer (i.e., sampling or validation)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [measTypeCrdCO2](measTypeCrdCO2.md)  <sub>OPT</sub>
    * Description: Measurement type for PICARRO G2131-I cavity ring down isotopic analyzer (i.e., sampling or validation)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfValvIrga](qfValvIrga.md)  <sub>OPT</sub>
    * Description: Flag indicates whether the system fails because IRGA vent valve is open (1=fail, 0=pass, -1=NA (i.e, could not be run)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [measTypeIrga](measTypeIrga.md)  <sub>OPT</sub>
    * Description: Measurement type for LI-COR LI840A IRGA (i.e., sampling or validation or calibration)
    * range: [Integer](types/Integer.md)
    * inherited from: None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:profSnd_L0prime |
| **In Subsets:** | | IP0.00115.001 |
|  | | IP0.00113.001 |

