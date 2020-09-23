
# Type: sls_metagenomicsPooling_in




URI: [neon:SlsMetagenomicsPoolingIn](https://data.neonscience.org/SlsMetagenomicsPoolingIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SlsMetagenomicsPoolingIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;recordedBy:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;samplingProtocolVersion:string%20%3F;sampleCondition:string%20%3F;compositeSampleCode:string%20%3F;compositeSampleFate:string%20%3F;compositeSampleID:string%20%3F;horizon:string%20%3F;processedBy:string%20%3F;toCompositeBarcodeList:string%20%3F;toCompositeFateList:string%20%3F;toCompositeSampleIDList:string%20%3F;genomicsDataQF:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [compositeSampleCode](compositeSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode for a sample that is a composite of field collected material
    * range: [String](types/String.md)
 * [compositeSampleFate](compositeSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample that is a composite of field collected material
    * range: [String](types/String.md)
 * [compositeSampleID](compositeSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for a sample that is a composite of field collected material
    * range: [String](types/String.md)
 * [genomicsDataQF](genomicsDataQF.md)  <sub>OPT</sub>
    * Description: Quality flag for genomics sample
    * range: [String](types/String.md)
 * [horizon](horizon.md)  <sub>OPT</sub>
    * Description: Organic or mineral soil
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [processedBy](processedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who processed the sample(s)
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [toCompositeBarcodeList](toCompositeBarcodeList.md)  <sub>OPT</sub>
    * Description: List of barcodes of composite samples in a pooled sample
    * range: [String](types/String.md)
 * [toCompositeFateList](toCompositeFateList.md)  <sub>OPT</sub>
    * Description: List of fates of composite samples in a pooled sample
    * range: [String](types/String.md)
 * [toCompositeSampleIDList](toCompositeSampleIDList.md)  <sub>OPT</sub>
    * Description: List of composite identifiers in a pooled sample
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sls_metagenomicsPooling_in |

