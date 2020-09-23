
# Type: hbp_perbout_in




URI: [neon:HbpPerboutIn](https://data.neonscience.org/HbpPerboutIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[HbpPerboutIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;enteredBy:string%20%3F;boutNumber:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;targetTaxaPresent:string%20%3F;subplotID:string%20%3F;clipID:string%20%3F;exclosure:string%20%3F;bagCount:string%20%3F;clipCellNumber:string%20%3F;samplingProtocolVersion:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;hbpType:string%20%3F;subsamplesCreated:string%20%3F;clipArea:double%20%3F;clipLength:double%20%3F;clipWidth:double%20%3F])

## Attributes


### Own

 * [bagCount](bagCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of sample bags transported from the field to the laboratory for processing
    * range: [String](types/String.md)
 * [boutNumber](boutNumber.md)  <sub>OPT</sub>
    * Description: Number of the sampling bout within a calendar year, beginning with 1
    * range: [String](types/String.md)
 * [clipArea](clipArea.md)  <sub>OPT</sub>
    * Description: Total area sampled within the selected clipID
    * range: [Double](types/Double.md)
 * [clipCellNumber](clipCellNumber.md)  <sub>OPT</sub>
    * Description: A numeric identifier for the clip-harvest cell in which herbaceous biomass was sampled
    * range: [String](types/String.md)
 * [clipID](clipID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the clip-harvest location within the plot
    * range: [String](types/String.md)
 * [clipLength](clipLength.md)  <sub>OPT</sub>
    * Description: The length of the clip-harvest area in meters
    * range: [Double](types/Double.md)
 * [clipWidth](clipWidth.md)  <sub>OPT</sub>
    * Description: The width of the clip-harvest area in meters
    * range: [Double](types/Double.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [enteredBy](enteredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who entered the data
    * range: [String](types/String.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [exclosure](exclosure.md)  <sub>OPT</sub>
    * Description: Identifies whether clip harvest took place in an area protected by a grazing exclosure
    * range: [String](types/String.md)
 * [hbpType](hbpType.md)  <sub>OPT</sub>
    * Description: Indicator of whether sample is collected from a cropped agricultural or non-agricultural site
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [subplotID](subplotID.md)  <sub>OPT</sub>
    * Description: Identifier for the NEON subplot
    * range: [String](types/String.md)
 * [subsamplesCreated](subsamplesCreated.md)  <sub>OPT</sub>
    * Description: Indicator of whether sampleID was divided into subsamples
    * range: [String](types/String.md)
 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:hbp_perbout_in |
| **In Subsets:** | | DP0.10005.001 |

