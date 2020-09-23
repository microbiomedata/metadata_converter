
# Type: rea_plateauSampleFieldData_in




URI: [neon:ReaPlateauSampleFieldDataIn](https://data.neonscience.org/ReaPlateauSampleFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ReaPlateauSampleFieldDataIn&#124;uid:string%20%3F;collectDate:time%20%3F;stationID:string%20%3F;startDate:time%20%3F;replicateNumber:integer%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;gasSampleCode:string%20%3F;gasSampleID:string%20%3F;plateauSampleFieldDataQF:string%20%3F;plateauCollectTime:time%20%3F;saltTracerSampleCode:string%20%3F;saltTracerSampleID:string%20%3F;syringeID:string%20%3F;syringeCode:string%20%3F;gasSampleFate:string%20%3F;saltTracerSampleFate:string%20%3F;syringeFate:string%20%3F;gasSampleCond:string%20%3F;saltTracerSampleCond:string%20%3F;syringeCond:string%20%3F;incompleteExperimentQF:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [gasSampleCode](gasSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for the gas sample
    * range: [String](types/String.md)
 * [gasSampleCond](gasSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of the gas sample
    * range: [String](types/String.md)
 * [gasSampleFate](gasSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of the gas sample
    * range: [String](types/String.md)
 * [gasSampleID](gasSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the gas sample
    * range: [String](types/String.md)
 * [incompleteExperimentQF](incompleteExperimentQF.md)  <sub>OPT</sub>
    * Description: Data quality flag indicating a reaeration experiment that is incomplete This flag is populated on a semi-annual basis following science review
    * range: [String](types/String.md)
 * [plateauCollectTime](plateauCollectTime.md)  <sub>OPT</sub>
    * Description: The date-time of sample collection at tracer plateau
    * range: [Time](types/Time.md)
 * [plateauSampleFieldDataQF](plateauSampleFieldDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for plateau sample field data
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [replicateNumber](replicateNumber.md)  <sub>OPT</sub>
    * Description: The number for the sample replicate
    * range: [Integer](types/Integer.md)
 * [saltTracerSampleCode](saltTracerSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for the salt sample
    * range: [String](types/String.md)
 * [saltTracerSampleCond](saltTracerSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of the salt sample
    * range: [String](types/String.md)
 * [saltTracerSampleFate](saltTracerSampleFate.md)  <sub>OPT</sub>
    * Description: Fate for the salt sample
    * range: [String](types/String.md)
 * [saltTracerSampleID](saltTracerSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the salt sample
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [syringeCode](syringeCode.md)  <sub>OPT</sub>
    * Description: Barcode for the sample syringe
    * range: [String](types/String.md)
 * [syringeCond](syringeCond.md)  <sub>OPT</sub>
    * Description: Condition of the sample syringe
    * range: [String](types/String.md)
 * [syringeFate](syringeFate.md)  <sub>OPT</sub>
    * Description: Fate for the sample syringe
    * range: [String](types/String.md)
 * [syringeID](syringeID.md)  <sub>OPT</sub>
    * Description: Identifier for the sample syringe
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:rea_plateauSampleFieldData_in |

