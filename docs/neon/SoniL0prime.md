
# Type: soni_L0prime




URI: [neon:SoniL0prime](https://data.neonscience.org/SoniL0prime)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SoniL0prime&#124;heaterFlag:integer%20%3F;veloXaxs:double%20%3F;veloYaxs:double%20%3F;veloZaxs:double%20%3F;idx:integer%20%3F;veloSoni:double%20%3F;tempSoni:string%20%3F;qfSoniCode:string%20%3F;voucherStatus:string%20%3F;qfSoniSignalLow:integer%20%3F;qfSoniUnrs:integer%20%3F;qfSoniData:integer%20%3F;qfSoniTrig:integer%20%3F;qfSoniComm:integer%20%3F;qfSoniTemp:integer%20%3F;qfSoniSignalPoor:integer%20%3F;qfSoniSignalHigh:integer%20%3F])

## Attributes


### Own

 * [heaterFlag](heaterFlag.md)  <sub>OPT</sub>
    * Description: Heater flag indicating whether the heater was operational for a measurement period, (1 = on, no value = off)
    * range: [Integer](types/Integer.md)
 * [idx](idx.md)  <sub>OPT</sub>
    * Description: Index value (idx)
    * range: [Integer](types/Integer.md)
 * [qfSoniCode](qfSoniCode.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o5: Wrong embedded sensor code)
    * range: [String](types/String.md)
 * [qfSoniComm](qfSoniComm.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o4: SDM communications error)
    * range: [Integer](types/Integer.md)
 * [qfSoniData](qfSoniData.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o2: No data available)
    * range: [Integer](types/Integer.md)
 * [qfSoniSignalHigh](qfSoniSignalHigh.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC,s3: High signal amplitude)
    * range: [Integer](types/Integer.md)
 * [qfSoniSignalLow](qfSoniSignalLow.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC s4 Low signal amplitude)
    * range: [Integer](types/Integer.md)
 * [qfSoniSignalPoor](qfSoniSignalPoor.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC,s2: Poor signal lock)
    * range: [Integer](types/Integer.md)
 * [qfSoniTemp](qfSoniTemp.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC,s1: Axes TSONIC difference > 4K)
    * range: [Integer](types/Integer.md)
 * [qfSoniTrig](qfSoniTrig.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o3: Sensor trigger source lost)
    * range: [Integer](types/Integer.md)
 * [qfSoniUnrs](qfSoniUnrs.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o1: Sensor unresponsive)
    * range: [Integer](types/Integer.md)
 * [tempSoni](tempSoni.md)  <sub>OPT</sub>
    * Description: Sonic temperature (TSONIC)
    * range: [String](types/String.md)
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
 * [voucherStatus](voucherStatus.md)  <sub>OPT</sub>
    * Description: Status of the specimen in an accessioning process
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:soni_L0prime |
| **In Subsets:** | | IP0.00007.001 |

