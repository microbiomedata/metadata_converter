
# Type: swc_fieldData_in




URI: [neon:SwcFieldDataIn](https://data.neonscience.org/SwcFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SwcFieldDataIn&#124;uid:string%20%3F;remarks:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;stationID:string%20%3F;processedDate:time%20%3F;sampleVolumeFiltered:double%20%3F;startDate:time%20%3F;parentSampleID:string%20%3F;processedDateFilters:time%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;parentSampleFate:string%20%3F;parentSampleCode:string%20%3F;sampleClass:string%20%3F;sampleCondition:string%20%3F;fieldDataQF:string%20%3F;replicateNumber:integer%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;filtSampleCode:string%20%3F;filtSampleCond:string%20%3F;filtSampleFate:string%20%3F;filtSampleID:string%20%3F;pcnSampleCode:string%20%3F;pcnSampleCond:string%20%3F;pcnSampleFate:string%20%3F;pcnSampleID:string%20%3F;rawSampleCode:string%20%3F;rawSampleCond:string%20%3F;rawSampleFate:string%20%3F;rawSampleID:string%20%3F;dicSampleCode:string%20%3F;dicSampleCond:string%20%3F;dicSampleFate:string%20%3F;dicSampleID:string%20%3F;filtSampleBottleSize:string%20%3F;gwwAlkSampleBubbleFree:string%20%3F;gwwAlkSampleHeadspace:string%20%3F;gwwFiltBubbleFree:string%20%3F;gwwFiltSampleHeadspace:string%20%3F;filtNutSampleBarcode:string%20%3F;filtNutSampleClass:string%20%3F;filtNutSampleCond:string%20%3F;filtNutSampleFate:string%20%3F;filtNutSampleID:string%20%3F;gwwDICBubbleFree:string%20%3F;rawNutSampleBarcode:string%20%3F;rawNutSampleClass:string%20%3F;rawNutSampleCond:string%20%3F;rawNutSampleFate:string%20%3F;rawNutSampleID:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dicSampleCode](dicSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a dissolved inorganic carbon sample
    * range: [String](types/String.md)
 * [dicSampleCond](dicSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of a dissolved inorganic carbon sample
    * range: [String](types/String.md)
 * [dicSampleFate](dicSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a dissolved inorganic carbon sample
    * range: [String](types/String.md)
 * [dicSampleID](dicSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for dissolved inorganic carbon sample
    * range: [String](types/String.md)
 * [fieldDataQF](fieldDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for field data
    * range: [String](types/String.md)
 * [filtNutSampleBarcode](filtNutSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of a filtered nutrient sample
    * range: [String](types/String.md)
 * [filtNutSampleClass](filtNutSampleClass.md)  <sub>OPT</sub>
    * Description: Sample class of a filtered nutrient sample
    * range: [String](types/String.md)
 * [filtNutSampleCond](filtNutSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of a filtered nutrient sample
    * range: [String](types/String.md)
 * [filtNutSampleFate](filtNutSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a filtered nutrient sample
    * range: [String](types/String.md)
 * [filtNutSampleID](filtNutSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for filtered nutrient sample
    * range: [String](types/String.md)
 * [filtSampleBottleSize](filtSampleBottleSize.md)  <sub>OPT</sub>
    * Description: The bottle size used to collect the filtered sample
    * range: [String](types/String.md)
 * [filtSampleCode](filtSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a filtered sample
    * range: [String](types/String.md)
 * [filtSampleCond](filtSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of filtered sample
    * range: [String](types/String.md)
 * [filtSampleFate](filtSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a filtered sample
    * range: [String](types/String.md)
 * [filtSampleID](filtSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for filtered sample
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [gwwAlkSampleBubbleFree](gwwAlkSampleBubbleFree.md)  <sub>OPT</sub>
    * Description: An indication of whether or not the alkalinity groundwater sample was collected with a bubble free method
    * range: [String](types/String.md)
 * [gwwAlkSampleHeadspace](gwwAlkSampleHeadspace.md)  <sub>OPT</sub>
    * Description: An indication of whether or not the alkalinity groundwater sample has headspace; for surface water samples no headspace is present in alkalinity samples
    * range: [String](types/String.md)
 * [gwwDICBubbleFree](gwwDICBubbleFree.md)  <sub>OPT</sub>
    * Description: An indication of whether or not the DIC groundwater subsample was collected with a bubble free method
    * range: [String](types/String.md)
 * [gwwFiltBubbleFree](gwwFiltBubbleFree.md)  <sub>OPT</sub>
    * Description: An indication of whether or not the filtered groundwater sample was collected with a bubble free method
    * range: [String](types/String.md)
 * [gwwFiltSampleHeadspace](gwwFiltSampleHeadspace.md)  <sub>OPT</sub>
    * Description: An indication of whether or not the filtered groundwater sample has headspace; for surface water samples no headspace is present in filtered samples
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
 * [pcnSampleCode](pcnSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a particulate carbon and nitrogen sample
    * range: [String](types/String.md)
 * [pcnSampleCond](pcnSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of a particulate carbon and nitrogen sample
    * range: [String](types/String.md)
 * [pcnSampleFate](pcnSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a particulate carbon and nitrogen sample
    * range: [String](types/String.md)
 * [pcnSampleID](pcnSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for particulate carbon and nitrogen sample
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [processedDate](processedDate.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event
    * range: [Time](types/Time.md)
 * [processedDateFilters](processedDateFilters.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event of filtered samples
    * range: [Time](types/Time.md)
 * [rawNutSampleBarcode](rawNutSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of a raw nutrient sample
    * range: [String](types/String.md)
 * [rawNutSampleClass](rawNutSampleClass.md)  <sub>OPT</sub>
    * Description: Sample class of a raw nutrient sample
    * range: [String](types/String.md)
 * [rawNutSampleCond](rawNutSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of a raw nutrient sample
    * range: [String](types/String.md)
 * [rawNutSampleFate](rawNutSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a raw nutrient sample
    * range: [String](types/String.md)
 * [rawNutSampleID](rawNutSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for raw nutrient sample
    * range: [String](types/String.md)
 * [rawSampleCode](rawSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a raw whole water sample
    * range: [String](types/String.md)
 * [rawSampleCond](rawSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of a raw whole water sample
    * range: [String](types/String.md)
 * [rawSampleFate](rawSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a raw whole water sample
    * range: [String](types/String.md)
 * [rawSampleID](rawSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for raw whole water sample
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [replicateNumber](replicateNumber.md)  <sub>OPT</sub>
    * Description: The number for the sample replicate
    * range: [Integer](types/Integer.md)
 * [sampleClass](sampleClass.md)  <sub>OPT</sub>
    * Description: Class of a sample
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [sampleVolumeFiltered](sampleVolumeFiltered.md)  <sub>OPT</sub>
    * Description: Volume of water filtered onto the filter for external analysis
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:swc_fieldData_in |
| **In Subsets:** | | DP0.20093.001 |

