
# Type: dpm_fieldData_in




URI: [neon:DpmFieldDataIn](https://data.neonscience.org/DpmFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DpmFieldDataIn&#124;uid:string%20%3F;remarks:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;aCollectedBy:string%20%3F;bCollectedBy:string%20%3F;locationID:string%20%3F;aSetBy:string%20%3F;bSetBy:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;fieldFilterCondition:string%20%3F;fieldFilterConditionRemarks:string%20%3F;fieldFilterDamage:string%20%3F;fieldFilterDamageRemarks:string%20%3F;filterID:string%20%3F;filterWet:double%20%3F;equipCondition:string%20%3F;equipConditionDesc:string%20%3F;filterCode:string%20%3F])

## Attributes


### Own

 * [aCollectedBy](aCollectedBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [aSetBy](aSetBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who set the collector
    * range: [String](types/String.md)
 * [bCollectedBy](bCollectedBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [bSetBy](bSetBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who set the collector
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [equipCondition](equipCondition.md)  <sub>OPT</sub>
    * Description: Condition of the equipment
    * range: [String](types/String.md)
 * [equipConditionDesc](equipConditionDesc.md)  <sub>OPT</sub>
    * Description: Description of problems with the equipment
    * range: [String](types/String.md)
 * [fieldFilterCondition](fieldFilterCondition.md)  <sub>OPT</sub>
    * Description: Condition of the filter reported in the field
    * range: [String](types/String.md)
 * [fieldFilterConditionRemarks](fieldFilterConditionRemarks.md)  <sub>OPT</sub>
    * Description: Additional description of the field filter condition
    * range: [String](types/String.md)
 * [fieldFilterDamage](fieldFilterDamage.md)  <sub>OPT</sub>
    * Description: Field description of how the filter is damaged, if at all
    * range: [String](types/String.md)
 * [fieldFilterDamageRemarks](fieldFilterDamageRemarks.md)  <sub>OPT</sub>
    * Description: Additional description of possible field damages, e.g., tear, hole, piece missing
    * range: [String](types/String.md)
 * [filterCode](filterCode.md)  <sub>OPT</sub>
    * Description: Barcode of the filter
    * range: [String](types/String.md)
 * [filterID](filterID.md)  <sub>OPT</sub>
    * Description: The non-repeating manufacturer-generated ID of each filter
    * range: [String](types/String.md)
 * [filterWet](filterWet.md)  <sub>OPT</sub>
    * Description: Percentage of the filter area that is wet
    * range: [Double](types/Double.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
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
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:dpm_fieldData_in |

