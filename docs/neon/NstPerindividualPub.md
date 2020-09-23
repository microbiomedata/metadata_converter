
# Type: nst_perindividual_pub




URI: [neon:NstPerindividualPub](https://data.neonscience.org/NstPerindividualPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NstPerindividualPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;date:time%20%3F;identificationReferences:string%20%3F;remarks:string%20%3F;taxonID:string%20%3F;identificationQualifier:string%20%3F;tagID:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;individualID:string%20%3F;scientificName:string%20%3F;taxonRank:string%20%3F;morphospeciesID:string%20%3F;growthForm:string%20%3F;canopyPosition:string%20%3F;plantStatus:string%20%3F;stemDiameter:double%20%3F;measurementHeight:double%20%3F;height:double%20%3F;subplotID:string%20%3F;morphospeciesIDRemarks:string%20%3F;endDate:time%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;individualBarcode:string%20%3F;tagStatus:string%20%3F;basalStemDiameter:double%20%3F;baseCrownHeight:double%20%3F;branchCount:string%20%3F;leafNumber:string%20%3F;maxBaseCrownDiameter:double%20%3F;maxCrownDiameter:double%20%3F;meanBasalDiameter:double%20%3F;meanBladeLength:double%20%3F;meanBranchLength:double%20%3F;meanLeafLength:double%20%3F;meanPetioleLength:double%20%3F;nestedSubplotID:string%20%3F;newPadCount:string%20%3F;ninetyBaseCrownDiameter:double%20%3F;ninetyCrownDiameter:double%20%3F;oldPadCount:string%20%3F;shape:string%20%3F;stemCount:string%20%3F;stemLength:double%20%3F])

## Attributes


### Own

 * [basalStemDiameter](basalStemDiameter.md)  <sub>OPT</sub>
    * Description: Cross-sectional stem diameter at base of stem
    * range: [Double](types/Double.md)
 * [baseCrownHeight](baseCrownHeight.md)  <sub>OPT</sub>
    * Description: Height above the ground for the lowest portion of the crown
    * range: [Double](types/Double.md)
 * [branchCount](branchCount.md)  <sub>OPT</sub>
    * Description: Count of branches
    * range: [String](types/String.md)
 * [canopyPosition](canopyPosition.md)  <sub>OPT</sub>
    * Description: Vertical status of an individual relative to its neighbors
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [date](date.md)  <sub>OPT</sub>
    * Description: Date or date and time of measurement, observation, or collection event
    * range: [Time](types/Time.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [growthForm](growthForm.md)  <sub>OPT</sub>
    * Description: The growth form classification
    * range: [String](types/String.md)
 * [height](height.md)  <sub>OPT</sub>
    * Description: Highest point of an individual or average height of a patch
    * range: [Double](types/Double.md)
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
 * [identificationReferences](identificationReferences.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) used to derive the specific taxon concept; including field guide editions, books, or versions of NEON keys used
    * range: [String](types/String.md)
 * [individualBarcode](individualBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a tagged individual
    * range: [String](types/String.md)
 * [individualID](individualID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier for an individual: NEON.MOD.D##.######
    * range: [String](types/String.md)
 * [leafNumber](leafNumber.md)  <sub>OPT</sub>
    * Description: The total number of leaves on an individual plant
    * range: [String](types/String.md)
 * [maxBaseCrownDiameter](maxBaseCrownDiameter.md)  <sub>OPT</sub>
    * Description: Maximum crown diameter, measured at ground level
    * range: [Double](types/Double.md)
 * [maxCrownDiameter](maxCrownDiameter.md)  <sub>OPT</sub>
    * Description: Maximum crown diameter of the individual or patch
    * range: [Double](types/Double.md)
 * [meanBasalDiameter](meanBasalDiameter.md)  <sub>OPT</sub>
    * Description: Average basal diameter of a group of stems
    * range: [Double](types/Double.md)
 * [meanBladeLength](meanBladeLength.md)  <sub>OPT</sub>
    * Description: The average length of a typical leaf blade, measured from the top of the petiole to leaf tip
    * range: [Double](types/Double.md)
 * [meanBranchLength](meanBranchLength.md)  <sub>OPT</sub>
    * Description: Average length of branches on an individual
    * range: [Double](types/Double.md)
 * [meanLeafLength](meanLeafLength.md)  <sub>OPT</sub>
    * Description: The average length of a typical leaf on the individual plant being measured
    * range: [Double](types/Double.md)
 * [meanPetioleLength](meanPetioleLength.md)  <sub>OPT</sub>
    * Description: The average length of a typical leaf or frond petiole, measured from the interstection with the stem to the base of the blade, lamina or first leaftet
    * range: [Double](types/Double.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [measurementHeight](measurementHeight.md)  <sub>OPT</sub>
    * Description: Height at which stemDiameter is measured
    * range: [Double](types/Double.md)
 * [morphospeciesID](morphospeciesID.md)  <sub>OPT</sub>
    * Description: Identifier for morphospecies
    * range: [String](types/String.md)
 * [morphospeciesIDRemarks](morphospeciesIDRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes about the morphospecies; free text comments accompanying the record
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [nestedSubplotID](nestedSubplotID.md)  <sub>OPT</sub>
    * Description: Numeric identifier for nested subplot ID within a subplotID
    * range: [String](types/String.md)
 * [newPadCount](newPadCount.md)  <sub>OPT</sub>
    * Description: The number of cladodes produced in the current growing season
    * range: [String](types/String.md)
 * [ninetyBaseCrownDiameter](ninetyBaseCrownDiameter.md)  <sub>OPT</sub>
    * Description: Crown diameter perpendicular to maxBaseCrownDiameter, measured at ground level
    * range: [Double](types/Double.md)
 * [ninetyCrownDiameter](ninetyCrownDiameter.md)  <sub>OPT</sub>
    * Description: Crown diameter perpendicular to maxDiameter
    * range: [Double](types/Double.md)
 * [oldPadCount](oldPadCount.md)  <sub>OPT</sub>
    * Description: The number of cladodes produced in previous growing seasons
    * range: [String](types/String.md)
 * [plantStatus](plantStatus.md)  <sub>OPT</sub>
    * Description: Physical status of individual: live, dead, lost
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
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
    * range: [String](types/String.md)
 * [shape](shape.md)  <sub>OPT</sub>
    * Description: Description of three dimensional form
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [stemCount](stemCount.md)  <sub>OPT</sub>
    * Description: Count of stems
    * range: [String](types/String.md)
 * [stemDiameter](stemDiameter.md)  <sub>OPT</sub>
    * Description: Cross-sectional stem diameter
    * range: [Double](types/Double.md)
 * [stemLength](stemLength.md)  <sub>OPT</sub>
    * Description: The length of the stem to the base of the leaves
    * range: [Double](types/Double.md)
 * [subplotID](subplotID.md)  <sub>OPT</sub>
    * Description: Identifier for the NEON subplot
    * range: [String](types/String.md)
 * [tagID](tagID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier of tag used to mark the individual
    * range: [String](types/String.md)
 * [tagStatus](tagStatus.md)  <sub>OPT</sub>
    * Description: Description of state or condition of the physical tag
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [taxonRank](taxonRank.md)  <sub>OPT</sub>
    * Description: The lowest level taxonomic rank that can be determined for the individual or specimen
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:nst_perindividual_pub |

