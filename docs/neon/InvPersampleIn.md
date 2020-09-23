
# Type: inv_persample_in




URI: [neon:InvPersampleIn](https://data.neonscience.org/InvPersampleIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[InvPersampleIn&#124;uid:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;laboratoryName:string%20%3F;internalLabID:string%20%3F;sortDate:time%20%3F;sortedBy:string%20%3F;testProtocolVersion:string%20%3F;locationID:string%20%3F;subsamplePercent:double%20%3F;qcSortDate:time%20%3F;primaryMatrix:string%20%3F;preRinseVolume:double%20%3F;postRinseVolume:double%20%3F;qcSortedBy:string%20%3F;qcPercentSimilarity:double%20%3F;benchRemarks:string%20%3F;qcSortingEfficacy:double%20%3F;qcIterationCount:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;qcEnumerationDifference:double%20%3F;qcTaxonomicDifference:double%20%3F;chironomidVialCode:string%20%3F;chironomidVialFate:string%20%3F;chironomidVialID:string%20%3F;oligochaeteVialCode:string%20%3F;oligochaeteVialFate:string%20%3F;oligochaeteVialID:string%20%3F])

## Attributes


### Own

 * [benchRemarks](benchRemarks.md)  <sub>OPT</sub>
    * Description: Lab technician notes; free text accompanying the record
    * range: [String](types/String.md)
 * [chironomidVialCode](chironomidVialCode.md)  <sub>OPT</sub>
    * Description: Barcode of a chironomid subsample
    * range: [String](types/String.md)
 * [chironomidVialFate](chironomidVialFate.md)  <sub>OPT</sub>
    * Description: Fate of a chironomid subsample
    * range: [String](types/String.md)
 * [chironomidVialID](chironomidVialID.md)  <sub>OPT</sub>
    * Description: Identifier for chironomid subsample
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
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
 * [oligochaeteVialCode](oligochaeteVialCode.md)  <sub>OPT</sub>
    * Description: Barcode of an oligochaete subsample
    * range: [String](types/String.md)
 * [oligochaeteVialFate](oligochaeteVialFate.md)  <sub>OPT</sub>
    * Description: Fate of an oligochaete subsample
    * range: [String](types/String.md)
 * [oligochaeteVialID](oligochaeteVialID.md)  <sub>OPT</sub>
    * Description: Identifier for oligochaete subsample
    * range: [String](types/String.md)
 * [postRinseVolume](postRinseVolume.md)  <sub>OPT</sub>
    * Description: Estimated volume of sample after preservative has been rinsed
    * range: [Double](types/Double.md)
 * [preRinseVolume](preRinseVolume.md)  <sub>OPT</sub>
    * Description: Estimated volume of sample upon arrival at lab
    * range: [Double](types/Double.md)
 * [primaryMatrix](primaryMatrix.md)  <sub>OPT</sub>
    * Description: Primary material in the sample
    * range: [String](types/String.md)
 * [qcEnumerationDifference](qcEnumerationDifference.md)  <sub>OPT</sub>
    * Description: Percent difference in enumeration (PDE) between the first taxonomist and the second taxonomist for the same sample
    * range: [Double](types/Double.md)
 * [qcIterationCount](qcIterationCount.md)  <sub>OPT</sub>
    * Description: Number of iterations of QC process performed
    * range: [String](types/String.md)
 * [qcPercentSimilarity](qcPercentSimilarity.md)  <sub>OPT</sub>
    * Description: Percent similarity of original taxonomy report and QC taxonomy report (identification + count)
    * range: [Double](types/Double.md)
 * [qcSortDate](qcSortDate.md)  <sub>OPT</sub>
    * Description: Date sample sorted for QC
    * range: [Time](types/Time.md)
 * [qcSortedBy](qcSortedBy.md)  <sub>OPT</sub>
    * Description: Anonymized name of lab personnel sorting for QC
    * range: [String](types/String.md)
 * [qcSortingEfficacy](qcSortingEfficacy.md)  <sub>OPT</sub>
    * Description: Total percent of sample recovered, verified by QC process
    * range: [Double](types/Double.md)
 * [qcTaxonomicDifference](qcTaxonomicDifference.md)  <sub>OPT</sub>
    * Description: Percent taxonomic difference (PTD) between the first taxonomist and the second taxonomist for the same sample
    * range: [Double](types/Double.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [sortDate](sortDate.md)  <sub>OPT</sub>
    * Description: Date sample was sorted
    * range: [Time](types/Time.md)
 * [sortedBy](sortedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who sorted the sample
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [subsamplePercent](subsamplePercent.md)  <sub>OPT</sub>
    * Description: Percent of the total sample contained in the subsample
    * range: [Double](types/Double.md)
 * [testProtocolVersion](testProtocolVersion.md)  <sub>OPT</sub>
    * Description: The protocol version used to test the sample
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:inv_persample_in |

