
# Type: inv_pcrAmplification_in




URI: [neon:InvPcrAmplificationIn](https://data.neonscience.org/InvPcrAmplificationIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[InvPcrAmplificationIn&#124;uid:string%20%3F;remarks:string%20%3F;collectDate:time%20%3F;processedDate:time%20%3F;startDate:time%20%3F;laboratoryName:string%20%3F;internalLabID:string%20%3F;testProtocolVersion:string%20%3F;locationID:string%20%3F;dataQF:string%20%3F;dnaSampleID:string%20%3F;dnaSampleFate:string%20%3F;dnaSampleCode:string%20%3F;processedBy:string%20%3F;forwardPrimer:string%20%3F;reversePrimer:string%20%3F;targetGene:string%20%3F;qaqcStatus:string%20%3F;replicate:string%20%3F;ampliconConcentration:double%20%3F;ampliconPooledStatus:string%20%3F;targetSubfragment:string%20%3F;primerSetID:string%20%3F])

## Attributes


### Own

 * [ampliconConcentration](ampliconConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of amplicon DNA used for sequencing reaction
    * range: [Double](types/Double.md)
 * [ampliconPooledStatus](ampliconPooledStatus.md)  <sub>OPT</sub>
    * Description: Indicates whether multiple PCR reactions were pooled
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [dnaSampleCode](dnaSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a DNA sample
    * range: [String](types/String.md)
 * [dnaSampleFate](dnaSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a DNA sample
    * range: [String](types/String.md)
 * [dnaSampleID](dnaSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for DNA sample
    * range: [String](types/String.md)
 * [forwardPrimer](forwardPrimer.md)  <sub>OPT</sub>
    * Description: DNA sequence of forward primer
    * range: [String](types/String.md)
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [primerSetID](primerSetID.md)  <sub>OPT</sub>
    * Description: Identifier for the primer set used
    * range: [String](types/String.md)
 * [processedBy](processedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who processed the sample(s)
    * range: [String](types/String.md)
 * [processedDate](processedDate.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event
    * range: [Time](types/Time.md)
 * [qaqcStatus](qaqcStatus.md)  <sub>OPT</sub>
    * Description: Status of internal QAQC
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [replicate](replicate.md)  <sub>OPT</sub>
    * Description: Sample replicate
    * range: [String](types/String.md)
 * [reversePrimer](reversePrimer.md)  <sub>OPT</sub>
    * Description: DNA sequence of reverse primer
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [targetGene](targetGene.md)  <sub>OPT</sub>
    * Description: Targeted gene or locus name
    * range: [String](types/String.md)
 * [targetSubfragment](targetSubfragment.md)  <sub>OPT</sub>
    * Description: Name of subfragment of a gene or locus
    * range: [String](types/String.md)
 * [testProtocolVersion](testProtocolVersion.md)  <sub>OPT</sub>
    * Description: The protocol version used to test the sample
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:inv_pcrAmplification_in |

