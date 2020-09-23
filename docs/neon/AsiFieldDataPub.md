
# Type: asi_fieldData_pub




URI: [neon:AsiFieldDataPub](https://data.neonscience.org/AsiFieldDataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AsiFieldDataPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;parentSampleID:string%20%3F;processedDateH2OIsotopes:time%20%3F;processedDateFilters:time%20%3F;sampleVolumeFilteredPOMRep1:double%20%3F;sampleVolumeFilteredPOMRep2:double%20%3F;isotopeH2OSampleID:string%20%3F;isotopePOMSampleID:string%20%3F;isotopePOMRep2SampleID:string%20%3F;isotopeH2OSampleCode:string%20%3F;isotopePOMRep2SampleCode:string%20%3F;isotopePOMSampleCode:string%20%3F;parentSampleCode:string%20%3F;fieldDataQF:string%20%3F;namedLocation:string%20%3F;isotopeH2OSampleCond:string%20%3F;isotopePOMSampleCond:string%20%3F;isotopePOMRep2SampleCond:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [fieldDataQF](fieldDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for field data
    * range: [String](types/String.md)
 * [isotopeH2OSampleCode](isotopeH2OSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of the water stable isotope sample
    * range: [String](types/String.md)
 * [isotopeH2OSampleCond](isotopeH2OSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of a sample for 2H:1H and 18O:16O water stable isotope sample
    * range: [String](types/String.md)
 * [isotopeH2OSampleID](isotopeH2OSampleID.md)  <sub>OPT</sub>
    * Description: Identifier of sample for 2H:1H and 18O:16O water stable isotope sample
    * range: [String](types/String.md)
 * [isotopePOMRep2SampleCode](isotopePOMRep2SampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of the particulate organic matter (POM) stable isotope sample, replicate 2
    * range: [String](types/String.md)
 * [isotopePOMRep2SampleCond](isotopePOMRep2SampleCond.md)  <sub>OPT</sub>
    * Description: Condition of a sample for 13C:12C and 15N:14N particulate organic matter (POM) stable isotope sample for replicate 2
    * range: [String](types/String.md)
 * [isotopePOMRep2SampleID](isotopePOMRep2SampleID.md)  <sub>OPT</sub>
    * Description: Identifier of sample for 13C:12C and 15N:14N particulate organic matter (POM) stable isotope sample for replicate 2
    * range: [String](types/String.md)
 * [isotopePOMSampleCode](isotopePOMSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of the particulate organic matter (POM) stable isotope sample
    * range: [String](types/String.md)
 * [isotopePOMSampleCond](isotopePOMSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of a sample for 13C:12C and 15N:14N particulate organic matter (POM) stable isotope sample
    * range: [String](types/String.md)
 * [isotopePOMSampleID](isotopePOMSampleID.md)  <sub>OPT</sub>
    * Description: Identifier of sample for 13C:12C and 15N:14N particulate organic matter (POM) stable isotope sample
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [parentSampleCode](parentSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a parent sample
    * range: [String](types/String.md)
 * [parentSampleID](parentSampleID.md)  <sub>OPT</sub>
    * Description: Parent sampleID of sample being processed
    * range: [String](types/String.md)
 * [processedDateFilters](processedDateFilters.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event of filtered samples
    * range: [Time](types/Time.md)
 * [processedDateH2OIsotopes](processedDateH2OIsotopes.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event of H2O isotope sample
    * range: [Time](types/Time.md)
 * [sampleVolumeFilteredPOMRep1](sampleVolumeFilteredPOMRep1.md)  <sub>OPT</sub>
    * Description: Volume of water filtered through the filter for particulate organic matter (POM) replicate 1 for isotope external analysis
    * range: [Double](types/Double.md)
 * [sampleVolumeFilteredPOMRep2](sampleVolumeFilteredPOMRep2.md)  <sub>OPT</sub>
    * Description: Volume of water filtered through the filter for particulate organic matter (POM) replicate 2 for isotope external analysis
    * range: [Double](types/Double.md)
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
| **Mappings:** | | neon:asi_fieldData_pub |

