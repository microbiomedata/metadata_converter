
# Type: wdp_collection_in




URI: [neon:WdpCollectionIn](https://data.neonscience.org/WdpCollectionIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WdpCollectionIn&#124;uid:string%20%3F;remarks:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;aCollectedBy:string%20%3F;bCollectedBy:string%20%3F;samplingProtocolVersion:string%20%3F;locationID:string%20%3F;equipmentProblems:string%20%3F;equipmentProblemsCategory:string%20%3F;equipmentProblemsRemarks:string%20%3F;aSetBy:string%20%3F;bSetBy:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;chemSubsampleID:string%20%3F;chemSubsampleFate:string%20%3F;chemSubsampleBarcode:string%20%3F;isoSubsampleID:string%20%3F;isoSubsampleFate:string%20%3F;isoSubsampleBarcode:string%20%3F;dataQF:string%20%3F;isoTestSubsampleID:string%20%3F;isoTestSubsampleFate:string%20%3F;isoTestSubsampleBarcode:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;shippingCaseCode:string%20%3F])

## Attributes


### Own

 * [aCollectedBy](aCollectedBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [aSetBy](aSetBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who set the collector
    * range: [String](types/String.md)
 * [bCollectedBy](bCollectedBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [bSetBy](bSetBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who set the collector
    * range: [String](types/String.md)
 * [chemSubsampleBarcode](chemSubsampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of chemistry subsample
    * range: [String](types/String.md)
 * [chemSubsampleFate](chemSubsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of chemistry subsample
    * range: [String](types/String.md)
 * [chemSubsampleID](chemSubsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with chemistry subsample per sampleID
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [equipmentProblems](equipmentProblems.md)  <sub>OPT</sub>
    * Description: Indicator of visible equipment problems of the wet deposition assembly at the time of sample collection; yes requires further specification in remarks
    * range: [String](types/String.md)
 * [equipmentProblemsCategory](equipmentProblemsCategory.md)  <sub>OPT</sub>
    * Description: List of visible equipment problem categories
    * range: [String](types/String.md)
 * [equipmentProblemsRemarks](equipmentProblemsRemarks.md)  <sub>OPT</sub>
    * Description: Additional remarks about additional visible equipment problems
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [isoSubsampleBarcode](isoSubsampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of isotope subsample
    * range: [String](types/String.md)
 * [isoSubsampleFate](isoSubsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of isotope subsample
    * range: [String](types/String.md)
 * [isoSubsampleID](isoSubsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with isotope subsample per sampleID
    * range: [String](types/String.md)
 * [isoTestSubsampleBarcode](isoTestSubsampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of isotope analysis subsample
    * range: [String](types/String.md)
 * [isoTestSubsampleFate](isoTestSubsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of isotope analysis subsample
    * range: [String](types/String.md)
 * [isoTestSubsampleID](isoTestSubsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with isotope analysis subsample per sampleID
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [shippingCaseCode](shippingCaseCode.md)  <sub>OPT</sub>
    * Description: The CAL/NADP barcode on the glassware shipping case being returned to the lab with sample
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:wdp_collection_in |
| **In Subsets:** | | DP0.00018.001 |

