
# Type: geo_missingLine_in




URI: [neon:GeoMissingLineIn](https://data.neonscience.org/GeoMissingLineIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GeoMissingLineIn&#124;uid:string%20%3F;remarks:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;locationID:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;attemptNumber:integer%20%3F;missingLinePoint1:string%20%3F;missingLinePoint2:string%20%3F;missingLineResultsdH:double%20%3F;missingLineResultsHD:double%20%3F;missingLineReultsStDev:double%20%3F])

## Attributes


### Own

 * [attemptNumber](attemptNumber.md)  <sub>OPT</sub>
    * Description: The attempt number associated with the missing line workflow
    * range: [Integer](types/Integer.md)
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
 * [missingLinePoint1](missingLinePoint1.md)  <sub>OPT</sub>
    * Description: Identifier for the first point used in the missing line workflow
    * range: [String](types/String.md)
 * [missingLinePoint2](missingLinePoint2.md)  <sub>OPT</sub>
    * Description: Identifier for the second point used in the missing line workflow
    * range: [String](types/String.md)
 * [missingLineResultsHD](missingLineResultsHD.md)  <sub>OPT</sub>
    * Description: The difference in horizontal distance calculated between the first and second shots during the missing line workflow
    * range: [Double](types/Double.md)
 * [missingLineResultsdH](missingLineResultsdH.md)  <sub>OPT</sub>
    * Description: The difference in elevation calculated between the first and second shots during the missing line workflow
    * range: [Double](types/Double.md)
 * [missingLineReultsStDev](missingLineReultsStDev.md)  <sub>OPT</sub>
    * Description: The standard deviation calculated between the first and second shots during the missing line workflow
    * range: [Double](types/Double.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:geo_missingLine_in |

