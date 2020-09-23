
# Type: dpm_field_pub




URI: [neon:DpmFieldPub](https://data.neonscience.org/DpmFieldPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DpmFieldPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;aCollectedBy:string%20%3F;bCollectedBy:string%20%3F;aSetBy:string%20%3F;bSetBy:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;fieldFilterCondition:string%20%3F;fieldFilterConditionRemarks:string%20%3F;fieldFilterDamage:string%20%3F;fieldFilterDamageRemarks:string%20%3F;filterID:string%20%3F;filterWet:double%20%3F;equipCondition:string%20%3F;equipConditionDesc:string%20%3F])

## Attributes


### Own

 * [aCollectedBy](aCollectedBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [aSetBy](aSetBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who set the collector
    * range: [String](types/String.md)
 * [bCollectedBy](bCollectedBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [bSetBy](bSetBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who set the collector
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [coordinateUncertainty](coordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [decimalLatitude](decimalLatitude.md)  <sub>OPT</sub>
    * Description: The geographic latitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [decimalLongitude](decimalLongitude.md)  <sub>OPT</sub>
    * Description: The geographic longitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [elevation](elevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level
    * range: [Double](types/Double.md)
 * [elevationUncertainty](elevationUncertainty.md)  <sub>OPT</sub>
    * Description: Uncertainty in elevation values (in meters)
    * range: [Double](types/Double.md)
 * [equipCondition](equipCondition.md)  <sub>OPT</sub>
    * Description: Condition of the equipment
    * range: [String](types/String.md)
 * [equipConditionDesc](equipConditionDesc.md)  <sub>OPT</sub>
    * Description: Description of problems with the equipment
    * range: [String](types/String.md)
 * [fieldFilterCondition](fieldFilterCondition.md)  <sub>OPT</sub>
    * Description: Condition of the filter reported in the field
    * range: [String](types/String.md)
 * [fieldFilterConditionRemarks](fieldFilterConditionRemarks.md)  <sub>OPT</sub>
    * Description: Additional description of the field filter condition
    * range: [String](types/String.md)
 * [fieldFilterDamage](fieldFilterDamage.md)  <sub>OPT</sub>
    * Description: Field description of how the filter is damaged, if at all
    * range: [String](types/String.md)
 * [fieldFilterDamageRemarks](fieldFilterDamageRemarks.md)  <sub>OPT</sub>
    * Description: Additional description of possible field damages, e.g., tear, hole, piece missing
    * range: [String](types/String.md)
 * [filterID](filterID.md)  <sub>OPT</sub>
    * Description: The non-repeating manufacturer-generated ID of each filter
    * range: [String](types/String.md)
 * [filterWet](filterWet.md)  <sub>OPT</sub>
    * Description: Percentage of the filter area that is wet
    * range: [Double](types/Double.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:dpm_field_pub |
| **In Subsets:** | | DP1.00101.001 |

