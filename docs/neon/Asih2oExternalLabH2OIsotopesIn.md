
# Type: asih2o_externalLabH2OIsotopes_in




URI: [neon:Asih2oExternalLabH2OIsotopesIn](https://data.neonscience.org/Asih2oExternalLabH2OIsotopesIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Asih2oExternalLabH2OIsotopesIn&#124;uid:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;laboratoryName:string%20%3F;receivedBy:string%20%3F;shipmentID:string%20%3F;externalRemarks:string%20%3F;receivedDate:time%20%3F;locationID:string%20%3F;analysisDate:time%20%3F;analyzedBy:string%20%3F;d18OWater:double%20%3F;d2HWater:double%20%3F;isotopeH2OSampleID:string%20%3F;isotopeH2OSampleFate:string%20%3F;isotopeH2OSampleCode:string%20%3F;d18OsdWater:double%20%3F;d2HsdWater:double%20%3F;instrumentSN:string%20%3F;isotopeH2OExternalLabQF:string%20%3F;sampleCondition:string%20%3F;externalLabDataQF:string%20%3F;isotopeH2OExternalLabTest:string%20%3F])

## Attributes


### Own

 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [d18OWater](d18OWater.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 18O:16O in H2O, relative to the Vienna Standard Mean Ocean Water
    * range: [Double](types/Double.md)
 * [d18OsdWater](d18OsdWater.md)  <sub>OPT</sub>
    * Description: Standard deviation of d18O of replicate H2O samples
    * range: [Double](types/Double.md)
 * [d2HWater](d2HWater.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 2H:1H in H2O, relative to the Vienna Standard Mean Ocean Water
    * range: [Double](types/Double.md)
 * [d2HsdWater](d2HsdWater.md)  <sub>OPT</sub>
    * Description: Standard deviation of d2H of replicate H2O samples
    * range: [Double](types/Double.md)
 * [externalLabDataQF](externalLabDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for external lab data
    * range: [String](types/String.md)
 * [externalRemarks](externalRemarks.md)  <sub>OPT</sub>
    * Description: External lab notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [instrumentSN](instrumentSN.md)  <sub>OPT</sub>
    * Description: Serial number of instrument used to analyze sample
    * range: [String](types/String.md)
 * [isotopeH2OExternalLabQF](isotopeH2OExternalLabQF.md)  <sub>OPT</sub>
    * Description: Quality flag for samples with high standard deviation (del2Hsd >=0.75 or del18Osd>=0.2) of H2O isotope samples. High standard deviations are flagged with a 1, else flag set to 0
    * range: [String](types/String.md)
 * [isotopeH2OExternalLabTest](isotopeH2OExternalLabTest.md)  <sub>OPT</sub>
    * Description: Test to ensure that either 18O or 2H isotope data is returned
    * range: [String](types/String.md)
 * [isotopeH2OSampleCode](isotopeH2OSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of the water stable isotope sample
    * range: [String](types/String.md)
 * [isotopeH2OSampleFate](isotopeH2OSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of the water stable isotope sample
    * range: [String](types/String.md)
 * [isotopeH2OSampleID](isotopeH2OSampleID.md)  <sub>OPT</sub>
    * Description: Identifier of sample for 2H:1H and 18O:16O water stable isotope sample
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [receivedBy](receivedBy.md)  <sub>OPT</sub>
    * Description: Anonymized name of lab personnel receiving the shipment
    * range: [String](types/String.md)
 * [receivedDate](receivedDate.md)  <sub>OPT</sub>
    * Description: Date a sample was received
    * range: [Time](types/Time.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [shipmentID](shipmentID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with shipment
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
| **Mappings:** | | neon:asih2o_externalLabH2OIsotopes_in |
| **In Subsets:** | | DP0.20205.001 |

