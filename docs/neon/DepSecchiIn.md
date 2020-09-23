
# Type: dep_secchi_in




URI: [neon:DepSecchiIn](https://data.neonscience.org/DepSecchiIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DepSecchiIn&#124;uid:string%20%3F;date:time%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;stationID:string%20%3F;maxDepth:double%20%3F;startDate:time%20%3F;samplingProtocolVersion:string%20%3F;secchi1Depth:double%20%3F;secchi2Depth:double%20%3F;clearToBottom:string%20%3F;secchiMeanDepth:double%20%3F;euphoticDepth:double%20%3F;dataQF:string%20%3F;samplingImpractical:string%20%3F;additionalCoordUncertainty:double%20%3F;fulcrumVersion:string%20%3F;icePresent:string%20%3F;platformInfo:string%20%3F])

## Attributes


### Own

 * [additionalCoordUncertainty](additionalCoordUncertainty.md)  <sub>OPT</sub>
    * Description: Additional uncertainty to be added to the coordinate uncertainty at all sites
    * range: [Double](types/Double.md)
 * [clearToBottom](clearToBottom.md)  <sub>OPT</sub>
    * Description: Designation for when the secchi disk can be seen all the way to the bottom
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [date](date.md)  <sub>OPT</sub>
    * Description: Date or date and time of measurement, observation, or collection event
    * range: [Time](types/Time.md)
 * [euphoticDepth](euphoticDepth.md)  <sub>OPT</sub>
    * Description: Depth of euphotic zone, 2.5 x secchiMeanDepth
    * range: [Double](types/Double.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [icePresent](icePresent.md)  <sub>OPT</sub>
    * Description: Indication of the presence of ice
    * range: [String](types/String.md)
 * [maxDepth](maxDepth.md)  <sub>OPT</sub>
    * Description: Maximum depth
    * range: [Double](types/Double.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
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
 * [secchi1Depth](secchi1Depth.md)  <sub>OPT</sub>
    * Description: First secchi disk depth at sampling location
    * range: [Double](types/Double.md)
 * [secchi2Depth](secchi2Depth.md)  <sub>OPT</sub>
    * Description: Second secchi disk depth at sampling location
    * range: [Double](types/Double.md)
 * [secchiMeanDepth](secchiMeanDepth.md)  <sub>OPT</sub>
    * Description: Mean secchi depth at sampling location
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:dep_secchi_in |
| **In Subsets:** | | DP0.20252.001 |

