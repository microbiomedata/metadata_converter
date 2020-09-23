
# Type: bry_productivity_in




URI: [neon:BryProductivityIn](https://data.neonscience.org/BryProductivityIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BryProductivityIn&#124;uid:string%20%3F;plotID:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;targetTaxaPresent:string%20%3F;subplotID:string%20%3F;clipID:string%20%3F;bagCount:string%20%3F;weighDate:time%20%3F;qaDryMass:string%20%3F;dryMass:double%20%3F;storageHours:double%20%3F;samplingProtocolVersion:string%20%3F;collectedBy:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;totalSampledArea:double%20%3F;setNetCount:string%20%3F;sampledNetCount:string%20%3F;missingNetCount:string%20%3F;ovenStartDate:time%20%3F;ovenEndDate:time%20%3F;setBy:string%20%3F;setRemarks:string%20%3F;collectRemarks:string%20%3F;weighRemarks:string%20%3F;sampleCondition:string%20%3F;growthInterval:string%20%3F;bryType:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F])

## Attributes


### Own

 * [bagCount](bagCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of sample bags transported from the field to the laboratory for processing
    * range: [String](types/String.md)
 * [bryType](bryType.md)  <sub>OPT</sub>
    * Description: Describes the dominant type of bryophyte present in a clipped sample
    * range: [String](types/String.md)
 * [clipID](clipID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the clip-harvest location within the plot
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [collectRemarks](collectRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the collect activity
    * range: [String](types/String.md)
 * [collectedBy](collectedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who collected the sample or specimen
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [dryMass](dryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of sample or subsample
    * range: [Double](types/Double.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [growthInterval](growthInterval.md)  <sub>OPT</sub>
    * Description: The number of growing days between when sampling began and the collection event
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [missingNetCount](missingNetCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of nets missing since set event
    * range: [String](types/String.md)
 * [ovenEndDate](ovenEndDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample was removed from the drying oven
    * range: [Time](types/Time.md)
 * [ovenStartDate](ovenStartDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample was placed in the drying oven
    * range: [Time](types/Time.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [qaDryMass](qaDryMass.md)  <sub>OPT</sub>
    * Description: Indicates whether 'dryMass' value is associated with 'qa' measurement type
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [sampledNetCount](sampledNetCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of nets sampled
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [setBy](setBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who set the trap
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [setNetCount](setNetCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of nets set for sample collection
    * range: [String](types/String.md)
 * [setRemarks](setRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the set activity
    * range: [String](types/String.md)
 * [storageHours](storageHours.md)  <sub>OPT</sub>
    * Description: Total number of hours clipped biomass was stored between collection and processing
    * range: [Double](types/Double.md)
 * [subplotID](subplotID.md)  <sub>OPT</sub>
    * Description: Identifier for the NEON subplot
    * range: [String](types/String.md)
 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [totalSampledArea](totalSampledArea.md)  <sub>OPT</sub>
    * Description: Total area sampled
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [weighDate](weighDate.md)  <sub>OPT</sub>
    * Description: Date that sample or subsample was weighed
    * range: [Time](types/Time.md)
 * [weighRemarks](weighRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the weigh activity
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:bry_productivity_in |
| **In Subsets:** | | DP0.10035.001 |

