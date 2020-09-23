
# Type: sim_eventData_in




URI: [neon:SimEventDataIn](https://data.neonscience.org/SimEventDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SimEventDataIn&#124;uid:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;scientificName:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;locationID:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;biomassRemoval:string%20%3F;eventType:string%20%3F;fireSeverity:string%20%3F;maxQuantity:double%20%3F;maxStartDate:time%20%3F;methodTypeChoice:string%20%3F;minEndDate:time%20%3F;minQuantity:double%20%3F;name:string%20%3F;otherScientificName:string%20%3F;quantityUnit:string%20%3F;reporterType:string%20%3F])

## Attributes


### Own

 * [biomassRemoval](biomassRemoval.md)  <sub>OPT</sub>
    * Description: Indicates whether or not biomass was removed for plant reduction
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
 * [fireSeverity](fireSeverity.md)  <sub>OPT</sub>
    * Description: Fire severity classification
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [maxQuantity](maxQuantity.md)  <sub>OPT</sub>
    * Description: The maximum quantity of the event measured
    * range: [Double](types/Double.md)
 * [maxStartDate](maxStartDate.md)  <sub>OPT</sub>
    * Description: The maximum start date range entered by the technician when the exact start date is unknown
    * range: [Time](types/Time.md)
 * [methodTypeChoice](methodTypeChoice.md)  <sub>OPT</sub>
    * Description: Category information for the method or type choice associated with the event type
    * range: [String](types/String.md)
 * [minEndDate](minEndDate.md)  <sub>OPT</sub>
    * Description: The earliest end date range entered by the technician when the exact end date is unknown
    * range: [Time](types/Time.md)
 * [minQuantity](minQuantity.md)  <sub>OPT</sub>
    * Description: The minimum quantity of the event measured 
    * range: [Double](types/Double.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: Person name or common name associated with an ownership change or chemical application event type
    * range: [String](types/String.md)
 * [otherScientificName](otherScientificName.md)  <sub>OPT</sub>
    * Description: Other scientific name, not included in the NEON constrained taxon tables. This is the name of the lowest level taxonomic rank that can be determined
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [quantityUnit](quantityUnit.md)  <sub>OPT</sub>
    * Description: The unit that corresponds to the quantity measurement
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [reporterType](reporterType.md)  <sub>OPT</sub>
    * Description: Indicates source of observation reporting; 'primary' for NEON team member observed and 'secondary' for non-NEON individuals observed
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
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
| **Mappings:** | | neon:sim_eventData_in |
| **In Subsets:** | | DP0.10111.001 |

