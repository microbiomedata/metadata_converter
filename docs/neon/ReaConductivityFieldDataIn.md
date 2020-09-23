
# Type: rea_conductivityFieldData_in




URI: [neon:ReaConductivityFieldDataIn](https://data.neonscience.org/ReaConductivityFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ReaConductivityFieldDataIn&#124;uid:string%20%3F;collectDate:time%20%3F;stationID:string%20%3F;waterTemp:double%20%3F;startDate:time%20%3F;handheldDeviceID:string%20%3F;fullRangeSpCondLinear:double%20%3F;fullRangeSpCondNonlinear:double%20%3F;lowRangeSpCondLinear:double%20%3F;lowRangeSpCondNonlinear:double%20%3F;recorduid:string%20%3F;dateTimeLogger:time%20%3F;fullRangeHobo:double%20%3F;hoboSampleCode:string%20%3F;hoboSampleID:string%20%3F;loggerDataQF:string%20%3F;lowRangeHobo:double%20%3F;measurementNumber:string%20%3F;hoboSampleFate:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dateTimeLogger](dateTimeLogger.md)  <sub>OPT</sub>
    * Description: Local date and time returned by a field data logger
    * range: [Time](types/Time.md)
 * [fullRangeHobo](fullRangeHobo.md)  <sub>OPT</sub>
    * Description: Conductivity from a hobo logger for the full range
    * range: [Double](types/Double.md)
 * [fullRangeSpCondLinear](fullRangeSpCondLinear.md)  <sub>OPT</sub>
    * Description: Specific conductance calculated using linear method and fullRangeHobo
    * range: [Double](types/Double.md)
 * [fullRangeSpCondNonlinear](fullRangeSpCondNonlinear.md)  <sub>OPT</sub>
    * Description: Specific conductance calculated using non-linear method and fullRangeHobo
    * range: [Double](types/Double.md)
 * [handheldDeviceID](handheldDeviceID.md)  <sub>OPT</sub>
    * Description: Serial number of the handheld stream velocity device
    * range: [String](types/String.md)
 * [hoboSampleCode](hoboSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of the HOBO conductivity logger file
    * range: [String](types/String.md)
 * [hoboSampleFate](hoboSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of the HOBO conductivity logger file
    * range: [String](types/String.md)
 * [hoboSampleID](hoboSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the HOBO conductivity logger file
    * range: [String](types/String.md)
 * [loggerDataQF](loggerDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for conductiivty logger data
    * range: [String](types/String.md)
 * [lowRangeHobo](lowRangeHobo.md)  <sub>OPT</sub>
    * Description: Conductivity returned from a hobo logger for the low range
    * range: [Double](types/Double.md)
 * [lowRangeSpCondLinear](lowRangeSpCondLinear.md)  <sub>OPT</sub>
    * Description: Specific conductance calculated using linear method and lowRangeHobo
    * range: [Double](types/Double.md)
 * [lowRangeSpCondNonlinear](lowRangeSpCondNonlinear.md)  <sub>OPT</sub>
    * Description: Specific conductance calculated using non-linear method and lowRangeHobo
    * range: [Double](types/Double.md)
 * [measurementNumber](measurementNumber.md)  <sub>OPT</sub>
    * Description: The number of the measurement in a time series
    * range: [String](types/String.md)
 * [recorduid](recorduid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the parent and associated child records
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [waterTemp](waterTemp.md)  <sub>OPT</sub>
    * Description: Temperature of water (C)
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:rea_conductivityFieldData_in |

