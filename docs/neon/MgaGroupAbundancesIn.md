
# Type: mga_groupAbundances_in




URI: [neon:MgaGroupAbundancesIn](https://data.neonscience.org/MgaGroupAbundancesIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MgaGroupAbundancesIn&#124;uid:string%20%3F;remarks:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;processedDate:time%20%3F;laboratoryName:string%20%3F;internalLabID:string%20%3F;testProtocolVersion:string%20%3F;locationID:string%20%3F;dataQF:string%20%3F;sampleCondition:string%20%3F;dnaSampleID:string%20%3F;dnaSampleFate:string%20%3F;dnaSampleCode:string%20%3F;processedBy:string%20%3F;batchID:string%20%3F;inhibitorRemovalRequired:string%20%3F;nucleicAcidConcentration:double%20%3F;reviewedBy:string%20%3F;sampleMaterial:string%20%3F;targetGene:string%20%3F;targetTaxonGroup:string%20%3F;qaqcStatus:string%20%3F;copyNumberStandardDeviation:double%20%3F;meanCopyNumber:double%20%3F;meanCqValue:double%20%3F;rep1CopyNumber:double%20%3F;rep1CqValue:double%20%3F;rep1MeltingTemperature:double%20%3F;rep2CopyNumber:double%20%3F;rep2CqValue:double%20%3F;rep2MeltingTemperature:double%20%3F;rep3CopyNumber:double%20%3F;rep3CqValue:double%20%3F;rep3MeltingTemperature:double%20%3F;rep4CopyNumber:double%20%3F;rep4CqValue:double%20%3F;rep5CopyNumber:double%20%3F;rep5CqValue:double%20%3F;targetTaxonCode:string%20%3F;targetTaxonFate:string%20%3F;targetTaxonID:string%20%3F])

## Attributes


### Own

 * [batchID](batchID.md)  <sub>OPT</sub>
    * Description: Identifier for batch or analytical run
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [copyNumberStandardDeviation](copyNumberStandardDeviation.md)  <sub>OPT</sub>
    * Description: Standard deviation in gene copy number in a sample
    * range: [Double](types/Double.md)
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
 * [inhibitorRemovalRequired](inhibitorRemovalRequired.md)  <sub>OPT</sub>
    * Description: Indicates whether nucleic acid inhibitor removal was required prior to analysis
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
 * [meanCopyNumber](meanCopyNumber.md)  <sub>OPT</sub>
    * Description: Average gene copy number in a sample in copies per nanogram of DNA
    * range: [Double](types/Double.md)
 * [meanCqValue](meanCqValue.md)  <sub>OPT</sub>
    * Description: Average quantification cycle or threshold number in a sample
    * range: [Double](types/Double.md)
 * [nucleicAcidConcentration](nucleicAcidConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of extracted nucleic acids
    * range: [Double](types/Double.md)
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
 * [rep1CopyNumber](rep1CopyNumber.md)  <sub>OPT</sub>
    * Description: Gene copy number in a sample replicate 1 in copies per nanogram of DNA
    * range: [Double](types/Double.md)
 * [rep1CqValue](rep1CqValue.md)  <sub>OPT</sub>
    * Description: Quantification cycle or threshold number in sample replicate 1
    * range: [Double](types/Double.md)
 * [rep1MeltingTemperature](rep1MeltingTemperature.md)  <sub>OPT</sub>
    * Description: Melting temperature measurement for replicate 1
    * range: [Double](types/Double.md)
 * [rep2CopyNumber](rep2CopyNumber.md)  <sub>OPT</sub>
    * Description: Gene copy number in a sample replicate 2 in copies per nanogram of DNA
    * range: [Double](types/Double.md)
 * [rep2CqValue](rep2CqValue.md)  <sub>OPT</sub>
    * Description: Quantification cycle or threshold number in sample replicate 2
    * range: [Double](types/Double.md)
 * [rep2MeltingTemperature](rep2MeltingTemperature.md)  <sub>OPT</sub>
    * Description: Melting temperature measurement for replicate 2
    * range: [Double](types/Double.md)
 * [rep3CopyNumber](rep3CopyNumber.md)  <sub>OPT</sub>
    * Description: Gene copy number in a sample replicate 3 in copies per nanogram of DNA
    * range: [Double](types/Double.md)
 * [rep3CqValue](rep3CqValue.md)  <sub>OPT</sub>
    * Description: Quantification cycle or threshold number in sample replicate 3
    * range: [Double](types/Double.md)
 * [rep3MeltingTemperature](rep3MeltingTemperature.md)  <sub>OPT</sub>
    * Description: Melting temperature measurement for replicate 3
    * range: [Double](types/Double.md)
 * [rep4CopyNumber](rep4CopyNumber.md)  <sub>OPT</sub>
    * Description: Gene copy number in a sample replicate 4 in copies per nanogram of DNA
    * range: [Double](types/Double.md)
 * [rep4CqValue](rep4CqValue.md)  <sub>OPT</sub>
    * Description: Quantification cycle or threshold number in sample replicate 4
    * range: [Double](types/Double.md)
 * [rep5CopyNumber](rep5CopyNumber.md)  <sub>OPT</sub>
    * Description: Gene copy number in a sample replicate 5 in copies per nanogram of DNA
    * range: [Double](types/Double.md)
 * [rep5CqValue](rep5CqValue.md)  <sub>OPT</sub>
    * Description: Quantification cycle or threshold number in sample replicate 5
    * range: [Double](types/Double.md)
 * [reviewedBy](reviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed the data prior to submission
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [sampleMaterial](sampleMaterial.md)  <sub>OPT</sub>
    * Description: The material in which a sample was embedded prior to the sampling event
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [targetGene](targetGene.md)  <sub>OPT</sub>
    * Description: Targeted gene or locus name
    * range: [String](types/String.md)
 * [targetTaxonCode](targetTaxonCode.md)  <sub>OPT</sub>
    * Description: Barcode of taxon group-specific sample
    * range: [String](types/String.md)
 * [targetTaxonFate](targetTaxonFate.md)  <sub>OPT</sub>
    * Description: Fate of taxon group-specific sample
    * range: [String](types/String.md)
 * [targetTaxonGroup](targetTaxonGroup.md)  <sub>OPT</sub>
    * Description: Taxonomic group targeted
    * range: [String](types/String.md)
 * [targetTaxonID](targetTaxonID.md)  <sub>OPT</sub>
    * Description: Taxon group-specific identifier for sample
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
| **Mappings:** | | neon:mga_groupAbundances_in |
| **In Subsets:** | | DP0.10109.001 |

