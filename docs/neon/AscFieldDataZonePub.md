
# Type: asc_fieldDataZone_pub




URI: [neon:AscFieldDataZonePub](https://data.neonscience.org/AscFieldDataZonePub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AscFieldDataZonePub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;startDate:time%20%3F;endDate:time%20%3F;habitatType:string%20%3F;samplerType:string%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;downstreamCoordUncert:double%20%3F;downstreamDecimalLatitude:double%20%3F;downstreamDecimalLongitude:double%20%3F;downstreamGeodeticDatum:string%20%3F;pointSampleCount:string%20%3F;sedimentSampleBarcode:string%20%3F;sedimentSampleID:string%20%3F;upstreamCoordUncert:double%20%3F;upstreamDecimalLatitude:double%20%3F;upstreamDecimalLongitude:double%20%3F;upstreamGeodeticDatum:string%20%3F;zoneNumber:string%20%3F])

## Attributes


### Own

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
 * [downstreamCoordUncert](downstreamCoordUncert.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the downstream location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [downstreamDecimalLatitude](downstreamDecimalLatitude.md)  <sub>OPT</sub>
    * Description: The geographic latitude (in decimal degrees, WGS84) of the geographic center of the reference area of a downstream location
    * range: [Double](types/Double.md)
 * [downstreamDecimalLongitude](downstreamDecimalLongitude.md)  <sub>OPT</sub>
    * Description: The geographic longitude (in decimal degrees, WGS84) of the geographic center of the reference area at a downstream location
    * range: [Double](types/Double.md)
 * [downstreamGeodeticDatum](downstreamGeodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure downstream horizontal position on the earth
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [habitatType](habitatType.md)  <sub>OPT</sub>
    * Description: Habitat type sampled
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [pointSampleCount](pointSampleCount.md)  <sub>OPT</sub>
    * Description: Number of point samples collected for a given location
    * range: [String](types/String.md)
 * [samplerType](samplerType.md)  <sub>OPT</sub>
    * Description: Type of sampler used to collect the sample
    * range: [String](types/String.md)
 * [sedimentSampleBarcode](sedimentSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a sediment sample
    * range: [String](types/String.md)
 * [sedimentSampleID](sedimentSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for a sediment sample
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
 * [upstreamCoordUncert](upstreamCoordUncert.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given upstreamDecimalLatitude and upstreamDecimalLongitude describing the smallest circle containing the whole of the downstream location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [upstreamDecimalLatitude](upstreamDecimalLatitude.md)  <sub>OPT</sub>
    * Description: The geographic latitude (in decimal degrees; WGS84) of the upstream geographic extent of the reference area of a downstream location
    * range: [Double](types/Double.md)
 * [upstreamDecimalLongitude](upstreamDecimalLongitude.md)  <sub>OPT</sub>
    * Description: The geographic longitude (in decimal degrees; WGS84) of the upstream geographic extent of the reference area at a downstream location
    * range: [Double](types/Double.md)
 * [upstreamGeodeticDatum](upstreamGeodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure upstream horizontal position on the earth
    * range: [String](types/String.md)
 * [zoneNumber](zoneNumber.md)  <sub>OPT</sub>
    * Description: Number of the zone sampled for a given location
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:asc_fieldDataZone_pub |

