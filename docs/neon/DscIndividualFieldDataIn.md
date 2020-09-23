
# Type: dsc_individualFieldData_in




URI: [neon:DscIndividualFieldDataIn](https://data.neonscience.org/DscIndividualFieldDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DscIndividualFieldDataIn&#124;uid:string%20%3F;siteID:string%20%3F;collectDate:time%20%3F;stationID:string%20%3F;startDate:time%20%3F;collectedBy:string%20%3F;dataQF:string%20%3F;averageVelocity:double%20%3F;bedVelocity:double%20%3F;edgeFactor:string%20%3F;fourFifthDepthVelocity:double%20%3F;lowVelocityQF:integer%20%3F;oneFifthDepthVelocity:double%20%3F;recorduid:string%20%3F;sectionArea:double%20%3F;sectionFlow:double%20%3F;stationNumber:integer%20%3F;streamProfilingMethod:string%20%3F;surfaceVelocity:double%20%3F;tapeDistance:double%20%3F;threeFifthDepthVelocity:double%20%3F;twoFifthDepthVelocity:double%20%3F;waterDepth:double%20%3F])

## Attributes


### Own

 * [averageVelocity](averageVelocity.md)  <sub>OPT</sub>
    * Description: Mean velocity from all measured points
    * range: [Double](types/Double.md)
 * [bedVelocity](bedVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at the bed
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
 * [edgeFactor](edgeFactor.md)  <sub>OPT</sub>
    * Description: Roughness factor used only for right angled cross sections
    * range: [String](types/String.md)
 * [fourFifthDepthVelocity](fourFifthDepthVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at 80 percent of the water depth from the bed
    * range: [Double](types/Double.md)
 * [lowVelocityQF](lowVelocityQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for reported velocity below the instrument detection limit
    * range: [Integer](types/Integer.md)
 * [oneFifthDepthVelocity](oneFifthDepthVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at 20 percent water depth from the bed
    * range: [Double](types/Double.md)
 * [recorduid](recorduid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the parent and associated child records
    * range: [String](types/String.md)
 * [sectionArea](sectionArea.md)  <sub>OPT</sub>
    * Description: Depth times width of the transect section
    * range: [Double](types/Double.md)
 * [sectionFlow](sectionFlow.md)  <sub>OPT</sub>
    * Description: Calculated flow of water for a section
    * range: [Double](types/Double.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [stationNumber](stationNumber.md)  <sub>OPT</sub>
    * Description: Numeric identified for station number
    * range: [Integer](types/Integer.md)
 * [streamProfilingMethod](streamProfilingMethod.md)  <sub>OPT</sub>
    * Description: Zero; one; two; three; five; or six point (velocity method - USGS and ISO)
    * range: [String](types/String.md)
 * [surfaceVelocity](surfaceVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at the surface
    * range: [Double](types/Double.md)
 * [tapeDistance](tapeDistance.md)  <sub>OPT</sub>
    * Description: Distance along a tape where the point measurement of velocity and depth were taken for a transect
    * range: [Double](types/Double.md)
 * [threeFifthDepthVelocity](threeFifthDepthVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at 60 percent of the water depth from the bed
    * range: [Double](types/Double.md)
 * [twoFifthDepthVelocity](twoFifthDepthVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at 40 percent of the water depth from the bed
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [waterDepth](waterDepth.md)  <sub>OPT</sub>
    * Description: Depth of water
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:dsc_individualFieldData_in |

