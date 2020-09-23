
# Type: sdrc_stageDischargeCurveInfo_pub




URI: [neon:SdrcStageDischargeCurveInfoPub](https://data.neonscience.org/SdrcStageDischargeCurveInfoPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SdrcStageDischargeCurveInfoPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;curveID:string%20%3F;allEventID:string%20%3F;maxQ:double%20%3F;maxStage:double%20%3F;minQ:double%20%3F;minStage:double%20%3F;waterYear:string%20%3F;curveEndDate:time%20%3F;curveStartDate:time%20%3F])

## Attributes


### Own

 * [allEventID](allEventID.md)  <sub>OPT</sub>
    * Description: All of the eventIDs associated with guage and discharge readings that are used to determine the rating curve fit
    * range: [String](types/String.md)
 * [curveEndDate](curveEndDate.md)  <sub>OPT</sub>
    * Description: End date for the curve
    * range: [Time](types/Time.md)
 * [curveID](curveID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the curve fit to gauge and discharge measurements
    * range: [String](types/String.md)
 * [curveStartDate](curveStartDate.md)  <sub>OPT</sub>
    * Description: Start date for the curve
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [maxQ](maxQ.md)  <sub>OPT</sub>
    * Description: The maximum empirical discharge measurement included in the stage discharge rating curve
    * range: [Double](types/Double.md)
 * [maxStage](maxStage.md)  <sub>OPT</sub>
    * Description: The maximum empirical stage measurement included in the stage discharge rating curve
    * range: [Double](types/Double.md)
 * [minQ](minQ.md)  <sub>OPT</sub>
    * Description: The minimum empirical discharge measurement included in the stage discharge rating curve
    * range: [Double](types/Double.md)
 * [minStage](minStage.md)  <sub>OPT</sub>
    * Description: The minimum empirical stage measurement included in the stage discharge rating curve
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
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
 * [waterYear](waterYear.md)  <sub>OPT</sub>
    * Description: The USGS standard definition: the 12-month period October 1, for any given year through September 30, of the following year. The water year is designated by the calendar year in which it ends and which includes 9 of the 12 months
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sdrc_stageDischargeCurveInfo_pub |

