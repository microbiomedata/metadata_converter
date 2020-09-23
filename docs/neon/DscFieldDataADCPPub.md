
# Type: dsc_fieldDataADCP_pub




URI: [neon:DscFieldDataADCPPub](https://data.neonscience.org/DscFieldDataADCPPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DscFieldDataADCPPub&#124;uid:string%20%3F;domainID:string%20%3F;samplingProtocol:string%20%3F;stationID:string%20%3F;aCollectedBy:string%20%3F;bCollectedBy:string%20%3F;maxDepth:double%20%3F;startDate:time%20%3F;endDate:time%20%3F;streamStage:double%20%3F;totalDischarge:double%20%3F;totalDischargeUnits:string%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;streamStageUnits:string%20%3F;rawDataFileName:string%20%3F;adcpCompassCalibrated:string%20%3F;adcpCompassError:double%20%3F;loopMBT:string%20%3F;magneticVariation:double%20%3F;riverDepthMean:double%20%3F;riverDischargeMeasDuration:double%20%3F;riverVelocityMaximum:double%20%3F;riverWidthMean:double%20%3F;stationaryMBT:string%20%3F;totalDischargeRU:double%20%3F;velocityUnits:string%20%3F;waterTemperature:double%20%3F;widthUnits:string%20%3F;windDirRelativeToFlow:string%20%3F;windSpeedPrior:double%20%3F])

## Attributes


### Own

 * [aCollectedBy](aCollectedBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [adcpCompassCalibrated](adcpCompassCalibrated.md)  <sub>OPT</sub>
    * Description: Whether or not the Acoustic Doppler Current Profiler compass was calibrated prior to the discharge measurement
    * range: [String](types/String.md)
 * [adcpCompassError](adcpCompassError.md)  <sub>OPT</sub>
    * Description: The Acoustic Doppler Current Profiler compass error calculated prior to discharge measurement
    * range: [Double](types/Double.md)
 * [bCollectedBy](bCollectedBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [loopMBT](loopMBT.md)  <sub>OPT</sub>
    * Description: Whether or not a loop moving bed test was performed prior to the discharge measurement
    * range: [String](types/String.md)
 * [magneticVariation](magneticVariation.md)  <sub>OPT</sub>
    * Description: The angle between magnetic north and true north depending on geographic location
    * range: [Double](types/Double.md)
 * [maxDepth](maxDepth.md)  <sub>OPT</sub>
    * Description: Maximum depth
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [rawDataFileName](rawDataFileName.md)  <sub>OPT</sub>
    * Description: Name of file or folder containing raw data, including file extension
    * range: [String](types/String.md)
 * [riverDepthMean](riverDepthMean.md)  <sub>OPT</sub>
    * Description: The mean river depth measured in all transects included in the discharge measurement
    * range: [Double](types/Double.md)
 * [riverDischargeMeasDuration](riverDischargeMeasDuration.md)  <sub>OPT</sub>
    * Description: The total duration of all transects included in the discharge measurement
    * range: [Double](types/Double.md)
 * [riverVelocityMaximum](riverVelocityMaximum.md)  <sub>OPT</sub>
    * Description: The maximum velocity measured in all transects included in the discharge measurement
    * range: [Double](types/Double.md)
 * [riverWidthMean](riverWidthMean.md)  <sub>OPT</sub>
    * Description: The mean river width measured in all transects included in the discharge measurement
    * range: [Double](types/Double.md)
 * [samplingProtocol](samplingProtocol.md)  <sub>OPT</sub>
    * Description: The NEON document number where detailed information regarding the sampling method used is available; format NEON.DOC.######
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [stationaryMBT](stationaryMBT.md)  <sub>OPT</sub>
    * Description: Whether or not a stationary moving bed test was performed prior to the discharge measurement
    * range: [String](types/String.md)
 * [streamStage](streamStage.md)  <sub>OPT</sub>
    * Description: Reading of water height on staff gauge
    * range: [Double](types/Double.md)
 * [streamStageUnits](streamStageUnits.md)  <sub>OPT</sub>
    * Description: Stage measurement units
    * range: [String](types/String.md)
 * [totalDischarge](totalDischarge.md)  <sub>OPT</sub>
    * Description: Calculated discharge from the velocity meter device
    * range: [Double](types/Double.md)
 * [totalDischargeRU](totalDischargeRU.md)  <sub>OPT</sub>
    * Description: The relative uncertainty of the total measured discharge as expressed by the standard deviation of the mean discharge within all transects used for the discharge measurement
    * range: [Double](types/Double.md)
 * [totalDischargeUnits](totalDischargeUnits.md)  <sub>OPT</sub>
    * Description: Discharge measurement units; should be in lps - liters per second or m^3/s - cubic meters per second
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [velocityUnits](velocityUnits.md)  <sub>OPT</sub>
    * Description: Velocity units
    * range: [String](types/String.md)
 * [waterTemperature](waterTemperature.md)  <sub>OPT</sub>
    * Description: The measured water temperature
    * range: [Double](types/Double.md)
 * [widthUnits](widthUnits.md)  <sub>OPT</sub>
    * Description: Width units
    * range: [String](types/String.md)
 * [windDirRelativeToFlow](windDirRelativeToFlow.md)  <sub>OPT</sub>
    * Description: The observed wind direction prior to the discharge measurement, relative to the direction of streamflow
    * range: [String](types/String.md)
 * [windSpeedPrior](windSpeedPrior.md)  <sub>OPT</sub>
    * Description: The measured wind speed prior to the discharge measurement
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:dsc_fieldDataADCP_pub |

