
# Type: vst_perplotperyear_in




URI: [neon:VstPerplotperyearIn](https://data.neonscience.org/VstPerplotperyearIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VstPerplotperyearIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;targetTaxaPresent:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;dataQF:string%20%3F;samplingImpractical:string%20%3F;yearBoutBegan:integer%20%3F;cactiAbsentList:string%20%3F;cactiPresent:string%20%3F;fernsAbsentList:string%20%3F;fernsPresent:string%20%3F;lianasAbsentList:string%20%3F;lianasPresent:string%20%3F;nestedSubplotAreaLiana:string%20%3F;nestedSubplotAreaOther:string%20%3F;nestedSubplotAreaShrubSapling:string%20%3F;ocotillosAbsentList:string%20%3F;ocotillosPresent:string%20%3F;palmsAbsentList:string%20%3F;palmsPresent:string%20%3F;shrubsAbsentList:string%20%3F;shrubsPresent:string%20%3F;totalSampledAreaLiana:double%20%3F;totalSampledAreaOther:double%20%3F;totalSampledAreaShrubSapling:double%20%3F;totalSampledAreaTrees:double%20%3F;treesAbsentList:string%20%3F;treesPresent:string%20%3F;xerophyllumAbsentList:string%20%3F;xerophyllumPresent:string%20%3F;yuccasAbsentList:string%20%3F;yuccasPresent:string%20%3F;eventType:string%20%3F;dataCollected:string%20%3F])

## Attributes


### Own

 * [cactiAbsentList](cactiAbsentList.md)  <sub>OPT</sub>
    * Description: List of subplots or nested subplots in which cacti are not present
    * range: [String](types/String.md)
 * [cactiPresent](cactiPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the plot contains cacti
    * range: [String](types/String.md)
 * [dataCollected](dataCollected.md)  <sub>OPT</sub>
    * Description: Specific measurements made in a given event
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
 * [eventType](eventType.md)  <sub>OPT</sub>
    * Description: Classification of information associated with the event type
    * range: [String](types/String.md)
 * [fernsAbsentList](fernsAbsentList.md)  <sub>OPT</sub>
    * Description: List of subplots or nested subplots in which ferns are not present
    * range: [String](types/String.md)
 * [fernsPresent](fernsPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the plot contains ferns
    * range: [String](types/String.md)
 * [lianasAbsentList](lianasAbsentList.md)  <sub>OPT</sub>
    * Description: List of subplots or nested subplots in which lianas are not present
    * range: [String](types/String.md)
 * [lianasPresent](lianasPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the plot contains lianas
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [nestedSubplotAreaLiana](nestedSubplotAreaLiana.md)  <sub>OPT</sub>
    * Description: Size of nested plot in which lianas were measured
    * range: [String](types/String.md)
 * [nestedSubplotAreaOther](nestedSubplotAreaOther.md)  <sub>OPT</sub>
    * Description: Size of nested plot in which other qualifying growthForms were measured
    * range: [String](types/String.md)
 * [nestedSubplotAreaShrubSapling](nestedSubplotAreaShrubSapling.md)  <sub>OPT</sub>
    * Description: Size of nested plot in which shrubs, saplings and small trees were measured
    * range: [String](types/String.md)
 * [ocotillosAbsentList](ocotillosAbsentList.md)  <sub>OPT</sub>
    * Description: List of subplots or nested subplots in which ocotillos are not present
    * range: [String](types/String.md)
 * [ocotillosPresent](ocotillosPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the plot contains ocotillo
    * range: [String](types/String.md)
 * [palmsAbsentList](palmsAbsentList.md)  <sub>OPT</sub>
    * Description: List of subplots or nested subplots in which palm are not present
    * range: [String](types/String.md)
 * [palmsPresent](palmsPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the plot contains palms of any size
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
 * [samplingImpractical](samplingImpractical.md)  <sub>OPT</sub>
    * Description: Samples and/or measurements were not collected due to the indicated circumstance
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [shrubsAbsentList](shrubsAbsentList.md)  <sub>OPT</sub>
    * Description: List of subplots or nested subplots in which shrubs, saplings and small trees are not present
    * range: [String](types/String.md)
 * [shrubsPresent](shrubsPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the plot contains shrubs, saplings, or small trees
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [totalSampledAreaLiana](totalSampledAreaLiana.md)  <sub>OPT</sub>
    * Description: Total plot area sampled for liana
    * range: [Double](types/Double.md)
 * [totalSampledAreaOther](totalSampledAreaOther.md)  <sub>OPT</sub>
    * Description: Total plot area sampled for qualifying non-woody growth forms
    * range: [Double](types/Double.md)
 * [totalSampledAreaShrubSapling](totalSampledAreaShrubSapling.md)  <sub>OPT</sub>
    * Description: Total plot area sampled for saplings, shrubs, and small trees
    * range: [Double](types/Double.md)
 * [totalSampledAreaTrees](totalSampledAreaTrees.md)  <sub>OPT</sub>
    * Description: Total plot area sampled for single and multi-bole trees
    * range: [Double](types/Double.md)
 * [treesAbsentList](treesAbsentList.md)  <sub>OPT</sub>
    * Description: List of subplots in which trees are not present
    * range: [String](types/String.md)
 * [treesPresent](treesPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the plot contains trees of any size
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [xerophyllumAbsentList](xerophyllumAbsentList.md)  <sub>OPT</sub>
    * Description: List of subplots or nested subplots in which xerophyllum are not present
    * range: [String](types/String.md)
 * [xerophyllumPresent](xerophyllumPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the plot contains xerophyllum
    * range: [String](types/String.md)
 * [yearBoutBegan](yearBoutBegan.md)  <sub>OPT</sub>
    * Description: The calendar year that the bout began
    * range: [Integer](types/Integer.md)
 * [yuccasAbsentList](yuccasAbsentList.md)  <sub>OPT</sub>
    * Description: List of subplots or nested subplots in which yuccas are not present
    * range: [String](types/String.md)
 * [yuccasPresent](yuccasPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the plot contains yucca or yucca-like growth forms
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:vst_perplotperyear_in |
| **In Subsets:** | | DP0.10098.001 |

