
# Type: asp_externalLabData_pub




URI: [neon:AspExternalLabDataPub](https://data.neonscience.org/AspExternalLabDataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AspExternalLabDataPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;sampleID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;analyte:string%20%3F;method:string%20%3F;methodDetectionLimit:double%20%3F;analyteUnits:string%20%3F;receivedDate:time%20%3F;analysisDate:time%20%3F;analyzedBy:string%20%3F;primaryMatrix:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;sampleCondition:string%20%3F;namedLocation:string%20%3F;analyticalRepNumber:string%20%3F;analyteConcentration:double%20%3F;analyteSurrogate:string%20%3F;cas:string%20%3F;deptName:string%20%3F;extendedQualifier1:string%20%3F;extendedQualifier2:string%20%3F;extendedQualifier3:string%20%3F;extendedQualifier4:string%20%3F;extendedQualifier5:string%20%3F;externalQualifier:string%20%3F;practicalQuantitationLimit:double%20%3F])

## Attributes


### Own

 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
 * [analyte](analyte.md)  <sub>OPT</sub>
    * Description: Analyte or parameter measured
    * range: [String](types/String.md)
 * [analyteConcentration](analyteConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of analyte
    * range: [Double](types/Double.md)
 * [analyteSurrogate](analyteSurrogate.md)  <sub>OPT</sub>
    * Description: Indicator for whether an analyte is a surrogate
    * range: [String](types/String.md)
 * [analyteUnits](analyteUnits.md)  <sub>OPT</sub>
    * Description: Associated units of measure for analyte
    * range: [String](types/String.md)
 * [analyticalRepNumber](analyticalRepNumber.md)  <sub>OPT</sub>
    * Description: Number of the analytical replicate
    * range: [String](types/String.md)
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
 * [cas](cas.md)  <sub>OPT</sub>
    * Description: Chemical Abstracts Service registry number
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [deptName](deptName.md)  <sub>OPT</sub>
    * Description: External lab department
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [extendedQualifier1](extendedQualifier1.md)  <sub>OPT</sub>
    * Description: First extended data qualifier returned for the sample and analyte
    * range: [String](types/String.md)
 * [extendedQualifier2](extendedQualifier2.md)  <sub>OPT</sub>
    * Description: Second extended data qualifier returned for the sample and analyte
    * range: [String](types/String.md)
 * [extendedQualifier3](extendedQualifier3.md)  <sub>OPT</sub>
    * Description: Third extended data qualifier returned for the sample and analyte
    * range: [String](types/String.md)
 * [extendedQualifier4](extendedQualifier4.md)  <sub>OPT</sub>
    * Description: Fourth extended data qualifier returned for the sample and analyte
    * range: [String](types/String.md)
 * [extendedQualifier5](extendedQualifier5.md)  <sub>OPT</sub>
    * Description: Fifth extended data qualifier returned for the sample and analyte
    * range: [String](types/String.md)
 * [externalQualifier](externalQualifier.md)  <sub>OPT</sub>
    * Description: A data qualifier returned by an external laboratory
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [method](method.md)  <sub>OPT</sub>
    * Description: Published method used for analysis
    * range: [String](types/String.md)
 * [methodDetectionLimit](methodDetectionLimit.md)  <sub>OPT</sub>
    * Description: Detection limit for method used
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [practicalQuantitationLimit](practicalQuantitationLimit.md)  <sub>OPT</sub>
    * Description: Practical Quantitation Limit.  Synonymous with the EPA term: minimum level
    * range: [Double](types/Double.md)
 * [primaryMatrix](primaryMatrix.md)  <sub>OPT</sub>
    * Description: Primary material in the sample
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
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:asp_externalLabData_pub |

