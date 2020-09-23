
# Type: tck_identificationQA_in




URI: [neon:TckIdentificationQAIn](https://data.neonscience.org/TckIdentificationQAIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TckIdentificationQAIn&#124;uid:string%20%3F;remarks:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;dataQF:string%20%3F;batchID:string%20%3F;genusPTD:double%20%3F;speciesPTD:double%20%3F;PDE:double%20%3F])

## Attributes


### Own

 * [PDE](PDE.md)  <sub>OPT</sub>
    * Description: Percent difference in enumeration (PDE) between the first count and the second count for the same sample
    * range: [Double](types/Double.md)
 * [batchID](batchID.md)  <sub>OPT</sub>
    * Description: Identifier for batch or analytical run
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [genusPTD](genusPTD.md)  <sub>OPT</sub>
    * Description: Genus-level percent taxonomic difference (PTD) between the first taxonomist and the second taxonomist for the same sample
    * range: [Double](types/Double.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [speciesPTD](speciesPTD.md)  <sub>OPT</sub>
    * Description: Species-level percent taxonomic difference (PTD) between the first taxonomist and the second taxonomist for the same sample
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:tck_identificationQA_in |

