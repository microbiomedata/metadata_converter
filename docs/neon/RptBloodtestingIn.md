
# Type: rpt_bloodtesting_in




URI: [neon:RptBloodtestingIn](https://data.neonscience.org/RptBloodtestingIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[RptBloodtestingIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;bloodSampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;laboratoryName:string%20%3F;internalLabID:string%20%3F;testedDate:time%20%3F;testProtocolVersion:string%20%3F;testResult:string%20%3F;testPathogenName:string%20%3F;dataQF:string%20%3F;sampleCondition:string%20%3F;batchID:string%20%3F;bloodSampleBarcode:string%20%3F;bloodSampleFate:string%20%3F;agWellOpticalDensity:double%20%3F;cAgWellOpticalDensity:double%20%3F;conjugateDilution:string%20%3F;conjugateLot:string%20%3F;diluentDilution:string%20%3F;diluentLot:string%20%3F;internalLabBarcode:string%20%3F;internalLabFate:string%20%3F;negAbDilution:string%20%3F;negAbLot:string%20%3F;netOpticalDensity:double%20%3F;plateLot:string%20%3F;posAbDilution:string%20%3F;posAbLot:string%20%3F;rawTestResult:string%20%3F;substrateLot:string%20%3F;substrateTime:double%20%3F])

## Attributes


### Own

 * [agWellOpticalDensity](agWellOpticalDensity.md)  <sub>OPT</sub>
    * Description: Antigen well optical density value
    * range: [Double](types/Double.md)
 * [batchID](batchID.md)  <sub>OPT</sub>
    * Description: Identifier for batch or analytical run
    * range: [String](types/String.md)
 * [bloodSampleBarcode](bloodSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of the blood sample
    * range: [String](types/String.md)
 * [bloodSampleFate](bloodSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of the blood sample
    * range: [String](types/String.md)
 * [bloodSampleID](bloodSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the blood sample
    * range: [String](types/String.md)
 * [cAgWellOpticalDensity](cAgWellOpticalDensity.md)  <sub>OPT</sub>
    * Description: Control antigen well optical density value
    * range: [Double](types/Double.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [conjugateDilution](conjugateDilution.md)  <sub>OPT</sub>
    * Description: Recommended use dilution based off of manufacturer product sheet (rat/peromyscus)
    * range: [String](types/String.md)
 * [conjugateLot](conjugateLot.md)  <sub>OPT</sub>
    * Description: ELISA conjugate lot number (rat/peromyscus)
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [diluentDilution](diluentDilution.md)  <sub>OPT</sub>
    * Description: Diluent (skim milk) stock concentration
    * range: [String](types/String.md)
 * [diluentLot](diluentLot.md)  <sub>OPT</sub>
    * Description: Sample diluent lot number (skim milk)
    * range: [String](types/String.md)
 * [internalLabBarcode](internalLabBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of a subsample with internalLabID
    * range: [String](types/String.md)
 * [internalLabFate](internalLabFate.md)  <sub>OPT</sub>
    * Description: Fate of a subsample with internalLabID
    * range: [String](types/String.md)
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [negAbDilution](negAbDilution.md)  <sub>OPT</sub>
    * Description: Negative control antibody dilution
    * range: [String](types/String.md)
 * [negAbLot](negAbLot.md)  <sub>OPT</sub>
    * Description: Negative control antibody lot number
    * range: [String](types/String.md)
 * [netOpticalDensity](netOpticalDensity.md)  <sub>OPT</sub>
    * Description: Quantitative comparison of sample against standard curve
    * range: [Double](types/Double.md)
 * [plateLot](plateLot.md)  <sub>OPT</sub>
    * Description: ELISA plate lot number
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [posAbDilution](posAbDilution.md)  <sub>OPT</sub>
    * Description: Positive control antibody dilution (based on plate production QC)
    * range: [String](types/String.md)
 * [posAbLot](posAbLot.md)  <sub>OPT</sub>
    * Description: Positive control antibody lot number
    * range: [String](types/String.md)
 * [rawTestResult](rawTestResult.md)  <sub>OPT</sub>
    * Description: Test result code or value returned from lab
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [substrateLot](substrateLot.md)  <sub>OPT</sub>
    * Description: ELISA substrate lot number
    * range: [String](types/String.md)
 * [substrateTime](substrateTime.md)  <sub>OPT</sub>
    * Description: How long the substrate has been added to the plate before the plate is analyzed
    * range: [Double](types/Double.md)
 * [testPathogenName](testPathogenName.md)  <sub>OPT</sub>
    * Description: The name of the pathogen
    * range: [String](types/String.md)
 * [testProtocolVersion](testProtocolVersion.md)  <sub>OPT</sub>
    * Description: The protocol version used to test the sample
    * range: [String](types/String.md)
 * [testResult](testResult.md)  <sub>OPT</sub>
    * Description: Result of the test
    * range: [String](types/String.md)
 * [testedDate](testedDate.md)  <sub>OPT</sub>
    * Description: Date test was conducted
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:rpt_bloodtesting_in |
| **In Subsets:** | | DP0.10064.001 |

