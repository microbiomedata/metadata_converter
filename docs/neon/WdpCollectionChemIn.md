
# Type: wdp_collectionChem_in




URI: [neon:WdpCollectionChemIn](https://data.neonscience.org/WdpCollectionChemIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WdpCollectionChemIn&#124;uid:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;locationID:string%20%3F;chemSubsampleBottleNumber:string%20%3F;chemSubsampleBottleStartMass:double%20%3F;chemSubsampleBottleEndMass:double%20%3F;chemSubsampleMass:double%20%3F;chemSubsampleID:string%20%3F;chemSubsampleFate:string%20%3F;chemSubsampleBarcode:string%20%3F;dataQF:string%20%3F;chemSubsampleCondition:string%20%3F;chemSubsampleConditionRemarks:string%20%3F;chemFunnelCode:string%20%3F;chemTubeCode:string%20%3F;extChemBottleCode:string%20%3F])

## Attributes


### Own

 * [chemFunnelCode](chemFunnelCode.md)  <sub>OPT</sub>
    * Description: The CAL/NADP barcode on the chemistry sample funnel
    * range: [String](types/String.md)
 * [chemSubsampleBarcode](chemSubsampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of chemistry subsample
    * range: [String](types/String.md)
 * [chemSubsampleBottleEndMass](chemSubsampleBottleEndMass.md)  <sub>OPT</sub>
    * Description: Mass of the chemistry subsample collection bottle and sample after being collected from wet deposition assembly; as measured by NEON field technicians
    * range: [Double](types/Double.md)
 * [chemSubsampleBottleNumber](chemSubsampleBottleNumber.md)  <sub>OPT</sub>
    * Description: Number of bottles chemistry subsample was transferred to prior to shipping
    * range: [String](types/String.md)
 * [chemSubsampleBottleStartMass](chemSubsampleBottleStartMass.md)  <sub>OPT</sub>
    * Description: Mass of the chemistry subsample collection bottle prior to deployment as measured by NEON field technicians
    * range: [Double](types/Double.md)
 * [chemSubsampleCondition](chemSubsampleCondition.md)  <sub>OPT</sub>
    * Description: List of chemistry subsample condition categories
    * range: [String](types/String.md)
 * [chemSubsampleConditionRemarks](chemSubsampleConditionRemarks.md)  <sub>OPT</sub>
    * Description: Additional remarks about the condition of the chemistry subsample
    * range: [String](types/String.md)
 * [chemSubsampleFate](chemSubsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of chemistry subsample
    * range: [String](types/String.md)
 * [chemSubsampleID](chemSubsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with chemistry subsample per sampleID
    * range: [String](types/String.md)
 * [chemSubsampleMass](chemSubsampleMass.md)  <sub>OPT</sub>
    * Description: Mass of the chemistry subsample, i.e.,  (chemSubsampleBottleEndMass minus chemSubsampleBottleStartMass)
    * range: [Double](types/Double.md)
 * [chemTubeCode](chemTubeCode.md)  <sub>OPT</sub>
    * Description: The CAL/NADP barcode on the chemistry sample thistle tube
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [extChemBottleCode](extChemBottleCode.md)  <sub>OPT</sub>
    * Description: The CAL/NADP barcode on the chemistry sample bottle; not the NEON sample barcode
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
| **Mappings:** | | neon:wdp_collectionChem_in |

