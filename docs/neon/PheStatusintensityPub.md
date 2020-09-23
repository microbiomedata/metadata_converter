
# Type: phe_statusintensity_pub




URI: [neon:PheStatusintensityPub](https://data.neonscience.org/PheStatusintensityPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PheStatusintensityPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;plotID:string%20%3F;date:time%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;individualID:string%20%3F;growthForm:string%20%3F;phenophaseName:string%20%3F;phenophaseStatus:string%20%3F;phenophaseIntensityDefinition:string%20%3F;phenophaseIntensity:string%20%3F;dayOfYear:string%20%3F;endDate:time%20%3F;samplingProtocolVersion:string%20%3F;dataQF:string%20%3F;namedLocation:string%20%3F;editedDate:time%20%3F;individualBarcode:string%20%3F])

## Attributes


### Own

 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [date](date.md)  <sub>OPT</sub>
    * Description: Date or date and time of measurement, observation, or collection event
    * range: [Time](types/Time.md)
 * [dayOfYear](dayOfYear.md)  <sub>OPT</sub>
    * Description: The ordinal day of the year on which the object or observation was collected_(1 for January 1, 365 for December 31, except in a leap year, in which case it is 366)
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [editedDate](editedDate.md)  <sub>OPT</sub>
    * Description: The date-time that record was edited
    * range: [Time](types/Time.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [growthForm](growthForm.md)  <sub>OPT</sub>
    * Description: The growth form classification
    * range: [String](types/String.md)
 * [individualBarcode](individualBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a tagged individual
    * range: [String](types/String.md)
 * [individualID](individualID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier for an individual: NEON.MOD.D##.######
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [phenophaseIntensity](phenophaseIntensity.md)  <sub>OPT</sub>
    * Description: Intensity value range for the corresponding phenophase
    * range: [String](types/String.md)
 * [phenophaseIntensityDefinition](phenophaseIntensityDefinition.md)  <sub>OPT</sub>
    * Description: Quantity monitored for evaluating phenophase intensity, derived from NPN intensity questions
    * range: [String](types/String.md)
 * [phenophaseName](phenophaseName.md)  <sub>OPT</sub>
    * Description: Name of phenophase following NPN definitions
    * range: [String](types/String.md)
 * [phenophaseStatus](phenophaseStatus.md)  <sub>OPT</sub>
    * Description: Status of the phenophase: yes, no, uncertain or missed
    * range: [String](types/String.md)
 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:phe_statusintensity_pub |

