
# Type: apc_pointTransect_in




URI: [neon:ApcPointTransectIn](https://data.neonscience.org/ApcPointTransectIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ApcPointTransectIn&#124;uid:string%20%3F;remarks:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;collectDate:time%20%3F;targetTaxaPresent:string%20%3F;startDate:time%20%3F;samplingProtocolVersion:string%20%3F;collectedBy:string%20%3F;habitatType:string%20%3F;dataQF:string%20%3F;aquaticSiteType:string%20%3F;transectID:string%20%3F;samplingImpractical:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;pointNumber:string%20%3F;substrate:string%20%3F;transectDistance:double%20%3F])

## Attributes


### Own

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
 * [habitatType](habitatType.md)  <sub>OPT</sub>
    * Description: Habitat type sampled
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [pointNumber](pointNumber.md)  <sub>OPT</sub>
    * Description: Number of the point sampled for a given location
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
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
 * [substrate](substrate.md)  <sub>OPT</sub>
    * Description: Organic or inorganic surface material at the location
    * range: [String](types/String.md)
 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [transectDistance](transectDistance.md)  <sub>OPT</sub>
    * Description: Distance along the transect
    * range: [Double](types/Double.md)
 * [transectID](transectID.md)  <sub>OPT</sub>
    * Description: An identifier for the transect
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:apc_pointTransect_in |
| **In Subsets:** | | DP0.20072.001 |

