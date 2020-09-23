
# Type: sls_soilStableIsotopes_pub




URI: [neon:SlsSoilStableIsotopesPub](https://data.neonscience.org/SlsSoilStableIsotopesPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SlsSoilStableIsotopesPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;sampleType:string%20%3F;plotType:string%20%3F;laboratoryName:string%20%3F;instrument:string%20%3F;testMethod:string%20%3F;analysisDate:time%20%3F;analyzedBy:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;cnSampleCode:string%20%3F;cnSampleID:string%20%3F;reviewedBy:string%20%3F;namedLocation:string%20%3F;acidTreatment:string%20%3F;analyticalRepNumber:string%20%3F;cnIsotopeQF:string%20%3F;d15N:double%20%3F;isotopeAccuracyQF:string%20%3F;organicd13C:double%20%3F])

## Attributes


### Own

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
 * [cnIsotopeQF](cnIsotopeQF.md)  <sub>OPT</sub>
    * Description: Quality flag for stable isotope values outside the calibration range
    * range: [String](types/String.md)
 * [cnSampleCode](cnSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a carbon-nitrogen sample
    * range: [String](types/String.md)
 * [cnSampleID](cnSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a carbon-nitrogen sample
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [d15N](d15N.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of 15N:14N in a sample, relative to atmospheric N2
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [instrument](instrument.md)  <sub>OPT</sub>
    * Description: Type of instrument used for the analysis
    * range: [String](types/String.md)
 * [isotopeAccuracyQF](isotopeAccuracyQF.md)  <sub>OPT</sub>
    * Description: Quality flag for accuracy of stable isotope values of QA materials associated with the run
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [organicd13C](organicd13C.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of 13C:12C in soil organic carbon, relative to Vienna Pee Dee Belemnite
    * range: [Double](types/Double.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [plotType](plotType.md)  <sub>OPT</sub>
    * Description: NEON plot type in which sampling occurred: tower, distributed or gradient
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [reviewedBy](reviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed the data prior to submission
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [sampleType](sampleType.md)  <sub>OPT</sub>
    * Description: Type of sample
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [testMethod](testMethod.md)  <sub>OPT</sub>
    * Description: Method used to conduct test
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sls_soilStableIsotopes_pub |
| **In Subsets:** | | DP1.10100.001 |

