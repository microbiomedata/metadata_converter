
# Type: inv_fielddata_in




URI: [neon:InvFielddataIn](https://data.neonscience.org/InvFielddataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[InvFielddataIn&#124;uid:string%20%3F;remarks:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;samplingProtocolVersion:string%20%3F;collectedBy:string%20%3F;habitatType:string%20%3F;locationID:string%20%3F;benthicArea:double%20%3F;samplerType:string%20%3F;sampleNumber:string%20%3F;substratumSizeClass:string%20%3F;ponarDepth:double%20%3F;snagLength:double%20%3F;snagDiameter:double%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;geneticSampleID:string%20%3F;aquaticSiteType:string%20%3F;geneticSampleCode:string%20%3F;geneticSampleFate:string%20%3F;samplingImpractical:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;dnaSnagDiameter:double%20%3F;dnaSnagLength:double%20%3F])

## Attributes


### Own

 * [aquaticSiteType](aquaticSiteType.md)  <sub>OPT</sub>
    * Description: Type of aquatic site, includes lake, river or stream
    * range: [String](types/String.md)
 * [benthicArea](benthicArea.md)  <sub>OPT</sub>
    * Description: Area of the benthos sampled
    * range: [Double](types/Double.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [collectedBy](collectedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who collected the sample or specimen
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [dnaSnagDiameter](dnaSnagDiameter.md)  <sub>OPT</sub>
    * Description: Diameter of snag sampled for DNA
    * range: [Double](types/Double.md)
 * [dnaSnagLength](dnaSnagLength.md)  <sub>OPT</sub>
    * Description: Length of snag sampled for DNA
    * range: [Double](types/Double.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [geneticSampleCode](geneticSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a genetic sample
    * range: [String](types/String.md)
 * [geneticSampleFate](geneticSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a genetic sample
    * range: [String](types/String.md)
 * [geneticSampleID](geneticSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for the genetic sample
    * range: [String](types/String.md)
 * [habitatType](habitatType.md)  <sub>OPT</sub>
    * Description: Habitat type sampled
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [ponarDepth](ponarDepth.md)  <sub>OPT</sub>
    * Description: Depth of petite ponar sample
    * range: [Double](types/Double.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
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
 * [snagDiameter](snagDiameter.md)  <sub>OPT</sub>
    * Description: Diameter of snag sampled
    * range: [Double](types/Double.md)
 * [snagLength](snagLength.md)  <sub>OPT</sub>
    * Description: Length of snag sampled
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [substratumSizeClass](substratumSizeClass.md)  <sub>OPT</sub>
    * Description: Size class of the substratum sampled
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:inv_fielddata_in |
| **In Subsets:** | | DP0.20120.001 |

