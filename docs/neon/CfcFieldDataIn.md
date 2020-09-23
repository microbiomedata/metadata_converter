
# Type: cfc_fieldData_in




URI: [neon:CfcFieldDataIn](https://data.neonscience.org/CfcFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[CfcFieldDataIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;taxonID:string%20%3F;tagID:string%20%3F;recordedBy:string%20%3F;individualID:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;sampleType:string%20%3F;plantStatus:string%20%3F;subplotID:string%20%3F;clipID:string%20%3F;bagCount:string%20%3F;clipCellNumber:string%20%3F;samplingProtocolVersion:string%20%3F;collectedBy:string%20%3F;sampleNumber:string%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;sampleCondition:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;clipLength:double%20%3F;clipWidth:double%20%3F;samplingMethod:string%20%3F;individualCode:string%20%3F;individualFate:string%20%3F;vstTag:string%20%3F;chlorophyllSampleCode:string%20%3F;chlorophyllSampleFate:string%20%3F;chlorophyllSampleID:string%20%3F;percentCoverClip:double%20%3F;subsample1Height:double%20%3F;subsample2Height:double%20%3F;subsample3Height:double%20%3F;vd1BaseHeight:double%20%3F;vd1Sample:double%20%3F;vd2BaseHeight:double%20%3F;vd2Sample:double%20%3F;vd3BaseHeight:double%20%3F;vd3Sample:double%20%3F;toxicodendronPossible:string%20%3F;chlorophyllSampleCondition:string%20%3F])

## Attributes


### Own

 * [bagCount](bagCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of sample bags transported from the field to the laboratory for processing
    * range: [String](types/String.md)
 * [chlorophyllSampleCode](chlorophyllSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a chlorophyll sample
    * range: [String](types/String.md)
 * [chlorophyllSampleCondition](chlorophyllSampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a chlorophyll sample
    * range: [String](types/String.md)
 * [chlorophyllSampleFate](chlorophyllSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a chlorophyll sample
    * range: [String](types/String.md)
 * [chlorophyllSampleID](chlorophyllSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a chlorophyll sample
    * range: [String](types/String.md)
 * [clipCellNumber](clipCellNumber.md)  <sub>OPT</sub>
    * Description: A numeric identifier for the clip-harvest cell in which herbaceous biomass was sampled
    * range: [String](types/String.md)
 * [clipID](clipID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the clip-harvest location within the plot
    * range: [String](types/String.md)
 * [clipLength](clipLength.md)  <sub>OPT</sub>
    * Description: The length of the clip-harvest area in meters
    * range: [Double](types/Double.md)
 * [clipWidth](clipWidth.md)  <sub>OPT</sub>
    * Description: The width of the clip-harvest area in meters
    * range: [Double](types/Double.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [collectedBy](collectedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who collected the sample or specimen
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [individualCode](individualCode.md)  <sub>OPT</sub>
    * Description: Barcode of an individual
    * range: [String](types/String.md)
 * [individualFate](individualFate.md)  <sub>OPT</sub>
    * Description: Fate of a tagged individual
    * range: [String](types/String.md)
 * [individualID](individualID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier for an individual: NEON.MOD.D##.######
    * range: [String](types/String.md)
 * [percentCoverClip](percentCoverClip.md)  <sub>OPT</sub>
    * Description: Ocular estimate of percent cover of all vegetation in the clip strip
    * range: [Double](types/Double.md)
 * [plantStatus](plantStatus.md)  <sub>OPT</sub>
    * Description: Physical status of individual: live, dead, lost
    * range: [String](types/String.md)
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
 * [sampleNumber](sampleNumber.md)  <sub>OPT</sub>
    * Description: Number of sample collected
    * range: [String](types/String.md)
 * [sampleType](sampleType.md)  <sub>OPT</sub>
    * Description: Type of sample
    * range: [String](types/String.md)
 * [samplingMethod](samplingMethod.md)  <sub>OPT</sub>
    * Description: Name or code for the method used to collect or test a sample
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [subplotID](subplotID.md)  <sub>OPT</sub>
    * Description: Identifier for the NEON subplot
    * range: [String](types/String.md)
 * [subsample1Height](subsample1Height.md)  <sub>OPT</sub>
    * Description: Vertical distance from ground to height of first canopy subsample
    * range: [Double](types/Double.md)
 * [subsample2Height](subsample2Height.md)  <sub>OPT</sub>
    * Description: Vertical distance from ground to height of second canopy subsample
    * range: [Double](types/Double.md)
 * [subsample3Height](subsample3Height.md)  <sub>OPT</sub>
    * Description: Vertical distance from ground to height of third canopy subsample
    * range: [Double](types/Double.md)
 * [tagID](tagID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier of tag used to mark the individual
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [toxicodendronPossible](toxicodendronPossible.md)  <sub>OPT</sub>
    * Description: Indicator for whether a sample may contain Toxicodendron spp
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [vd1BaseHeight](vd1BaseHeight.md)  <sub>OPT</sub>
    * Description: Vertical distance from observer to base of stem for first canopy subsample
    * range: [Double](types/Double.md)
 * [vd1Sample](vd1Sample.md)  <sub>OPT</sub>
    * Description: Vertical distance from observer to height of first canopy subsample
    * range: [Double](types/Double.md)
 * [vd2BaseHeight](vd2BaseHeight.md)  <sub>OPT</sub>
    * Description: Vertical distance from observer to base of stem for second canopy subsample
    * range: [Double](types/Double.md)
 * [vd2Sample](vd2Sample.md)  <sub>OPT</sub>
    * Description: Vertical distance from observer to height of second canopy subsample
    * range: [Double](types/Double.md)
 * [vd3BaseHeight](vd3BaseHeight.md)  <sub>OPT</sub>
    * Description: Vertical distance from observer to base of stem for third canopy leaf subsample
    * range: [Double](types/Double.md)
 * [vd3Sample](vd3Sample.md)  <sub>OPT</sub>
    * Description: Vertical distance from observer to height of third canopy leaf subsample
    * range: [Double](types/Double.md)
 * [vstTag](vstTag.md)  <sub>OPT</sub>
    * Description: Indicator for whether a tagID is associated with vegetation structure measurements
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:cfc_fieldData_in |
| **In Subsets:** | | DP0.10026.001 |

