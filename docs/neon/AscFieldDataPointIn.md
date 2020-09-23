
# Type: asc_fieldDataPoint_in




URI: [neon:AscFieldDataPointIn](https://data.neonscience.org/AscFieldDataPointIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AscFieldDataPointIn&#124;uid:string%20%3F;remarks:string%20%3F;stationID:string%20%3F;waterTemp:double%20%3F;specificConductance:double%20%3F;startDate:time%20%3F;endDate:time%20%3F;dissolvedOxygen:double%20%3F;dissolvedOxygenSaturation:double%20%3F;dataQF:string%20%3F;waterDepth:double%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;pointNumber:string%20%3F;coreLength:double%20%3F;sedimentSampleBarcode:string%20%3F;sedimentSampleFate:string%20%3F;sedimentSampleID:string%20%3F;zoneNumber:string%20%3F])

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
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
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
 * [sedimentSampleFate](sedimentSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sediment sample
    * range: [String](types/String.md)
 * [sedimentSampleID](sedimentSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for a sediment sample
    * range: [String](types/String.md)
 * [specificConductance](specificConductance.md)  <sub>OPT</sub>
    * Description: Conductivity auto-corrected to 25 degrees C
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
| **Mappings:** | | neon:asc_fieldDataPoint_in |
| **In Subsets:** | | DP0.20194.001 |

