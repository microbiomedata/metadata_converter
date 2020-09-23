
# Type: sdg_fieldDataProc_in




URI: [neon:SdgFieldDataProcIn](https://data.neonscience.org/SdgFieldDataProcIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SdgFieldDataProcIn&#124;uid:string%20%3F;remarks:string%20%3F;collectDate:time%20%3F;stationID:string%20%3F;processedDate:time%20%3F;startDate:time%20%3F;equilibratedAirSampleID:string%20%3F;referenceAirSampleID:string%20%3F;storageWaterTemp:double%20%3F;ptBarometricPressure:double%20%3F;waterVolumeSyringe:double%20%3F;gasVolumeSyringe:double%20%3F;gasVolumeSample:double%20%3F;lowGasVolumeQF:integer%20%3F;waterSampleID:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F;equilibratedAirSampleCode:string%20%3F;equilibratedAirSampleCond:string%20%3F;equilibratedAirSampleFate:string%20%3F;referenceAirSampleCode:string%20%3F;referenceAirSampleCond:string%20%3F;referenceAirSampleFate:string%20%3F;sdgProcessDataQF:string%20%3F;waterSampleCode:string%20%3F;waterSampleFate:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [equilibratedAirSampleCode](equilibratedAirSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for a sample of air that has been equilibrated with water (i.e., a mixture)
    * range: [String](types/String.md)
 * [equilibratedAirSampleCond](equilibratedAirSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of the sample of air that has been equilibrated with water (i.e. a mixture)
    * range: [String](types/String.md)
 * [equilibratedAirSampleFate](equilibratedAirSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample of air that has been equilibrated with water (i.e., a mixture)
    * range: [String](types/String.md)
 * [equilibratedAirSampleID](equilibratedAirSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample of air that has been equilibrated with water (i.e., a mixture)
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
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
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
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
 * [referenceAirSampleCond](referenceAirSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of the reference air sample
    * range: [String](types/String.md)
 * [referenceAirSampleFate](referenceAirSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample of reference air
    * range: [String](types/String.md)
 * [referenceAirSampleID](referenceAirSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample of reference air
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sdgProcessDataQF](sdgProcessDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for dissolved gas field processing
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [storageWaterTemp](storageWaterTemp.md)  <sub>OPT</sub>
    * Description: Temperature of storage water
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [waterSampleCode](waterSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for the water sample to be equilibrated with air
    * range: [String](types/String.md)
 * [waterSampleFate](waterSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of the water sample to be equilibrated with air
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
| **Mappings:** | | neon:sdg_fieldDataProc_in |

