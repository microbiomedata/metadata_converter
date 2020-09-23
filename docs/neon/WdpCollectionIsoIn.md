
# Type: wdp_collectionIso_in




URI: [neon:WdpCollectionIsoIn](https://data.neonscience.org/WdpCollectionIsoIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WdpCollectionIsoIn&#124;uid:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;locationID:string%20%3F;isoSubsampleBottleNumber:string%20%3F;isoSubsampleBottleStartMass:double%20%3F;isoSubsampleBottleEndMass:double%20%3F;isoSubsampleMass:double%20%3F;isoSubsampleID:string%20%3F;isoSubsampleFate:string%20%3F;isoSubsampleBarcode:string%20%3F;dataQF:string%20%3F;isoSubsampleCondition:string%20%3F;isoSubsampleConditionRemarks:string%20%3F;extIsoBottleCode:string%20%3F;isoFunnelCode:string%20%3F;isoTubeCode:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [extIsoBottleCode](extIsoBottleCode.md)  <sub>OPT</sub>
    * Description: The CAL/NADP barcode on the isotope sample bottle; not the NEON sample barcode
    * range: [String](types/String.md)
 * [isoFunnelCode](isoFunnelCode.md)  <sub>OPT</sub>
    * Description: The CAL/NADP barcode on the isotope sample funnel
    * range: [String](types/String.md)
 * [isoSubsampleBarcode](isoSubsampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of isotope subsample
    * range: [String](types/String.md)
 * [isoSubsampleBottleEndMass](isoSubsampleBottleEndMass.md)  <sub>OPT</sub>
    * Description: Mass of the isotope subsample collection bottle and sample after being collected from wet deposition assembly; as measured by NEON field technicians
    * range: [Double](types/Double.md)
 * [isoSubsampleBottleNumber](isoSubsampleBottleNumber.md)  <sub>OPT</sub>
    * Description: Number of bottles isotope subsample was transferred to prior to shipping
    * range: [String](types/String.md)
 * [isoSubsampleBottleStartMass](isoSubsampleBottleStartMass.md)  <sub>OPT</sub>
    * Description: Mass of the isotope subsample collection bottle prior to deployment as measured by NEON field technicians
    * range: [Double](types/Double.md)
 * [isoSubsampleCondition](isoSubsampleCondition.md)  <sub>OPT</sub>
    * Description: List of isotope subsample condition categories
    * range: [String](types/String.md)
 * [isoSubsampleConditionRemarks](isoSubsampleConditionRemarks.md)  <sub>OPT</sub>
    * Description: Additional remarks about the condition of the isotope subsample
    * range: [String](types/String.md)
 * [isoSubsampleFate](isoSubsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of isotope subsample
    * range: [String](types/String.md)
 * [isoSubsampleID](isoSubsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with isotope subsample per sampleID
    * range: [String](types/String.md)
 * [isoSubsampleMass](isoSubsampleMass.md)  <sub>OPT</sub>
    * Description: Mass of the isotope subsample, i.e.,  (isoSubsampleBottleEndMass minus isoSubsampleBottleStartMass)
    * range: [Double](types/Double.md)
 * [isoTubeCode](isoTubeCode.md)  <sub>OPT</sub>
    * Description: The CAL/NADP barcode on the isotope sample thistle tube
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
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
| **Mappings:** | | neon:wdp_collectionIso_in |

