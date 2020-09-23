
# Type: vst_mappingandtagging_in




URI: [neon:VstMappingandtaggingIn](https://data.neonscience.org/VstMappingandtaggingIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VstMappingandtaggingIn&#124;uid:string%20%3F;plotID:string%20%3F;identificationReferences:string%20%3F;remarks:string%20%3F;taxonID:string%20%3F;identificationQualifier:string%20%3F;tagID:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;individualID:string%20%3F;morphospeciesID:string%20%3F;subplotID:string%20%3F;morphospeciesIDRemarks:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;pointID:string%20%3F;dataQF:string%20%3F;individualFate:string%20%3F;individualBarcode:string%20%3F;yearBoutBegan:integer%20%3F;cfcOnlyTag:string%20%3F;nestedSubplotID:string%20%3F;previouslyTaggedAs:string%20%3F;stemAzimuth:double%20%3F;stemDistance:double%20%3F;supportingStemIndividualID:string%20%3F;supportingStemTagID:string%20%3F;vstBarcode:string%20%3F;vstFate:string%20%3F;vstID:string%20%3F;initialBandStemDiameter:double%20%3F;initialDendrometerGap:double%20%3F;dendrometerHeight:double%20%3F;recordType:string%20%3F])

## Attributes


### Own

 * [cfcOnlyTag](cfcOnlyTag.md)  <sub>OPT</sub>
    * Description: Indicator for whether a tagID is a associated with canopy foliage sampling only
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [dendrometerHeight](dendrometerHeight.md)  <sub>OPT</sub>
    * Description: Distance along stem at which dendrometer band is installed
    * range: [Double](types/Double.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
 * [identificationReferences](identificationReferences.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) used to derive the specific taxon concept; including field guide editions, books, or versions of NEON keys used
    * range: [String](types/String.md)
 * [individualBarcode](individualBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a tagged individual
    * range: [String](types/String.md)
 * [individualFate](individualFate.md)  <sub>OPT</sub>
    * Description: Fate of a tagged individual
    * range: [String](types/String.md)
 * [individualID](individualID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier for an individual: NEON.MOD.D##.######
    * range: [String](types/String.md)
 * [initialBandStemDiameter](initialBandStemDiameter.md)  <sub>OPT</sub>
    * Description: Cross sectional diameter at the time dendrometer band is installed
    * range: [Double](types/Double.md)
 * [initialDendrometerGap](initialDendrometerGap.md)  <sub>OPT</sub>
    * Description: Initial width of the measurement window
    * range: [Double](types/Double.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [morphospeciesID](morphospeciesID.md)  <sub>OPT</sub>
    * Description: Identifier for morphospecies
    * range: [String](types/String.md)
 * [morphospeciesIDRemarks](morphospeciesIDRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes about the morphospecies; free text comments accompanying the record
    * range: [String](types/String.md)
 * [nestedSubplotID](nestedSubplotID.md)  <sub>OPT</sub>
    * Description: Numeric identifier for nested subplot ID within a subplotID
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [pointID](pointID.md)  <sub>OPT</sub>
    * Description: Identifier for a point location
    * range: [String](types/String.md)
 * [previouslyTaggedAs](previouslyTaggedAs.md)  <sub>OPT</sub>
    * Description: Indicates the tagID previously reported for a given individual
    * range: [String](types/String.md)
 * [recordType](recordType.md)  <sub>OPT</sub>
    * Description: Categorical indicator for type of data record
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
 * [stemAzimuth](stemAzimuth.md)  <sub>OPT</sub>
    * Description: Azimuth relative to True North between stem and pointID location
    * range: [Double](types/Double.md)
 * [stemDistance](stemDistance.md)  <sub>OPT</sub>
    * Description: Horizontal distance from stem to pointID location
    * range: [Double](types/Double.md)
 * [subplotID](subplotID.md)  <sub>OPT</sub>
    * Description: Identifier for the NEON subplot
    * range: [String](types/String.md)
 * [supportingStemIndividualID](supportingStemIndividualID.md)  <sub>OPT</sub>
    * Description: Globally unique identifier for stem on which a liana is growing
    * range: [String](types/String.md)
 * [supportingStemTagID](supportingStemTagID.md)  <sub>OPT</sub>
    * Description: Unique tagID for stem on which a liana is growing
    * range: [String](types/String.md)
 * [tagID](tagID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier of tag used to mark the individual
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [vstBarcode](vstBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for vstID
    * range: [String](types/String.md)
 * [vstFate](vstFate.md)  <sub>OPT</sub>
    * Description: Fate for vstID
    * range: [String](types/String.md)
 * [vstID](vstID.md)  <sub>OPT</sub>
    * Description: Year specific identifier for the individual
    * range: [String](types/String.md)
 * [yearBoutBegan](yearBoutBegan.md)  <sub>OPT</sub>
    * Description: The calendar year that the bout began
    * range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:vst_mappingandtagging_in |

