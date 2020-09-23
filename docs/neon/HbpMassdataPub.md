
# Type: hbp_massdata_pub




URI: [neon:HbpMassdataPub](https://data.neonscience.org/HbpMassdataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[HbpMassdataPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;herbGroup:string%20%3F;weighDate:time%20%3F;qaDryMass:string%20%3F;dryMass:double%20%3F;subsampleID:string%20%3F;plotType:string%20%3F;dryingHours:double%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;freshMass:double%20%3F;subsampleCode:string%20%3F;subsampleDryMass:double%20%3F;subsampleFreshMass:double%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [dryMass](dryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of sample or subsample
    * range: [Double](types/Double.md)
 * [dryingHours](dryingHours.md)  <sub>OPT</sub>
    * Description: Number of hours material was in a drying oven until dried to constant weight
    * range: [Double](types/Double.md)
 * [freshMass](freshMass.md)  <sub>OPT</sub>
    * Description: Total fresh mass of a sample
    * range: [Double](types/Double.md)
 * [herbGroup](herbGroup.md)  <sub>OPT</sub>
    * Description: Categories indicating herbaceous plant functional group
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [plotType](plotType.md)  <sub>OPT</sub>
    * Description: NEON plot type in which sampling occurred: tower, distributed or gradient
    * range: [String](types/String.md)
 * [qaDryMass](qaDryMass.md)  <sub>OPT</sub>
    * Description: Indicates whether 'dryMass' value is associated with 'qa' measurement type
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
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
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [subsampleCode](subsampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a subsample
    * range: [String](types/String.md)
 * [subsampleDryMass](subsampleDryMass.md)  <sub>OPT</sub>
    * Description: Total dry mass of a subsample
    * range: [Double](types/Double.md)
 * [subsampleFreshMass](subsampleFreshMass.md)  <sub>OPT</sub>
    * Description: Total fresh mass of a subsample
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
| **Mappings:** | | neon:hbp_massdata_pub |

