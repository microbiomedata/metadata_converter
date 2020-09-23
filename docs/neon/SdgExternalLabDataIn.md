
# Type: sdg_externalLabData_in




URI: [neon:SdgExternalLabDataIn](https://data.neonscience.org/SdgExternalLabDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SdgExternalLabDataIn&#124;uid:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;stationID:string%20%3F;startDate:time%20%3F;laboratoryName:string%20%3F;internalLabID:string%20%3F;shipmentReceivedDate:time%20%3F;receivedBy:string%20%3F;shipmentID:string%20%3F;externalRemarks:string%20%3F;analysisDate:time%20%3F;internalSampleName:string%20%3F;internalLabFileName:string%20%3F;concentrationCH4:double%20%3F;concentrationCO2:double%20%3F;concentrationN2O:double%20%3F;volumeGasAnalyzed:double%20%3F;runDetectionLimitCH4:double%20%3F;runDetectionLimitCO2:double%20%3F;runDetectionLimitN2O:double%20%3F;precisionCH4:double%20%3F;precisionCO2:double%20%3F;precisionN2O:double%20%3F;gasStandardAccuracy:double%20%3F;analyzedBy:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;sampleCondition:string%20%3F;sdgExternalLabDataQF:string%20%3F;gasCheckStandardPercentDev:double%20%3F;gasCheckStandardQF:integer%20%3F])

## Attributes


### Own

 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [concentrationCH4](concentrationCH4.md)  <sub>OPT</sub>
    * Description: Concentration of CH4 in sample
    * range: [Double](types/Double.md)
 * [concentrationCO2](concentrationCO2.md)  <sub>OPT</sub>
    * Description: Concentration of CO2 in sample
    * range: [Double](types/Double.md)
 * [concentrationN2O](concentrationN2O.md)  <sub>OPT</sub>
    * Description: Concentration of N2O in sample
    * range: [Double](types/Double.md)
 * [externalRemarks](externalRemarks.md)  <sub>OPT</sub>
    * Description: External lab notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [gasCheckStandardPercentDev](gasCheckStandardPercentDev.md)  <sub>OPT</sub>
    * Description: Calculated percent deviation of the run for the gas check standards
    * range: [Double](types/Double.md)
 * [gasCheckStandardQF](gasCheckStandardQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating when the gas check standard percent deviation is above 2 %; 0 indicates percent deviation less than 2 %; 1 indicates percent deviation 2 % or above; and -1 indicates that the test could not be performed
    * range: [Integer](types/Integer.md)
 * [gasStandardAccuracy](gasStandardAccuracy.md)  <sub>OPT</sub>
    * Description: Accuracy of standards used for gas calibration
    * range: [Double](types/Double.md)
 * [internalLabFileName](internalLabFileName.md)  <sub>OPT</sub>
    * Description: Internal lab specific file name for raw data
    * range: [String](types/String.md)
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
 * [internalSampleName](internalSampleName.md)  <sub>OPT</sub>
    * Description: Internal lab specific identifier
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [precisionCH4](precisionCH4.md)  <sub>OPT</sub>
    * Description: Precision (CV%) - CH4ppm
    * range: [Double](types/Double.md)
 * [precisionCO2](precisionCO2.md)  <sub>OPT</sub>
    * Description: Precision (CV%) - CO2ppm
    * range: [Double](types/Double.md)
 * [precisionN2O](precisionN2O.md)  <sub>OPT</sub>
    * Description: Precision (CV%) - N2Oppm
    * range: [Double](types/Double.md)
 * [receivedBy](receivedBy.md)  <sub>OPT</sub>
    * Description: Anonymized name of lab personnel receiving the shipment
    * range: [String](types/String.md)
 * [runDetectionLimitCH4](runDetectionLimitCH4.md)  <sub>OPT</sub>
    * Description: Run detection limit - CH4ppm
    * range: [Double](types/Double.md)
 * [runDetectionLimitCO2](runDetectionLimitCO2.md)  <sub>OPT</sub>
    * Description: Run detection limit - CO2ppm
    * range: [Double](types/Double.md)
 * [runDetectionLimitN2O](runDetectionLimitN2O.md)  <sub>OPT</sub>
    * Description: Run detection limit - N2Oppm
    * range: [Double](types/Double.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [sdgExternalLabDataQF](sdgExternalLabDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for dissolved gas external laboratory data
    * range: [String](types/String.md)
 * [shipmentID](shipmentID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with shipment
    * range: [String](types/String.md)
 * [shipmentReceivedDate](shipmentReceivedDate.md)  <sub>OPT</sub>
    * Description: Date a sample was received
    * range: [Time](types/Time.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [volumeGasAnalyzed](volumeGasAnalyzed.md)  <sub>OPT</sub>
    * Description: Amount of gas sample analyzed
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sdg_externalLabData_in |

