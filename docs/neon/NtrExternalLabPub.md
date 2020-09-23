
# Type: ntr_externalLab_pub




URI: [neon:NtrExternalLabPub](https://data.neonscience.org/NtrExternalLabPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NtrExternalLabPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;laboratoryName:string%20%3F;receivedDate:time%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;sampleCondition:string%20%3F;namedLocation:string%20%3F;ammoniumNAnalysisDate:time%20%3F;ammoniumNAnalyzedBy:string%20%3F;ammoniumNInstrument:string%20%3F;ammoniumNMethod:string%20%3F;ammoniumNQF:string%20%3F;ammoniumNRemarks:string%20%3F;ammoniumNRepNum:string%20%3F;ammoniumNReviewedBy:string%20%3F;kclAmmoniumNConc:double%20%3F;kclNitrateNitriteNConc:double%20%3F;kclSampleCode:string%20%3F;kclSampleID:string%20%3F;nitrateNitriteNAnalysisDate:time%20%3F;nitrateNitriteNAnalyzedBy:string%20%3F;nitrateNitriteNInstrument:string%20%3F;nitrateNitriteNMethod:string%20%3F;nitrateNitriteNQF:string%20%3F;nitrateNitriteNRemarks:string%20%3F;nitrateNitriteNRepNum:string%20%3F;nitrateNitriteNReviewedBy:string%20%3F;receivedCondition:string%20%3F])

## Attributes


### Own

 * [ammoniumNAnalysisDate](ammoniumNAnalysisDate.md)  <sub>OPT</sub>
    * Description: Date an ammonium sample was analyzed
    * range: [Time](types/Time.md)
 * [ammoniumNAnalyzedBy](ammoniumNAnalyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample for ammonium N
    * range: [String](types/String.md)
 * [ammoniumNInstrument](ammoniumNInstrument.md)  <sub>OPT</sub>
    * Description: Type of instrument used for ammonium analysis
    * range: [String](types/String.md)
 * [ammoniumNMethod](ammoniumNMethod.md)  <sub>OPT</sub>
    * Description: Method used to test sample for ammonium N concentration
    * range: [String](types/String.md)
 * [ammoniumNQF](ammoniumNQF.md)  <sub>OPT</sub>
    * Description: Quality flag for ammonium N values
    * range: [String](types/String.md)
 * [ammoniumNRemarks](ammoniumNRemarks.md)  <sub>OPT</sub>
    * Description: Free text comments accompanying the ammonium record
    * range: [String](types/String.md)
 * [ammoniumNRepNum](ammoniumNRepNum.md)  <sub>OPT</sub>
    * Description: Analytical replicate number for ammonium sample
    * range: [String](types/String.md)
 * [ammoniumNReviewedBy](ammoniumNReviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed ammonium N data prior to submission
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [kclAmmoniumNConc](kclAmmoniumNConc.md)  <sub>OPT</sub>
    * Description: Concentration of ammonium N in a potassium chloride extract
    * range: [Double](types/Double.md)
 * [kclNitrateNitriteNConc](kclNitrateNitriteNConc.md)  <sub>OPT</sub>
    * Description: Concentration of nitrate + nitrite N in a potassium chloride extract
    * range: [Double](types/Double.md)
 * [kclSampleCode](kclSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a potassium chloride (KCl) extract sample
    * range: [String](types/String.md)
 * [kclSampleID](kclSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a potassium chloride (KCl) extract sample
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [nitrateNitriteNAnalysisDate](nitrateNitriteNAnalysisDate.md)  <sub>OPT</sub>
    * Description: Date a nitrate + nitrite N sample was analyzed
    * range: [Time](types/Time.md)
 * [nitrateNitriteNAnalyzedBy](nitrateNitriteNAnalyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample for nitrate + nitrite N
    * range: [String](types/String.md)
 * [nitrateNitriteNInstrument](nitrateNitriteNInstrument.md)  <sub>OPT</sub>
    * Description: Type of instrument used for nitrate + nitrite N analysis
    * range: [String](types/String.md)
 * [nitrateNitriteNMethod](nitrateNitriteNMethod.md)  <sub>OPT</sub>
    * Description: Method used to test sample for nitrate + nitrite N concentration
    * range: [String](types/String.md)
 * [nitrateNitriteNQF](nitrateNitriteNQF.md)  <sub>OPT</sub>
    * Description: Quality flag for nitrate + nitrite N values
    * range: [String](types/String.md)
 * [nitrateNitriteNRemarks](nitrateNitriteNRemarks.md)  <sub>OPT</sub>
    * Description: Free text comments accompanying the nitrate + nitrite N record
    * range: [String](types/String.md)
 * [nitrateNitriteNRepNum](nitrateNitriteNRepNum.md)  <sub>OPT</sub>
    * Description: Analytical replicate number for nitrate + nitrite N sample
    * range: [String](types/String.md)
 * [nitrateNitriteNReviewedBy](nitrateNitriteNReviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed nitrite + nitrate N data prior to submission
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [receivedCondition](receivedCondition.md)  <sub>OPT</sub>
    * Description: Condition of the sample on the date it was received
    * range: [String](types/String.md)
 * [receivedDate](receivedDate.md)  <sub>OPT</sub>
    * Description: Date a sample was received
    * range: [Time](types/Time.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:ntr_externalLab_pub |

