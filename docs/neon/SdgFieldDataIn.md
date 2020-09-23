
# Type: sdg_fieldData_in




URI: [neon:SdgFieldDataIn](https://data.neonscience.org/SdgFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SdgFieldDataIn&#124;uid:string%20%3F;collectDate:time%20%3F;stationID:string%20%3F;startDate:time%20%3F;parentSampleID:string%20%3F;waterSampleID:string%20%3F;parentSampleFate:string%20%3F;parentSampleCode:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;sdgFieldDataQF:string%20%3F;waterSampleCode:string%20%3F;waterSampleFate:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [parentSampleCode](parentSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a parent sample
    * range: [String](types/String.md)
 * [parentSampleFate](parentSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a parent sample
    * range: [String](types/String.md)
 * [parentSampleID](parentSampleID.md)  <sub>OPT</sub>
    * Description: Parent sampleID of sample being processed
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [sdgFieldDataQF](sdgFieldDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for dissolved gas field data
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [waterSampleCode](waterSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for the water sample to be equilibrated with air
    * range: [String](types/String.md)
 * [waterSampleFate](waterSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of the water sample to be equilibrated with air
    * range: [String](types/String.md)
 * [waterSampleID](waterSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the water sample to be equilibrated with air
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sdg_fieldData_in |

