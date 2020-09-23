
# Type: cdw_densitylog_in




URI: [neon:CdwDensitylogIn](https://data.neonscience.org/CdwDensitylogIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[CdwDensitylogIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;taxonID:string%20%3F;identificationQualifier:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;samplingProtocolVersion:string%20%3F;sizeCategory:string%20%3F;pointID:string%20%3F;sampleFate:string%20%3F;dataQF:string%20%3F;sampleBarcode:string%20%3F;vstTagID:string%20%3F;branchBarkCover:string%20%3F;branchesPresent:string%20%3F;decayClass:string%20%3F;leavesPresent:string%20%3F;logBarkCover:string%20%3F;logDistance:double%20%3F;logHandBreakable:string%20%3F;logHoldShape:string%20%3F;logID:string%20%3F;twigsPresent:string%20%3F;yearBoutBegan:integer%20%3F;logAzimuth:string%20%3F;mappingMethod:string%20%3F;sampleEasting:double%20%3F;sampleNorthing:double%20%3F])

## Attributes


### Own

 * [branchBarkCover](branchBarkCover.md)  <sub>OPT</sub>
    * Description: Visually estimated cover class of bark remaining on branches attached to a coarse downed wood particle
    * range: [String](types/String.md)
 * [branchesPresent](branchesPresent.md)  <sub>OPT</sub>
    * Description: Categorical indicator of branches > 1 cm diameter present on a coarse downed wood particle
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [decayClass](decayClass.md)  <sub>OPT</sub>
    * Description: The categorical decay class assigned to a sampled log
    * range: [String](types/String.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
 * [leavesPresent](leavesPresent.md)  <sub>OPT</sub>
    * Description: Categorical indicator of leaf/needle presence on a coarse downed wood particle
    * range: [String](types/String.md)
 * [logAzimuth](logAzimuth.md)  <sub>OPT</sub>
    * Description: The azimuth relative to true north, to the nearest degree, measured from the plot centroid facing toward the sampled log
    * range: [String](types/String.md)
 * [logBarkCover](logBarkCover.md)  <sub>OPT</sub>
    * Description: Visually estimated cover class of bark remaining on the bole of a coarse downed wood particle
    * range: [String](types/String.md)
 * [logDistance](logDistance.md)  <sub>OPT</sub>
    * Description: The distance, to the nearest 0.1 meters, from the log to a reference point with known position (typically the transect origin)
    * range: [Double](types/Double.md)
 * [logHandBreakable](logHandBreakable.md)  <sub>OPT</sub>
    * Description: Categorical indicator that the outer-most wood from a coarse downed wood particle can be broken apart by hand
    * range: [String](types/String.md)
 * [logHoldShape](logHoldShape.md)  <sub>OPT</sub>
    * Description: Categorical indicator that a piece of coarse downed wood particle holds its original shape
    * range: [String](types/String.md)
 * [logID](logID.md)  <sub>OPT</sub>
    * Description: Identifier for each log sampled
    * range: [String](types/String.md)
 * [mappingMethod](mappingMethod.md)  <sub>OPT</sub>
    * Description: Indicator for whether or not the specified location is mapped and the method used
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [pointID](pointID.md)  <sub>OPT</sub>
    * Description: Identifier for a point location
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleBarcode](sampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a sample
    * range: [String](types/String.md)
 * [sampleEasting](sampleEasting.md)  <sub>OPT</sub>
    * Description: Easting value of sampled location
    * range: [Double](types/Double.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [sampleNorthing](sampleNorthing.md)  <sub>OPT</sub>
    * Description: Northing value of sampled location
    * range: [Double](types/Double.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [sizeCategory](sizeCategory.md)  <sub>OPT</sub>
    * Description: Categorical size class of an individual or sample
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [twigsPresent](twigsPresent.md)  <sub>OPT</sub>
    * Description: Categorical indicator of twigs < 1 cm diameter present on a coarse downed wood particle
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [vstTagID](vstTagID.md)  <sub>OPT</sub>
    * Description: The vegetation structure tagID value
    * range: [String](types/String.md)
 * [yearBoutBegan](yearBoutBegan.md)  <sub>OPT</sub>
    * Description: The calendar year that the bout began
    * range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:cdw_densitylog_in |
| **In Subsets:** | | DP0.10014.001 |

