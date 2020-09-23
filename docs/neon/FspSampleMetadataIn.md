
# Type: fsp_sampleMetadata_in




URI: [neon:FspSampleMetadataIn](https://data.neonscience.org/FspSampleMetadataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[FspSampleMetadataIn&#124;uid:string%20%3F;remarks:string%20%3F;taxonID:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;individualID:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;plantStatus:string%20%3F;altLongitude:double%20%3F;altLatitude:double%20%3F;collectedBy:string%20%3F;locationID:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;altCoordinateUncertainty:double%20%3F;measurementDate:time%20%3F;individualCode:string%20%3F;individualFate:string%20%3F;cfcIndividual:string%20%3F;leafAge:string%20%3F;leafArrangement:string%20%3F;leafExposure:string%20%3F;leafSamplePosition:string%20%3F;leafStatus:string%20%3F;measurementVenue:string%20%3F;spectralSampleCode:string%20%3F;spectralSampleFate:string%20%3F;spectralSampleID:string%20%3F;targetStatus:string%20%3F;targetType:string%20%3F])

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
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [individualCode](individualCode.md)  <sub>OPT</sub>
    * Description: Barcode of an individual
    * range: [String](types/String.md)
 * [individualFate](individualFate.md)  <sub>OPT</sub>
    * Description: Fate of a tagged individual
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
 * [plantStatus](plantStatus.md)  <sub>OPT</sub>
    * Description: Physical status of individual: live, dead, lost
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
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
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [spectralSampleCode](spectralSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a spectral sample
    * range: [String](types/String.md)
 * [spectralSampleFate](spectralSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a spectral sample
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
| **Mappings:** | | neon:fsp_sampleMetadata_in |

