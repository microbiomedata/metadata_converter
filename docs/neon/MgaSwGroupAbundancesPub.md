
# Type: mga_swGroupAbundances_pub




URI: [neon:MgaSwGroupAbundancesPub](https://data.neonscience.org/MgaSwGroupAbundancesPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MgaSwGroupAbundancesPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;processedDate:time%20%3F;laboratoryName:string%20%3F;internalLabID:string%20%3F;testProtocolVersion:string%20%3F;dataQF:string%20%3F;geneticSampleID:string%20%3F;sampleCondition:string%20%3F;dnaSampleID:string%20%3F;dnaSampleCode:string%20%3F;geneticSampleCode:string%20%3F;processedBy:string%20%3F;batchID:string%20%3F;inhibitorRemovalRequired:string%20%3F;nucleicAcidConcentration:double%20%3F;reviewedBy:string%20%3F;sampleMaterial:string%20%3F;targetGene:string%20%3F;targetTaxonGroup:string%20%3F;namedLocation:string%20%3F;copyNumberStandardDeviation:double%20%3F;meanCopyNumber:double%20%3F;meanCqValue:double%20%3F])

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
 * [dnaSampleID](dnaSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for DNA sample
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [geneticSampleCode](geneticSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a genetic sample
    * range: [String](types/String.md)
 * [geneticSampleID](geneticSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for the genetic sample
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
 * [meanCopyNumber](meanCopyNumber.md)  <sub>OPT</sub>
    * Description: Average gene copy number in a sample in copies per nanogram of DNA
    * range: [Double](types/Double.md)
 * [meanCqValue](meanCqValue.md)  <sub>OPT</sub>
    * Description: Average quantification cycle or threshold number in a sample
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [nucleicAcidConcentration](nucleicAcidConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of extracted nucleic acids
    * range: [Double](types/Double.md)
 * [processedBy](processedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who processed the sample(s)
    * range: [String](types/String.md)
 * [processedDate](processedDate.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event
    * range: [Time](types/Time.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
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
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [targetGene](targetGene.md)  <sub>OPT</sub>
    * Description: Targeted gene or locus name
    * range: [String](types/String.md)
 * [targetTaxonGroup](targetTaxonGroup.md)  <sub>OPT</sub>
    * Description: Taxonomic group targeted
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
| **Mappings:** | | neon:mga_swGroupAbundances_pub |
| **In Subsets:** | | DP1.20278.001 |

