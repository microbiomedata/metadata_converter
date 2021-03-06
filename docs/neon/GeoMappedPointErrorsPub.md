
# Type: geo_mappedPointErrors_pub




URI: [neon:GeoMappedPointErrorsPub](https://data.neonscience.org/GeoMappedPointErrorsPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GeoMappedPointErrorsPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;pointID:string%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;deletePoint:string%20%3F;errorDescription:string%20%3F;errorDescriptionRemarks:string%20%3F])

## Attributes


### Own

 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [deletePoint](deletePoint.md)  <sub>OPT</sub>
    * Description: Indicator of whether a point is to be deleted during post-processing
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [errorDescription](errorDescription.md)  <sub>OPT</sub>
    * Description: Description of the type of error associated with the mapped point
    * range: [String](types/String.md)
 * [errorDescriptionRemarks](errorDescriptionRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments that describe the error record
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [pointID](pointID.md)  <sub>OPT</sub>
    * Description: Identifier for a point location
    * range: [String](types/String.md)
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
| **Mappings:** | | neon:geo_mappedPointErrors_pub |
| **In Subsets:** | | DP4.00131.001 |

