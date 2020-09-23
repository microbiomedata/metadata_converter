
# Type: zoo_fieldData_in




URI: [neon:ZooFieldDataIn](https://data.neonscience.org/ZooFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ZooFieldDataIn&#124;uid:string%20%3F;remarks:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;samplingProtocolVersion:string%20%3F;collectedBy:string%20%3F;locationID:string%20%3F;samplerType:string%20%3F;sampleNumber:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;towsTrapsNumber:string%20%3F;aquaticSiteType:string%20%3F;zooDepth1:double%20%3F;zooDepth2:double%20%3F;zooDepth3:double%20%3F;sampleClass:string%20%3F;samplingImpractical:string%20%3F;additionalCoordUncertainty:double%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;towsTrapsVolume:double%20%3F])

## Attributes


### Own

 * [additionalCoordUncertainty](additionalCoordUncertainty.md)  <sub>OPT</sub>
    * Description: Additional uncertainty to be added to the coordinate uncertainty at all sites
    * range: [Double](types/Double.md)
 * [aquaticSiteType](aquaticSiteType.md)  <sub>OPT</sub>
    * Description: Type of aquatic site, includes lake, river or stream
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [collectedBy](collectedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who collected the sample or specimen
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
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
 * [sampleNumber](sampleNumber.md)  <sub>OPT</sub>
    * Description: Number of sample collected
    * range: [String](types/String.md)
 * [samplerType](samplerType.md)  <sub>OPT</sub>
    * Description: Type of sampler used to collect the sample
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
 * [towsTrapsNumber](towsTrapsNumber.md)  <sub>OPT</sub>
    * Description: Number of zooplankton tows or traps composited into one sample
    * range: [String](types/String.md)
 * [towsTrapsVolume](towsTrapsVolume.md)  <sub>OPT</sub>
    * Description: Sample volume collected for zooplankton
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [zooDepth1](zooDepth1.md)  <sub>OPT</sub>
    * Description: Depth of the first sample for a composite lake zooplankton sample
    * range: [Double](types/Double.md)
 * [zooDepth2](zooDepth2.md)  <sub>OPT</sub>
    * Description: Depth of the second sample for a composite lake zooplankton sample
    * range: [Double](types/Double.md)
 * [zooDepth3](zooDepth3.md)  <sub>OPT</sub>
    * Description: Depth of the third sample for a composite lake zooplankton sample
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:zoo_fieldData_in |
| **In Subsets:** | | DP0.20219.001 |

