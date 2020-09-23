
# Type: rea_externalLabDataGas_pub




URI: [neon:ReaExternalLabDataGasPub](https://data.neonscience.org/ReaExternalLabDataGasPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ReaExternalLabDataGasPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;laboratoryName:string%20%3F;receivedBy:string%20%3F;shipmentID:string%20%3F;receivedDate:time%20%3F;analysisDate:time%20%3F;analyzedBy:string%20%3F;sampleCode:string%20%3F;sampleCondition:string%20%3F;namedLocation:string%20%3F;certifiedStandardAccuracy:double%20%3F;externalLabGasDataQF:string%20%3F;gasSampleID:string%20%3F;gasTracerConcentration:double%20%3F;gasTracerType:string%20%3F;gasVolumeAnalyzed:double%20%3F;labStandardPrecision:double%20%3F;runDetectionLimit:double%20%3F;gasCheckStandardPercentDev:double%20%3F;gasCheckStandardQF:integer%20%3F])

## Attributes


### Own

 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
 * [certifiedStandardAccuracy](certifiedStandardAccuracy.md)  <sub>OPT</sub>
    * Description: Analytical accuracy of certified standard
    * range: [Double](types/Double.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [externalLabGasDataQF](externalLabGasDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for external lab gas data
    * range: [String](types/String.md)
 * [gasCheckStandardPercentDev](gasCheckStandardPercentDev.md)  <sub>OPT</sub>
    * Description: Calculated percent deviation of the run for the gas check standards
    * range: [Double](types/Double.md)
 * [gasCheckStandardQF](gasCheckStandardQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating when the gas check standard percent deviation is above 2 %; 0 indicates percent deviation less than 2 %; 1 indicates percent deviation 2 % or above; and -1 indicates that the test could not be performed
    * range: [Integer](types/Integer.md)
 * [gasSampleID](gasSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the gas sample
    * range: [String](types/String.md)
 * [gasTracerConcentration](gasTracerConcentration.md)  <sub>OPT</sub>
    * Description: Tracer concentration in sample
    * range: [Double](types/Double.md)
 * [gasTracerType](gasTracerType.md)  <sub>OPT</sub>
    * Description: Type of gas used as a tracer
    * range: [String](types/String.md)
 * [gasVolumeAnalyzed](gasVolumeAnalyzed.md)  <sub>OPT</sub>
    * Description: Volume of sample analyzed, in milliliters
    * range: [Double](types/Double.md)
 * [labStandardPrecision](labStandardPrecision.md)  <sub>OPT</sub>
    * Description: Precision of the laboratory standard used in the development of the standard curve, measured as coefficient of variance
    * range: [Double](types/Double.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [receivedBy](receivedBy.md)  <sub>OPT</sub>
    * Description: Anonymized name of lab personnel receiving the shipment
    * range: [String](types/String.md)
 * [receivedDate](receivedDate.md)  <sub>OPT</sub>
    * Description: Date a sample was received
    * range: [Time](types/Time.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [runDetectionLimit](runDetectionLimit.md)  <sub>OPT</sub>
    * Description: Detection limit of the sample run
    * range: [Double](types/Double.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [shipmentID](shipmentID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with shipment
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:rea_externalLabDataGas_pub |

