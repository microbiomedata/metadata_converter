
# Type: sls_soilCoreCollection_pub




URI: [neon:SlsSoilCoreCollectionPub](https://data.neonscience.org/SlsSoilCoreCollectionPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SlsSoilCoreCollectionPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;nlcdClass:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;plotType:string%20%3F;easting:double%20%3F;northing:double%20%3F;utmZone:string%20%3F;samplingProtocolVersion:string%20%3F;collectedBy:string%20%3F;sampleTiming:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;geneticSampleID:string%20%3F;biomassCode:string%20%3F;biomassID:string%20%3F;coreCoordinateX:double%20%3F;coreCoordinateY:double%20%3F;geneticArchiveSample1Code:string%20%3F;geneticArchiveSample1ID:string%20%3F;geneticArchiveSample2Code:string%20%3F;geneticArchiveSample2ID:string%20%3F;geneticArchiveSample3Code:string%20%3F;geneticArchiveSample3ID:string%20%3F;geneticArchiveSample4Code:string%20%3F;geneticArchiveSample4ID:string%20%3F;geneticArchiveSample5Code:string%20%3F;geneticArchiveSample5ID:string%20%3F;geneticSampleCode:string%20%3F;geneticSampleCondition:string%20%3F;horizon:string%20%3F;litterDepth:double%20%3F;nTransBoutType:string%20%3F;sampleBottomDepth:double%20%3F;sampleTopDepth:double%20%3F;soilCoreCount:string%20%3F;soilSamplingDevice:string%20%3F;soilTemp:double%20%3F;incubationMethod:string%20%3F;namedLocation:string%20%3F;sampleExtent:string%20%3F;standingWaterDepth:double%20%3F;incubationCondition:string%20%3F])

## Attributes


### Own

 * [biomassCode](biomassCode.md)  <sub>OPT</sub>
    * Description: Barcode of biomass sample
    * range: [String](types/String.md)
 * [biomassID](biomassID.md)  <sub>OPT</sub>
    * Description: Identifier for biomass sample
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
 * [coreCoordinateX](coreCoordinateX.md)  <sub>OPT</sub>
    * Description: x location of the soil core relative to the SW corner
    * range: [Double](types/Double.md)
 * [coreCoordinateY](coreCoordinateY.md)  <sub>OPT</sub>
    * Description: y location of the soil core relative to the SW corner
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
 * [easting](easting.md)  <sub>OPT</sub>
    * Description: Geographic coordinate specifying the east-west position of a point on the Earth's surface (Universal Transverse Mercator, UTM)
    * range: [Double](types/Double.md)
 * [elevation](elevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level
    * range: [Double](types/Double.md)
 * [elevationUncertainty](elevationUncertainty.md)  <sub>OPT</sub>
    * Description: Uncertainty in elevation values (in meters)
    * range: [Double](types/Double.md)
 * [geneticArchiveSample1Code](geneticArchiveSample1Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 1
    * range: [String](types/String.md)
 * [geneticArchiveSample1ID](geneticArchiveSample1ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 1
    * range: [String](types/String.md)
 * [geneticArchiveSample2Code](geneticArchiveSample2Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 2
    * range: [String](types/String.md)
 * [geneticArchiveSample2ID](geneticArchiveSample2ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 2
    * range: [String](types/String.md)
 * [geneticArchiveSample3Code](geneticArchiveSample3Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 3
    * range: [String](types/String.md)
 * [geneticArchiveSample3ID](geneticArchiveSample3ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 3
    * range: [String](types/String.md)
 * [geneticArchiveSample4Code](geneticArchiveSample4Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 4
    * range: [String](types/String.md)
 * [geneticArchiveSample4ID](geneticArchiveSample4ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 4
    * range: [String](types/String.md)
 * [geneticArchiveSample5Code](geneticArchiveSample5Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 5
    * range: [String](types/String.md)
 * [geneticArchiveSample5ID](geneticArchiveSample5ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 5
    * range: [String](types/String.md)
 * [geneticSampleCode](geneticSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a genetic sample
    * range: [String](types/String.md)
 * [geneticSampleCondition](geneticSampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of genetic sample storage or processing
    * range: [String](types/String.md)
 * [geneticSampleID](geneticSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for the genetic sample
    * range: [String](types/String.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [horizon](horizon.md)  <sub>OPT</sub>
    * Description: Organic or mineral soil
    * range: [String](types/String.md)
 * [incubationCondition](incubationCondition.md)  <sub>OPT</sub>
    * Description: Condition of incubated nitrogen transformation sample upon retrieval
    * range: [String](types/String.md)
 * [incubationMethod](incubationMethod.md)  <sub>OPT</sub>
    * Description: Method used for soil incubation
    * range: [String](types/String.md)
 * [litterDepth](litterDepth.md)  <sub>OPT</sub>
    * Description: Depth of litter layer
    * range: [Double](types/Double.md)
 * [nTransBoutType](nTransBoutType.md)  <sub>OPT</sub>
    * Description: Category of bout in relation to nitrogen transformation sample collection
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [nlcdClass](nlcdClass.md)  <sub>OPT</sub>
    * Description: National Land Cover Database Vegetation Type Name
    * range: [String](types/String.md)
 * [northing](northing.md)  <sub>OPT</sub>
    * Description: Geographic coordinate specifying the north-south position of a point on the Earth's surface (Universal Transverse Mercator, UTM)
    * range: [Double](types/Double.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [plotType](plotType.md)  <sub>OPT</sub>
    * Description: NEON plot type in which sampling occurred: tower, distributed or gradient
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleBottomDepth](sampleBottomDepth.md)  <sub>OPT</sub>
    * Description: Depth below the soil surface of the bottom of a soil sample
    * range: [Double](types/Double.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleExtent](sampleExtent.md)  <sub>OPT</sub>
    * Description: Extent of the soil sample relative to the local soil horizon conditions
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [sampleTiming](sampleTiming.md)  <sub>OPT</sub>
    * Description: Timing of the sampling event with regard to the field season
    * range: [String](types/String.md)
 * [sampleTopDepth](sampleTopDepth.md)  <sub>OPT</sub>
    * Description: Depth below the soil surface of the top of a soil sample
    * range: [Double](types/Double.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [soilCoreCount](soilCoreCount.md)  <sub>OPT</sub>
    * Description: Number of soil cores combined per sample
    * range: [String](types/String.md)
 * [soilSamplingDevice](soilSamplingDevice.md)  <sub>OPT</sub>
    * Description: Type of soil collection device used for sampling
    * range: [String](types/String.md)
 * [soilTemp](soilTemp.md)  <sub>OPT</sub>
    * Description: In-situ temperature of soil at approximately 10 cm depth
    * range: [Double](types/Double.md)
 * [standingWaterDepth](standingWaterDepth.md)  <sub>OPT</sub>
    * Description: Depth of standing water present at a sampling location
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [utmZone](utmZone.md)  <sub>OPT</sub>
    * Description: UTM zone
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sls_soilCoreCollection_pub |
| **In Subsets:** | | DP1.10086.001 |

