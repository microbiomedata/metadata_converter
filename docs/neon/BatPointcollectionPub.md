
# Type: bat_pointcollection_pub




URI: [neon:BatPointcollectionPub](https://data.neonscience.org/BatPointcollectionPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BatPointcollectionPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplerType:string%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;waterDepth:double%20%3F;substrate:string%20%3F;gpsDatafile:string%20%3F;bathymetryDataType:string%20%3F;gpsAntennaHeight:double%20%3F;gpsUsed:string%20%3F;plantsPresent:string%20%3F;pointCollectionDate:time%20%3F;waypoint:string%20%3F;waypointDescription:string%20%3F;gpsAccuracy:double%20%3F;gpsAccuracyUnits:string%20%3F;gpsAccuracyValue:double%20%3F])

## Attributes


### Own

 * [bathymetryDataType](bathymetryDataType.md)  <sub>OPT</sub>
    * Description: Type of bathymetry metadata collected
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [gpsAccuracy](gpsAccuracy.md)  <sub>OPT</sub>
    * Description: Position accuracy displayed on the gps unit in meters
    * range: [Double](types/Double.md)
 * [gpsAccuracyUnits](gpsAccuracyUnits.md)  <sub>OPT</sub>
    * Description: Unit of measure used to record gps accuracy
    * range: [String](types/String.md)
 * [gpsAccuracyValue](gpsAccuracyValue.md)  <sub>OPT</sub>
    * Description: Position accuracy displayed on the gps unit
    * range: [Double](types/Double.md)
 * [gpsAntennaHeight](gpsAntennaHeight.md)  <sub>OPT</sub>
    * Description: Height of the GPS antenna above the GPS unit
    * range: [Double](types/Double.md)
 * [gpsDatafile](gpsDatafile.md)  <sub>OPT</sub>
    * Description: Name assigned to GPS file
    * range: [String](types/String.md)
 * [gpsUsed](gpsUsed.md)  <sub>OPT</sub>
    * Description: GPS unit used to collect the associated latitude and longitude
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [plantsPresent](plantsPresent.md)  <sub>OPT</sub>
    * Description: Indicator of plant presence or absence at the groundtruthing point
    * range: [String](types/String.md)
 * [pointCollectionDate](pointCollectionDate.md)  <sub>OPT</sub>
    * Description: Date and time associated with a point collection
    * range: [Time](types/Time.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [samplerType](samplerType.md)  <sub>OPT</sub>
    * Description: Type of sampler used to collect the sample
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [substrate](substrate.md)  <sub>OPT</sub>
    * Description: Organic or inorganic surface material at the location
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [waterDepth](waterDepth.md)  <sub>OPT</sub>
    * Description: Depth of water
    * range: [Double](types/Double.md)
 * [waypoint](waypoint.md)  <sub>OPT</sub>
    * Description: Location information for a point of interest
    * range: [String](types/String.md)
 * [waypointDescription](waypointDescription.md)  <sub>OPT</sub>
    * Description: Descriptor for the waypoint
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:bat_pointcollection_pub |

