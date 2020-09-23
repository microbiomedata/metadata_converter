
# Type: brd_countdata_in




URI: [neon:BrdCountdataIn](https://data.neonscience.org/BrdCountdataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BrdCountdataIn&#124;uid:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;taxonID:string%20%3F;eventID:string%20%3F;targetTaxaPresent:string%20%3F;identifiedBy:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;internalLabID:string%20%3F;locationID:string%20%3F;pointCountMinute:string%20%3F;observerDistance:double%20%3F;detectionMethod:string%20%3F;sexOrAge:string%20%3F;visualConfirmation:string%20%3F;clusterCode:string%20%3F;clusterSize:string%20%3F;pointID:string%20%3F;dataQF:string%20%3F;taxonRaw:string%20%3F])

## Attributes


### Own

 * [clusterCode](clusterCode.md)  <sub>OPT</sub>
    * Description: Alphabetic code (A-Z) linked to clusters (groups of individuals of the same species) spanning multiple records
    * range: [String](types/String.md)
 * [clusterSize](clusterSize.md)  <sub>OPT</sub>
    * Description: Number of individuals in a cluster (a group of individuals of the same species)
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [detectionMethod](detectionMethod.md)  <sub>OPT</sub>
    * Description: How the individual(s) was (were) first detected by the observer
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [identifiedBy](identifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who identified the specimen
    * range: [String](types/String.md)
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [observerDistance](observerDistance.md)  <sub>OPT</sub>
    * Description: Radial distance between the observer and the individual(s) being observed
    * range: [Double](types/Double.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [pointCountMinute](pointCountMinute.md)  <sub>OPT</sub>
    * Description: The minute of sampling within the point count period
    * range: [String](types/String.md)
 * [pointID](pointID.md)  <sub>OPT</sub>
    * Description: Identifier for a point location
    * range: [String](types/String.md)
 * [sexOrAge](sexOrAge.md)  <sub>OPT</sub>
    * Description: Sex of individual if detectable, age of individual if individual can not be sexed
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [taxonRaw](taxonRaw.md)  <sub>OPT</sub>
    * Description: Raw species code
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [visualConfirmation](visualConfirmation.md)  <sub>OPT</sub>
    * Description: Whether the individual(s) was (were) seen after the initial detection
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:brd_countdata_in |

