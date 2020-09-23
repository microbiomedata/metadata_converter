
# Type: swc_domainLabData_in




URI: [neon:SwcDomainLabDataIn](https://data.neonscience.org/SwcDomainLabDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SwcDomainLabDataIn&#124;uid:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;collectDate:time%20%3F;sampleType:string%20%3F;stationID:string%20%3F;titrationLocation:string%20%3F;pH4CheckValue:double%20%3F;pH7CheckValue:double%20%3F;pHMeterCalibration:string%20%3F;initialSamplepH:double%20%3F;initialSampleTemp:double%20%3F;normality:string%20%3F;sampleVolume:double%20%3F;methodType:string%20%3F;titrationDate:time%20%3F;startDate:time%20%3F;alkMeqPerL:double%20%3F;alkMgPerL:double%20%3F;ancMeqPerL:double%20%3F;ancMgPerL:double%20%3F;domainSampleID:string%20%3F;parentSampleID:string%20%3F;dataQF:string%20%3F;parentSampleFate:string%20%3F;parentSampleCode:string%20%3F;domainSampleCode:string%20%3F;titrationDataString:string%20%3F;domainSampleFate:string%20%3F])

## Attributes


### Own

 * [alkMeqPerL](alkMeqPerL.md)  <sub>OPT</sub>
    * Description: alkalinity titration result in milliequivalents per Liter
    * range: [Double](types/Double.md)
 * [alkMgPerL](alkMgPerL.md)  <sub>OPT</sub>
    * Description: alkalinity titration result in milligrams of Calcium Carbonate per Liter
    * range: [Double](types/Double.md)
 * [ancMeqPerL](ancMeqPerL.md)  <sub>OPT</sub>
    * Description: acid neutralizing capacity titration result in milliequivalents per Liter
    * range: [Double](types/Double.md)
 * [ancMgPerL](ancMgPerL.md)  <sub>OPT</sub>
    * Description: acid neutralizing capacity titration result in milligrams of Calcium Carbonate per Liter
    * range: [Double](types/Double.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainSampleCode](domainSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of the domain lab sample
    * range: [String](types/String.md)
 * [domainSampleFate](domainSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of the domain lab sample
    * range: [String](types/String.md)
 * [domainSampleID](domainSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample from domain lab
    * range: [String](types/String.md)
 * [initialSampleTemp](initialSampleTemp.md)  <sub>OPT</sub>
    * Description: Temperature at start of titration
    * range: [Double](types/Double.md)
 * [initialSamplepH](initialSamplepH.md)  <sub>OPT</sub>
    * Description: pH at start of titration
    * range: [Double](types/Double.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [methodType](methodType.md)  <sub>OPT</sub>
    * Description: Method of titration used
    * range: [String](types/String.md)
 * [normality](normality.md)  <sub>OPT</sub>
    * Description: Titrant normality used
    * range: [String](types/String.md)
 * [pH4CheckValue](pH4CheckValue.md)  <sub>OPT</sub>
    * Description: pH meter reading during pH 4 check
    * range: [Double](types/Double.md)
 * [pH7CheckValue](pH7CheckValue.md)  <sub>OPT</sub>
    * Description: pH meter reading during pH 7 check
    * range: [Double](types/Double.md)
 * [pHMeterCalibration](pHMeterCalibration.md)  <sub>OPT</sub>
    * Description: Was pH meter recalibrated?
    * range: [String](types/String.md)
 * [parentSampleCode](parentSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a parent sample
    * range: [String](types/String.md)
 * [parentSampleFate](parentSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a parent sample
    * range: [String](types/String.md)
 * [parentSampleID](parentSampleID.md)  <sub>OPT</sub>
    * Description: Parent sampleID of sample being processed
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleType](sampleType.md)  <sub>OPT</sub>
    * Description: Type of sample
    * range: [String](types/String.md)
 * [sampleVolume](sampleVolume.md)  <sub>OPT</sub>
    * Description: Sample volume in milliliters
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [titrationDataString](titrationDataString.md)  <sub>OPT</sub>
    * Description: x,y pairs of pH and Counter Reading on digital titrator concatenated into a string
    * range: [String](types/String.md)
 * [titrationDate](titrationDate.md)  <sub>OPT</sub>
    * Description: Date and time of titration
    * range: [Time](types/Time.md)
 * [titrationLocation](titrationLocation.md)  <sub>OPT</sub>
    * Description: Location where sample titration was completed
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:swc_domainLabData_in |

