
# Type: fsp_sampleMetadata_pub




URI: [neon:FspSampleMetadataPub](https://data.neonscience.org/FspSampleMetadataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[FspSampleMetadataPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;taxonID:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;individualID:string%20%3F;nlcdClass:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;scientificName:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;plantStatus:string%20%3F;plotType:string%20%3F;altLongitude:double%20%3F;altLatitude:double%20%3F;collectedBy:string%20%3F;locationID:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;altCoordinateUncertainty:double%20%3F;measurementDate:time%20%3F;individualCode:string%20%3F;cfcIndividual:string%20%3F;leafAge:string%20%3F;leafArrangement:string%20%3F;leafExposure:string%20%3F;leafSamplePosition:string%20%3F;leafStatus:string%20%3F;measurementVenue:string%20%3F;spectralSampleCode:string%20%3F;spectralSampleID:string%20%3F;targetStatus:string%20%3F;targetType:string%20%3F])

## Attributes


### Own

 * [altCoordinateUncertainty](altCoordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given altLatitude and altLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [altLatitude](altLatitude.md)  <sub>OPT</sub>
    * Description: Alternate Sampling Location coordinate - latitude
    * range: [Double](types/Double.md)
 * [altLongitude](altLongitude.md)  <sub>OPT</sub>
    * Description: Alternate Sampling Location coordinate - longitude
    * range: [Double](types/Double.md)
 * [cfcIndividual](cfcIndividual.md)  <sub>OPT</sub>
    * Description: Indicator for whether the sample comes from a canopy foliage individual
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
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [individualCode](individualCode.md)  <sub>OPT</sub>
    * Description: Barcode of an individual
    * range: [String](types/String.md)
 * [individualID](individualID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier for an individual: NEON.MOD.D##.######
    * range: [String](types/String.md)
 * [leafAge](leafAge.md)  <sub>OPT</sub>
    * Description: Relative age of the leaf or needles
    * range: [String](types/String.md)
 * [leafArrangement](leafArrangement.md)  <sub>OPT</sub>
    * Description: Physical arrangement of leaves or needles during spectral measurement
    * range: [String](types/String.md)
 * [leafExposure](leafExposure.md)  <sub>OPT</sub>
    * Description: Sun exposure of the leaf or needles
    * range: [String](types/String.md)
 * [leafSamplePosition](leafSamplePosition.md)  <sub>OPT</sub>
    * Description: Vertical position of a leaf or needle sample in the canopy
    * range: [String](types/String.md)
 * [leafStatus](leafStatus.md)  <sub>OPT</sub>
    * Description: Status of the leaf or needles
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [measurementDate](measurementDate.md)  <sub>OPT</sub>
    * Description: Date of the measurement event
    * range: [Time](types/Time.md)
 * [measurementVenue](measurementVenue.md)  <sub>OPT</sub>
    * Description: Physical setting for measurements
    * range: [String](types/String.md)
 * [nlcdClass](nlcdClass.md)  <sub>OPT</sub>
    * Description: National Land Cover Database Vegetation Type Name
    * range: [String](types/String.md)
 * [plantStatus](plantStatus.md)  <sub>OPT</sub>
    * Description: Physical status of individual: live, dead, lost
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [plotType](plotType.md)  <sub>OPT</sub>
    * Description: NEON plot type in which sampling occurred: tower, distributed or gradient
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
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [spectralSampleCode](spectralSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a spectral sample
    * range: [String](types/String.md)
 * [spectralSampleID](spectralSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a spectral sample
    * range: [String](types/String.md)
 * [targetStatus](targetStatus.md)  <sub>OPT</sub>
    * Description: Status of foliage targeted for measurements
    * range: [String](types/String.md)
 * [targetType](targetType.md)  <sub>OPT</sub>
    * Description: Type of foliage targeted for measurments
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:fsp_sampleMetadata_pub |

