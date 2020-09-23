
# Type: sdg_fieldDataProc_pub




URI: [neon:SdgFieldDataProcPub](https://data.neonscience.org/SdgFieldDataProcPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SdgFieldDataProcPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;collectDate:time%20%3F;processedDate:time%20%3F;startDate:time%20%3F;equilibratedAirSampleID:string%20%3F;referenceAirSampleID:string%20%3F;storageWaterTemp:double%20%3F;ptBarometricPressure:double%20%3F;waterVolumeSyringe:double%20%3F;gasVolumeSyringe:double%20%3F;gasVolumeSample:double%20%3F;lowGasVolumeQF:integer%20%3F;waterSampleID:string%20%3F;namedLocation:string%20%3F;equilibratedAirSampleCode:string%20%3F;referenceAirSampleCode:string%20%3F;sdgProcessDataQF:string%20%3F;waterSampleCode:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [equilibratedAirSampleCode](equilibratedAirSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for a sample of air that has been equilibrated with water (i.e., a mixture)
    * range: [String](types/String.md)
 * [equilibratedAirSampleID](equilibratedAirSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample of air that has been equilibrated with water (i.e., a mixture)
    * range: [String](types/String.md)
 * [gasVolumeSample](gasVolumeSample.md)  <sub>OPT</sub>
    * Description: Volume of sample gas injected into sample vial
    * range: [Double](types/Double.md)
 * [gasVolumeSyringe](gasVolumeSyringe.md)  <sub>OPT</sub>
    * Description: Volume of air in syringe
    * range: [Double](types/Double.md)
 * [lowGasVolumeQF](lowGasVolumeQF.md)  <sub>OPT</sub>
    * Description: Quality flag for low gas volume injected into evacuated vial
    * range: [Integer](types/Integer.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [processedDate](processedDate.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event
    * range: [Time](types/Time.md)
 * [ptBarometricPressure](ptBarometricPressure.md)  <sub>OPT</sub>
    * Description: Point (pt)-based barometric pressure, measured by a handheld device during sampling activity
    * range: [Double](types/Double.md)
 * [referenceAirSampleCode](referenceAirSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for sample of reference air
    * range: [String](types/String.md)
 * [referenceAirSampleID](referenceAirSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample of reference air
    * range: [String](types/String.md)
 * [sdgProcessDataQF](sdgProcessDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for dissolved gas field processing
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [storageWaterTemp](storageWaterTemp.md)  <sub>OPT</sub>
    * Description: Temperature of storage water
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [waterSampleCode](waterSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for the water sample to be equilibrated with air
    * range: [String](types/String.md)
 * [waterSampleID](waterSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the water sample to be equilibrated with air
    * range: [String](types/String.md)
 * [waterVolumeSyringe](waterVolumeSyringe.md)  <sub>OPT</sub>
    * Description: Volume of water in syringe
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sdg_fieldDataProc_pub |

