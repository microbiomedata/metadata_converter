
# Type: mos_sorting_in




URI: [neon:MosSortingIn](https://data.neonscience.org/MosSortingIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MosSortingIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;subsampleID:string%20%3F;laboratoryName:string%20%3F;sampleCompromised:string%20%3F;receivedDate:time%20%3F;sortDate:time%20%3F;totalWeight:double%20%3F;subsampleWeight:double%20%3F;bycatchWeight:double%20%3F;sortedBy:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;subsampleCode:string%20%3F;subsampleFate:string%20%3F;genusPTD:double%20%3F;speciesPTD:double%20%3F;PDE:double%20%3F])

## Attributes


### Own

 * [PDE](PDE.md)  <sub>OPT</sub>
    * Description: Percent difference in enumeration (PDE) between the first count and the second count for the same sample
    * range: [Double](types/Double.md)
 * [bycatchWeight](bycatchWeight.md)  <sub>OPT</sub>
    * Description: Weight of bycatch
    * range: [Double](types/Double.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [genusPTD](genusPTD.md)  <sub>OPT</sub>
    * Description: Genus-level percent taxonomic difference (PTD) between the first taxonomist and the second taxonomist for the same sample
    * range: [Double](types/Double.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [receivedDate](receivedDate.md)  <sub>OPT</sub>
    * Description: Date a sample was received
    * range: [Time](types/Time.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCompromised](sampleCompromised.md)  <sub>OPT</sub>
    * Description: Indicator of compromised sample integrity; 'other' requires further specification in remarks
    * range: [String](types/String.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [sortDate](sortDate.md)  <sub>OPT</sub>
    * Description: Date sample was sorted
    * range: [Time](types/Time.md)
 * [sortedBy](sortedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who sorted the sample
    * range: [String](types/String.md)
 * [speciesPTD](speciesPTD.md)  <sub>OPT</sub>
    * Description: Species-level percent taxonomic difference (PTD) between the first taxonomist and the second taxonomist for the same sample
    * range: [Double](types/Double.md)
 * [subsampleCode](subsampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a subsample
    * range: [String](types/String.md)
 * [subsampleFate](subsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a subsample
    * range: [String](types/String.md)
 * [subsampleID](subsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with each subsample per sampleID
    * range: [String](types/String.md)
 * [subsampleWeight](subsampleWeight.md)  <sub>OPT</sub>
    * Description: Weight of subsample
    * range: [Double](types/Double.md)
 * [totalWeight](totalWeight.md)  <sub>OPT</sub>
    * Description: Weight of entire sample
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mos_sorting_in |

