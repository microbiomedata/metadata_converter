
# Type: PRIPRE_30min




URI: [neon:PRIPRE30min](https://data.neonscience.org/PRIPRE30min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PRIPRE30min&#124;priPrecipBulk:double%20%3F;priPrecipExpUncert:double%20%3F;priPrecipNullQF:integer%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;inletHeaters1QM:double%20%3F;inletHeaters2QM:double%20%3F;inletHeaters3QM:double%20%3F;priPrecipFinalQF:string%20%3F;priPrecipNumPts:double%20%3F;inletHeatersNAQM:double%20%3F;priPrecipFinalQFSciRvw:string%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [inletHeaters1QM](inletHeaters1QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when one of the inlet heaters was on over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [inletHeaters2QM](inletHeaters2QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when two of the inlet heaters were on over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [inletHeaters3QM](inletHeaters3QM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when all three of the inlet heaters were on over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [inletHeatersNAQM](inletHeatersNAQM.md)  <sub>OPT</sub>
    * Description: Quality metric that summarizes when no heater information was available over the measurement period, as a percent
    * range: [Double](types/Double.md)
 * [priPrecipBulk](priPrecipBulk.md)  <sub>OPT</sub>
    * Description: Bulk primary precipitation
    * range: [Double](types/Double.md)
 * [priPrecipExpUncert](priPrecipExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for primary precipitation
    * range: [Double](types/Double.md)
 * [priPrecipFinalQF](priPrecipFinalQF.md)  <sub>OPT</sub>
    * Description: Primary precipitation quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.000898 (0 = pass, 1 = fail)
    * range: [String](types/String.md)
 * [priPrecipFinalQFSciRvw](priPrecipFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Primary precipitation quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [priPrecipNullQF](priPrecipNullQF.md)  <sub>OPT</sub>
    * Description: Primary precipitation quality flag for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [priPrecipNumPts](priPrecipNumPts.md)  <sub>OPT</sub>
    * Description: Number of five-minute bulk precipitation values that were used to compute the 30-minute bulk precipitation value
    * range: [Double](types/Double.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:PRIPRE_30min |

