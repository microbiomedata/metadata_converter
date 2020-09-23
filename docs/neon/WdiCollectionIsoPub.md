
# Type: wdi_collectionIso_pub




URI: [neon:WdiCollectionIsoPub](https://data.neonscience.org/WdiCollectionIsoPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WdiCollectionIsoPub&#124;uid:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;isoSubsampleMass:double%20%3F;sampleCode:string%20%3F;isoSubsampleID:string%20%3F;isoSubsampleBarcode:string%20%3F;dataQF:string%20%3F;isoSubsampleCondition:string%20%3F;isoSubsampleConditionRemarks:string%20%3F;namedLocation:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [isoSubsampleBarcode](isoSubsampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of isotope subsample
    * range: [String](types/String.md)
 * [isoSubsampleCondition](isoSubsampleCondition.md)  <sub>OPT</sub>
    * Description: List of isotope subsample condition categories
    * range: [String](types/String.md)
 * [isoSubsampleConditionRemarks](isoSubsampleConditionRemarks.md)  <sub>OPT</sub>
    * Description: Additional remarks about the condition of the isotope subsample
    * range: [String](types/String.md)
 * [isoSubsampleID](isoSubsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with isotope subsample per sampleID
    * range: [String](types/String.md)
 * [isoSubsampleMass](isoSubsampleMass.md)  <sub>OPT</sub>
    * Description: Mass of the isotope subsample, i.e.,  (isoSubsampleBottleEndMass minus isoSubsampleBottleStartMass)
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:wdi_collectionIso_pub |

