
# Type: SECPRE_1min




URI: [neon:SECPRE1min](https://data.neonscience.org/SECPRE1min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SECPRE1min&#124;secPrecipBulk:double%20%3F;secPrecipExpUncert:double%20%3F;secPrecipHeaterQAQCRpt:string%20%3F;secPrecipHeater0QM:double%20%3F;secPrecipHeater1QM:double%20%3F;secPrecipHeater2QM:double%20%3F;secPrecipHeater3QM:double%20%3F;secPrecipRangeQF:integer%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;secPrecipSciRvwQF:string%20%3F;secPrecipValidCalQF:integer%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [secPrecipBulk](secPrecipBulk.md)  <sub>OPT</sub>
    * Description: Bulk secondary precipitation
    * range: [Double](types/Double.md)
 * [secPrecipExpUncert](secPrecipExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for secondary precipitation
    * range: [Double](types/Double.md)
 * [secPrecipHeater0QM](secPrecipHeater0QM.md)  <sub>OPT</sub>
    * Description: Secondary precipitation quality metric that summarizes when the heater flag was set to 0 over the averaging period, as a percent and detailed in NEON.DOC.000816
    * range: [Double](types/Double.md)
 * [secPrecipHeater1QM](secPrecipHeater1QM.md)  <sub>OPT</sub>
    * Description: Secondary precipitation quality metric that summarizes when the heater flag was set to 1 over the averaging period, as a percent and detailed in NEON.DOC.000816
    * range: [Double](types/Double.md)
 * [secPrecipHeater2QM](secPrecipHeater2QM.md)  <sub>OPT</sub>
    * Description: Secondary precipitation quality metric that summarizes when the heater flag was set to 2 over the averaging period, as a percent and detailed in NEON.DOC.000816
    * range: [Double](types/Double.md)
 * [secPrecipHeater3QM](secPrecipHeater3QM.md)  <sub>OPT</sub>
    * Description: Secondary precipitation quality metric that summarizes when the heater flag was set to 3 over the averaging period, as a percent and detailed in NEON.DOC.000816
    * range: [Double](types/Double.md)
 * [secPrecipHeaterQAQCRpt](secPrecipHeaterQAQCRpt.md)  <sub>OPT</sub>
    * Description: Secondary precipitation quality assurance and quality control report for the heater test, which indicates the state of the sensor's heaters, detailed in NEON.DOC.000816 (0=off, 1=base heater is active, 2=funnel heater is active, 3=both heaters are active)
    * range: [String](types/String.md)
 * [secPrecipRangeQF](secPrecipRangeQF.md)  <sub>OPT</sub>
    * Description: Secondary precipitation quality flag for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [secPrecipSciRvwQF](secPrecipSciRvwQF.md)  <sub>OPT</sub>
    * Description: Secondary precipitation stand-alone quality flag (does not interact with final quality flag) indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [secPrecipValidCalQF](secPrecipValidCalQF.md)  <sub>OPT</sub>
    * Description: Secondary precipitation quality flag for the valid calibration check detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:SECPRE_1min |

