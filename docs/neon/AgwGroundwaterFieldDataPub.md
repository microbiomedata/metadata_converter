
# Type: agw_groundwaterFieldData_pub




URI: [neon:AgwGroundwaterFieldDataPub](https://data.neonscience.org/AgwGroundwaterFieldDataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AgwGroundwaterFieldDataPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;recordedBy:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;collectDate:time%20%3F;startDate:time%20%3F;collectedBy:string%20%3F;locationID:string%20%3F;dataQF:string%20%3F;groundSurfToThawDist:double%20%3F;groundSurfToWaterDist:double%20%3F;thawProbeDepth1:double%20%3F;thawProbeDepth10:double%20%3F;thawProbeDepth2:double%20%3F;thawProbeDepth3:double%20%3F;thawProbeDepth4:double%20%3F;thawProbeDepth5:double%20%3F;thawProbeDepth6:double%20%3F;thawProbeDepth7:double%20%3F;thawProbeDepth8:double%20%3F;thawProbeDepth9:double%20%3F;thawProbeDepthAverage:double%20%3F;thawProbeDepthStdDev:double%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [collectedBy](collectedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who collected the sample or specimen
    * range: [String](types/String.md)
 * [coordinateUncertainty](coordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [decimalLatitude](decimalLatitude.md)  <sub>OPT</sub>
    * Description: The geographic latitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [decimalLongitude](decimalLongitude.md)  <sub>OPT</sub>
    * Description: The geographic longitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [elevation](elevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level
    * range: [Double](types/Double.md)
 * [elevationUncertainty](elevationUncertainty.md)  <sub>OPT</sub>
    * Description: Uncertainty in elevation values (in meters)
    * range: [Double](types/Double.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [groundSurfToThawDist](groundSurfToThawDist.md)  <sub>OPT</sub>
    * Description: Distance between ground surface and refusal; i.e. bottom of thawed layer
    * range: [Double](types/Double.md)
 * [groundSurfToWaterDist](groundSurfToWaterDist.md)  <sub>OPT</sub>
    * Description: Distance between ground surface and surface of liquid water
    * range: [Double](types/Double.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
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
 * [thawProbeDepth1](thawProbeDepth1.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; first measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth10](thawProbeDepth10.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; tenth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth2](thawProbeDepth2.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; second measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth3](thawProbeDepth3.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; third measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth4](thawProbeDepth4.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; fourth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth5](thawProbeDepth5.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; fifth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth6](thawProbeDepth6.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; sixth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth7](thawProbeDepth7.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; seventh measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth8](thawProbeDepth8.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; eighth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth9](thawProbeDepth9.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; ninth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepthAverage](thawProbeDepthAverage.md)  <sub>OPT</sub>
    * Description: Mean depth of thawed layer above permafrost from ground surface within 2 meter radius of well
    * range: [Double](types/Double.md)
 * [thawProbeDepthStdDev](thawProbeDepthStdDev.md)  <sub>OPT</sub>
    * Description: Standard deviation of 10 thaw depth measurements collected within 2 meter radius of well
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:agw_groundwaterFieldData_pub |
| **In Subsets:** | | DP1.20099.001 |

