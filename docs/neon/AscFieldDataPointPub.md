
# Type: asc_fieldDataPoint_pub




URI: [neon:AscFieldDataPointPub](https://data.neonscience.org/AscFieldDataPointPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AscFieldDataPointPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;waterTemp:double%20%3F;specificConductance:double%20%3F;startDate:time%20%3F;endDate:time%20%3F;dissolvedOxygen:double%20%3F;dissolvedOxygenSaturation:double%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;waterDepth:double%20%3F;pointNumber:string%20%3F;coreLength:double%20%3F;observations:string%20%3F;sedimentSampleBarcode:string%20%3F;sedimentSampleID:string%20%3F;zoneNumber:string%20%3F])

## Attributes


### Own

 * [coreLength](coreLength.md)  <sub>OPT</sub>
    * Description: Length of core
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [dissolvedOxygen](dissolvedOxygen.md)  <sub>OPT</sub>
    * Description: Dissolved Oxygen Concentration
    * range: [Double](types/Double.md)
 * [dissolvedOxygenSaturation](dissolvedOxygenSaturation.md)  <sub>OPT</sub>
    * Description: Dissolved Oxygen Percent Saturation
    * range: [Double](types/Double.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [observations](observations.md)  <sub>OPT</sub>
    * Description: Notes about quality of a sample; measurement; or area
    * range: [String](types/String.md)
 * [pointNumber](pointNumber.md)  <sub>OPT</sub>
    * Description: Number of the point sampled for a given location
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
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
 * [specificConductance](specificConductance.md)  <sub>OPT</sub>
    * Description: Conductivity auto-corrected to 25 degrees C
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [waterDepth](waterDepth.md)  <sub>OPT</sub>
    * Description: Depth of water
    * range: [Double](types/Double.md)
 * [waterTemp](waterTemp.md)  <sub>OPT</sub>
    * Description: Temperature of water (C)
    * range: [Double](types/Double.md)
 * [zoneNumber](zoneNumber.md)  <sub>OPT</sub>
    * Description: Number of the zone sampled for a given location
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:asc_fieldDataPoint_pub |
| **In Subsets:** | | DP1.20197.001 |

