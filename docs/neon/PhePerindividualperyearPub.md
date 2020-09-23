
# Type: phe_perindividualperyear_pub




URI: [neon:PhePerindividualperyearPub](https://data.neonscience.org/PhePerindividualperyearPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PhePerindividualperyearPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;date:time%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;individualID:string%20%3F;patchOrIndividual:string%20%3F;canopyPosition:string%20%3F;plantStatus:string%20%3F;stemDiameter:double%20%3F;measurementHeight:double%20%3F;maxCanopyDiameter:double%20%3F;ninetyCanopyDiameter:double%20%3F;percentCover:double%20%3F;height:double%20%3F;adultLeafLength:double%20%3F;diseaseType:string%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;editedDate:time%20%3F;individualBarcode:string%20%3F;patchSize:double%20%3F])

## Attributes


### Own

 * [adultLeafLength](adultLeafLength.md)  <sub>OPT</sub>
    * Description: The length of an average adult leaf
    * range: [Double](types/Double.md)
 * [canopyPosition](canopyPosition.md)  <sub>OPT</sub>
    * Description: Vertical status of an individual relative to its neighbors
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [date](date.md)  <sub>OPT</sub>
    * Description: Date or date and time of measurement, observation, or collection event
    * range: [Time](types/Time.md)
 * [diseaseType](diseaseType.md)  <sub>OPT</sub>
    * Description: Specific disease present, if known
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [editedDate](editedDate.md)  <sub>OPT</sub>
    * Description: The date-time that record was edited
    * range: [Time](types/Time.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [height](height.md)  <sub>OPT</sub>
    * Description: Highest point of an individual or average height of a patch
    * range: [Double](types/Double.md)
 * [individualBarcode](individualBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a tagged individual
    * range: [String](types/String.md)
 * [individualID](individualID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier for an individual: NEON.MOD.D##.######
    * range: [String](types/String.md)
 * [maxCanopyDiameter](maxCanopyDiameter.md)  <sub>OPT</sub>
    * Description: Maximum canopy diameter of the individual or patch
    * range: [Double](types/Double.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [measurementHeight](measurementHeight.md)  <sub>OPT</sub>
    * Description: Height at which stemDiameter is measured
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [ninetyCanopyDiameter](ninetyCanopyDiameter.md)  <sub>OPT</sub>
    * Description: Canopy diameter perpendicular to maxCanopyDiameter
    * range: [Double](types/Double.md)
 * [patchOrIndividual](patchOrIndividual.md)  <sub>OPT</sub>
    * Description: Unit of measurement
    * range: [String](types/String.md)
 * [patchSize](patchSize.md)  <sub>OPT</sub>
    * Description: Size (in square meters) of the patch
    * range: [Double](types/Double.md)
 * [percentCover](percentCover.md)  <sub>OPT</sub>
    * Description: Ocular estimate of cover of the index (e.g., species) as a percent
    * range: [Double](types/Double.md)
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
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [stemDiameter](stemDiameter.md)  <sub>OPT</sub>
    * Description: Cross-sectional stem diameter
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:phe_perindividualperyear_pub |

