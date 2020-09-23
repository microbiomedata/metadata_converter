
# Type: ltr_fielddata_in




URI: [neon:LtrFielddataIn](https://data.neonscience.org/LtrFielddataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[LtrFielddataIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;trapID:string%20%3F;boutNumber:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;samplingProtocolVersion:string%20%3F;dataQF:string%20%3F;trapCondition:string%20%3F;fieldSampleBarcode:string%20%3F;fieldSampleFate:string%20%3F;fieldSampleID:string%20%3F;yearBoutBegan:integer%20%3F;trappingDays:double%20%3F;toxicodendronPossible:string%20%3F])

## Attributes


### Own

 * [boutNumber](boutNumber.md)  <sub>OPT</sub>
    * Description: Number of the sampling bout within a calendar year, beginning with 1
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fieldSampleBarcode](fieldSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of a field sample
    * range: [String](types/String.md)
 * [fieldSampleFate](fieldSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a field sample
    * range: [String](types/String.md)
 * [fieldSampleID](fieldSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for a field sample
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
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [toxicodendronPossible](toxicodendronPossible.md)  <sub>OPT</sub>
    * Description: Indicator for whether a sample may contain Toxicodendron spp
    * range: [String](types/String.md)
 * [trapCondition](trapCondition.md)  <sub>OPT</sub>
    * Description: Condition of litter trap and indication of whether litter was collected
    * range: [String](types/String.md)
 * [trapID](trapID.md)  <sub>OPT</sub>
    * Description: Identifier for trap
    * range: [String](types/String.md)
 * [trappingDays](trappingDays.md)  <sub>OPT</sub>
    * Description: Decimal days between trap setting and collecting events
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [yearBoutBegan](yearBoutBegan.md)  <sub>OPT</sub>
    * Description: The calendar year that the bout began
    * range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:ltr_fielddata_in |
| **In Subsets:** | | DP0.10033.001 |

