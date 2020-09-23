
# Type: sbd_plateauSampleFieldData_pub




URI: [neon:SbdPlateauSampleFieldDataPub](https://data.neonscience.org/SbdPlateauSampleFieldDataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SbdPlateauSampleFieldDataPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;replicateNumber:integer%20%3F;namedLocation:string%20%3F;plateauSampleFieldDataQF:string%20%3F;plateauCollectTime:time%20%3F;saltTracerSampleCode:string%20%3F;saltTracerSampleID:string%20%3F;syringeID:string%20%3F;syringeCode:string%20%3F;incompleteExperimentQF:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [incompleteExperimentQF](incompleteExperimentQF.md)  <sub>OPT</sub>
    * Description: Data quality flag indicating a reaeration experiment that is incomplete This flag is populated on a semi-annual basis following science review
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [plateauCollectTime](plateauCollectTime.md)  <sub>OPT</sub>
    * Description: The date-time of sample collection at tracer plateau
    * range: [Time](types/Time.md)
 * [plateauSampleFieldDataQF](plateauSampleFieldDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for plateau sample field data
    * range: [String](types/String.md)
 * [replicateNumber](replicateNumber.md)  <sub>OPT</sub>
    * Description: The number for the sample replicate
    * range: [Integer](types/Integer.md)
 * [saltTracerSampleCode](saltTracerSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for the salt sample
    * range: [String](types/String.md)
 * [saltTracerSampleID](saltTracerSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the salt sample
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [syringeCode](syringeCode.md)  <sub>OPT</sub>
    * Description: Barcode for the sample syringe
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
| **Mappings:** | | neon:sbd_plateauSampleFieldData_pub |

