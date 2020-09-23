
# Type: bry_productivity_pub




URI: [neon:BryProductivityPub](https://data.neonscience.org/BryProductivityPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BryProductivityPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;targetTaxaPresent:string%20%3F;subplotID:string%20%3F;clipID:string%20%3F;weighDate:time%20%3F;qaDryMass:string%20%3F;dryMass:double%20%3F;storageHours:double%20%3F;dryingHours:double%20%3F;samplingProtocolVersion:string%20%3F;collectedBy:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;totalSampledArea:double%20%3F;setNetCount:string%20%3F;sampledNetCount:string%20%3F;missingNetCount:string%20%3F;setBy:string%20%3F;setRemarks:string%20%3F;collectRemarks:string%20%3F;weighRemarks:string%20%3F;sampleCondition:string%20%3F;growthInterval:string%20%3F;bryType:string%20%3F;namedLocation:string%20%3F])

## Attributes


### Own

 * [bryType](bryType.md)  <sub>OPT</sub>
    * Description: Describes the dominant type of bryophyte present in a clipped sample
    * range: [String](types/String.md)
 * [clipID](clipID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the clip-harvest location within the plot
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [collectRemarks](collectRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the collect activity
    * range: [String](types/String.md)
 * [collectedBy](collectedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who collected the sample or specimen
    * range: [String](types/String.md)
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
 * [dryMass](dryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of sample or subsample
    * range: [Double](types/Double.md)
 * [dryingHours](dryingHours.md)  <sub>OPT</sub>
    * Description: Number of hours material was in a drying oven until dried to constant weight
    * range: [Double](types/Double.md)
 * [elevation](elevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level
    * range: [Double](types/Double.md)
 * [elevationUncertainty](elevationUncertainty.md)  <sub>OPT</sub>
    * Description: Uncertainty in elevation values (in meters)
    * range: [Double](types/Double.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [growthInterval](growthInterval.md)  <sub>OPT</sub>
    * Description: The number of growing days between when sampling began and the collection event
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [missingNetCount](missingNetCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of nets missing since set event
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [qaDryMass](qaDryMass.md)  <sub>OPT</sub>
    * Description: Indicates whether 'dryMass' value is associated with 'qa' measurement type
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [sampledNetCount](sampledNetCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of nets sampled
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [setBy](setBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who set the trap
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [setNetCount](setNetCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of nets set for sample collection
    * range: [String](types/String.md)
 * [setRemarks](setRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the set activity
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [storageHours](storageHours.md)  <sub>OPT</sub>
    * Description: Total number of hours clipped biomass was stored between collection and processing
    * range: [Double](types/Double.md)
 * [subplotID](subplotID.md)  <sub>OPT</sub>
    * Description: Identifier for the NEON subplot
    * range: [String](types/String.md)
 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [totalSampledArea](totalSampledArea.md)  <sub>OPT</sub>
    * Description: Total area sampled
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [weighDate](weighDate.md)  <sub>OPT</sub>
    * Description: Date that sample or subsample was weighed
    * range: [Time](types/Time.md)
 * [weighRemarks](weighRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the weigh activity
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:bry_productivity_pub |
| **In Subsets:** | | DP1.10035.001 |

