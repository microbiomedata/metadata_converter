
# Type: DPSD




URI: [neon:DPSD](https://data.neonscience.org/DPSD)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [flowRateMassFM](flowRateMassFM.md)  <sub>OPT</sub>
    * Description: Mass flow rate from flow meter at NIST standard conditions (293.15 K, 101.325 kPa)
    * range: [Double](types/Double.md)
 * [flowRateVolFM](flowRateVolFM.md)  <sub>OPT</sub>
    * Description: Volumetric flow rate from flow meter at ambient conditions
    * range: [Double](types/Double.md)
 * [particulateMass1.0](particulateMass1.0.md)  <sub>OPT</sub>
    * Description: Near real-time measurements of particulate mass 1.0 in the atmosphere using a optical sensor
    * range: [Double](types/Double.md)
 * [particulateMass10](particulateMass10.md)  <sub>OPT</sub>
    * Description: Near real-time measurements of particulate mass 10 in the atmosphere using a optical sensor
    * range: [Double](types/Double.md)
 * [particulateMass15](particulateMass15.md)  <sub>OPT</sub>
    * Description: Near real-time measurements of particulate mass 15 in the atmosphere using a optical sensor
    * range: [Double](types/Double.md)
 * [particulateMass2.5](particulateMass2.5.md)  <sub>OPT</sub>
    * Description: Near real-time measurements of particulate mass 2.5 in the atmosphere using a optical sensor
    * range: [Double](types/Double.md)
 * [particulateMass4.0](particulateMass4.0.md)  <sub>OPT</sub>
    * Description: Near real-time measurements of particulate mass 4.0 in the atmosphere using a optical sensor
    * range: [Double](types/Double.md)
 * [pressureFM](pressureFM.md)  <sub>OPT</sub>
    * Description: Absolute pressure from flow meter
    * range: [Double](types/Double.md)
 * [tempFM](tempFM.md)  <sub>OPT</sub>
    * Description: Temperature output from flow meter
    * range: [Double](types/Double.md)

### Inherited from profMfcVali_L0prime:

 * [frtSet0](frtSet0.md)  <sub>OPT</sub>
    * Description: Flow rate (frt) set point (Set) at National Institute of Standards and Technology standard conditions (0, which are 293.15 K, 101.325 kPa), synonymous with mass flow rate set point
    * range: [Double](types/Double.md)
 * [qfFrt0](qfFrt0.md)  <sub>OPT</sub>
    * Description: Flag indicates whether the gas flow rate is within the acceptable tolerance (1=fail, 0=pass, -1=NA (i.e, could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None

### Inherited from profMfm_L0prime:

 * [presAtm](presAtm.md)  <sub>OPT</sub>
    * Description: Pressure (pres), measured as atmospheric (Atm) pressure, synonymous with absolute pressure or total pressure (at sea level the standard atmospheric pressure is 101.325 kPa)
    * range: [Double](types/Double.md)
 * [temp](temp.md)  <sub>OPT</sub>
    * Description: Temperature (temp)
    * range: [Double](types/Double.md)
 * [frt](frt.md)  <sub>OPT</sub>
    * Description: Flow rate (frt) at site temperature and pressure, synonymous with volumetric flow rate
    * range: [Double](types/Double.md)
 * [frt0](frt0.md)  <sub>OPT</sub>
    * Description: Flow rate (frt) at National Institute of Standards and Technology standard conditions (0, which are  293.15 K, 101.325 kPa), synonymous with mass flow rate
    * range: [Double](types/Double.md)

### Inherited from profPumpSmp_L0prime:

 * [pumpVoltage](pumpVoltage.md)  <sub>OPT</sub>
    * Description: Voltage provided to pump
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:DPSD |
| **In Subsets:** | | DP0.00017.001 |

