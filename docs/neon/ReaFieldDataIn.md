
# Type: rea_fieldData_in




URI: [neon:ReaFieldDataIn](https://data.neonscience.org/ReaFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ReaFieldDataIn&#124;uid:string%20%3F;siteID:string%20%3F;recordedBy:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;samplingProtocolVersion:string%20%3F;collectedBy:string%20%3F;fieldDataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;betweenLoggersDist:double%20%3F;carboyVolume:double%20%3F;constantRateTracerMass:double%20%3F;dripEndTime:time%20%3F;dripRateStart:double%20%3F;dripRateEnd:double%20%3F;dripStartTime:time%20%3F;gasTracerType:string%20%3F;injectateSampleCode:string%20%3F;injectateSampleCollected:string%20%3F;injectateSampleID:string%20%3F;injectionType:string%20%3F;loggersAtSensorSets:string%20%3F;slugPourTime:time%20%3F;slugTracerMass:double%20%3F;tracerAnalysisType:string%20%3F;injectateSampleFate:string%20%3F;injectateSampleCond:string%20%3F;incompleteExperimentQF:string%20%3F;injectateSampleClass:string%20%3F;iceCover:string%20%3F;streambedLeafCover:string%20%3F])

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
 * [fieldDataQF](fieldDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for field data
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [gasTracerType](gasTracerType.md)  <sub>OPT</sub>
    * Description: Type of gas used as a tracer
    * range: [String](types/String.md)
 * [iceCover](iceCover.md)  <sub>OPT</sub>
    * Description: The percent of ice cover in the stream
    * range: [String](types/String.md)
 * [incompleteExperimentQF](incompleteExperimentQF.md)  <sub>OPT</sub>
    * Description: Data quality flag indicating a reaeration experiment that is incomplete This flag is populated on a semi-annual basis following science review
    * range: [String](types/String.md)
 * [injectateSampleClass](injectateSampleClass.md)  <sub>OPT</sub>
    * Description: Sample class of the reaeration salt tracer sample
    * range: [String](types/String.md)
 * [injectateSampleCode](injectateSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for the reaeration salt tracer sample
    * range: [String](types/String.md)
 * [injectateSampleCollected](injectateSampleCollected.md)  <sub>OPT</sub>
    * Description: Indicator of whether an injectate sample was collected
    * range: [String](types/String.md)
 * [injectateSampleCond](injectateSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of the reaeration salt tracer sample
    * range: [String](types/String.md)
 * [injectateSampleFate](injectateSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of the reaeration salt tracer sample
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
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
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
| **Mappings:** | | neon:rea_fieldData_in |

