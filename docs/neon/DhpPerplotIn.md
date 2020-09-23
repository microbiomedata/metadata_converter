
# Type: dhp_perplot_in




URI: [neon:DhpPerplotIn](https://data.neonscience.org/DhpPerplotIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DhpPerplotIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;boutNumber:string%20%3F;sampleID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;overstoryHeight:double%20%3F;understoryHeight:double%20%3F;yearBoutBegan:integer%20%3F;snowPresent:string%20%3F])

## Attributes


### Own

 * [boutNumber](boutNumber.md)  <sub>OPT</sub>
    * Description: Number of the sampling bout within a calendar year, beginning with 1
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [overstoryHeight](overstoryHeight.md)  <sub>OPT</sub>
    * Description: Average height of the overstory vegetation in a plot, assessed by visual survey to guide LAI photo collection
    * range: [Double](types/Double.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
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
 * [snowPresent](snowPresent.md)  <sub>OPT</sub>
    * Description: Categorical indicator of whether snow is present within the plot or sampling area
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [understoryHeight](understoryHeight.md)  <sub>OPT</sub>
    * Description: Average height of the understory vegetation in a plot, assessed by visual survey to guide LAI photo collection
    * range: [Double](types/Double.md)
 * [yearBoutBegan](yearBoutBegan.md)  <sub>OPT</sub>
    * Description: The calendar year that the bout began
    * range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:dhp_perplot_in |
| **In Subsets:** | | DP0.10017.001 |

