
# Type: rea_backgroundFieldCondData_in




URI: [neon:ReaBackgroundFieldCondDataIn](https://data.neonscience.org/ReaBackgroundFieldCondDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ReaBackgroundFieldCondDataIn&#124;uid:string%20%3F;collectDate:time%20%3F;stationID:string%20%3F;startDate:time%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;backgroundFieldCondDataQF:string%20%3F;hoboSampleCode:string%20%3F;hoboSampleID:string%20%3F;stationToInjectionDistance:double%20%3F;hoboSampleFate:string%20%3F;hoboSampleCond:string%20%3F;hoboSampleClass:string%20%3F])

## Attributes


### Own

 * [backgroundFieldCondDataQF](backgroundFieldCondDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for background conductivity field data
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [hoboSampleClass](hoboSampleClass.md)  <sub>OPT</sub>
    * Description: Sample class of the HOBO conductivity logger file
    * range: [String](types/String.md)
 * [hoboSampleCode](hoboSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of the HOBO conductivity logger file
    * range: [String](types/String.md)
 * [hoboSampleCond](hoboSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of the HOBO conductivity logger file
    * range: [String](types/String.md)
 * [hoboSampleFate](hoboSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of the HOBO conductivity logger file
    * range: [String](types/String.md)
 * [hoboSampleID](hoboSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the HOBO conductivity logger file
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [stationToInjectionDistance](stationToInjectionDistance.md)  <sub>OPT</sub>
    * Description: Stream distance between the station and the injection location
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:rea_backgroundFieldCondData_in |

