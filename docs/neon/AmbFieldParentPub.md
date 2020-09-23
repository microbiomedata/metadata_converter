
# Type: amb_fieldParent_pub




URI: [neon:AmbFieldParentPub](https://data.neonscience.org/AmbFieldParentPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AmbFieldParentPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;samplingProtocolVersion:string%20%3F;archiveID:string%20%3F;collectedBy:string%20%3F;habitatType:string%20%3F;sampleNumber:string%20%3F;substratumSizeClass:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;geneticSampleID:string%20%3F;aquaticSiteType:string%20%3F;fieldSampleVolume:double%20%3F;geneticSampleCode:string%20%3F;samplingImpractical:string%20%3F;sampleMaterial:string%20%3F;namedLocation:string%20%3F;archiveFilteredSampleVolume:string%20%3F;archiveSampleCode:string%20%3F;geneticFilteredSampleVolume:string%20%3F;aquMicrobeType:string%20%3F;aquMicrobeScrubArea:double%20%3F;labSampleMedium:string%20%3F])

## Attributes


### Own

 * [aquMicrobeScrubArea](aquMicrobeScrubArea.md)  <sub>OPT</sub>
    * Description: Sampler area of epilithon or epixylon sample
    * range: [Double](types/Double.md)
 * [aquMicrobeType](aquMicrobeType.md)  <sub>OPT</sub>
    * Description: Group of organisms in an aquatic microbes sample defined by habitat or location
    * range: [String](types/String.md)
 * [aquaticSiteType](aquaticSiteType.md)  <sub>OPT</sub>
    * Description: Type of aquatic site, includes lake, river or stream
    * range: [String](types/String.md)
 * [archiveFilteredSampleVolume](archiveFilteredSampleVolume.md)  <sub>OPT</sub>
    * Description: Volume of water filtered for microbial archive
    * range: [String](types/String.md)
 * [archiveID](archiveID.md)  <sub>OPT</sub>
    * Description: Identifier for the archive sample
    * range: [String](types/String.md)
 * [archiveSampleCode](archiveSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of archive sample
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
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
 * [elevation](elevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level
    * range: [Double](types/Double.md)
 * [elevationUncertainty](elevationUncertainty.md)  <sub>OPT</sub>
    * Description: Uncertainty in elevation values (in meters)
    * range: [Double](types/Double.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fieldSampleVolume](fieldSampleVolume.md)  <sub>OPT</sub>
    * Description: Sample volume collected in the field
    * range: [Double](types/Double.md)
 * [geneticFilteredSampleVolume](geneticFilteredSampleVolume.md)  <sub>OPT</sub>
    * Description: Volume of filtered water for genetic analysis of microbes
    * range: [String](types/String.md)
 * [geneticSampleCode](geneticSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a genetic sample
    * range: [String](types/String.md)
 * [geneticSampleID](geneticSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for the genetic sample
    * range: [String](types/String.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [habitatType](habitatType.md)  <sub>OPT</sub>
    * Description: Habitat type sampled
    * range: [String](types/String.md)
 * [labSampleMedium](labSampleMedium.md)  <sub>OPT</sub>
    * Description: Physical form of the specimen
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
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
 * [sampleMaterial](sampleMaterial.md)  <sub>OPT</sub>
    * Description: The material in which a sample was embedded prior to the sampling event
    * range: [String](types/String.md)
 * [sampleNumber](sampleNumber.md)  <sub>OPT</sub>
    * Description: Number of sample collected
    * range: [String](types/String.md)
 * [samplingImpractical](samplingImpractical.md)  <sub>OPT</sub>
    * Description: Samples and/or measurements were not collected due to the indicated circumstance
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [substratumSizeClass](substratumSizeClass.md)  <sub>OPT</sub>
    * Description: Size class of the substratum sampled
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:amb_fieldParent_pub |
| **In Subsets:** | | DP1.20280.001 |
|  | | DP1.20279.001 |

