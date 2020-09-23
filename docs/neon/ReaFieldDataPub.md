
# Type: rea_fieldData_pub




URI: [neon:ReaFieldDataPub](https://data.neonscience.org/ReaFieldDataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ReaFieldDataPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;recordedBy:string%20%3F;decimalLatitude:double%20%3F;decimalLongitude:double%20%3F;geodeticDatum:string%20%3F;coordinateUncertainty:double%20%3F;elevation:double%20%3F;elevationUncertainty:double%20%3F;collectDate:time%20%3F;startDate:time%20%3F;samplingProtocolVersion:string%20%3F;collectedBy:string%20%3F;fieldDataQF:string%20%3F;namedLocation:string%20%3F;betweenLoggersDist:double%20%3F;carboyVolume:double%20%3F;constantRateTracerMass:double%20%3F;dripEndTime:time%20%3F;dripRateStart:double%20%3F;dripRateEnd:double%20%3F;dripStartTime:time%20%3F;gasTracerType:string%20%3F;injectateSampleCode:string%20%3F;injectateSampleCollected:string%20%3F;injectateSampleID:string%20%3F;injectionType:string%20%3F;loggersAtSensorSets:string%20%3F;slugPourTime:time%20%3F;slugTracerMass:double%20%3F;tracerAnalysisType:string%20%3F;incompleteExperimentQF:string%20%3F;iceCover:string%20%3F;streambedLeafCover:string%20%3F])

## Attributes


### Own

 * [betweenLoggersDist](betweenLoggersDist.md)  <sub>OPT</sub>
    * Description: Distance between conductivity loggers that are not positioned at the sensor sets
    * range: [Double](types/Double.md)
 * [carboyVolume](carboyVolume.md)  <sub>OPT</sub>
    * Description: Volume of salt tracer storage tank in liters
    * range: [Double](types/Double.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [collectedBy](collectedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who collected the sample or specimen
    * range: [String](types/String.md)
 * [constantRateTracerMass](constantRateTracerMass.md)  <sub>OPT</sub>
    * Description: Mass of constant rate tracer added to carboy
    * range: [Double](types/Double.md)
 * [coordinateUncertainty](coordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [decimalLatitude](decimalLatitude.md)  <sub>OPT</sub>
    * Description: The geographic latitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [decimalLongitude](decimalLongitude.md)  <sub>OPT</sub>
    * Description: The geographic longitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [dripEndTime](dripEndTime.md)  <sub>OPT</sub>
    * Description: End date and time of the salt tracer injection
    * range: [Time](types/Time.md)
 * [dripRateEnd](dripRateEnd.md)  <sub>OPT</sub>
    * Description: Rate of salt pumped into stream at end of salt tracer injection
    * range: [Double](types/Double.md)
 * [dripRateStart](dripRateStart.md)  <sub>OPT</sub>
    * Description: Rate of salt pumped into stream at start of salt tracer injection
    * range: [Double](types/Double.md)
 * [dripStartTime](dripStartTime.md)  <sub>OPT</sub>
    * Description: Start date and time of the salt tracer injection
    * range: [Time](types/Time.md)
 * [elevation](elevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level
    * range: [Double](types/Double.md)
 * [elevationUncertainty](elevationUncertainty.md)  <sub>OPT</sub>
    * Description: Uncertainty in elevation values (in meters)
    * range: [Double](types/Double.md)
 * [fieldDataQF](fieldDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for field data
    * range: [String](types/String.md)
 * [gasTracerType](gasTracerType.md)  <sub>OPT</sub>
    * Description: Type of gas used as a tracer
    * range: [String](types/String.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [iceCover](iceCover.md)  <sub>OPT</sub>
    * Description: The percent of ice cover in the stream
    * range: [String](types/String.md)
 * [incompleteExperimentQF](incompleteExperimentQF.md)  <sub>OPT</sub>
    * Description: Data quality flag indicating a reaeration experiment that is incomplete This flag is populated on a semi-annual basis following science review
    * range: [String](types/String.md)
 * [injectateSampleCode](injectateSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for the reaeration salt tracer sample
    * range: [String](types/String.md)
 * [injectateSampleCollected](injectateSampleCollected.md)  <sub>OPT</sub>
    * Description: Indicator of whether an injectate sample was collected
    * range: [String](types/String.md)
 * [injectateSampleID](injectateSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the reaeration salt tracer sample
    * range: [String](types/String.md)
 * [injectionType](injectionType.md)  <sub>OPT</sub>
    * Description: Type of tracer injection, e.g. slug or constant rate
    * range: [String](types/String.md)
 * [loggersAtSensorSets](loggersAtSensorSets.md)  <sub>OPT</sub>
    * Description: Indication of whether or not the conductivity loggers are positioned at sensor sets 1 and 2
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [slugPourTime](slugPourTime.md)  <sub>OPT</sub>
    * Description: Start date and time of the salt slug
    * range: [Time](types/Time.md)
 * [slugTracerMass](slugTracerMass.md)  <sub>OPT</sub>
    * Description: Mass of slug tracer used
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [streambedLeafCover](streambedLeafCover.md)  <sub>OPT</sub>
    * Description: The amount of fallen leaves covering the streambed
    * range: [String](types/String.md)
 * [tracerAnalysisType](tracerAnalysisType.md)  <sub>OPT</sub>
    * Description: Type of analysis used to determine tracer concentration
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:rea_fieldData_pub |

