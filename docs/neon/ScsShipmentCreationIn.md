
# Type: scs_shipmentCreation_in




URI: [neon:ScsShipmentCreationIn](https://data.neonscience.org/ScsShipmentCreationIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ScsShipmentCreationIn&#124;uid:string%20%3F;remarks:string%20%3F;taxonID:string%20%3F;sampleID:string%20%3F;sampleType:string%20%3F;individualCount:string%20%3F;sampleVolume:double%20%3F;startDate:time%20%3F;endDate:time%20%3F;shipDate:time%20%3F;shipmentID:string%20%3F;numVialsSampleID:string%20%3F;senderID:string%20%3F;locationID:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;sampleClass:string%20%3F;preservativeType:string%20%3F;preservativeVolume:double%20%3F;namedLocation:string%20%3F;sampleMass:double%20%3F;wellCoordinates:string%20%3F;analysisType:string%20%3F;containerID:string%20%3F;containerMass:double%20%3F;destinationFacility:string%20%3F;filterVolume:double%20%3F;holdingTime:time%20%3F;quarantineStatus:string%20%3F;sentTo:string%20%3F;shipmentMethod:string%20%3F;shipmentService:string%20%3F;shippedFrom:string%20%3F;trackingNumber:string%20%3F])

## Attributes


### Own

 * [analysisType](analysisType.md)  <sub>OPT</sub>
    * Description: Type of analysis at external lab
    * range: [String](types/String.md)
 * [containerID](containerID.md)  <sub>OPT</sub>
    * Description: The identifier for the container in which the sample is located
    * range: [String](types/String.md)
 * [containerMass](containerMass.md)  <sub>OPT</sub>
    * Description: Mass of the container in grams
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [destinationFacility](destinationFacility.md)  <sub>OPT</sub>
    * Description: Name of institution to which shipment was sent
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [filterVolume](filterVolume.md)  <sub>OPT</sub>
    * Description: Volume of material passed through filter
    * range: [Double](types/Double.md)
 * [holdingTime](holdingTime.md)  <sub>OPT</sub>
    * Description: The holding time associated with the samples
    * range: [Time](types/Time.md)
 * [individualCount](individualCount.md)  <sub>OPT</sub>
    * Description: Number of individuals of the same type
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [numVialsSampleID](numVialsSampleID.md)  <sub>OPT</sub>
    * Description: Number of vials associated with a sampleID
    * range: [String](types/String.md)
 * [preservativeType](preservativeType.md)  <sub>OPT</sub>
    * Description: Type of preservative used in the sample
    * range: [String](types/String.md)
 * [preservativeVolume](preservativeVolume.md)  <sub>OPT</sub>
    * Description: Volume of preservative used in the sample
    * range: [Double](types/Double.md)
 * [quarantineStatus](quarantineStatus.md)  <sub>OPT</sub>
    * Description: An indicator of whether the samples being shipped have associated quarantine restrictions
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
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [sampleMass](sampleMass.md)  <sub>OPT</sub>
    * Description: Mass of sample
    * range: [Double](types/Double.md)
 * [sampleType](sampleType.md)  <sub>OPT</sub>
    * Description: Type of sample
    * range: [String](types/String.md)
 * [sampleVolume](sampleVolume.md)  <sub>OPT</sub>
    * Description: Sample volume in milliliters
    * range: [Double](types/Double.md)
 * [senderID](senderID.md)  <sub>OPT</sub>
    * Description: Identifier for the facility or technician sending the sample or specimen
    * range: [String](types/String.md)
 * [sentTo](sentTo.md)  <sub>OPT</sub>
    * Description: Name of person or institution to which shipment was sent following identifications or analyses
    * range: [String](types/String.md)
 * [shipDate](shipDate.md)  <sub>OPT</sub>
    * Description: Date shipment sent by domain lab
    * range: [Time](types/Time.md)
 * [shipmentID](shipmentID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with shipment
    * range: [String](types/String.md)
 * [shipmentMethod](shipmentMethod.md)  <sub>OPT</sub>
    * Description: The method of shipment
    * range: [String](types/String.md)
 * [shipmentService](shipmentService.md)  <sub>OPT</sub>
    * Description: The name of the company performing shipment fulfillment
    * range: [String](types/String.md)
 * [shippedFrom](shippedFrom.md)  <sub>OPT</sub>
    * Description: Named location from which the sample was shipped
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [trackingNumber](trackingNumber.md)  <sub>OPT</sub>
    * Description: The tracking number assigned by the shipment fulfillment organization
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [wellCoordinates](wellCoordinates.md)  <sub>OPT</sub>
    * Description: Location of sample in multi-well storage box or plate
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:scs_shipmentCreation_in |
| **In Subsets:** | | DP0.10000.001 |

