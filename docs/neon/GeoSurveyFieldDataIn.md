
# Type: geo_surveyFieldData_in




URI: [neon:GeoSurveyFieldDataIn](https://data.neonscience.org/GeoSurveyFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GeoSurveyFieldDataIn&#124;uid:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;locationID:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;missingLineWorkflow:string%20%3F;pebbleCountD16:string%20%3F;pebbleCountD5:string%20%3F;pebbleCountD50:string%20%3F;pebbleCountD84:string%20%3F;totalLWDCount:integer%20%3F])

## Attributes


### Own

 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [missingLineWorkflow](missingLineWorkflow.md)  <sub>OPT</sub>
    * Description: Indicator of whether the missing line workflow was conducted
    * range: [String](types/String.md)
 * [pebbleCountD16](pebbleCountD16.md)  <sub>OPT</sub>
    * Description: The particle size that 16 percent of the particles are equal to or smaller than in the pebble count distribution
    * range: [String](types/String.md)
 * [pebbleCountD5](pebbleCountD5.md)  <sub>OPT</sub>
    * Description: The particle size that 5 percent of the particles are equal to or smaller than in the pebble count distribution
    * range: [String](types/String.md)
 * [pebbleCountD50](pebbleCountD50.md)  <sub>OPT</sub>
    * Description: The particle size that 50 percent of the particles are equal to or smaller than in the pebble count distribution
    * range: [String](types/String.md)
 * [pebbleCountD84](pebbleCountD84.md)  <sub>OPT</sub>
    * Description: The particle size that 84 percent of the particles are equal to or smaller than in the pebble count distribution
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
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [totalLWDCount](totalLWDCount.md)  <sub>OPT</sub>
    * Description: A running tally of large woody debris that meets a set criteria within the aquatic reach
    * range: [Integer](types/Integer.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:geo_surveyFieldData_in |

