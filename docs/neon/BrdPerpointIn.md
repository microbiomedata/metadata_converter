
# Type: brd_perpoint_in




URI: [neon:BrdPerpointIn](https://data.neonscience.org/BrdPerpointIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BrdPerpointIn&#124;uid:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;eventID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;laboratoryName:string%20%3F;internalLabID:string%20%3F;locationID:string%20%3F;startCloudCoverPercentage:string%20%3F;endCloudCoverPercentage:string%20%3F;startRH:string%20%3F;endRH:string%20%3F;observedHabitat:string%20%3F;observedAirTemp:double%20%3F;kmPerHourObservedWindSpeed:double%20%3F;pointID:string%20%3F;dataQF:string%20%3F])

## Attributes


### Own

 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endCloudCoverPercentage](endCloudCoverPercentage.md)  <sub>OPT</sub>
    * Description: Observer estimate of percent cloud cover at end of sampling
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [endRH](endRH.md)  <sub>OPT</sub>
    * Description: Relative humidity as measured by handheld weather meter at the end of sampling
    * range: [String](types/String.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
 * [kmPerHourObservedWindSpeed](kmPerHourObservedWindSpeed.md)  <sub>OPT</sub>
    * Description: The average wind speed measured with a handheld weather meter, in kilometers per hour
    * range: [Double](types/Double.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [observedAirTemp](observedAirTemp.md)  <sub>OPT</sub>
    * Description: The air temperature measured with a handheld weather meter
    * range: [Double](types/Double.md)
 * [observedHabitat](observedHabitat.md)  <sub>OPT</sub>
    * Description: Observer assessment of dominant habitat at the sampling point at sampling time
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [pointID](pointID.md)  <sub>OPT</sub>
    * Description: Identifier for a point location
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startCloudCoverPercentage](startCloudCoverPercentage.md)  <sub>OPT</sub>
    * Description: Observer estimate of percent cloud cover at start of sampling
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [startRH](startRH.md)  <sub>OPT</sub>
    * Description: Relative humidity as measured by handheld weather meter at the start of sampling
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:brd_perpoint_in |

