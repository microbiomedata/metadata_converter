
# Type: wdi_isoPerSample_pub




URI: [neon:WdiIsoPerSamplePub](https://data.neonscience.org/WdiIsoPerSamplePub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WdiIsoPerSamplePub&#124;uid:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;laboratoryName:string%20%3F;externalRemarks:string%20%3F;analysisDate:time%20%3F;d18OWater:double%20%3F;d2HWater:double%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;isoTestSubsampleID:string%20%3F;isoTestSubsampleBarcode:string%20%3F;d18OsdWater:double%20%3F;d2HsdWater:double%20%3F;sampleCondition:string%20%3F;namedLocation:string%20%3F])

## Attributes


### Own

 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [d18OWater](d18OWater.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 18O:16O in H2O, relative to the Vienna Standard Mean Ocean Water
    * range: [Double](types/Double.md)
 * [d18OsdWater](d18OsdWater.md)  <sub>OPT</sub>
    * Description: Standard deviation of d18O of replicate H2O samples
    * range: [Double](types/Double.md)
 * [d2HWater](d2HWater.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 2H:1H in H2O, relative to the Vienna Standard Mean Ocean Water
    * range: [Double](types/Double.md)
 * [d2HsdWater](d2HsdWater.md)  <sub>OPT</sub>
    * Description: Standard deviation of d2H of replicate H2O samples
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [externalRemarks](externalRemarks.md)  <sub>OPT</sub>
    * Description: External lab notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [isoTestSubsampleBarcode](isoTestSubsampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of isotope analysis subsample
    * range: [String](types/String.md)
 * [isoTestSubsampleID](isoTestSubsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with isotope analysis subsample per sampleID
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
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
| **Mappings:** | | neon:wdi_isoPerSample_pub |

