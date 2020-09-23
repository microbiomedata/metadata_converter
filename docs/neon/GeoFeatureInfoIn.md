
# Type: geo_featureInfo_in




URI: [neon:GeoFeatureInfoIn](https://data.neonscience.org/GeoFeatureInfoIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GeoFeatureInfoIn&#124;uid:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;locationID:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;bankfullDepth:double%20%3F;bankfullWidth:double%20%3F;featureID:string%20%3F;featureType:string%20%3F;floodproneHeight:double%20%3F;pebbleCountsCollected:string%20%3F;staffGaugeInstalled:string%20%3F;staffGaugeMark:double%20%3F;totalStationLocation:string%20%3F;upsDwnsHabitatType:string%20%3F])

## Attributes


### Own

 * [bankfullDepth](bankfullDepth.md)  <sub>OPT</sub>
    * Description: The measured bankfull depth of the transect
    * range: [Double](types/Double.md)
 * [bankfullWidth](bankfullWidth.md)  <sub>OPT</sub>
    * Description: The measured bankfull width of the transect
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [featureID](featureID.md)  <sub>OPT</sub>
    * Description: Identifier for the transect named location
    * range: [String](types/String.md)
 * [featureType](featureType.md)  <sub>OPT</sub>
    * Description: The type of feature surveyed at a given total station location
    * range: [String](types/String.md)
 * [floodproneHeight](floodproneHeight.md)  <sub>OPT</sub>
    * Description: The measured floodprone height of the transect; two times the bankfull depth
    * range: [Double](types/Double.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [pebbleCountsCollected](pebbleCountsCollected.md)  <sub>OPT</sub>
    * Description: Indicator of whether a pebble count survey was conducted at the transect
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [staffGaugeInstalled](staffGaugeInstalled.md)  <sub>OPT</sub>
    * Description: Indicator of whether a staff gauge is installed at the site
    * range: [String](types/String.md)
 * [staffGaugeMark](staffGaugeMark.md)  <sub>OPT</sub>
    * Description: The graduated mark on the staff gauge used for mapping
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [totalStationLocation](totalStationLocation.md)  <sub>OPT</sub>
    * Description: Identifier for sequential total station locations throughout the survey 
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [upsDwnsHabitatType](upsDwnsHabitatType.md)  <sub>OPT</sub>
    * Description: The habitat type associated with the upstream or downstream transect 
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:geo_featureInfo_in |

