
# Type: TGW_5_minute




URI: [neon:TGW5Minute](https://data.neonscience.org/TGW5Minute)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TGW5Minute&#124;groundwaterTemp:double%20%3F;startDateTime:time%20%3F;endDateTime:time%20%3F;groundwaterTempExpUncert:double%20%3F;groundwaterTempRangeQF:integer%20%3F;groundwaterTempPersistenceQF:integer%20%3F;groundwaterTempStepQF:integer%20%3F;groundwaterTempNullQF:integer%20%3F;groundwaterTempGapQF:integer%20%3F;groundwaterTempConsistencyQF:integer%20%3F;groundwaterTempSpikeQF:integer%20%3F;validCalQF:integer%20%3F;sciRvwQF:string%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [groundwaterTemp](groundwaterTemp.md)  <sub>OPT</sub>
    * Description: Temperature in groundwater
    * range: [Double](types/Double.md)
 * [groundwaterTempConsistencyQF](groundwaterTempConsistencyQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the consistency test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempExpUncert](groundwaterTempExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for temperature of groundwater in degrees celsius
    * range: [Double](types/Double.md)
 * [groundwaterTempGapQF](groundwaterTempGapQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the gap test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempNullQF](groundwaterTempNullQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the null test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempPersistenceQF](groundwaterTempPersistenceQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the persistence test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempRangeQF](groundwaterTempRangeQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the range test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempSpikeQF](groundwaterTempSpikeQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the spike test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterTempStepQF](groundwaterTempStepQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the step test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [sciRvwQF](sciRvwQF.md)  <sub>OPT</sub>
    * Description: Stand-alone quality flag (does not interact with final quality flag) indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
 * [validCalQF](validCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:TGW_5_minute |
| **In Subsets:** | | DP1.20217.001 |

