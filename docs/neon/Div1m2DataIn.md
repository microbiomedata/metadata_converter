
# Type: div_1m2Data_in




URI: [neon:Div1m2DataIn](https://data.neonscience.org/Div1m2DataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Div1m2DataIn&#124;uid:string%20%3F;plotID:string%20%3F;identificationReferences:string%20%3F;remarks:string%20%3F;taxonID:string%20%3F;identificationQualifier:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;enteredBy:string%20%3F;boutNumber:string%20%3F;targetTaxaPresent:string%20%3F;acceptedTaxonID:string%20%3F;morphospeciesID:string%20%3F;percentCover:double%20%3F;subplotID:string%20%3F;divDataType:string%20%3F;otherVariablesPresent:string%20%3F;taxonIDRemarks:string%20%3F;otherVariables:string%20%3F;heightPlantOver300cm:string%20%3F;heightPlantSpecies:string%20%3F;morphospeciesIDRemarks:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F])

## Attributes


### Own

 * [acceptedTaxonID](acceptedTaxonID.md)  <sub>OPT</sub>
    * Description: Accepted species code, based on one or more sources
    * range: [String](types/String.md)
 * [boutNumber](boutNumber.md)  <sub>OPT</sub>
    * Description: Number of the sampling bout within a calendar year, beginning with 1
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [divDataType](divDataType.md)  <sub>OPT</sub>
    * Description: Identifier for the type of data recorded: plantSpecies or otherVariables
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [enteredBy](enteredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who entered the data
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [heightPlantOver300cm](heightPlantOver300cm.md)  <sub>OPT</sub>
    * Description: Indicator of whether individuals of the species in the sample are taller than 300 cm
    * range: [String](types/String.md)
 * [heightPlantSpecies](heightPlantSpecies.md)  <sub>OPT</sub>
    * Description: Ocular estimate of the height of the plant species
    * range: [String](types/String.md)
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
 * [identificationReferences](identificationReferences.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) used to derive the specific taxon concept; including field guide editions, books, or versions of NEON keys used
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [morphospeciesID](morphospeciesID.md)  <sub>OPT</sub>
    * Description: Identifier for morphospecies
    * range: [String](types/String.md)
 * [morphospeciesIDRemarks](morphospeciesIDRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes about the morphospecies; free text comments accompanying the record
    * range: [String](types/String.md)
 * [otherVariables](otherVariables.md)  <sub>OPT</sub>
    * Description: Descriptor of other variables present in the sample, including abiotic, biotic, and non-vascular plant cover
    * range: [String](types/String.md)
 * [otherVariablesPresent](otherVariablesPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained other variables, such as abiotic, biotic, and non-vascular plant cover
    * range: [String](types/String.md)
 * [percentCover](percentCover.md)  <sub>OPT</sub>
    * Description: Ocular estimate of cover of the index (e.g., species) as a percent
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
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [subplotID](subplotID.md)  <sub>OPT</sub>
    * Description: Identifier for the NEON subplot
    * range: [String](types/String.md)
 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [taxonIDRemarks](taxonIDRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes about the specific taxon; free text comments accompanying the record
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:div_1m2Data_in |
| **In Subsets:** | | DP0.10004.001 |

