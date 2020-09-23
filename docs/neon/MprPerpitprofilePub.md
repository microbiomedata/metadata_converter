
# Type: mpr_perpitprofile_pub




URI: [neon:MprPerpitprofilePub](https://data.neonscience.org/MprPerpitprofilePub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MprPerpitprofilePub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;pitID:string%20%3F;rootsCollectedByA:string%20%3F;rootsCollectedByB:string%20%3F;pitNamedLocation:string%20%3F;pitProfileID:string%20%3F;rootStatus:string%20%3F;sizeCategory:string%20%3F;maxProfileDepth:double%20%3F;totalRootBiomass:double%20%3F;depth100RootBiomass:double%20%3F;dataQF:string%20%3F])

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
 * [depth100RootBiomass](depth100RootBiomass.md)  <sub>OPT</sub>
    * Description: Total root biomass per horizontal surface area to 100 cm depth
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
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [maxProfileDepth](maxProfileDepth.md)  <sub>OPT</sub>
    * Description: The bottom most sampling depth per pitProfileID
    * range: [Double](types/Double.md)
 * [pitID](pitID.md)  <sub>OPT</sub>
    * Description: An identifier for the soil pit
    * range: [String](types/String.md)
 * [pitNamedLocation](pitNamedLocation.md)  <sub>OPT</sub>
    * Description: Named location identifier for the soil pit
    * range: [String](types/String.md)
 * [pitProfileID](pitProfileID.md)  <sub>OPT</sub>
    * Description: An identifier for the vertical sampling profile
    * range: [String](types/String.md)
 * [rootStatus](rootStatus.md)  <sub>OPT</sub>
    * Description: The state of an individual or sample
    * range: [String](types/String.md)
 * [rootsCollectedByA](rootsCollectedByA.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who collected the root sample(s) or specimen(s)
    * range: [String](types/String.md)
 * [rootsCollectedByB](rootsCollectedByB.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who collected the root sample(s) or specimen(s)
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [sizeCategory](sizeCategory.md)  <sub>OPT</sub>
    * Description: Categorical size class of an individual or sample
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [totalRootBiomass](totalRootBiomass.md)  <sub>OPT</sub>
    * Description: Total root biomass per horizontal surface area to max pit depth
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mpr_perpitprofile_pub |
| **In Subsets:** | | DP1.10066.001 |

