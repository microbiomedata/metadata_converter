
# Type: geo_missingLine_pub




URI: [neon:GeoMissingLinePub](https://data.neonscience.org/GeoMissingLinePub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GeoMissingLinePub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;attemptNumber:integer%20%3F;missingLinePoint1:string%20%3F;missingLinePoint2:string%20%3F;missingLineResultsdH:double%20%3F;missingLineResultsHD:double%20%3F;missingLineReultsStDev:double%20%3F])

## Attributes


### Own

 * [attemptNumber](attemptNumber.md)  <sub>OPT</sub>
    * Description: The attempt number associated with the missing line workflow
    * range: [Integer](types/Integer.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [missingLinePoint1](missingLinePoint1.md)  <sub>OPT</sub>
    * Description: Identifier for the first point used in the missing line workflow
    * range: [String](types/String.md)
 * [missingLinePoint2](missingLinePoint2.md)  <sub>OPT</sub>
    * Description: Identifier for the second point used in the missing line workflow
    * range: [String](types/String.md)
 * [missingLineResultsHD](missingLineResultsHD.md)  <sub>OPT</sub>
    * Description: The difference in horizontal distance calculated between the first and second shots during the missing line workflow
    * range: [Double](types/Double.md)
 * [missingLineResultsdH](missingLineResultsdH.md)  <sub>OPT</sub>
    * Description: The difference in elevation calculated between the first and second shots during the missing line workflow
    * range: [Double](types/Double.md)
 * [missingLineReultsStDev](missingLineReultsStDev.md)  <sub>OPT</sub>
    * Description: The standard deviation calculated between the first and second shots during the missing line workflow
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
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
| **Mappings:** | | neon:geo_missingLine_pub |

