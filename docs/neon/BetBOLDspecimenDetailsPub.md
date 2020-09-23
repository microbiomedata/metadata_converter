
# Type: bet_BOLDspecimenDetails_pub




URI: [neon:BetBOLDspecimenDetailsPub](https://data.neonscience.org/BetBOLDspecimenDetailsPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BetBOLDspecimenDetailsPub&#124;uid:string%20%3F;sex:string%20%3F;lifeStage:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;namedLocation:string%20%3F;associatedSpecimens:string%20%3F;associatedTaxa:string%20%3F;externalURLs:string%20%3F;reproduction:string%20%3F;extraInfo:string%20%3F;notes:string%20%3F;tissueDescriptor:string%20%3F;voucherStatus:string%20%3F])

## Attributes


### Own

 * [associatedSpecimens](associatedSpecimens.md)  <sub>OPT</sub>
    * Description: A list of specimens associated with the subject specimen at the time of its collection. References to other specimen identifiers should be preceded by the relationship
    * range: [String](types/String.md)
 * [associatedTaxa](associatedTaxa.md)  <sub>OPT</sub>
    * Description: A list of taxa associated with the taxon at the time of its collection. References to taxa are preceded by the relationship
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [externalURLs](externalURLs.md)  <sub>OPT</sub>
    * Description: Pipe-delimited list of web accessible links that provide additional information about the specimen
    * range: [String](types/String.md)
 * [extraInfo](extraInfo.md)  <sub>OPT</sub>
    * Description: A brief note or project term associated with the specimen for rapid analysis
    * range: [String](types/String.md)
 * [lifeStage](lifeStage.md)  <sub>OPT</sub>
    * Description: The age class of the individual at the time the Occurrence was recorded. juvenile = obvious signs of a very young individual, small size, distinctive pelage coloration; subabult; adult
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [notes](notes.md)  <sub>OPT</sub>
    * Description: General notes regarding the specimen
    * range: [String](types/String.md)
 * [reproduction](reproduction.md)  <sub>OPT</sub>
    * Description: The presumed method of reproduction
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [sex](sex.md)  <sub>OPT</sub>
    * Description: M for male, F for female, U for unknown
    * range: [String](types/String.md)
 * [tissueDescriptor](tissueDescriptor.md)  <sub>OPT</sub>
    * Description: A brief description of the type of tissue or material analyzed
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [voucherStatus](voucherStatus.md)  <sub>OPT</sub>
    * Description: Status of the specimen in an accessioning process
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:bet_BOLDspecimenDetails_pub |

