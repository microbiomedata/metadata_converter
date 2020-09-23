
# Type: dep_profileHeader_pub




URI: [neon:DepProfileHeaderPub](https://data.neonscience.org/DepProfileHeaderPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DepProfileHeaderPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;date:time%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;maxDepth:double%20%3F;startDate:time%20%3F;samplingProtocolVersion:string%20%3F;iceThickness:double%20%3F;thermalStratification:string%20%3F;dataQF:string%20%3F;samplingImpractical:string%20%3F;namedLocation:string%20%3F;additionalCoordUncertainty:double%20%3F;estimatedMetalimnionDepths:string%20%3F;lowerMetalimnionDepth:string%20%3F;lowerMetalimnion2Depth:string%20%3F;upperMetalimnionDepth:string%20%3F;upperMetalimnion2Depth:string%20%3F;snowThickness:double%20%3F])

## Attributes


### Own

 * [additionalCoordUncertainty](additionalCoordUncertainty.md)  <sub>OPT</sub>
    * Description: Additional uncertainty to be added to the coordinate uncertainty at all sites
    * range: [Double](types/Double.md)
 * [coordinateUncertainty](coordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [date](date.md)  <sub>OPT</sub>
    * Description: Date or date and time of measurement, observation, or collection event
    * range: [Time](types/Time.md)
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
 * [estimatedMetalimnionDepths](estimatedMetalimnionDepths.md)  <sub>OPT</sub>
    * Description: An indication that the depths used in the calculation of the metalimnion are spaced wider than 1 m apart, resulting in estimates for the upper and lower depths of the metalimnion
    * range: [String](types/String.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [iceThickness](iceThickness.md)  <sub>OPT</sub>
    * Description: Thickness of the ice covering the lake or river
    * range: [Double](types/Double.md)
 * [lowerMetalimnion2Depth](lowerMetalimnion2Depth.md)  <sub>OPT</sub>
    * Description: Depth of lower bound of the second, deeper metalimnion
    * range: [String](types/String.md)
 * [lowerMetalimnionDepth](lowerMetalimnionDepth.md)  <sub>OPT</sub>
    * Description: Depth of lower bound of the metalimnion
    * range: [String](types/String.md)
 * [maxDepth](maxDepth.md)  <sub>OPT</sub>
    * Description: Maximum depth
    * range: [Double](types/Double.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [samplingImpractical](samplingImpractical.md)  <sub>OPT</sub>
    * Description: Samples and/or measurements were not collected due to the indicated circumstance
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [snowThickness](snowThickness.md)  <sub>OPT</sub>
    * Description: Thickness of the snow covering the lake or river
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [thermalStratification](thermalStratification.md)  <sub>OPT</sub>
    * Description: Indication of whether the water column is stratified or non-stratified
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [upperMetalimnion2Depth](upperMetalimnion2Depth.md)  <sub>OPT</sub>
    * Description: Depth of upper bound of the second, deeper metalimnion
    * range: [String](types/String.md)
 * [upperMetalimnionDepth](upperMetalimnionDepth.md)  <sub>OPT</sub>
    * Description: Depth of upper bound of the metalimnion
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:dep_profileHeader_pub |
| **In Subsets:** | | DP1.20254.001 |

