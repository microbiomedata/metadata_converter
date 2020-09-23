
# Type: THRPRE_1min




URI: [neon:THRPRE1min](https://data.neonscience.org/THRPRE1min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[THRPRE1min&#124;TFPrecipBulk:double%20%3F;TFPrecipExpUncert:double%20%3F;TFPrecipRangeQF:integer%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;TFPrecipSciRvwQF:string%20%3F;TFPrecipValidCalQF:integer%20%3F])

## Attributes


### Own

 * [TFPrecipBulk](TFPrecipBulk.md)  <sub>OPT</sub>
    * Description: Bulk throughfall precipitation
    * range: [Double](types/Double.md)
 * [TFPrecipExpUncert](TFPrecipExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for throughfall precipitation
    * range: [Double](types/Double.md)
 * [TFPrecipRangeQF](TFPrecipRangeQF.md)  <sub>OPT</sub>
    * Description: Throughfall precipitation quality flag for the range test, which indicates whether a bulk precipitation value exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [TFPrecipSciRvwQF](TFPrecipSciRvwQF.md)  <sub>OPT</sub>
    * Description: Throughfall precipitation stand-alone quality flag (does not interact with final quality flag) indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [TFPrecipValidCalQF](TFPrecipValidCalQF.md)  <sub>OPT</sub>
    * Description: Throughfall precipitation quality flag for the valid calibration check detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:THRPRE_1min |

