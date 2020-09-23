
# Type: EOG_5_min




URI: [neon:EOG5Min](https://data.neonscience.org/EOG5Min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[EOG5Min&#124;startDateTime:time%20%3F;endDateTime:time%20%3F;groundwaterElev:double%20%3F;groundwaterElevExpUncert:double%20%3F;groundwaterElevRangeQF:integer%20%3F;groundwaterElevPersistQF:integer%20%3F;groundwaterElevStepQF:integer%20%3F;groundwaterElevNullQF:integer%20%3F;groundwaterElevGapQF:integer%20%3F;groundwaterElevConsistQF:integer%20%3F;groundwaterElevSpikeQF:integer%20%3F;validCalQF:integer%20%3F;sciRvwQF:string%20%3F])

## Attributes


### Own

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [groundwaterElev](groundwaterElev.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater
    * range: [Double](types/Double.md)
 * [groundwaterElevConsistQF](groundwaterElevConsistQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the consistency test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevExpUncert](groundwaterElevExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for elevation of groundwater
    * range: [Double](types/Double.md)
 * [groundwaterElevGapQF](groundwaterElevGapQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the gap test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevNullQF](groundwaterElevNullQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the null test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevPersistQF](groundwaterElevPersistQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the persistence test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevRangeQF](groundwaterElevRangeQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the range test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevSpikeQF](groundwaterElevSpikeQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the spike test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [groundwaterElevStepQF](groundwaterElevStepQF.md)  <sub>OPT</sub>
    * Description: Elevation of groundwater quality flag for the step test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
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
| **Mappings:** | | neon:EOG_5_min |
| **In Subsets:** | | DP1.20100.001 |

