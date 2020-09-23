
# Type: geo_resultsFile_in




URI: [neon:GeoResultsFileIn](https://data.neonscience.org/GeoResultsFileIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GeoResultsFileIn&#124;uid:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;locationID:string%20%3F;dataQF:string%20%3F;rawDataFileName:string%20%3F;rawDataFilePath:string%20%3F;dataFileName:string%20%3F;dataFilePath:string%20%3F;sopVersion:string%20%3F])

## Attributes


### Own

 * [dataFileName](dataFileName.md)  <sub>OPT</sub>
    * Description: Name of file or folder containing data, including file extension
    * range: [String](types/String.md)
 * [dataFilePath](dataFilePath.md)  <sub>OPT</sub>
    * Description: The system path identifying the data file location
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [rawDataFileName](rawDataFileName.md)  <sub>OPT</sub>
    * Description: Name of file or folder containing raw data, including file extension
    * range: [String](types/String.md)
 * [rawDataFilePath](rawDataFilePath.md)  <sub>OPT</sub>
    * Description: The system path identifying the raw data file location
    * range: [String](types/String.md)
 * [sopVersion](sopVersion.md)  <sub>OPT</sub>
    * Description: Version of the SOP used to create the final data
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
| **Mappings:** | | neon:geo_resultsFile_in |

