
# Type: mga_soilLabSummary_pub




URI: [neon:MgaSoilLabSummaryPub](https://data.neonscience.org/MgaSoilLabSummaryPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MgaSoilLabSummaryPub&#124;uid:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;labSpecificStartDate:time%20%3F;labSpecificEndDate:time%20%3F;targetTaxonGroup:string%20%3F])

## Attributes


### Own

 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [labSpecificEndDate](labSpecificEndDate.md)  <sub>OPT</sub>
    * Description: Date a specific analyte, instrument, and associated method detection limit combination ended
    * range: [Time](types/Time.md)
 * [labSpecificStartDate](labSpecificStartDate.md)  <sub>OPT</sub>
    * Description: Date a specific analyte, instrument, and associated method detection limit combination started
    * range: [Time](types/Time.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [targetTaxonGroup](targetTaxonGroup.md)  <sub>OPT</sub>
    * Description: Taxonomic group targeted
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mga_soilLabSummary_pub |

