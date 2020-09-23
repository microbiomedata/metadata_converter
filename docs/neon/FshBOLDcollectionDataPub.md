
# Type: fsh_BOLDcollectionData_pub




URI: [neon:FshBOLDcollectionDataPub](https://data.neonscience.org/FshBOLDcollectionDataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[FshBOLDcollectionDataPub&#124;uid:string%20%3F;samplingProtocol:string%20%3F;elevation:double%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;namedLocation:string%20%3F;collectionDateAccuracy:string%20%3F;collectionEventID:string%20%3F;collectionNotes:string%20%3F;collectors:string%20%3F;coordinateAccuracy:double%20%3F;countryOcean:string%20%3F;depth:double%20%3F;depthPrecision:double%20%3F;elevationPrecision:double%20%3F;eventTime:string%20%3F;exactSite:string%20%3F;gpsSource:string%20%3F;habitat:string%20%3F;latitude:double%20%3F;longitude:double%20%3F;region:string%20%3F;sector:string%20%3F;siteCode:string%20%3F;stateProvince:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [collectionDateAccuracy](collectionDateAccuracy.md)  <sub>OPT</sub>
    * Description: A numerical representation of the precision of the Collection Date given in days
    * range: [String](types/String.md)
 * [collectionEventID](collectionEventID.md)  <sub>OPT</sub>
    * Description: A optional event ID for submission purposes that allows for relational data support when multiple specimens are collected from a single site
    * range: [String](types/String.md)
 * [collectionNotes](collectionNotes.md)  <sub>OPT</sub>
    * Description: Comments or notes about the collection event
    * range: [String](types/String.md)
 * [collectors](collectors.md)  <sub>OPT</sub>
    * Description: The full or abbreviated names of the individuals or team responsible for collecting the sample in the field
    * range: [String](types/String.md)
 * [coordinateAccuracy](coordinateAccuracy.md)  <sub>OPT</sub>
    * Description: A decimal representation of the precision of the coordinates given in the decimalLatitude and decimalLongitude
    * range: [Double](types/Double.md)
 * [countryOcean](countryOcean.md)  <sub>OPT</sub>
    * Description: The full, unabbreviated name of the country, major political unit, or ocean in which the organism was collected
    * range: [String](types/String.md)
 * [depth](depth.md)  <sub>OPT</sub>
    * Description: For organisms collected beneath the surface of a water body
    * range: [Double](types/Double.md)
 * [depthPrecision](depthPrecision.md)  <sub>OPT</sub>
    * Description: A numerical representation of the precision of the depth given in meters and is represented as greater or less than the depth value
    * range: [Double](types/Double.md)
 * [elevation](elevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level
    * range: [Double](types/Double.md)
 * [elevationPrecision](elevationPrecision.md)  <sub>OPT</sub>
    * Description: A numerical representation of the precision of the elevation given in meters and is represented as greater or less than the elevation value
    * range: [Double](types/Double.md)
 * [eventTime](eventTime.md)  <sub>OPT</sub>
    * Description: The time or time of day during which the sample was collected
    * range: [String](types/String.md)
 * [exactSite](exactSite.md)  <sub>OPT</sub>
    * Description: Additional text descriptions regarding the exact location of the collection site relative to a geographic or biologically relevant landmark
    * range: [String](types/String.md)
 * [gpsSource](gpsSource.md)  <sub>OPT</sub>
    * Description: The source of the latitude and longitude measurements
    * range: [String](types/String.md)
 * [habitat](habitat.md)  <sub>OPT</sub>
    * Description: A category or description of the habitat in which the event occurred
    * range: [String](types/String.md)
 * [latitude](latitude.md)  <sub>OPT</sub>
    * Description: The geographic latitude (in decimal degrees) of the geographic center of a location
    * range: [Double](types/Double.md)
 * [longitude](longitude.md)  <sub>OPT</sub>
    * Description: The geographic longitude (in decimal degrees) of the geographic center of a location
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [region](region.md)  <sub>OPT</sub>
    * Description: The full, unabbreviated name of the county, shire, municipality, or park in which the organism was collected
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [samplingProtocol](samplingProtocol.md)  <sub>OPT</sub>
    * Description: The NEON document number where detailed information regarding the sampling method used is available; format NEON.DOC.######
    * range: [String](types/String.md)
 * [sector](sector.md)  <sub>OPT</sub>
    * Description: The full, unabbreviated name of the lake, conservation area or sector of park in which the organism was collected
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [siteCode](siteCode.md)  <sub>OPT</sub>
    * Description: The name of the sampling location
    * range: [String](types/String.md)
 * [stateProvince](stateProvince.md)  <sub>OPT</sub>
    * Description: State or province where data was collected
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:fsh_BOLDcollectionData_pub |

