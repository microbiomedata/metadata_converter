
# Type: sls_metagenomicsPooling_pub




URI: [neon:SlsMetagenomicsPoolingPub](https://data.neonscience.org/SlsMetagenomicsPoolingPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SlsMetagenomicsPoolingPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;samplingProtocolVersion:string%20%3F;sampleCondition:string%20%3F;processedBy:string%20%3F;namedLocation:string%20%3F;genomicsDataQF:string%20%3F;genomicsPooledCodeList:string%20%3F;genomicsPooledIDList:string%20%3F;genomicsSampleCode:string%20%3F;genomicsSampleID:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [genomicsDataQF](genomicsDataQF.md)  <sub>OPT</sub>
    * Description: Quality flag for genomics sample
    * range: [String](types/String.md)
 * [genomicsPooledCodeList](genomicsPooledCodeList.md)  <sub>OPT</sub>
    * Description: List of barcodes for pooled samples in a genomics sample
    * range: [String](types/String.md)
 * [genomicsPooledIDList](genomicsPooledIDList.md)  <sub>OPT</sub>
    * Description: List of sample identifiers pooled for a genomics sample
    * range: [String](types/String.md)
 * [genomicsSampleCode](genomicsSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a genomics sample
    * range: [String](types/String.md)
 * [genomicsSampleID](genomicsSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a genomics sample
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [processedBy](processedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who processed the sample(s)
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
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:sls_metagenomicsPooling_pub |

