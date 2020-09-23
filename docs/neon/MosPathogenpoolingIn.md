
# Type: mos_pathogenpooling_in




URI: [neon:MosPathogenpoolingIn](https://data.neonscience.org/MosPathogenpoolingIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MosPathogenpoolingIn&#124;uid:string%20%3F;processingDate:time%20%3F;laboratoryName:string%20%3F;testingID:string%20%3F;testingVialID:string%20%3F;poolSize:string%20%3F;startCollectDate:time%20%3F;endCollectDate:time%20%3F;locationID:string%20%3F;dataQF:string%20%3F;testingIDCode:string%20%3F;testingIDFate:string%20%3F;testingVialIDCode:string%20%3F;testingVialIDFate:string%20%3F])

## Attributes


### Own

 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endCollectDate](endCollectDate.md)  <sub>OPT</sub>
    * Description: Latest known collection date for this sample
    * range: [Time](types/Time.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [poolSize](poolSize.md)  <sub>OPT</sub>
    * Description: Number of individuals in the pathogen testing pool
    * range: [String](types/String.md)
 * [processingDate](processingDate.md)  <sub>OPT</sub>
    * Description: Date that sample was processed (i.e., sorted or pinned) in the domain lab
    * range: [Time](types/Time.md)
 * [startCollectDate](startCollectDate.md)  <sub>OPT</sub>
    * Description: Earliest known collection date for this sample
    * range: [Time](types/Time.md)
 * [testingID](testingID.md)  <sub>OPT</sub>
    * Description: Identifier for the group of specimens for testing
    * range: [String](types/String.md)
 * [testingIDCode](testingIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of a test sample
    * range: [String](types/String.md)
 * [testingIDFate](testingIDFate.md)  <sub>OPT</sub>
    * Description: Fate of a test sample
    * range: [String](types/String.md)
 * [testingVialID](testingVialID.md)  <sub>OPT</sub>
    * Description: Identifier for the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
    * range: [String](types/String.md)
 * [testingVialIDCode](testingVialIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
    * range: [String](types/String.md)
 * [testingVialIDFate](testingVialIDFate.md)  <sub>OPT</sub>
    * Description: Fate of the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mos_pathogenpooling_in |

