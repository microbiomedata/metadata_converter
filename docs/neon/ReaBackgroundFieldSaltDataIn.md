
# Type: rea_backgroundFieldSaltData_in




URI: [neon:ReaBackgroundFieldSaltDataIn](https://data.neonscience.org/ReaBackgroundFieldSaltDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ReaBackgroundFieldSaltDataIn&#124;uid:string%20%3F;remarks:string%20%3F;collectDate:time%20%3F;stationID:string%20%3F;startDate:time%20%3F;sampleCollected:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;backgroundFieldSaltDataQF:string%20%3F;saltBackgroundSampleCode:string%20%3F;saltBackgroundSampleID:string%20%3F;specificConductanceRep1:double%20%3F;specificConductanceRep2:double%20%3F;specificConductanceRep3:double%20%3F;specificConductanceRep4:double%20%3F;stationToInjectionDistance:double%20%3F;saltBackgroundSampleClass:string%20%3F;saltBackgroundSampleFate:string%20%3F;saltBackgroundSampleCond:string%20%3F;incompleteExperimentQF:string%20%3F])

## Attributes


### Own

 * [backgroundFieldSaltDataQF](backgroundFieldSaltDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for background salt field data
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [incompleteExperimentQF](incompleteExperimentQF.md)  <sub>OPT</sub>
    * Description: Data quality flag indicating a reaeration experiment that is incomplete This flag is populated on a semi-annual basis following science review
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [saltBackgroundSampleClass](saltBackgroundSampleClass.md)  <sub>OPT</sub>
    * Description: Sample class of the reaeration background salt sample
    * range: [String](types/String.md)
 * [saltBackgroundSampleCode](saltBackgroundSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of the reaeration background salt sample
    * range: [String](types/String.md)
 * [saltBackgroundSampleCond](saltBackgroundSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of the reaeration background salt sample
    * range: [String](types/String.md)
 * [saltBackgroundSampleFate](saltBackgroundSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of the reaeration background salt sample
    * range: [String](types/String.md)
 * [saltBackgroundSampleID](saltBackgroundSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the reaeration background salt sample
    * range: [String](types/String.md)
 * [sampleCollected](sampleCollected.md)  <sub>OPT</sub>
    * Description: Indicator of whether a sample was collected
    * range: [String](types/String.md)
 * [specificConductanceRep1](specificConductanceRep1.md)  <sub>OPT</sub>
    * Description: Conductivity auto-corrected to 25 degrees C measurement replicate 1
    * range: [Double](types/Double.md)
 * [specificConductanceRep2](specificConductanceRep2.md)  <sub>OPT</sub>
    * Description: Conductivity auto-corrected to 25 degrees C measurement replicate 2
    * range: [Double](types/Double.md)
 * [specificConductanceRep3](specificConductanceRep3.md)  <sub>OPT</sub>
    * Description: Conductivity auto-corrected to 25 degrees C measurement replicate 3
    * range: [Double](types/Double.md)
 * [specificConductanceRep4](specificConductanceRep4.md)  <sub>OPT</sub>
    * Description: Conductivity auto-corrected to 25 degrees C measurement replicate 4
    * range: [Double](types/Double.md)
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
| **Mappings:** | | neon:rea_backgroundFieldSaltData_in |

