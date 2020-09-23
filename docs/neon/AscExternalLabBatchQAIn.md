
# Type: asc_externalLabBatchQA_in




URI: [neon:AscExternalLabBatchQAIn](https://data.neonscience.org/AscExternalLabBatchQAIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AscExternalLabBatchQAIn&#124;uid:string%20%3F;laboratoryName:string%20%3F;internalLabID:string%20%3F;analyte:string%20%3F;analyteUnits:string%20%3F;analysisDate:time%20%3F;analysisEndDate:time%20%3F;batchID:string%20%3F;analyteKnownValue:double%20%3F;runID:string%20%3F;qaType:string%20%3F;analyteObservedValue:double%20%3F;analyteSampleValue:double%20%3F;analyteSurrogate:string%20%3F;qaQF:string%20%3F;reagentSN:string%20%3F;recovery:double%20%3F;recoveryLimitLower:double%20%3F;recoveryLimitUpper:double%20%3F;relativePercentDifference:double%20%3F;relativePercentLimit:double%20%3F])

## Attributes


### Own

 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
 * [analysisEndDate](analysisEndDate.md)  <sub>OPT</sub>
    * Description: The end date or dateTime of analysis
    * range: [Time](types/Time.md)
 * [analyte](analyte.md)  <sub>OPT</sub>
    * Description: Analyte or parameter measured
    * range: [String](types/String.md)
 * [analyteKnownValue](analyteKnownValue.md)  <sub>OPT</sub>
    * Description: The known value of a given analyte for a quality assurance reference material or standard, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [analyteObservedValue](analyteObservedValue.md)  <sub>OPT</sub>
    * Description: The measured value of a given analyte for a standard reference material, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [analyteSampleValue](analyteSampleValue.md)  <sub>OPT</sub>
    * Description: The known value of a given analyte for a sample, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [analyteSurrogate](analyteSurrogate.md)  <sub>OPT</sub>
    * Description: Indicator for whether an analyte is a surrogate
    * range: [String](types/String.md)
 * [analyteUnits](analyteUnits.md)  <sub>OPT</sub>
    * Description: Associated units of measure for analyte
    * range: [String](types/String.md)
 * [batchID](batchID.md)  <sub>OPT</sub>
    * Description: Identifier for batch or analytical run
    * range: [String](types/String.md)
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [qaQF](qaQF.md)  <sub>OPT</sub>
    * Description: Quality flag for quality control sample
    * range: [String](types/String.md)
 * [qaType](qaType.md)  <sub>OPT</sub>
    * Description: Type of quality assurance used in analysis
    * range: [String](types/String.md)
 * [reagentSN](reagentSN.md)  <sub>OPT</sub>
    * Description: Serial number assigned to reagents or standards to trace to the manufacturer certificate of analysis
    * range: [String](types/String.md)
 * [recovery](recovery.md)  <sub>OPT</sub>
    * Description: Recovered amount of the known value or spike
    * range: [Double](types/Double.md)
 * [recoveryLimitLower](recoveryLimitLower.md)  <sub>OPT</sub>
    * Description: Lower limit for percent recovery
    * range: [Double](types/Double.md)
 * [recoveryLimitUpper](recoveryLimitUpper.md)  <sub>OPT</sub>
    * Description: Upper limit for percent recovery
    * range: [Double](types/Double.md)
 * [relativePercentDifference](relativePercentDifference.md)  <sub>OPT</sub>
    * Description: Percent difference between observed values of a sample or standard run in duplicate
    * range: [Double](types/Double.md)
 * [relativePercentLimit](relativePercentLimit.md)  <sub>OPT</sub>
    * Description: Upper limit for relative percent difference
    * range: [Double](types/Double.md)
 * [runID](runID.md)  <sub>OPT</sub>
    * Description: A linking value provided by the external lab that associates the sample data to the run metadata, including QA values
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:asc_externalLabBatchQA_in |

