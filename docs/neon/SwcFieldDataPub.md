
# Type: swc_fieldData_pub




URI: [neon:SwcFieldDataPub](https://data.neonscience.org/SwcFieldDataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SwcFieldDataPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;processedDate:time%20%3F;sampleVolumeFiltered:double%20%3F;startDate:time%20%3F;parentSampleID:string%20%3F;processedDateFilters:time%20%3F;sampleCode:string%20%3F;parentSampleCode:string%20%3F;sampleCondition:string%20%3F;fieldDataQF:string%20%3F;replicateNumber:integer%20%3F;namedLocation:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [fieldDataQF](fieldDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for field data
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [parentSampleCode](parentSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a parent sample
    * range: [String](types/String.md)
 * [parentSampleID](parentSampleID.md)  <sub>OPT</sub>
    * Description: Parent sampleID of sample being processed
    * range: [String](types/String.md)
 * [processedDate](processedDate.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event
    * range: [Time](types/Time.md)
 * [processedDateFilters](processedDateFilters.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event of filtered samples
    * range: [Time](types/Time.md)
 * [replicateNumber](replicateNumber.md)  <sub>OPT</sub>
    * Description: The number for the sample replicate
    * range: [Integer](types/Integer.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [sampleVolumeFiltered](sampleVolumeFiltered.md)  <sub>OPT</sub>
    * Description: Volume of water filtered onto the filter for external analysis
    * range: [Double](types/Double.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:swc_fieldData_pub |

