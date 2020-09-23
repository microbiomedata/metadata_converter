
# Type: soni




URI: [neon:Soni](https://data.neonscience.org/Soni)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Soni&#124;heaterFlag:integer%20%3F;veloXaxs:double%20%3F;veloYaxs:double%20%3F;veloZaxs:double%20%3F;idx:integer%20%3F;tempTranTop:double%20%3F;tempArmTop:double%20%3F;tempArmBot:double%20%3F;tempTranBot:double%20%3F;tempBloc:double%20%3F;diag16:integer%20%3F;veloSoni:double%20%3F])

## Attributes


### Own

 * [diag16](diag16.md)  <sub>OPT</sub>
    * Description: Diagnostic value (diag), output as a 16-bit (16) integer Bit assignment according to NEONDOC000807 (L0 prime processing ATBD)
    * range: [Integer](types/Integer.md)
 * [heaterFlag](heaterFlag.md)  <sub>OPT</sub>
    * Description: Heater flag indicating whether the heater was operational for a measurement period, (1 = on, no value = off)
    * range: [Integer](types/Integer.md)
 * [idx](idx.md)  <sub>OPT</sub>
    * Description: Index value (idx)
    * range: [Integer](types/Integer.md)
 * [tempArmBot](tempArmBot.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the arm (Arm) bottom (Bot) zone measured by platinum resistance thermometers (heated 3-D sonic anemometer only)
    * range: [Double](types/Double.md)
 * [tempArmTop](tempArmTop.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the arm (Arm) top zone (Top) measured by platinum resistance thermometers (heated 3-D sonic anemometer only)
    * range: [Double](types/Double.md)
 * [tempBloc](tempBloc.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the instrument block (Bloc)
    * range: [Double](types/Double.md)
 * [tempTranBot](tempTranBot.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the transducer (Tran) bottom zone (Bot) measured by platinum resistance thermometers (heated 3-D sonic anemometer only)
    * range: [Double](types/Double.md)
 * [tempTranTop](tempTranTop.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the transducer (Tran) top zone (Top) measured by platinum resistance thermometers (heated 3-D sonic anemometer only)
    * range: [Double](types/Double.md)
 * [veloSoni](veloSoni.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of sound (Soni)
    * range: [Double](types/Double.md)
 * [veloXaxs](veloXaxs.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of wind in 3-D sonic anemometer along-axis direction (Xaxs), positive backward
    * range: [Double](types/Double.md)
 * [veloYaxs](veloYaxs.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of wind in 3-D sonic anemometer cross-axis direction (Yaxs), positive right
    * range: [Double](types/Double.md)
 * [veloZaxs](veloZaxs.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of wind in 3-D sonic anemometer vertical-axis direction (Zaxs), positive upwards
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:soni |
| **In Subsets:** | | DP0.00007.001 |

