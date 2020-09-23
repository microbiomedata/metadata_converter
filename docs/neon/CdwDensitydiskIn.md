
# Type: cdw_densitydisk_in




URI: [neon:CdwDensitydiskIn](https://data.neonscience.org/CdwDensitydiskIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[CdwDensitydiskIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;weighDate:time%20%3F;dryMass:double%20%3F;subsampleID:string%20%3F;dryingHours:double%20%3F;startDate:time%20%3F;bulkDensVolume:double%20%3F;sampleFate:string%20%3F;dataQF:string%20%3F;sampleBarcode:string%20%3F;ovenStartDate:time%20%3F;ovenEndDate:time%20%3F;subsampleFreshMassRatio:double%20%3F;subsampleCode:string%20%3F;subsampleFate:string%20%3F;aDiskHeight:double%20%3F;bagNumber:string%20%3F;bDiskHeight:double%20%3F;bulkDensDisk:double%20%3F;diameter:double%20%3F;diskDryMass:double%20%3F;diskFreshMass:double%20%3F;diskID:string%20%3F;maxDiskHeight:double%20%3F;minDiskHeight:double%20%3F;ninetyDiameter:double%20%3F;sampleFreshMass:double%20%3F;qaSample:string%20%3F])

## Attributes


### Own

 * [aDiskHeight](aDiskHeight.md)  <sub>OPT</sub>
    * Description: The height, to the nearest 0.1 cm, of the log cross-sectional disk used for bulk density sampling; measurement location 1
    * range: [Double](types/Double.md)
 * [bDiskHeight](bDiskHeight.md)  <sub>OPT</sub>
    * Description: The height, to the nearest 0.1 cm, of the log cross-sectional disk used for bulk density sampling; measurement location 2
    * range: [Double](types/Double.md)
 * [bagNumber](bagNumber.md)  <sub>OPT</sub>
    * Description: Unique value for tracking a field collected sample
    * range: [String](types/String.md)
 * [bulkDensDisk](bulkDensDisk.md)  <sub>OPT</sub>
    * Description: Bulk density of a cdw disk
    * range: [Double](types/Double.md)
 * [bulkDensVolume](bulkDensVolume.md)  <sub>OPT</sub>
    * Description: Volume of the bulk density sample
    * range: [Double](types/Double.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [diameter](diameter.md)  <sub>OPT</sub>
    * Description: The maximum cross-sectional diameter
    * range: [Double](types/Double.md)
 * [diskDryMass](diskDryMass.md)  <sub>OPT</sub>
    * Description: Calculated oven-dried mass of a cdw disk
    * range: [Double](types/Double.md)
 * [diskFreshMass](diskFreshMass.md)  <sub>OPT</sub>
    * Description: Mass of fresh, undried material
    * range: [Double](types/Double.md)
 * [diskID](diskID.md)  <sub>OPT</sub>
    * Description: Numeric identifier for each log cross-sectional disk sampled for bulk density
    * range: [String](types/String.md)
 * [dryMass](dryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of sample or subsample
    * range: [Double](types/Double.md)
 * [dryingHours](dryingHours.md)  <sub>OPT</sub>
    * Description: Number of hours material was in a drying oven until dried to constant weight
    * range: [Double](types/Double.md)
 * [maxDiskHeight](maxDiskHeight.md)  <sub>OPT</sub>
    * Description: The maximum disk height
    * range: [Double](types/Double.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [minDiskHeight](minDiskHeight.md)  <sub>OPT</sub>
    * Description: The minimum disk height
    * range: [Double](types/Double.md)
 * [ninetyDiameter](ninetyDiameter.md)  <sub>OPT</sub>
    * Description: The cross-sectional diameter perpendicular to the maximum diameter
    * range: [Double](types/Double.md)
 * [ovenEndDate](ovenEndDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample was removed from the drying oven
    * range: [Time](types/Time.md)
 * [ovenStartDate](ovenStartDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample was placed in the drying oven
    * range: [Time](types/Time.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [qaSample](qaSample.md)  <sub>OPT</sub>
    * Description: Indicates whether sample measurements are replicates for quality assurance purposes
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleBarcode](sampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a sample
    * range: [String](types/String.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleFreshMass](sampleFreshMass.md)  <sub>OPT</sub>
    * Description: Mass of fresh, undried subsample
    * range: [Double](types/Double.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [subsampleCode](subsampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a subsample
    * range: [String](types/String.md)
 * [subsampleFate](subsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a subsample
    * range: [String](types/String.md)
 * [subsampleFreshMassRatio](subsampleFreshMassRatio.md)  <sub>OPT</sub>
    * Description: The ratio of subsampleFreshMass to sampleFreshMass
    * range: [Double](types/Double.md)
 * [subsampleID](subsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with each subsample per sampleID
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [weighDate](weighDate.md)  <sub>OPT</sub>
    * Description: Date that sample or subsample was weighed
    * range: [Time](types/Time.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:cdw_densitydisk_in |

