
# Type: brd_countdata_pub




URI: [neon:BrdCountdataPub](https://data.neonscience.org/BrdCountdataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BrdCountdataPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;taxonID:string%20%3F;eventID:string%20%3F;scientificName:string%20%3F;taxonRank:string%20%3F;targetTaxaPresent:string%20%3F;identifiedBy:string%20%3F;plotType:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;family:string%20%3F;pointCountMinute:string%20%3F;observerDistance:double%20%3F;detectionMethod:string%20%3F;sexOrAge:string%20%3F;visualConfirmation:string%20%3F;clusterCode:string%20%3F;clusterSize:string%20%3F;pointID:string%20%3F;vernacularName:string%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;nativeStatusCode:string%20%3F])

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
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [family](family.md)  <sub>OPT</sub>
    * Description: The scientific name of the family in which the taxon is classified
    * range: [String](types/String.md)
 * [identifiedBy](identifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who identified the specimen
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [nativeStatusCode](nativeStatusCode.md)  <sub>OPT</sub>
    * Description: The process by which the taxon became established in the location
    * range: [String](types/String.md)
 * [observerDistance](observerDistance.md)  <sub>OPT</sub>
    * Description: Radial distance between the observer and the individual(s) being observed
    * range: [Double](types/Double.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [plotType](plotType.md)  <sub>OPT</sub>
    * Description: NEON plot type in which sampling occurred: tower, distributed or gradient
    * range: [String](types/String.md)
 * [pointCountMinute](pointCountMinute.md)  <sub>OPT</sub>
    * Description: The minute of sampling within the point count period
    * range: [String](types/String.md)
 * [pointID](pointID.md)  <sub>OPT</sub>
    * Description: Identifier for a point location
    * range: [String](types/String.md)
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
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
 * [taxonRank](taxonRank.md)  <sub>OPT</sub>
    * Description: The lowest level taxonomic rank that can be determined for the individual or specimen
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [vernacularName](vernacularName.md)  <sub>OPT</sub>
    * Description: A common or vernacular name
    * range: [String](types/String.md)
 * [visualConfirmation](visualConfirmation.md)  <sub>OPT</sub>
    * Description: Whether the individual(s) was (were) seen after the initial detection
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:brd_countdata_pub |

