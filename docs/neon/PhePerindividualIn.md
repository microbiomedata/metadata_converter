
# Type: phe_perindividual_in




URI: [neon:PhePerindividualIn](https://data.neonscience.org/PhePerindividualIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PhePerindividualIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;taxonID:string%20%3F;identificationQualifier:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;individualID:string%20%3F;enteredBy:string%20%3F;acceptedTaxonID:string%20%3F;identifiedBy:string%20%3F;identifiedDate:time%20%3F;addDate:time%20%3F;transectMeter:double%20%3F;directionFromTransect:string%20%3F;ninetyDegreeDistance:double%20%3F;growthForm:string%20%3F;dropPlant:string%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;individualFate:string%20%3F;editedDate:time%20%3F;gpsDatafile:string%20%3F;individualBarcode:string%20%3F;logCount:double%20%3F;sampleCoordinateUncertainty:double%20%3F;sampleElevation:double%20%3F;sampleElevationUncertainty:double%20%3F;sampleLatitude:double%20%3F;sampleLongitude:double%20%3F;subtypeSpecification:string%20%3F;vstTag:string%20%3F])

## Attributes


### Own

 * [acceptedTaxonID](acceptedTaxonID.md)  <sub>OPT</sub>
    * Description: Accepted species code, based on one or more sources
    * range: [String](types/String.md)
 * [addDate](addDate.md)  <sub>OPT</sub>
    * Description: Date that individual was added for monitoring
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [directionFromTransect](directionFromTransect.md)  <sub>OPT</sub>
    * Description: Direction (right or left) of individual from transect, when transect is walked in a clockwise direction
    * range: [String](types/String.md)
 * [dropPlant](dropPlant.md)  <sub>OPT</sub>
    * Description: identifies an individual plant that will no longer be monitored, drop= dropped for good, seasonalDrop= Seasonally dropped
    * range: [String](types/String.md)
 * [editedDate](editedDate.md)  <sub>OPT</sub>
    * Description: The date-time that record was edited
    * range: [Time](types/Time.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [enteredBy](enteredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who entered the data
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [gpsDatafile](gpsDatafile.md)  <sub>OPT</sub>
    * Description: Name assigned to GPS file
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
 * [identifiedDate](identifiedDate.md)  <sub>OPT</sub>
    * Description: Date on which the sample, individual, or specimen was identified
    * range: [Time](types/Time.md)
 * [individualBarcode](individualBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a tagged individual
    * range: [String](types/String.md)
 * [individualFate](individualFate.md)  <sub>OPT</sub>
    * Description: Fate of a tagged individual
    * range: [String](types/String.md)
 * [individualID](individualID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier for an individual: NEON.MOD.D##.######
    * range: [String](types/String.md)
 * [logCount](logCount.md)  <sub>OPT</sub>
    * Description: Number of GPS points collected
    * range: [Double](types/Double.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [ninetyDegreeDistance](ninetyDegreeDistance.md)  <sub>OPT</sub>
    * Description: Perpendicular distance from transect to selected individual (in meters)
    * range: [Double](types/Double.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
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
 * [sampleLatitude](sampleLatitude.md)  <sub>OPT</sub>
    * Description: Latitude of the sampled location
    * range: [Double](types/Double.md)
 * [sampleLongitude](sampleLongitude.md)  <sub>OPT</sub>
    * Description: Longitude of the sampled location
    * range: [Double](types/Double.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [subtypeSpecification](subtypeSpecification.md)  <sub>OPT</sub>
    * Description: Type of plot or grid; mammal: diversity, pathogen, training; bird: ninePoints, onePoint; phenology: primary, phenocam
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
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
| **Mappings:** | | neon:phe_perindividual_in |
| **In Subsets:** | | DP0.10002.001 |

