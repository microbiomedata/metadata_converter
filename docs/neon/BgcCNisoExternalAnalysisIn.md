
# Type: bgc_CNiso_externalAnalysis_in




URI: [neon:BgcCNisoExternalAnalysisIn](https://data.neonscience.org/BgcCNisoExternalAnalysisIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BgcCNisoExternalAnalysisIn&#124;uid:string%20%3F;remarks:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;sampleType:string%20%3F;laboratoryName:string%20%3F;internalLabID:string%20%3F;instrument:string%20%3F;receivedDate:time%20%3F;testMethod:string%20%3F;locationID:string%20%3F;analysisDate:time%20%3F;analyzedBy:string%20%3F;dataQF:string%20%3F;cnSampleCode:string%20%3F;cnSampleFate:string%20%3F;cnSampleID:string%20%3F;reviewedBy:string%20%3F;acidTreatment:string%20%3F;analyticalRepNumber:string%20%3F;carbonPercent:double%20%3F;cnIsotopeQF:string%20%3F;cnPercentQF:string%20%3F;CNratio:double%20%3F;d13C:double%20%3F;d15N:double%20%3F;nitrogenPercent:double%20%3F;runID:string%20%3F;isotopeAccuracyQF:string%20%3F;percentAccuracyQF:string%20%3F;co2Trapped:string%20%3F])

## Attributes


### Own

 * [CNratio](CNratio.md)  <sub>OPT</sub>
    * Description: Ratio of carbon to nitrogen concentration in a sample on a dry weight basis
    * range: [Double](types/Double.md)
 * [acidTreatment](acidTreatment.md)  <sub>OPT</sub>
    * Description: Indicator for whether a sample has been acidified to remove carbonate prior to analysis
    * range: [String](types/String.md)
 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
 * [analyticalRepNumber](analyticalRepNumber.md)  <sub>OPT</sub>
    * Description: Number of the analytical replicate
    * range: [String](types/String.md)
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
 * [carbonPercent](carbonPercent.md)  <sub>OPT</sub>
    * Description: Percent carbon in a sample on a dry weight basis
    * range: [Double](types/Double.md)
 * [cnIsotopeQF](cnIsotopeQF.md)  <sub>OPT</sub>
    * Description: Quality flag for stable isotope values outside the calibration range
    * range: [String](types/String.md)
 * [cnPercentQF](cnPercentQF.md)  <sub>OPT</sub>
    * Description: Quality flag for concentration values outside the calibration range
    * range: [String](types/String.md)
 * [cnSampleCode](cnSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a carbon-nitrogen sample
    * range: [String](types/String.md)
 * [cnSampleFate](cnSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a carbon-nitrogen sample
    * range: [String](types/String.md)
 * [cnSampleID](cnSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a carbon-nitrogen sample
    * range: [String](types/String.md)
 * [co2Trapped](co2Trapped.md)  <sub>OPT</sub>
    * Description: Indicator for whether carbon dioxide was trapped prior to analysis; used for measuring nitrogen in high C:N samples
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [d13C](d13C.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of 13C:12C in a sample, relative to Vienna Pee Dee Belemnite
    * range: [Double](types/Double.md)
 * [d15N](d15N.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of 15N:14N in a sample, relative to atmospheric N2
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [instrument](instrument.md)  <sub>OPT</sub>
    * Description: Type of instrument used for the analysis
    * range: [String](types/String.md)
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
 * [isotopeAccuracyQF](isotopeAccuracyQF.md)  <sub>OPT</sub>
    * Description: Quality flag for accuracy of stable isotope values of QA materials associated with the run
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [nitrogenPercent](nitrogenPercent.md)  <sub>OPT</sub>
    * Description: Percent nitrogen in a sample on a dry weight basis
    * range: [Double](types/Double.md)
 * [percentAccuracyQF](percentAccuracyQF.md)  <sub>OPT</sub>
    * Description: Quality flag for accuracy of percent concentration values of QA materials associated with the run
    * range: [String](types/String.md)
 * [receivedDate](receivedDate.md)  <sub>OPT</sub>
    * Description: Date a sample was received
    * range: [Time](types/Time.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [reviewedBy](reviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed the data prior to submission
    * range: [String](types/String.md)
 * [runID](runID.md)  <sub>OPT</sub>
    * Description: A linking value provided by the external lab that associates the sample data to the run metadata, including QA values
    * range: [String](types/String.md)
 * [sampleType](sampleType.md)  <sub>OPT</sub>
    * Description: Type of sample
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [testMethod](testMethod.md)  <sub>OPT</sub>
    * Description: Method used to conduct test
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:bgc_CNiso_externalAnalysis_in |
| **In Subsets:** | | DP0.10103.001 |

