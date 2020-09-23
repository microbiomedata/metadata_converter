
# Type: gag_fieldData_pub




URI: [neon:GagFieldDataPub](https://data.neonscience.org/GagFieldDataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GagFieldDataPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;collectDate:time%20%3F;startDate:time%20%3F;initialStageHeight:double%20%3F;endStageHeight:double%20%3F;precipDescrip:string%20%3F;previousRain:string%20%3F;waterColorDescrip:string%20%3F;riparianPhenologyDescrip:string%20%3F;collectedBy:string%20%3F;locationID:string%20%3F;dataQF:string%20%3F;samplingImpractical:string%20%3F;icePresent:string%20%3F;beaufortScaleWind:string%20%3F;algaePresence:string%20%3F;leafLitterPresence:string%20%3F;macrophytePresence:string%20%3F;nominalCloudCover:string%20%3F;oilsPresence:string%20%3F;pollenPresence:string%20%3F;trashPresent:string%20%3F;waterClarityDescrip:string%20%3F;woodyDebrisPresence:string%20%3F;dscTempHydroCond:string%20%3F;dscTempHydroCondLoc:string%20%3F;gaugeTempHydroCond:string%20%3F;gaugeTempHydroCondLoc:string%20%3F])

## Attributes


### Own

 * [algaePresence](algaePresence.md)  <sub>OPT</sub>
    * Description: Presence of algae
    * range: [String](types/String.md)
 * [beaufortScaleWind](beaufortScaleWind.md)  <sub>OPT</sub>
    * Description: Qualitative description of wind conditions based on the beaufort scale
    * range: [String](types/String.md)
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
 * [dscTempHydroCond](dscTempHydroCond.md)  <sub>OPT</sub>
    * Description: Type of temporary hydrologic condition present at the discharge transect
    * range: [String](types/String.md)
 * [dscTempHydroCondLoc](dscTempHydroCondLoc.md)  <sub>OPT</sub>
    * Description: Location of the temporary hydrologic condition present at the discharge transect
    * range: [String](types/String.md)
 * [elevation](elevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level
    * range: [Double](types/Double.md)
 * [elevationUncertainty](elevationUncertainty.md)  <sub>OPT</sub>
    * Description: Uncertainty in elevation values (in meters)
    * range: [Double](types/Double.md)
 * [endStageHeight](endStageHeight.md)  <sub>OPT</sub>
    * Description: End stage (m)
    * range: [Double](types/Double.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [gaugeTempHydroCond](gaugeTempHydroCond.md)  <sub>OPT</sub>
    * Description: Type of temporary hydrologic condition present at the staff gauge
    * range: [String](types/String.md)
 * [gaugeTempHydroCondLoc](gaugeTempHydroCondLoc.md)  <sub>OPT</sub>
    * Description: Location of the temporary hydrologic condition present at the staff gauge
    * range: [String](types/String.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [icePresent](icePresent.md)  <sub>OPT</sub>
    * Description: Indication of the presence of ice
    * range: [String](types/String.md)
 * [initialStageHeight](initialStageHeight.md)  <sub>OPT</sub>
    * Description: Initial stage (m)
    * range: [Double](types/Double.md)
 * [leafLitterPresence](leafLitterPresence.md)  <sub>OPT</sub>
    * Description: Presence of leaf litter
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [macrophytePresence](macrophytePresence.md)  <sub>OPT</sub>
    * Description: Presence of macrophytes
    * range: [String](types/String.md)
 * [nominalCloudCover](nominalCloudCover.md)  <sub>OPT</sub>
    * Description: Sky Condition, estimate of cloud cover percent
    * range: [String](types/String.md)
 * [oilsPresence](oilsPresence.md)  <sub>OPT</sub>
    * Description: Presence of oils
    * range: [String](types/String.md)
 * [pollenPresence](pollenPresence.md)  <sub>OPT</sub>
    * Description: Presence of pollen as film, foam, or deposit
    * range: [String](types/String.md)
 * [precipDescrip](precipDescrip.md)  <sub>OPT</sub>
    * Description: Qualitative description of precipitation levels
    * range: [String](types/String.md)
 * [previousRain](previousRain.md)  <sub>OPT</sub>
    * Description: Previous Rain event within 48 hours (Yes/No)
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [riparianPhenologyDescrip](riparianPhenologyDescrip.md)  <sub>OPT</sub>
    * Description: Qualitative description of riparian phenology status
    * range: [String](types/String.md)
 * [samplingImpractical](samplingImpractical.md)  <sub>OPT</sub>
    * Description: Samples and/or measurements were not collected due to the indicated circumstance
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [trashPresent](trashPresent.md)  <sub>OPT</sub>
    * Description: Presence of trash
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [waterClarityDescrip](waterClarityDescrip.md)  <sub>OPT</sub>
    * Description: Qualitative description of water clarity
    * range: [String](types/String.md)
 * [waterColorDescrip](waterColorDescrip.md)  <sub>OPT</sub>
    * Description: Qualitative description of water color and clarity
    * range: [String](types/String.md)
 * [woodyDebrisPresence](woodyDebrisPresence.md)  <sub>OPT</sub>
    * Description: Presence of woody debris
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:gag_fieldData_pub |
| **In Subsets:** | | DP1.20267.001 |

