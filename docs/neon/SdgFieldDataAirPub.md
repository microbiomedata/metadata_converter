
# Type: sdg_fieldDataAir_pub




URI: [neon:SdgFieldDataAirPub](https://data.neonscience.org/SdgFieldDataAirPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SdgFieldDataAirPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;referenceAirSampleID:string%20%3F;airVolumeSample:double%20%3F;lowAirVolumeQF:integer%20%3F;namedLocation:string%20%3F;referenceAirSampleCode:string%20%3F;sdgAirDataQF:string%20%3F])

## Attributes


### Own

 * [airVolumeSample](airVolumeSample.md)  <sub>OPT</sub>
    * Description: Volume of background air injected into sample vial
    * range: [Double](types/Double.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [lowAirVolumeQF](lowAirVolumeQF.md)  <sub>OPT</sub>
    * Description: Quality flag for low air volume injected into evacuated vial
    * range: [Integer](types/Integer.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [referenceAirSampleCode](referenceAirSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for sample of reference air
    * range: [String](types/String.md)
 * [referenceAirSampleID](referenceAirSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample of reference air
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sdgAirDataQF](sdgAirDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for dissolved gas reference air collection
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sdg_fieldDataAir_pub |

