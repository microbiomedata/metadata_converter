
# Type: dhp_perplot_pub




URI: [neon:DhpPerplotPub](https://data.neonscience.org/DhpPerplotPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DhpPerplotPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;nlcdClass:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;sampleID:string%20%3F;plotType:string%20%3F;plotSize:double%20%3F;utmZone:string%20%3F;slopeAspect:double%20%3F;slopeGradient:double%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;dataQF:string%20%3F;sampleBarcode:string%20%3F;namedLocation:string%20%3F;overstoryHeight:double%20%3F;understoryHeight:double%20%3F;snowPresent:string%20%3F])

## Attributes


### Own

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
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [nlcdClass](nlcdClass.md)  <sub>OPT</sub>
    * Description: National Land Cover Database Vegetation Type Name
    * range: [String](types/String.md)
 * [overstoryHeight](overstoryHeight.md)  <sub>OPT</sub>
    * Description: Average height of the overstory vegetation in a plot, assessed by visual survey to guide LAI photo collection
    * range: [Double](types/Double.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [plotSize](plotSize.md)  <sub>OPT</sub>
    * Description: Size (in square meters) of the plot or grid
    * range: [Double](types/Double.md)
 * [plotType](plotType.md)  <sub>OPT</sub>
    * Description: NEON plot type in which sampling occurred: tower, distributed or gradient
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleBarcode](sampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [slopeAspect](slopeAspect.md)  <sub>OPT</sub>
    * Description: Representative azimuth of slope gradient (0-360 degrees)
    * range: [Double](types/Double.md)
 * [slopeGradient](slopeGradient.md)  <sub>OPT</sub>
    * Description: Representative inclination of slope in degrees
    * range: [Double](types/Double.md)
 * [snowPresent](snowPresent.md)  <sub>OPT</sub>
    * Description: Categorical indicator of whether snow is present within the plot or sampling area
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [understoryHeight](understoryHeight.md)  <sub>OPT</sub>
    * Description: Average height of the understory vegetation in a plot, assessed by visual survey to guide LAI photo collection
    * range: [Double](types/Double.md)
 * [utmZone](utmZone.md)  <sub>OPT</sub>
    * Description: UTM zone
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:dhp_perplot_pub |
| **In Subsets:** | | DP1.10017.001 |

