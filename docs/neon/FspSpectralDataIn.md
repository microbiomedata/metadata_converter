
# Type: fsp_spectralData_in




URI: [neon:FspSpectralDataIn](https://data.neonscience.org/FspSpectralDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[FspSpectralDataIn&#124;uid:string%20%3F;remarks:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;locationID:string%20%3F;dataQF:string%20%3F;processedBy:string%20%3F;reviewedBy:string%20%3F;downloadFileName:string%20%3F;downloadFileUrl:string%20%3F;wavelength:double%20%3F;reflectance:double%20%3F;reflectanceCondition:string%20%3F;software:string%20%3F;spectralSampleCode:string%20%3F;spectralSampleCodeDataFrame:string%20%3F;spectralSampleFate:string%20%3F;spectralSampleID:string%20%3F;spectralSampleIDDataFrame:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [downloadFileName](downloadFileName.md)  <sub>OPT</sub>
    * Description: The name of the user-downloaded file that is linked to the record
    * range: [String](types/String.md)
 * [downloadFileUrl](downloadFileUrl.md)  <sub>OPT</sub>
    * Description: The URL of the file linked to the record
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [processedBy](processedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who processed the sample(s)
    * range: [String](types/String.md)
 * [reflectance](reflectance.md)  <sub>OPT</sub>
    * Description: Reflectance of sample
    * range: [Double](types/Double.md)
 * [reflectanceCondition](reflectanceCondition.md)  <sub>OPT</sub>
    * Description: Conditions under which reflectance measurement was made
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [reviewedBy](reviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed the data prior to submission
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [software](software.md)  <sub>OPT</sub>
    * Description: Name and version of the software used to process the data
    * range: [String](types/String.md)
 * [spectralSampleCode](spectralSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a spectral sample
    * range: [String](types/String.md)
 * [spectralSampleCodeDataFrame](spectralSampleCodeDataFrame.md)  <sub>OPT</sub>
    * Description: Barcode copy of spectral sample to a data frame column
    * range: [String](types/String.md)
 * [spectralSampleFate](spectralSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a spectral sample
    * range: [String](types/String.md)
 * [spectralSampleID](spectralSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a spectral sample
    * range: [String](types/String.md)
 * [spectralSampleIDDataFrame](spectralSampleIDDataFrame.md)  <sub>OPT</sub>
    * Description: Identifier copy of spectral sample to a data frame column
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [wavelength](wavelength.md)  <sub>OPT</sub>
    * Description: Wavelength of measurement
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:fsp_spectralData_in |

