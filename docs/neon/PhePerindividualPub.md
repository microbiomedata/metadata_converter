
# Type: phe_perindividual_pub




URI: [neon:PhePerindividualPub](https://data.neonscience.org/PhePerindividualPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PhePerindividualPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;date:time%20%3F;remarks:string%20%3F;taxonID:string%20%3F;identificationQualifier:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;individualID:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;scientificName:string%20%3F;taxonRank:string%20%3F;identifiedBy:string%20%3F;transectMeter:double%20%3F;directionFromTransect:string%20%3F;ninetyDegreeDistance:double%20%3F;growthForm:string%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;editedDate:time%20%3F;individualBarcode:string%20%3F;sampleCoordinateUncertainty:double%20%3F;sampleElevation:double%20%3F;sampleElevationUncertainty:double%20%3F;sampleLatitude:double%20%3F;sampleLongitude:double%20%3F;subtypeSpecification:string%20%3F;sampleGeodeticDatum:string%20%3F;vstTag:string%20%3F])

## Attributes


### Own

 * [coordinateUncertainty](coordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [date](date.md)  <sub>OPT</sub>
    * Description: Date or date and time of measurement, observation, or collection event
    * range: [Time](types/Time.md)
 * [decimalLatitude](decimalLatitude.md)  <sub>OPT</sub>
    * Description: The geographic latitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [decimalLongitude](decimalLongitude.md)  <sub>OPT</sub>
    * Description: The geographic longitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [directionFromTransect](directionFromTransect.md)  <sub>OPT</sub>
    * Description: Direction (right or left) of individual from transect, when transect is walked in a clockwise direction
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [editedDate](editedDate.md)  <sub>OPT</sub>
    * Description: The date-time that record was edited
    * range: [Time](types/Time.md)
 * [elevation](elevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level
    * range: [Double](types/Double.md)
 * [elevationUncertainty](elevationUncertainty.md)  <sub>OPT</sub>
    * Description: Uncertainty in elevation values (in meters)
    * range: [Double](types/Double.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [growthForm](growthForm.md)  <sub>OPT</sub>
    * Description: The growth form classification
    * range: [String](types/String.md)
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
 * [identifiedBy](identifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who identified the specimen
    * range: [String](types/String.md)
 * [individualBarcode](individualBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a tagged individual
    * range: [String](types/String.md)
 * [individualID](individualID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier for an individual: NEON.MOD.D##.######
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [ninetyDegreeDistance](ninetyDegreeDistance.md)  <sub>OPT</sub>
    * Description: Perpendicular distance from transect to selected individual (in meters)
    * range: [Double](types/Double.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleCoordinateUncertainty](sampleCoordinateUncertainty.md)  <sub>OPT</sub>
    * Description: Coordinate uncertainty of a sampled location
    * range: [Double](types/Double.md)
 * [sampleElevation](sampleElevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level of a sampled location
    * range: [Double](types/Double.md)
 * [sampleElevationUncertainty](sampleElevationUncertainty.md)  <sub>OPT</sub>
    * Description: Uncertainty in elevation values (in meters) of a sampled location
    * range: [Double](types/Double.md)
 * [sampleGeodeticDatum](sampleGeodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position, of the sample, on the earth
    * range: [String](types/String.md)
 * [sampleLatitude](sampleLatitude.md)  <sub>OPT</sub>
    * Description: Latitude of the sampled location
    * range: [Double](types/Double.md)
 * [sampleLongitude](sampleLongitude.md)  <sub>OPT</sub>
    * Description: Longitude of the sampled location
    * range: [Double](types/Double.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [subtypeSpecification](subtypeSpecification.md)  <sub>OPT</sub>
    * Description: Type of plot or grid; mammal: diversity, pathogen, training; bird: ninePoints, onePoint; phenology: primary, phenocam
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [taxonRank](taxonRank.md)  <sub>OPT</sub>
    * Description: The lowest level taxonomic rank that can be determined for the individual or specimen
    * range: [String](types/String.md)
 * [transectMeter](transectMeter.md)  <sub>OPT</sub>
    * Description: Distance (in meters) of individual from beginning of transect, when transect is walked in clockwise direction
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [vstTag](vstTag.md)  <sub>OPT</sub>
    * Description: Indicator for whether a tagID is associated with vegetation structure measurements
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:phe_perindividual_pub |
| **In Subsets:** | | DP1.10055.001 |

