
# Type: mos_pathogenresults_in




URI: [neon:MosPathogenresultsIn](https://data.neonscience.org/MosPathogenresultsIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MosPathogenresultsIn&#124;uid:string%20%3F;remarks:string%20%3F;laboratoryName:string%20%3F;sampleCompromised:string%20%3F;receivedDate:time%20%3F;testingVialID:string%20%3F;deprecatedVialID:string%20%3F;testedDate:time%20%3F;senderID:string%20%3F;testProtocolVersion:string%20%3F;testMethod:string%20%3F;testResult:string%20%3F;testPathogenName:string%20%3F;testNumber:string%20%3F;finalResult:string%20%3F;locus:string%20%3F;percentIdentity:string%20%3F;sequenceDatabase:string%20%3F;sequenceDatabaseID:string%20%3F;extractDepleted:string%20%3F;testedBy:string%20%3F;startCollectDate:time%20%3F;endCollectDate:time%20%3F;locationID:string%20%3F;dataQF:string%20%3F;batchID:string%20%3F;testingVialIDCode:string%20%3F;testingVialIDFate:string%20%3F])

## Attributes


### Own

 * [batchID](batchID.md)  <sub>OPT</sub>
    * Description: Identifier for batch or analytical run
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [deprecatedVialID](deprecatedVialID.md)  <sub>OPT</sub>
    * Description: Identifier on vial label, if different from standard ID
    * range: [String](types/String.md)
 * [endCollectDate](endCollectDate.md)  <sub>OPT</sub>
    * Description: Latest known collection date for this sample
    * range: [Time](types/Time.md)
 * [extractDepleted](extractDepleted.md)  <sub>OPT</sub>
    * Description: Whether or not sample extract is depleted
    * range: [String](types/String.md)
 * [finalResult](finalResult.md)  <sub>OPT</sub>
    * Description: Whether or not this is the conclusive test result for this sample
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [locus](locus.md)  <sub>OPT</sub>
    * Description: Name of genetic marker sequenced
    * range: [String](types/String.md)
 * [percentIdentity](percentIdentity.md)  <sub>OPT</sub>
    * Description: Percent match between sample and reference sequence
    * range: [String](types/String.md)
 * [receivedDate](receivedDate.md)  <sub>OPT</sub>
    * Description: Date a sample was received
    * range: [Time](types/Time.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleCompromised](sampleCompromised.md)  <sub>OPT</sub>
    * Description: Indicator of compromised sample integrity; 'other' requires further specification in remarks
    * range: [String](types/String.md)
 * [senderID](senderID.md)  <sub>OPT</sub>
    * Description: Identifier for the facility or technician sending the sample or specimen
    * range: [String](types/String.md)
 * [sequenceDatabase](sequenceDatabase.md)  <sub>OPT</sub>
    * Description: Name of database where sequence is stored
    * range: [String](types/String.md)
 * [sequenceDatabaseID](sequenceDatabaseID.md)  <sub>OPT</sub>
    * Description: Identifier for sample in sequence database
    * range: [String](types/String.md)
 * [startCollectDate](startCollectDate.md)  <sub>OPT</sub>
    * Description: Earliest known collection date for this sample
    * range: [Time](types/Time.md)
 * [testMethod](testMethod.md)  <sub>OPT</sub>
    * Description: Method used to conduct test
    * range: [String](types/String.md)
 * [testNumber](testNumber.md)  <sub>OPT</sub>
    * Description: Test number in a sequence of tests
    * range: [String](types/String.md)
 * [testPathogenName](testPathogenName.md)  <sub>OPT</sub>
    * Description: The name of the pathogen
    * range: [String](types/String.md)
 * [testProtocolVersion](testProtocolVersion.md)  <sub>OPT</sub>
    * Description: The protocol version used to test the sample
    * range: [String](types/String.md)
 * [testResult](testResult.md)  <sub>OPT</sub>
    * Description: Result of the test
    * range: [String](types/String.md)
 * [testedBy](testedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who tested the sample
    * range: [String](types/String.md)
 * [testedDate](testedDate.md)  <sub>OPT</sub>
    * Description: Date test was conducted
    * range: [Time](types/Time.md)
 * [testingVialID](testingVialID.md)  <sub>OPT</sub>
    * Description: Identifier for the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
    * range: [String](types/String.md)
 * [testingVialIDCode](testingVialIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
    * range: [String](types/String.md)
 * [testingVialIDFate](testingVialIDFate.md)  <sub>OPT</sub>
    * Description: Fate of the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mos_pathogenresults_in |

