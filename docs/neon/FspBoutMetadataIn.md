
# Type: fsp_boutMetadata_in




URI: [neon:FspBoutMetadataIn](https://data.neonscience.org/FspBoutMetadataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[FspBoutMetadataIn&#124;uid:string%20%3F;remarks:string%20%3F;eventID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;instrument:string%20%3F;locationID:string%20%3F;dataQF:string%20%3F;wavelengthIncrement:double%20%3F;fieldSpectrometerSettings:string%20%3F;foreopticConnection:string%20%3F;foreopticType:string%20%3F;lightSource:string%20%3F;measurementQuantity:string%20%3F;measurementUnits:string%20%3F])

## Attributes


### Own

 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fieldSpectrometerSettings](fieldSpectrometerSettings.md)  <sub>OPT</sub>
    * Description: Settings used in the field spectrometer software
    * range: [String](types/String.md)
 * [foreopticConnection](foreopticConnection.md)  <sub>OPT</sub>
    * Description: Foreoptic connection used to make measurements
    * range: [String](types/String.md)
 * [foreopticType](foreopticType.md)  <sub>OPT</sub>
    * Description: Type of foreoptic used to make measurements
    * range: [String](types/String.md)
 * [instrument](instrument.md)  <sub>OPT</sub>
    * Description: Type of instrument used for the analysis
    * range: [String](types/String.md)
 * [lightSource](lightSource.md)  <sub>OPT</sub>
    * Description: Description of the light source used for measurements
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [measurementQuantity](measurementQuantity.md)  <sub>OPT</sub>
    * Description: Type of measurement
    * range: [String](types/String.md)
 * [measurementUnits](measurementUnits.md)  <sub>OPT</sub>
    * Description: Units of measurement
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [wavelengthIncrement](wavelengthIncrement.md)  <sub>OPT</sub>
    * Description: Increment size of wavelength
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:fsp_boutMetadata_in |
| **In Subsets:** | | DP0.30012.001 |

