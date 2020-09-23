
# Type: spc_perplot_pub




URI: [neon:SpcPerplotPub](https://data.neonscience.org/SpcPerplotPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SpcPerplotPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;nlcdClass:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;setDate:time%20%3F;collectDate:time%20%3F;plotType:string%20%3F;pitID:string%20%3F;pitDepth:double%20%3F;recordedByA:string%20%3F;soilProfileDescriberA:string%20%3F;soilProfileDescriberInst:string%20%3F;nrcsDescriptionID:string%20%3F;soilSeries:string%20%3F;soilFamily:string%20%3F;soilSubgroup:string%20%3F;soilGreatGroup:string%20%3F;soilSuborder:string%20%3F;soilOrder:string%20%3F;testProtocolVersion:string%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;pitCode:string%20%3F;referenceCorner:string%20%3F;sampleBearing:double%20%3F;sampleDistance:double%20%3F;sampleRelativeLocation:string%20%3F;soilSamplingMethod:string%20%3F])

## Attributes


### Own

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
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [nlcdClass](nlcdClass.md)  <sub>OPT</sub>
    * Description: National Land Cover Database Vegetation Type Name
    * range: [String](types/String.md)
 * [nrcsDescriptionID](nrcsDescriptionID.md)  <sub>OPT</sub>
    * Description: NRCS identifier assigned to the soil profile description
    * range: [String](types/String.md)
 * [pitCode](pitCode.md)  <sub>OPT</sub>
    * Description: Barcode of the pit
    * range: [String](types/String.md)
 * [pitDepth](pitDepth.md)  <sub>OPT</sub>
    * Description: Depth of the bottom of the soil pit below the soil surface
    * range: [Double](types/Double.md)
 * [pitID](pitID.md)  <sub>OPT</sub>
    * Description: An identifier for the soil pit
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [plotType](plotType.md)  <sub>OPT</sub>
    * Description: NEON plot type in which sampling occurred: tower, distributed or gradient
    * range: [String](types/String.md)
 * [recordedByA](recordedByA.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who recorded the data
    * range: [String](types/String.md)
 * [referenceCorner](referenceCorner.md)  <sub>OPT</sub>
    * Description: Reference corner from which distance and compass bearing were measured
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleBearing](sampleBearing.md)  <sub>OPT</sub>
    * Description: Compass bearing of the sample location from a plot reference corner
    * range: [Double](types/Double.md)
 * [sampleDistance](sampleDistance.md)  <sub>OPT</sub>
    * Description: Distance of the sample location from a plot reference corner
    * range: [Double](types/Double.md)
 * [sampleRelativeLocation](sampleRelativeLocation.md)  <sub>OPT</sub>
    * Description: Relative position of a sample location
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [soilFamily](soilFamily.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the family level
    * range: [String](types/String.md)
 * [soilGreatGroup](soilGreatGroup.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the great group level
    * range: [String](types/String.md)
 * [soilOrder](soilOrder.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the order level
    * range: [String](types/String.md)
 * [soilProfileDescriberA](soilProfileDescriberA.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who described the soil profile
    * range: [String](types/String.md)
 * [soilProfileDescriberInst](soilProfileDescriberInst.md)  <sub>OPT</sub>
    * Description: Institution of the person/people that performed the soil profile description
    * range: [String](types/String.md)
 * [soilSamplingMethod](soilSamplingMethod.md)  <sub>OPT</sub>
    * Description: The methodology used for collecting soil at a plot (pit or core)
    * range: [String](types/String.md)
 * [soilSeries](soilSeries.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the series level
    * range: [String](types/String.md)
 * [soilSubgroup](soilSubgroup.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the subgroup level
    * range: [String](types/String.md)
 * [soilSuborder](soilSuborder.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the suborder level
    * range: [String](types/String.md)
 * [testProtocolVersion](testProtocolVersion.md)  <sub>OPT</sub>
    * Description: The protocol version used to test the sample
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:spc_perplot_pub |
| **In Subsets:** | | DP1.10047.001 |

