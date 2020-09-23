
# Type: fsh_fieldData_in




URI: [neon:FshFieldDataIn](https://data.neonscience.org/FshFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[FshFieldDataIn&#124;uid:string%20%3F;remarks:string%20%3F;identifiedBy:string%20%3F;aCollectedBy:string%20%3F;bCollectedBy:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;locationID:string%20%3F;dataQF:string%20%3F;aquaticSiteType:string%20%3F;samplingImpractical:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;cCollectedBy:string%20%3F;fixedRandomReach:string%20%3F;measuredReachLength:double%20%3F;reachCondition:string%20%3F;reachID:string%20%3F])

## Attributes


### Own

 * [aCollectedBy](aCollectedBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [aquaticSiteType](aquaticSiteType.md)  <sub>OPT</sub>
    * Description: Type of aquatic site, includes lake, river or stream
    * range: [String](types/String.md)
 * [bCollectedBy](bCollectedBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [cCollectedBy](cCollectedBy.md)  <sub>OPT</sub>
    * Description: Additional NEON technician username who collected the data
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [fixedRandomReach](fixedRandomReach.md)  <sub>OPT</sub>
    * Description: An indication of whether the reach is fixed or random
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [identifiedBy](identifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who identified the specimen
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [measuredReachLength](measuredReachLength.md)  <sub>OPT</sub>
    * Description: The length of the reach as measured by the technicians when the reach was established
    * range: [Double](types/Double.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [reachCondition](reachCondition.md)  <sub>OPT</sub>
    * Description: An indication of the condition of the sampling reach
    * range: [String](types/String.md)
 * [reachID](reachID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the reach
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [samplingImpractical](samplingImpractical.md)  <sub>OPT</sub>
    * Description: Samples and/or measurements were not collected due to the indicated circumstance
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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:fsh_fieldData_in |
| **In Subsets:** | | DP0.20107.001 |

