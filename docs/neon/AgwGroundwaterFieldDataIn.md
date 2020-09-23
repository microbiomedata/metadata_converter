
# Type: agw_groundwaterFieldData_in




URI: [neon:AgwGroundwaterFieldDataIn](https://data.neonscience.org/AgwGroundwaterFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AgwGroundwaterFieldDataIn&#124;uid:string%20%3F;remarks:string%20%3F;recordedBy:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;collectedBy:string%20%3F;locationID:string%20%3F;dataQF:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;groundSurfToThawDist:double%20%3F;groundSurfToWaterDist:double%20%3F;liquidWaterPresence:string%20%3F;thawProbeDepth1:double%20%3F;thawProbeDepth10:double%20%3F;thawProbeDepth2:double%20%3F;thawProbeDepth3:double%20%3F;thawProbeDepth4:double%20%3F;thawProbeDepth5:double%20%3F;thawProbeDepth6:double%20%3F;thawProbeDepth7:double%20%3F;thawProbeDepth8:double%20%3F;thawProbeDepth9:double%20%3F;thawProbeDepthAverage:double%20%3F;thawProbeDepthStdDev:double%20%3F;topOfWellToGroundDist:double%20%3F;topOfWellToRefusalDist:double%20%3F;topOfWellToWaterDist:double%20%3F;transducerLowered:string%20%3F;wellPushedDownToThawLayer:string%20%3F])

## Attributes


### Own

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
 * [groundSurfToThawDist](groundSurfToThawDist.md)  <sub>OPT</sub>
    * Description: Distance between ground surface and refusal; i.e. bottom of thawed layer
    * range: [Double](types/Double.md)
 * [groundSurfToWaterDist](groundSurfToWaterDist.md)  <sub>OPT</sub>
    * Description: Distance between ground surface and surface of liquid water
    * range: [Double](types/Double.md)
 * [liquidWaterPresence](liquidWaterPresence.md)  <sub>OPT</sub>
    * Description: Presence of liquid water
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [thawProbeDepth1](thawProbeDepth1.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; first measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth10](thawProbeDepth10.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; tenth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth2](thawProbeDepth2.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; second measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth3](thawProbeDepth3.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; third measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth4](thawProbeDepth4.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; fourth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth5](thawProbeDepth5.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; fifth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth6](thawProbeDepth6.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; sixth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth7](thawProbeDepth7.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; seventh measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth8](thawProbeDepth8.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; eighth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepth9](thawProbeDepth9.md)  <sub>OPT</sub>
    * Description: Depth of thawed layer above permafrost from ground surface; ninth measurement
    * range: [Double](types/Double.md)
 * [thawProbeDepthAverage](thawProbeDepthAverage.md)  <sub>OPT</sub>
    * Description: Mean depth of thawed layer above permafrost from ground surface within 2 meter radius of well
    * range: [Double](types/Double.md)
 * [thawProbeDepthStdDev](thawProbeDepthStdDev.md)  <sub>OPT</sub>
    * Description: Standard deviation of 10 thaw depth measurements collected within 2 meter radius of well
    * range: [Double](types/Double.md)
 * [topOfWellToGroundDist](topOfWellToGroundDist.md)  <sub>OPT</sub>
    * Description: Distance between top of well casing and ground surface
    * range: [Double](types/Double.md)
 * [topOfWellToRefusalDist](topOfWellToRefusalDist.md)  <sub>OPT</sub>
    * Description: Distance between top of well casing and refusal
    * range: [Double](types/Double.md)
 * [topOfWellToWaterDist](topOfWellToWaterDist.md)  <sub>OPT</sub>
    * Description: Distance between top of well casing and surface of liquid water
    * range: [Double](types/Double.md)
 * [transducerLowered](transducerLowered.md)  <sub>OPT</sub>
    * Description: Indication of whether or not the pressure transducer was lowered to the well bottom
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [wellPushedDownToThawLayer](wellPushedDownToThawLayer.md)  <sub>OPT</sub>
    * Description: Indication of whether or not the well was pushed down to thaw layer
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:agw_groundwaterFieldData_in |
| **In Subsets:** | | DP0.20099.001 |

