
# Type: gwc_fieldSuperParent_pub




URI: [neon:GwcFieldSuperParentPub](https://data.neonscience.org/GwcFieldSuperParentPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GwcFieldSuperParentPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;eventID:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;collectDate:time%20%3F;waterTemp:double%20%3F;specificConductance:double%20%3F;aCollectedBy:string%20%3F;bCollectedBy:string%20%3F;altLocation:string%20%3F;altLongitude:double%20%3F;altLatitude:double%20%3F;maxDepth:double%20%3F;upperSegmentDepth:double%20%3F;lowerSegmentDepth:double%20%3F;startDate:time%20%3F;waterColorDescrip:string%20%3F;dissolvedOxygen:double%20%3F;dissolvedOxygenSaturation:double%20%3F;pH:double%20%3F;wellWaterDepth:double%20%3F;sampleDepth:double%20%3F;sampleExtractionMethod:string%20%3F;wellVolumePurged:double%20%3F;samplerType:string%20%3F;parentSampleID:string%20%3F;lakeSampleDepth1:double%20%3F;lakeSampleDepth2:double%20%3F;sdgSamplingProtocolVersion:string%20%3F;asiSamplingProtocolVersion:string%20%3F;aquaticSiteType:string%20%3F;parentSampleCode:string%20%3F;fieldDataQF:string%20%3F;samplingImpractical:string%20%3F;namedLocation:string%20%3F;waterClarityDescrip:string%20%3F;altCoordinateUncertainty:double%20%3F;altGeodeticDatum:string%20%3F;amcSamplingProtocolVersion:string%20%3F;swcSamplingProtocolVersion:string%20%3F;adequateSampleVol:string%20%3F])

## Attributes


### Own

 * [aCollectedBy](aCollectedBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [adequateSampleVol](adequateSampleVol.md)  <sub>OPT</sub>
    * Description: An indication of whether or not there was adequate sample volume available for collecting all samples. When no: samples are prioritized in this order: isotopes; filtered analytes; alkalinity titrations; unfiltered analytes; particulate analysis
    * range: [String](types/String.md)
 * [altCoordinateUncertainty](altCoordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given altLatitude and altLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [altGeodeticDatum](altGeodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth for alternate location coordinate
    * range: [String](types/String.md)
 * [altLatitude](altLatitude.md)  <sub>OPT</sub>
    * Description: Alternate Sampling Location coordinate - latitude
    * range: [Double](types/Double.md)
 * [altLocation](altLocation.md)  <sub>OPT</sub>
    * Description: Alternate Sampling Location description
    * range: [String](types/String.md)
 * [altLongitude](altLongitude.md)  <sub>OPT</sub>
    * Description: Alternate Sampling Location coordinate - longitude
    * range: [Double](types/Double.md)
 * [amcSamplingProtocolVersion](amcSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the aquatic microbes protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [aquaticSiteType](aquaticSiteType.md)  <sub>OPT</sub>
    * Description: Type of aquatic site, includes lake, river or stream
    * range: [String](types/String.md)
 * [asiSamplingProtocolVersion](asiSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the aquatic stable isotopes protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [bCollectedBy](bCollectedBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [coordinateUncertainty](coordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [decimalLatitude](decimalLatitude.md)  <sub>OPT</sub>
    * Description: The geographic latitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [decimalLongitude](decimalLongitude.md)  <sub>OPT</sub>
    * Description: The geographic longitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [dissolvedOxygen](dissolvedOxygen.md)  <sub>OPT</sub>
    * Description: Dissolved Oxygen Concentration
    * range: [Double](types/Double.md)
 * [dissolvedOxygenSaturation](dissolvedOxygenSaturation.md)  <sub>OPT</sub>
    * Description: Dissolved Oxygen Percent Saturation
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
 * [fieldDataQF](fieldDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for field data
    * range: [String](types/String.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [lakeSampleDepth1](lakeSampleDepth1.md)  <sub>OPT</sub>
    * Description: Sample depth of a single lake sample collected below the surface; the sample depth of the upper sample for a composite lake sample collected below the surface
    * range: [Double](types/Double.md)
 * [lakeSampleDepth2](lakeSampleDepth2.md)  <sub>OPT</sub>
    * Description: Sample depth of the lower sample for a composite lake sample collected below the surface
    * range: [Double](types/Double.md)
 * [lowerSegmentDepth](lowerSegmentDepth.md)  <sub>OPT</sub>
    * Description: Depth at bottom of stratified lake segment
    * range: [Double](types/Double.md)
 * [maxDepth](maxDepth.md)  <sub>OPT</sub>
    * Description: Maximum depth
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [pH](pH.md)  <sub>OPT</sub>
    * Description: Measurement of pH in sample
    * range: [Double](types/Double.md)
 * [parentSampleCode](parentSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a parent sample
    * range: [String](types/String.md)
 * [parentSampleID](parentSampleID.md)  <sub>OPT</sub>
    * Description: Parent sampleID of sample being processed
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleDepth](sampleDepth.md)  <sub>OPT</sub>
    * Description: Depth sample was collected
    * range: [Double](types/Double.md)
 * [sampleExtractionMethod](sampleExtractionMethod.md)  <sub>OPT</sub>
    * Description: Method used to extract the sample
    * range: [String](types/String.md)
 * [samplerType](samplerType.md)  <sub>OPT</sub>
    * Description: Type of sampler used to collect the sample
    * range: [String](types/String.md)
 * [samplingImpractical](samplingImpractical.md)  <sub>OPT</sub>
    * Description: Samples and/or measurements were not collected due to the indicated circumstance
    * range: [String](types/String.md)
 * [sdgSamplingProtocolVersion](sdgSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the dissolved gas protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [specificConductance](specificConductance.md)  <sub>OPT</sub>
    * Description: Conductivity auto-corrected to 25 degrees C
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [swcSamplingProtocolVersion](swcSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the water chemistry protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [upperSegmentDepth](upperSegmentDepth.md)  <sub>OPT</sub>
    * Description: Depth at top of stratified lake segment
    * range: [Double](types/Double.md)
 * [waterClarityDescrip](waterClarityDescrip.md)  <sub>OPT</sub>
    * Description: Qualitative description of water clarity
    * range: [String](types/String.md)
 * [waterColorDescrip](waterColorDescrip.md)  <sub>OPT</sub>
    * Description: Qualitative description of water color and clarity
    * range: [String](types/String.md)
 * [waterTemp](waterTemp.md)  <sub>OPT</sub>
    * Description: Temperature of water (C)
    * range: [Double](types/Double.md)
 * [wellVolumePurged](wellVolumePurged.md)  <sub>OPT</sub>
    * Description: Total volume removed from the well, prior to sampling
    * range: [Double](types/Double.md)
 * [wellWaterDepth](wellWaterDepth.md)  <sub>OPT</sub>
    * Description: Depth of water in well from top of well casing
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:gwc_fieldSuperParent_pub |
| **In Subsets:** | | DP1.20092.001 |

