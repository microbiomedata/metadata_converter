
# Type: brd_personnel_pub




URI: [neon:BrdPersonnelPub](https://data.neonscience.org/BrdPersonnelPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BrdPersonnelPub&#124;uid:string%20%3F;siteID:string%20%3F;date:time%20%3F;endDate:time%20%3F;laboratoryName:string%20%3F;observerInstitutionName:string%20%3F;technicianID:string%20%3F;evaluationMethod:string%20%3F;evaluationScore:string%20%3F;dataQF:string%20%3F])

## Attributes


### Own

 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [date](date.md)  <sub>OPT</sub>
    * Description: Date or date and time of measurement, observation, or collection event
    * range: [Time](types/Time.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [evaluationMethod](evaluationMethod.md)  <sub>OPT</sub>
    * Description: Method of evaluation for technician
    * range: [String](types/String.md)
 * [evaluationScore](evaluationScore.md)  <sub>OPT</sub>
    * Description: Score for the evaluation method
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [observerInstitutionName](observerInstitutionName.md)  <sub>OPT</sub>
    * Description: The name of the institution with which the observer is affiliated
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [technicianID](technicianID.md)  <sub>OPT</sub>
    * Description: Unique identifier for technician
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:brd_personnel_pub |
| **In Subsets:** | | DP1.10003.001 |

