
# Type: mos_trapping_in




URI: [neon:MosTrappingIn](https://data.neonscience.org/MosTrappingIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MosTrappingIn&#124;uid:string%20%3F;plotID:string%20%3F;remarks:string%20%3F;recordedBy:string%20%3F;eventID:string%20%3F;enteredBy:string%20%3F;sampleID:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;targetTaxaPresent:string%20%3F;samplingProtocolVersion:string%20%3F;sampleTiming:string%20%3F;numVialsSampleID:string%20%3F;fanStatus:string%20%3F;catchCupStatus:string%20%3F;dryIceStatus:string%20%3F;pdaDecimalLatitude:double%20%3F;pdaDecimalLongitude:double%20%3F;pdaAccuracy:double%20%3F;pdaElevation:double%20%3F;nightOrDay:string%20%3F;trapHours:double%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;sampleCondition:string%20%3F;samplingImpractical:string%20%3F;fulcrumVersion:string%20%3F;platformInfo:string%20%3F])

## Attributes


### Own

 * [catchCupStatus](catchCupStatus.md)  <sub>OPT</sub>
    * Description: Indicator of the status of the trap catch cup at the time of sample collection
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [dryIceStatus](dryIceStatus.md)  <sub>OPT</sub>
    * Description: Dry ice status at the time of sample collection
    * range: [String](types/String.md)
 * [enteredBy](enteredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who entered the data
    * range: [String](types/String.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [fanStatus](fanStatus.md)  <sub>OPT</sub>
    * Description: Indicator of the status of the trap fan at the time of sample collection
    * range: [String](types/String.md)
 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [nightOrDay](nightOrDay.md)  <sub>OPT</sub>
    * Description: Whether sampling occurred primarily during the day or at night
    * range: [String](types/String.md)
 * [numVialsSampleID](numVialsSampleID.md)  <sub>OPT</sub>
    * Description: Number of vials associated with a sampleID
    * range: [String](types/String.md)
 * [pdaAccuracy](pdaAccuracy.md)  <sub>OPT</sub>
    * Description: The 68% confidence (1 standard deviation) horizontal distance (in meters) from the given pdaDecimalLatitude and pdaDecimalLongitude. If this location does not have an accuracy, then 0.0 is returned.
    * range: [Double](types/Double.md)
 * [pdaDecimalLatitude](pdaDecimalLatitude.md)  <sub>OPT</sub>
    * Description: The geographic latitude (in decimal degrees, WGS84) of the geographic center of the reference area as recorded by the PDA in the field
    * range: [Double](types/Double.md)
 * [pdaDecimalLongitude](pdaDecimalLongitude.md)  <sub>OPT</sub>
    * Description: The geographic longitude (in decimal degrees, WGS84) of the geographic center of the reference area as recorded by the PDA in the field
    * range: [Double](types/Double.md)
 * [pdaElevation](pdaElevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level as recorded by the PDA in the field
    * range: [Double](types/Double.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
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
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [sampleTiming](sampleTiming.md)  <sub>OPT</sub>
    * Description: Timing of the sampling event with regard to the field season
    * range: [String](types/String.md)
 * [samplingImpractical](samplingImpractical.md)  <sub>OPT</sub>
    * Description: Samples and/or measurements were not collected due to the indicated circumstance
    * range: [String](types/String.md)
 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [trapHours](trapHours.md)  <sub>OPT</sub>
    * Description: Number of hours between trap setting and collecting events
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mos_trapping_in |
| **In Subsets:** | | DP0.10043.001 |

