
# Type: scs_shipmentVerification_in




URI: [neon:ScsShipmentVerificationIn](https://data.neonscience.org/ScsShipmentVerificationIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ScsShipmentVerificationIn&#124;uid:string%20%3F;remarks:string%20%3F;sampleID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;coolerTemp:double%20%3F;shipmentReceivedDate:time%20%3F;receivedBy:string%20%3F;shipmentID:string%20%3F;shipmentCondition:string%20%3F;deprecatedVialID:string%20%3F;locationID:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;sampleClass:string%20%3F;sampleCondition:string%20%3F;acceptedForAnalysis:string%20%3F;sampleReceived:string%20%3F])

## Attributes


### Own

 * [acceptedForAnalysis](acceptedForAnalysis.md)  <sub>OPT</sub>
    * Description: An indication of whether the shipped sample is accepted for planned analysis
    * range: [String](types/String.md)
 * [coolerTemp](coolerTemp.md)  <sub>OPT</sub>
    * Description: Temperature of the cooler when the sample arrived at the external lab
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [deprecatedVialID](deprecatedVialID.md)  <sub>OPT</sub>
    * Description: Identifier on vial label, if different from standard ID
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [receivedBy](receivedBy.md)  <sub>OPT</sub>
    * Description: Anonymized name of lab personnel receiving the shipment
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleClass](sampleClass.md)  <sub>OPT</sub>
    * Description: Class of a sample
    * range: [String](types/String.md)
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
 * [sampleReceived](sampleReceived.md)  <sub>OPT</sub>
    * Description: An indication of whether the shipped sample was received
    * range: [String](types/String.md)
 * [shipmentCondition](shipmentCondition.md)  <sub>OPT</sub>
    * Description: The condition in which the shipment was received
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
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:scs_shipmentVerification_in |

