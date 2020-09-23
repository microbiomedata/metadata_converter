
# Type: dsc_fieldData_in




URI: [neon:DscFieldDataIn](https://data.neonscience.org/DscFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DscFieldDataIn&#124;uid:string%20%3F;siteID:string%20%3F;samplingProtocol:string%20%3F;collectDate:time%20%3F;stationID:string%20%3F;startDate:time%20%3F;samplingProtocolVersion:string%20%3F;collectedBy:string%20%3F;streamStage:double%20%3F;handheldDeviceID:string%20%3F;velocitySensorID:string%20%3F;filterParamTime:double%20%3F;stationEntryTest:string%20%3F;waterEdge:string%20%3F;totalDischarge:double%20%3F;totalDischargeUnits:string%20%3F;dataQF:string%20%3F;averageVelocityUnits:string%20%3F;averageVelocityUnitsQF:integer%20%3F;dischargeUnitsQF:integer%20%3F;flowCalcQF:string%20%3F;flowCalculation:string%20%3F;lowVelocityFinalQF:double%20%3F;recorduid:string%20%3F;streamStageUnits:string%20%3F;streamStageUnitsQF:integer%20%3F;tapeDistanceUnits:string%20%3F;tapeDistanceUnitsQF:integer%20%3F;waterDepthUnits:string%20%3F;waterDepthUnitsQF:integer%20%3F])

## Attributes


### Own

 * [averageVelocityUnits](averageVelocityUnits.md)  <sub>OPT</sub>
    * Description: Average velocity units
    * range: [String](types/String.md)
 * [averageVelocityUnitsQF](averageVelocityUnitsQF.md)  <sub>OPT</sub>
    * Description: Data quality flag indicating that average velocity was reported with units other than meterPerSecond. 1 indicates data is not reported with the proper units and 0 indicates data is reported with the proper units
    * range: [Integer](types/Integer.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [collectedBy](collectedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who collected the sample or specimen
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [dischargeUnitsQF](dischargeUnitsQF.md)  <sub>OPT</sub>
    * Description: Data quality flag indicating that discharge was reported with units other than litersPerSecond (lps). 1 indicates data is not reported with the proper units and 0 indicates data is reported with the proper units
    * range: [Integer](types/Integer.md)
 * [filterParamTime](filterParamTime.md)  <sub>OPT</sub>
    * Description: Length of time over which each velocity measurement was collected; this is for fixed point averaging
    * range: [Double](types/Double.md)
 * [flowCalcQF](flowCalcQF.md)  <sub>OPT</sub>
    * Description: Data quality flag indicating that mid-point calculation was not used. 1 indicates data is not comparable and 0 indicates Mid-point method was used and data is comparable
    * range: [String](types/String.md)
 * [flowCalculation](flowCalculation.md)  <sub>OPT</sub>
    * Description: Flow calculation method used by the meter
    * range: [String](types/String.md)
 * [handheldDeviceID](handheldDeviceID.md)  <sub>OPT</sub>
    * Description: Serial number of the handheld stream velocity device
    * range: [String](types/String.md)
 * [lowVelocityFinalQF](lowVelocityFinalQF.md)  <sub>OPT</sub>
    * Description: Percent of point measurements for a discharge transect with velocity below the instrument detection limit
    * range: [Double](types/Double.md)
 * [recorduid](recorduid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the parent and associated child records
    * range: [String](types/String.md)
 * [samplingProtocol](samplingProtocol.md)  <sub>OPT</sub>
    * Description: The NEON document number where detailed information regarding the sampling method used is available; format NEON.DOC.######
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationEntryTest](stationEntryTest.md)  <sub>OPT</sub>
    * Description: Fixed or non-fixed sample station widths; should be non-fixed
    * range: [String](types/String.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [streamStage](streamStage.md)  <sub>OPT</sub>
    * Description: Reading of water height on staff gauge
    * range: [Double](types/Double.md)
 * [streamStageUnits](streamStageUnits.md)  <sub>OPT</sub>
    * Description: Stage measurement units
    * range: [String](types/String.md)
 * [streamStageUnitsQF](streamStageUnitsQF.md)  <sub>OPT</sub>
    * Description: Data quality flag indicating that stream stage was reported with units other than meter (m). 1 indicates data is not reported with the proper units and 0 indicates data is reported with the proper units
    * range: [Integer](types/Integer.md)
 * [tapeDistanceUnits](tapeDistanceUnits.md)  <sub>OPT</sub>
    * Description: Tape distance units
    * range: [String](types/String.md)
 * [tapeDistanceUnitsQF](tapeDistanceUnitsQF.md)  <sub>OPT</sub>
    * Description: Data quality flag indicating that tape distance was reported with units other than meter (m). 1 indicates data is not reported with the proper units and 0 indicates data is reported with the proper units
    * range: [Integer](types/Integer.md)
 * [totalDischarge](totalDischarge.md)  <sub>OPT</sub>
    * Description: Calculated discharge from the velocity meter device
    * range: [Double](types/Double.md)
 * [totalDischargeUnits](totalDischargeUnits.md)  <sub>OPT</sub>
    * Description: Discharge measurement units; should be in lps - liters per second or m^3/s - cubic meters per second
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [velocitySensorID](velocitySensorID.md)  <sub>OPT</sub>
    * Description: Serial number of the velocity sensor for the handheld stream velocity device
    * range: [String](types/String.md)
 * [waterDepthUnits](waterDepthUnits.md)  <sub>OPT</sub>
    * Description: Water depth units
    * range: [String](types/String.md)
 * [waterDepthUnitsQF](waterDepthUnitsQF.md)  <sub>OPT</sub>
    * Description: Data quality flag indicating that water depth was reported with units other than meter (m). 1 indicates data is not reported with the proper units and 0 indicates data is reported with the proper units
    * range: [Integer](types/Integer.md)
 * [waterEdge](waterEdge.md)  <sub>OPT</sub>
    * Description: Defines which edge of the stream where transect starts; follows standard right - left convention for streams
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:dsc_fieldData_in |
| **In Subsets:** | | DP0.20048.001 |

