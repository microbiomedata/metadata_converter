
# Type: cfc_chlorophyllBatchQA_in




URI: [neon:CfcChlorophyllBatchQAIn](https://data.neonscience.org/CfcChlorophyllBatchQAIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[CfcChlorophyllBatchQAIn&#124;uid:string%20%3F;remarks:string%20%3F;laboratoryName:string%20%3F;testMethod:string%20%3F;analysisDate:time%20%3F;analyzedBy:string%20%3F;dataQF:string%20%3F;qaReferenceID:string%20%3F;analysisEndDate:time%20%3F;reviewedBy:string%20%3F;analyticalRepNumber:string%20%3F;runID:string%20%3F;qaQF:string%20%3F;extractCarotConc:double%20%3F;extractChlAConc:double%20%3F;extractChlBConc:double%20%3F;standardChlAConc:double%20%3F])

## Attributes


### Own

 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
 * [analysisEndDate](analysisEndDate.md)  <sub>OPT</sub>
    * Description: The end date or dateTime of analysis
    * range: [Time](types/Time.md)
 * [analyticalRepNumber](analyticalRepNumber.md)  <sub>OPT</sub>
    * Description: Number of the analytical replicate
    * range: [String](types/String.md)
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [extractCarotConc](extractCarotConc.md)  <sub>OPT</sub>
    * Description: Calculated total carotenoid concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
 * [extractChlAConc](extractChlAConc.md)  <sub>OPT</sub>
    * Description: Calculated chlorophyll A concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
 * [extractChlBConc](extractChlBConc.md)  <sub>OPT</sub>
    * Description: Calculated chlorophyll B concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [qaQF](qaQF.md)  <sub>OPT</sub>
    * Description: Quality flag for quality control sample
    * range: [String](types/String.md)
 * [qaReferenceID](qaReferenceID.md)  <sub>OPT</sub>
    * Description: Identifier for quality assurance reference material or standard
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [reviewedBy](reviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed the data prior to submission
    * range: [String](types/String.md)
 * [runID](runID.md)  <sub>OPT</sub>
    * Description: A linking value provided by the external lab that associates the sample data to the run metadata, including QA values
    * range: [String](types/String.md)
 * [standardChlAConc](standardChlAConc.md)  <sub>OPT</sub>
    * Description: Known chlorophyll A concentration in a standard
    * range: [Double](types/Double.md)
 * [testMethod](testMethod.md)  <sub>OPT</sub>
    * Description: Method used to conduct test
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:cfc_chlorophyllBatchQA_in |

