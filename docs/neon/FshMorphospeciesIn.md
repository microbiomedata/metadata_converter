
# Type: fsh_morphospecies_in




URI: [neon:FshMorphospeciesIn](https://data.neonscience.org/FshMorphospeciesIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[FshMorphospeciesIn&#124;uid:string%20%3F;siteID:string%20%3F;identificationReferences:string%20%3F;taxonID:string%20%3F;identificationQualifier:string%20%3F;recordedBy:string%20%3F;morphospeciesID:string%20%3F;identifiedBy:string%20%3F;morphospeciesIDRemarks:string%20%3F;dataQF:string%20%3F;aquaticSiteType:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;morphospeciesCreatedDate:time%20%3F;morphospeciesResolved:string%20%3F;morphospeciesResolvedDate:time%20%3F])

## Attributes


### Own

 * [aquaticSiteType](aquaticSiteType.md)  <sub>OPT</sub>
    * Description: Type of aquatic site, includes lake, river or stream
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
 * [identificationReferences](identificationReferences.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) used to derive the specific taxon concept; including field guide editions, books, or versions of NEON keys used
    * range: [String](types/String.md)
 * [identifiedBy](identifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who identified the specimen
    * range: [String](types/String.md)
 * [morphospeciesCreatedDate](morphospeciesCreatedDate.md)  <sub>OPT</sub>
    * Description: Date and time of morphospecies record creation
    * range: [Time](types/Time.md)
 * [morphospeciesID](morphospeciesID.md)  <sub>OPT</sub>
    * Description: Identifier for morphospecies
    * range: [String](types/String.md)
 * [morphospeciesIDRemarks](morphospeciesIDRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes about the morphospecies; free text comments accompanying the record
    * range: [String](types/String.md)
 * [morphospeciesResolved](morphospeciesResolved.md)  <sub>OPT</sub>
    * Description: Indicator of whether the morphospecies has been identified
    * range: [String](types/String.md)
 * [morphospeciesResolvedDate](morphospeciesResolvedDate.md)  <sub>OPT</sub>
    * Description: Date and time of resolving the morphospecies identification
    * range: [Time](types/Time.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:fsh_morphospecies_in |

