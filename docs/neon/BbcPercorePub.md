
# Type: bbc_percore_pub




URI: [neon:BbcPercorePub](https://data.neonscience.org/BbcPercorePub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BbcPercorePub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;subplotID:string%20%3F;clipID:string%20%3F;samplingProtocolVersion:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;litterDepth:double%20%3F;namedLocation:string%20%3F;bareGround:string%20%3F;coreDiameter:double%20%3F;coreID:string%20%3F;monolithLength:double%20%3F;monolithWidth:double%20%3F;rootSampleArea:double%20%3F;rootSampleDepth:double%20%3F;rootSamplingMethod:string%20%3F;rootSamplingPossible:string%20%3F;wst10cmDist:double%20%3F;wst1cmDist:double%20%3F;toxicodendronPossible:string%20%3F])

## Attributes


### Own

 * [bareGround](bareGround.md)  <sub>OPT</sub>
    * Description: Percent of the sampling area from which sample was collected that is bare ground
    * range: [String](types/String.md)
 * [clipID](clipID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the clip-harvest location within the plot
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [coordinateUncertainty](coordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [coreDiameter](coreDiameter.md)  <sub>OPT</sub>
    * Description: Diameter of the core sample
    * range: [Double](types/Double.md)
 * [coreID](coreID.md)  <sub>OPT</sub>
    * Description: Identifier for the soil sample within the clipID
    * range: [String](types/String.md)
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
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [litterDepth](litterDepth.md)  <sub>OPT</sub>
    * Description: Depth of litter layer
    * range: [Double](types/Double.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [monolithLength](monolithLength.md)  <sub>OPT</sub>
    * Description: Length of the monolith sample top surface
    * range: [Double](types/Double.md)
 * [monolithWidth](monolithWidth.md)  <sub>OPT</sub>
    * Description: Width of the monolith sample top surface
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
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
 * [rootSampleArea](rootSampleArea.md)  <sub>OPT</sub>
    * Description: Area of soil sample, calculated from coreDiameter or monolith dimensions
    * range: [Double](types/Double.md)
 * [rootSampleDepth](rootSampleDepth.md)  <sub>OPT</sub>
    * Description: Depth to which soil sample was collected
    * range: [Double](types/Double.md)
 * [rootSamplingMethod](rootSamplingMethod.md)  <sub>OPT</sub>
    * Description: Method by which soil sample was collected
    * range: [String](types/String.md)
 * [rootSamplingPossible](rootSamplingPossible.md)  <sub>OPT</sub>
    * Description: Indicator of whether collection of a soil sample was possible
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [subplotID](subplotID.md)  <sub>OPT</sub>
    * Description: Identifier for the NEON subplot
    * range: [String](types/String.md)
 * [toxicodendronPossible](toxicodendronPossible.md)  <sub>OPT</sub>
    * Description: Indicator for whether a sample may contain Toxicodendron spp
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [wst10cmDist](wst10cmDist.md)  <sub>OPT</sub>
    * Description: Distance to nearest woody stem >= 10 cm diameter at breast height
    * range: [Double](types/Double.md)
 * [wst1cmDist](wst1cmDist.md)  <sub>OPT</sub>
    * Description: Distance to nearest woody stem with diameter at breast height < 10 cm and >= 1 cm
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:bbc_percore_pub |
| **In Subsets:** | | DP1.10067.001 |

