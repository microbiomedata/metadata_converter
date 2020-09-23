
# Type: asih2o_externalLabQAQCDataH2O_in




URI: [neon:Asih2oExternalLabQAQCDataH2OIn](https://data.neonscience.org/Asih2oExternalLabQAQCDataH2OIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Asih2oExternalLabQAQCDataH2OIn&#124;uid:string%20%3F;startDate:time%20%3F;laboratoryName:string%20%3F;analysisDate:time%20%3F;d18OsdWater:double%20%3F;d2HsdWater:double%20%3F;instrumentSN:string%20%3F;H2OIsotopeQAQCID:string%20%3F;d18OMeasured:double%20%3F;d2HMeasured:double%20%3F;d18OKnown:double%20%3F;d2HKnown:double%20%3F;subsamplesProcessed:string%20%3F;isotopeH2OexternalLabQAQCFlag:string%20%3F;labSampleID:string%20%3F;externalLabDataQF:string%20%3F])

## Attributes


### Own

 * [H2OIsotopeQAQCID](H2OIsotopeQAQCID.md)  <sub>OPT</sub>
    * Description: ID indicating function of standard. PLRM-1 and PLRM-2 are used to calibrate values. SLRM is used to check calibration and to generate drift corrections
    * range: [String](types/String.md)
 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
 * [d18OKnown](d18OKnown.md)  <sub>OPT</sub>
    * Description: Known value of the ratio of stable isotopes 18O:16O, relative to the standard Vienna Standard Mean Ocean Water (VSMOW)
    * range: [Double](types/Double.md)
 * [d18OMeasured](d18OMeasured.md)  <sub>OPT</sub>
    * Description: Corrected measure of the ratio of stable isotopes 18O:16O, relative to the standard Vienna Standard Mean Ocean Water (VSMOW)
    * range: [Double](types/Double.md)
 * [d18OsdWater](d18OsdWater.md)  <sub>OPT</sub>
    * Description: Standard deviation of d18O of replicate H2O samples
    * range: [Double](types/Double.md)
 * [d2HKnown](d2HKnown.md)  <sub>OPT</sub>
    * Description: Known value of the ratio of stable isotopes 2H:1H, relative to the standard Vienna Standard Mean Ocean Water (VSMOW)
    * range: [Double](types/Double.md)
 * [d2HMeasured](d2HMeasured.md)  <sub>OPT</sub>
    * Description: Corrected measure of the ratio of stable isotopes 2H:1H, relative to the standard Vienna Standard Mean Ocean Water (VSMOW)
    * range: [Double](types/Double.md)
 * [d2HsdWater](d2HsdWater.md)  <sub>OPT</sub>
    * Description: Standard deviation of d2H of replicate H2O samples
    * range: [Double](types/Double.md)
 * [externalLabDataQF](externalLabDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for external lab data
    * range: [String](types/String.md)
 * [instrumentSN](instrumentSN.md)  <sub>OPT</sub>
    * Description: Serial number of instrument used to analyze sample
    * range: [String](types/String.md)
 * [isotopeH2OexternalLabQAQCFlag](isotopeH2OexternalLabQAQCFlag.md)  <sub>OPT</sub>
    * Description: Quality flag for secondary laboratory reference materials with high SD (d2Hsd >=0.5 or d18Osd >=0.1) or with d18O or d2H values outside the acceptable range for the known values (d18O +/- 0.13 per mill or d2H +/- 1.1). High SD are flagged with a 1
    * range: [String](types/String.md)
 * [labSampleID](labSampleID.md)  <sub>OPT</sub>
    * Description: Identifier of laboratory-specific samples analyzed at external lab facility
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [subsamplesProcessed](subsamplesProcessed.md)  <sub>OPT</sub>
    * Description: Number of subsamples processed of each standard
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:asih2o_externalLabQAQCDataH2O_in |

