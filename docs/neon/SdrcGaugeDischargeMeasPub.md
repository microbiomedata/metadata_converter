
# Type: sdrc_gaugeDischargeMeas_pub




URI: [neon:SdrcGaugeDischargeMeasPub](https://data.neonscience.org/SdrcGaugeDischargeMeasPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SdrcGaugeDischargeMeasPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;eventID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;gaugeHeight:double%20%3F;gaugeHeightOffset:double%20%3F;gaugeHeightUnc:double%20%3F;includedInRatingCurve:string%20%3F;L1DataQF:string%20%3F;recalculatedL1QF:string%20%3F;streamDischarge:double%20%3F;streamDischargeUnc:double%20%3F])

## Attributes


### Own

 * [L1DataQF](L1DataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag associated with the L1 data
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [gaugeHeight](gaugeHeight.md)  <sub>OPT</sub>
    * Description: Height of water at staff gauge
    * range: [Double](types/Double.md)
 * [gaugeHeightOffset](gaugeHeightOffset.md)  <sub>OPT</sub>
    * Description: Offset applied to the staff gauge reading to account for changes over time in position
    * range: [Double](types/Double.md)
 * [gaugeHeightUnc](gaugeHeightUnc.md)  <sub>OPT</sub>
    * Description: Uncertainty associated with the gaugeHeight measurements
    * range: [Double](types/Double.md)
 * [includedInRatingCurve](includedInRatingCurve.md)  <sub>OPT</sub>
    * Description: Indicator of whether or not a gauging was included in the rating curve; true or false
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [recalculatedL1QF](recalculatedL1QF.md)  <sub>OPT</sub>
    * Description: Data quality flag generated when L1 discharge directly from the meter and streamDischarge from point data do not match
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [streamDischarge](streamDischarge.md)  <sub>OPT</sub>
    * Description: Calculated discharge from the velocity meter device point measurements
    * range: [Double](types/Double.md)
 * [streamDischargeUnc](streamDischargeUnc.md)  <sub>OPT</sub>
    * Description: Uncertainty associated with the streamDischarge measurements
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sdrc_gaugeDischargeMeas_pub |
| **In Subsets:** | | DP4.00133.001 |

