
# Type: mam_BOLDvoucherInfo_pub




URI: [neon:MamBOLDvoucherInfoPub](https://data.neonscience.org/MamBOLDvoucherInfoPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MamBOLDvoucherInfoPub&#124;uid:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;fieldID:string%20%3F;namedLocation:string%20%3F;collectionCode:string%20%3F;institutionStoring:string%20%3F;museumID:string%20%3F])

## Attributes


### Own

 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [collectionCode](collectionCode.md)  <sub>OPT</sub>
    * Description: Code associated with a given collection within an institution. The Collection Code is used in conjunction with Museum ID in order to disambiguate a ID that might be used in different collections within the same institution
    * range: [String](types/String.md)
 * [fieldID](fieldID.md)  <sub>OPT</sub>
    * Description: Identifier for sample generated in the field
    * range: [String](types/String.md)
 * [institutionStoring](institutionStoring.md)  <sub>OPT</sub>
    * Description: The full name of the institution that has physical possession of the voucher specimen
    * range: [String](types/String.md)
 * [museumID](museumID.md)  <sub>OPT</sub>
    * Description: Identifier for specimen assigned by formal collection upon accessioning, also referred to as the catalog number (format Institution acronym:collection code:catalog number)
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mam_BOLDvoucherInfo_pub |
| **In Subsets:** | | DP1.10076.001 |

