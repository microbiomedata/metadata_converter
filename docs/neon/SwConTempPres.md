
# Type: swConTempPres




URI: [neon:SwConTempPres](https://data.neonscience.org/SwConTempPres)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [conductance](conductance.md)  <sub>OPT</sub>
    * Description: Conductivity at ambient temperture
    * range: [Double](types/Double.md)
 * [conductanceDataQualityID](conductanceDataQualityID.md)  <sub>OPT</sub>
    * Description: Data quality code from sensor for conductance
    * range: [Double](types/Double.md)
 * [groundwaterPressure](groundwaterPressure.md)  <sub>OPT</sub>
    * Description: Pressure of groundwater
    * range: [Double](types/Double.md)

### Inherited from TGW_5_minute:

 * [groundwaterTemp](groundwaterTemp.md)  <sub>OPT</sub>
    * Description: Temperature in groundwater
    * range: [Double](types/Double.md)
 * [groundwaterTempRangeQF](groundwaterTempRangeQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the range test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterTempPersistenceQF](groundwaterTempPersistenceQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the persistence test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterTempStepQF](groundwaterTempStepQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the step test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterTempNullQF](groundwaterTempNullQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the null test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterTempGapQF](groundwaterTempGapQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the gap test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterTempConsistencyQF](groundwaterTempConsistencyQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the consistency test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterTempSpikeQF](groundwaterTempSpikeQF.md)  <sub>OPT</sub>
    * Description: Temperature of groundwater quality flag for the spike test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None

### Inherited from levelTroll:

 * [batteryVoltage](batteryVoltage.md)  <sub>OPT</sub>
    * Description: Battery voltage
    * range: [Double](types/Double.md)
 * [tempDataQualityID](tempDataQualityID.md)  <sub>OPT</sub>
    * Description: Data quality code from sensor for temperature
    * range: [Double](types/Double.md)
 * [pressureDataQualityID](pressureDataQualityID.md)  <sub>OPT</sub>
    * Description: Data quality code from sensor for pressure
    * range: [Double](types/Double.md)
 * [surfaceWaterTemperature](surfaceWaterTemperature.md)  <sub>OPT</sub>
    * Description: Temperature in surface water
    * range: [Double](types/Double.md)
    * inherited from: None
 * [surfaceWaterPressure](surfaceWaterPressure.md)  <sub>OPT</sub>
    * Description: Pressure of surface water
    * range: [Double](types/Double.md)
    * inherited from: None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:swConTempPres |
| **In Subsets:** | | DP0.20054.001 |

