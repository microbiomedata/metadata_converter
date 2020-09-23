
# Type: geo_totalStation_pub




URI: [neon:GeoTotalStationPub](https://data.neonscience.org/GeoTotalStationPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GeoTotalStationPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;featuresSurveyed:string%20%3F;featuresSurveyedOther:string%20%3F;firstControlPointID:string%20%3F;firstControlPointType:string%20%3F;firstThalwegPoint:integer%20%3F;firstThalwegPointName:string%20%3F;lastThalwegPoint:integer%20%3F;lastThalwegPointName:string%20%3F;secondControlPointID:string%20%3F;secondControlPointType:string%20%3F;stDevH:double%20%3F;stDevHADegrees:double%20%3F;stDevHAMinutes:double%20%3F;stDevHASeconds:double%20%3F;stDevPos:double%20%3F;thirdControlPointID:string%20%3F;thirdControlPointType:string%20%3F;totalStationLocation:string%20%3F])

## Attributes


### Own

 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [featuresSurveyed](featuresSurveyed.md)  <sub>OPT</sub>
    * Description: List of features that were surveyed from a given total station location
    * range: [String](types/String.md)
 * [featuresSurveyedOther](featuresSurveyedOther.md)  <sub>OPT</sub>
    * Description: List of additional features that were surveyed from a given total station location
    * range: [String](types/String.md)
 * [firstControlPointID](firstControlPointID.md)  <sub>OPT</sub>
    * Description: Identifier for the first control point used to orient the total station at a given location
    * range: [String](types/String.md)
 * [firstControlPointType](firstControlPointType.md)  <sub>OPT</sub>
    * Description: The first type of control point used to orient the total station at a given location
    * range: [String](types/String.md)
 * [firstThalwegPoint](firstThalwegPoint.md)  <sub>OPT</sub>
    * Description: Identifier for the first thalweg point mapped from a given total station location
    * range: [Integer](types/Integer.md)
 * [firstThalwegPointName](firstThalwegPointName.md)  <sub>OPT</sub>
    * Description: Name of the first thalweg point mapped from a given total station location
    * range: [String](types/String.md)
 * [lastThalwegPoint](lastThalwegPoint.md)  <sub>OPT</sub>
    * Description: Identifier for the last thalweg point mapped from a given total station location
    * range: [Integer](types/Integer.md)
 * [lastThalwegPointName](lastThalwegPointName.md)  <sub>OPT</sub>
    * Description: Name of the last thalweg point mapped from a given total station location
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [secondControlPointID](secondControlPointID.md)  <sub>OPT</sub>
    * Description: Identifier for the second control point used to orient the total station at a given location
    * range: [String](types/String.md)
 * [secondControlPointType](secondControlPointType.md)  <sub>OPT</sub>
    * Description: The second type of control point used to orient the total station at a given location
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [stDevH](stDevH.md)  <sub>OPT</sub>
    * Description: The standard deviation of the height calculated when two or three control points are used for orientation
    * range: [Double](types/Double.md)
 * [stDevHADegrees](stDevHADegrees.md)  <sub>OPT</sub>
    * Description: The standard deviation of the horizontal angle in degrees calculated when three control points are used for orientation
    * range: [Double](types/Double.md)
 * [stDevHAMinutes](stDevHAMinutes.md)  <sub>OPT</sub>
    * Description: The standard deviation of the horizontal angle in minutes calculated when three control points are used for orientation
    * range: [Double](types/Double.md)
 * [stDevHASeconds](stDevHASeconds.md)  <sub>OPT</sub>
    * Description: The standard deviation of the horizontal angle in seconds calculated when three control points are used for orientation
    * range: [Double](types/Double.md)
 * [stDevPos](stDevPos.md)  <sub>OPT</sub>
    * Description: The standard deviation of the position of the total station robotic head calculated when three control points are used for orientation
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [thirdControlPointID](thirdControlPointID.md)  <sub>OPT</sub>
    * Description: Identifier for the third control point used to orient the total station at a given location
    * range: [String](types/String.md)
 * [thirdControlPointType](thirdControlPointType.md)  <sub>OPT</sub>
    * Description: The third type of control point used to orient the total station at a given location
    * range: [String](types/String.md)
 * [totalStationLocation](totalStationLocation.md)  <sub>OPT</sub>
    * Description: Identifier for sequential total station locations throughout the survey 
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:geo_totalStation_pub |

