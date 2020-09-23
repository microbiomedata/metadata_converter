
# Type: fsh_perPass_in




URI: [neon:FshPerPassIn](https://data.neonscience.org/FshPerPassIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[FshPerPassIn&#124;uid:string%20%3F;remarks:string%20%3F;eventID:string%20%3F;targetTaxaPresent:string%20%3F;waterTemp:double%20%3F;specificConductance:double%20%3F;dissolvedOxygen:double%20%3F;habitatType:string%20%3F;locationID:string%20%3F;samplerType:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;efTime:double%20%3F;efTime2:double%20%3F;finalDutyCycle:double%20%3F;finalDutyCycle2:double%20%3F;finalFrequency:double%20%3F;finalFrequency2:double%20%3F;finalVoltage:double%20%3F;finalVoltage2:double%20%3F;initialDutyCycle:double%20%3F;initialDutyCycle2:double%20%3F;initialFrequency:double%20%3F;initialFrequency2:double%20%3F;initialVoltage:double%20%3F;initialVoltage2:double%20%3F;netDeploymentTime:double%20%3F;netDepth:double%20%3F;netEndTime:time%20%3F;netIntegrity:string%20%3F;netLength:double%20%3F;netSetTime:time%20%3F;passEndTime:time%20%3F;passNumber:string%20%3F;passStartTime:time%20%3F;reachID:string%20%3F;settingsChanged:string%20%3F;settingsChanged2:string%20%3F;subdominantHabitatType:string%20%3F])

## Attributes


### Own

 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [dissolvedOxygen](dissolvedOxygen.md)  <sub>OPT</sub>
    * Description: Dissolved Oxygen Concentration
    * range: [Double](types/Double.md)
 * [efTime](efTime.md)  <sub>OPT</sub>
    * Description: Operational time of the electrofisher
    * range: [Double](types/Double.md)
 * [efTime2](efTime2.md)  <sub>OPT</sub>
    * Description: Operational time of the electrofisher for the second electrofisher
    * range: [Double](types/Double.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [finalDutyCycle](finalDutyCycle.md)  <sub>OPT</sub>
    * Description: Duty cycle at the end of data collection
    * range: [Double](types/Double.md)
 * [finalDutyCycle2](finalDutyCycle2.md)  <sub>OPT</sub>
    * Description: Duty cycle at the end of data collection for the second electrofisher
    * range: [Double](types/Double.md)
 * [finalFrequency](finalFrequency.md)  <sub>OPT</sub>
    * Description: Frequency at the end of data collection
    * range: [Double](types/Double.md)
 * [finalFrequency2](finalFrequency2.md)  <sub>OPT</sub>
    * Description: Frequency at the end of data collection for the second electrofisher
    * range: [Double](types/Double.md)
 * [finalVoltage](finalVoltage.md)  <sub>OPT</sub>
    * Description: Voltage at the end of data collection
    * range: [Double](types/Double.md)
 * [finalVoltage2](finalVoltage2.md)  <sub>OPT</sub>
    * Description: Voltage at the end of data collection for the second electrofisher
    * range: [Double](types/Double.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [habitatType](habitatType.md)  <sub>OPT</sub>
    * Description: Habitat type sampled
    * range: [String](types/String.md)
 * [initialDutyCycle](initialDutyCycle.md)  <sub>OPT</sub>
    * Description: Duty cycle at the start of data collection
    * range: [Double](types/Double.md)
 * [initialDutyCycle2](initialDutyCycle2.md)  <sub>OPT</sub>
    * Description: Duty cycle at the start of data collection for the second electrofisher
    * range: [Double](types/Double.md)
 * [initialFrequency](initialFrequency.md)  <sub>OPT</sub>
    * Description: Frequency at the start of data collection
    * range: [Double](types/Double.md)
 * [initialFrequency2](initialFrequency2.md)  <sub>OPT</sub>
    * Description: Frequency at the start of data collection for the second electrofisher
    * range: [Double](types/Double.md)
 * [initialVoltage](initialVoltage.md)  <sub>OPT</sub>
    * Description: Voltage at the start of data collection
    * range: [Double](types/Double.md)
 * [initialVoltage2](initialVoltage2.md)  <sub>OPT</sub>
    * Description: Voltage at the start of data collection for the second electrofisher
    * range: [Double](types/Double.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [netDeploymentTime](netDeploymentTime.md)  <sub>OPT</sub>
    * Description: Total time of deployment of the net
    * range: [Double](types/Double.md)
 * [netDepth](netDepth.md)  <sub>OPT</sub>
    * Description: Deployment depth of the net
    * range: [Double](types/Double.md)
 * [netEndTime](netEndTime.md)  <sub>OPT</sub>
    * Description: Time the net was pulled
    * range: [Time](types/Time.md)
 * [netIntegrity](netIntegrity.md)  <sub>OPT</sub>
    * Description: Indication of the integrity of the net
    * range: [String](types/String.md)
 * [netLength](netLength.md)  <sub>OPT</sub>
    * Description: Length of the net
    * range: [Double](types/Double.md)
 * [netSetTime](netSetTime.md)  <sub>OPT</sub>
    * Description: Time the net was set
    * range: [Time](types/Time.md)
 * [passEndTime](passEndTime.md)  <sub>OPT</sub>
    * Description: The end time of the pass
    * range: [Time](types/Time.md)
 * [passNumber](passNumber.md)  <sub>OPT</sub>
    * Description: Number of the sampling pass within a reach
    * range: [String](types/String.md)
 * [passStartTime](passStartTime.md)  <sub>OPT</sub>
    * Description: The start time of the pass
    * range: [Time](types/Time.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [reachID](reachID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the reach
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [samplerType](samplerType.md)  <sub>OPT</sub>
    * Description: Type of sampler used to collect the sample
    * range: [String](types/String.md)
 * [settingsChanged](settingsChanged.md)  <sub>OPT</sub>
    * Description: Number of times the settings changed
    * range: [String](types/String.md)
 * [settingsChanged2](settingsChanged2.md)  <sub>OPT</sub>
    * Description: Number of times the settings changed for the second electrofisher
    * range: [String](types/String.md)
 * [specificConductance](specificConductance.md)  <sub>OPT</sub>
    * Description: Conductivity auto-corrected to 25 degrees C
    * range: [Double](types/Double.md)
 * [subdominantHabitatType](subdominantHabitatType.md)  <sub>OPT</sub>
    * Description: Subdominant habitat type sampled
    * range: [String](types/String.md)
 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
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
| **Mappings:** | | neon:fsh_perPass_in |

