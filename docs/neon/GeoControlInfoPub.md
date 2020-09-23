
# Type: geo_controlInfo_pub




URI: [neon:GeoControlInfoPub](https://data.neonscience.org/GeoControlInfoPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GeoControlInfoPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;controlActivationState:integer%20%3F;controlNumber:integer%20%3F;segmentNumber:integer%20%3F])

## Attributes


### Own

 * [controlActivationState](controlActivationState.md)  <sub>OPT</sub>
    * Description: Designation of whether or not a control is active for a given segment. 1 = active; 0 = inactive
    * range: [Integer](types/Integer.md)
 * [controlNumber](controlNumber.md)  <sub>OPT</sub>
    * Description: Numeric designation for the control number
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
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [segmentNumber](segmentNumber.md)  <sub>OPT</sub>
    * Description: Numeric designation for the segment number
    * range: [Integer](types/Integer.md)
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
| **Mappings:** | | neon:geo_controlInfo_pub |

