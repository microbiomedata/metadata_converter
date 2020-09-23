
# Type: vst_apparentindividual_in




URI: [neon:VstApparentindividualIn](https://data.neonscience.org/VstApparentindividualIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VstApparentindividualIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;tagID:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;individualID:string%20%3F;growthForm:string%20%3F;canopyPosition:string%20%3F;plantStatus:string%20%3F;stemDiameter:double%20%3F;measurementHeight:double%20%3F;height:double%20%3F;subplotID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;dataQF:string%20%3F;individualFate:string%20%3F;individualBarcode:string%20%3F;tagStatus:string%20%3F;nullFieldValidation:double%20%3F;basalStemDiameter:double%20%3F;basalStemDiameterMsrmntHeight:double%20%3F;baseCrownHeight:double%20%3F;breakDiameter:double%20%3F;breakHeight:double%20%3F;maxBaseCrownDiameter:double%20%3F;maxCrownDiameter:double%20%3F;ninetyBaseCrownDiameter:double%20%3F;ninetyCrownDiameter:double%20%3F;shape:string%20%3F;vdApexBreakHeight:double%20%3F;vdApexHeight:double%20%3F;vdBaseBreakHeight:double%20%3F;vdBaseHeight:double%20%3F;initialBandStemDiameter:double%20%3F;initialDendrometerGap:double%20%3F;dendrometerHeight:double%20%3F;tempStemID:string%20%3F;measurementStrategy:string%20%3F;changedMeasurementLocation:string%20%3F;dendrometerInstallationDate:string%20%3F;initalGapMeasurementDate:time%20%3F;dendrometerGap:double%20%3F;dendrometerCondition:string%20%3F;bandStemDiameter:double%20%3F])

## Attributes


### Own

 * [bandStemDiameter](bandStemDiameter.md)  <sub>OPT</sub>
    * Description: Calculated current year diameter at band location
    * range: [Double](types/Double.md)
 * [basalStemDiameter](basalStemDiameter.md)  <sub>OPT</sub>
    * Description: Cross-sectional stem diameter at base of stem
    * range: [Double](types/Double.md)
 * [basalStemDiameterMsrmntHeight](basalStemDiameterMsrmntHeight.md)  <sub>OPT</sub>
    * Description: Height at which basalStemDiameter is measured
    * range: [Double](types/Double.md)
 * [baseCrownHeight](baseCrownHeight.md)  <sub>OPT</sub>
    * Description: Height above the ground for the lowest portion of the crown
    * range: [Double](types/Double.md)
 * [breakDiameter](breakDiameter.md)  <sub>OPT</sub>
    * Description: Cross-sectional diameter at the break point along a broken bole
    * range: [Double](types/Double.md)
 * [breakHeight](breakHeight.md)  <sub>OPT</sub>
    * Description: Height from the ground to the highest point along a broken bole
    * range: [Double](types/Double.md)
 * [canopyPosition](canopyPosition.md)  <sub>OPT</sub>
    * Description: Vertical status of an individual relative to its neighbors
    * range: [String](types/String.md)
 * [changedMeasurementLocation](changedMeasurementLocation.md)  <sub>OPT</sub>
    * Description: Indicator for whether the measurement location on the individual changed from previous measurements
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [dendrometerCondition](dendrometerCondition.md)  <sub>OPT</sub>
    * Description: Condition of the dendrometer band
    * range: [String](types/String.md)
 * [dendrometerGap](dendrometerGap.md)  <sub>OPT</sub>
    * Description: Width of dendrometer measurement window
    * range: [Double](types/Double.md)
 * [dendrometerHeight](dendrometerHeight.md)  <sub>OPT</sub>
    * Description: Distance along stem at which dendrometer band is installed
    * range: [Double](types/Double.md)
 * [dendrometerInstallationDate](dendrometerInstallationDate.md)  <sub>OPT</sub>
    * Description: The date the dendrometer band was installed on the individual
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
 * [individualBarcode](individualBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a tagged individual
    * range: [String](types/String.md)
 * [individualFate](individualFate.md)  <sub>OPT</sub>
    * Description: Fate of a tagged individual
    * range: [String](types/String.md)
 * [individualID](individualID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier for an individual: NEON.MOD.D##.######
    * range: [String](types/String.md)
 * [initalGapMeasurementDate](initalGapMeasurementDate.md)  <sub>OPT</sub>
    * Description: The date initial dendrometer band gap measurement was made
    * range: [Time](types/Time.md)
 * [initialBandStemDiameter](initialBandStemDiameter.md)  <sub>OPT</sub>
    * Description: Cross sectional diameter at the time dendrometer band is installed
    * range: [Double](types/Double.md)
 * [initialDendrometerGap](initialDendrometerGap.md)  <sub>OPT</sub>
    * Description: Initial width of the measurement window
    * range: [Double](types/Double.md)
 * [maxBaseCrownDiameter](maxBaseCrownDiameter.md)  <sub>OPT</sub>
    * Description: Maximum crown diameter, measured at ground level
    * range: [Double](types/Double.md)
 * [maxCrownDiameter](maxCrownDiameter.md)  <sub>OPT</sub>
    * Description: Maximum crown diameter of the individual or patch
    * range: [Double](types/Double.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [measurementHeight](measurementHeight.md)  <sub>OPT</sub>
    * Description: Height at which stemDiameter is measured
    * range: [Double](types/Double.md)
 * [measurementStrategy](measurementStrategy.md)  <sub>OPT</sub>
    * Description: Identifier for the selected method of measuring an indivual
    * range: [String](types/String.md)
 * [ninetyBaseCrownDiameter](ninetyBaseCrownDiameter.md)  <sub>OPT</sub>
    * Description: Crown diameter perpendicular to maxBaseCrownDiameter, measured at ground level
    * range: [Double](types/Double.md)
 * [ninetyCrownDiameter](ninetyCrownDiameter.md)  <sub>OPT</sub>
    * Description: Crown diameter perpendicular to maxDiameter
    * range: [Double](types/Double.md)
 * [nullFieldValidation](nullFieldValidation.md)  <sub>OPT</sub>
    * Description: Synthetic field to verify data are present in minimum required fields
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
 * [shape](shape.md)  <sub>OPT</sub>
    * Description: Description of three dimensional form
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stemDiameter](stemDiameter.md)  <sub>OPT</sub>
    * Description: Cross-sectional stem diameter
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
 * [tempStemID](tempStemID.md)  <sub>OPT</sub>
    * Description: Stem-level identifier for a multi-stemmed individual with growth form of shrub, small shrub, sapling or small tree
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [vdApexBreakHeight](vdApexBreakHeight.md)  <sub>OPT</sub>
    * Description: Height from observer to the highest point along a broken bole
    * range: [Double](types/Double.md)
 * [vdApexHeight](vdApexHeight.md)  <sub>OPT</sub>
    * Description: Height from observer to highest crown point
    * range: [Double](types/Double.md)
 * [vdBaseBreakHeight](vdBaseBreakHeight.md)  <sub>OPT</sub>
    * Description: Height from observer to the base of a broken bole
    * range: [Double](types/Double.md)
 * [vdBaseHeight](vdBaseHeight.md)  <sub>OPT</sub>
    * Description: Height from observer to base of stem
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:vst_apparentindividual_in |

