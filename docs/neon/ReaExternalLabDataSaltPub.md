
# Type: rea_externalLabDataSalt_pub




URI: [neon:ReaExternalLabDataSaltPub](https://data.neonscience.org/ReaExternalLabDataSaltPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ReaExternalLabDataSaltPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;laboratoryName:string%20%3F;receivedBy:string%20%3F;shipmentID:string%20%3F;analyte:string%20%3F;receivedDate:time%20%3F;analysisDate:time%20%3F;analyzedBy:string%20%3F;sampleCode:string%20%3F;sampleCondition:string%20%3F;namedLocation:string%20%3F;externalLabSaltDataQF:string%20%3F;finalConcentration:double%20%3F;saltBelowDetectionQF:integer%20%3F;saltSampleID:string%20%3F;saltCheckStandardPercentDev:double%20%3F;saltCheckStandardQF:integer%20%3F])

## Attributes


### Own

 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
 * [analyte](analyte.md)  <sub>OPT</sub>
    * Description: Analyte or parameter measured
    * range: [String](types/String.md)
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [externalLabSaltDataQF](externalLabSaltDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for external lab salt data
    * range: [String](types/String.md)
 * [finalConcentration](finalConcentration.md)  <sub>OPT</sub>
    * Description: Concentration that has ben adjusted for any dilution during analysis
    * range: [Double](types/Double.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [receivedBy](receivedBy.md)  <sub>OPT</sub>
    * Description: Anonymized name of lab personnel receiving the shipment
    * range: [String](types/String.md)
 * [receivedDate](receivedDate.md)  <sub>OPT</sub>
    * Description: Date a sample was received
    * range: [Time](types/Time.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [saltBelowDetectionQF](saltBelowDetectionQF.md)  <sub>OPT</sub>
    * Description: finalConcentration below the detection limit. 1=less than detection limit; 0=greater than or equal to detection limit; -1=NA (i.e. could not be run)
    * range: [Integer](types/Integer.md)
 * [saltCheckStandardPercentDev](saltCheckStandardPercentDev.md)  <sub>OPT</sub>
    * Description: Calculated percent deviation of the run for the salt check standards
    * range: [Double](types/Double.md)
 * [saltCheckStandardQF](saltCheckStandardQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating when the salt check standard percent deviation is above 2 %; 0 indicates percent deviation less than 2 %; 1 indicates percent deviation 2 % or above; and -1 indicates that the test could not be performed
    * range: [Integer](types/Integer.md)
 * [saltSampleID](saltSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for reaeration salt sample
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [shipmentID](shipmentID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with shipment
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
| **Mappings:** | | neon:rea_externalLabDataSalt_pub |

