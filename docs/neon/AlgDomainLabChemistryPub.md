
# Type: alg_domainLabChemistry_pub




URI: [neon:AlgDomainLabChemistryPub](https://data.neonscience.org/AlgDomainLabChemistryPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AlgDomainLabChemistryPub&#124;uid:string%20%3F;domainID:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;measuredBy:string%20%3F;recordedBy:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;startDate:time%20%3F;boatMass:double%20%3F;dryMassBoatMass:double%20%3F;ashMassBoatMass:double%20%3F;storageDays:double%20%3F;adjAshFreeDryMass:double%20%3F;parentSampleID:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;fieldSampleVolume:double%20%3F;alternateFieldSampleVolume:double%20%3F;parentSampleCode:string%20%3F;labSampleVolume:double%20%3F;domainFilterVolume:double%20%3F;filterNumber:string%20%3F;preservativeType:string%20%3F;preservativeVolume:double%20%3F;sampleCondition:string%20%3F;plantDryMass:double%20%3F;plantSurfaceArea:double%20%3F;namedLocation:string%20%3F;analysisType:string%20%3F;originalFieldSampleVolume:double%20%3F;plantAdjAshFreeDryMass:double%20%3F;plantAshMassBoatMass:double%20%3F;plantBoatMass:double%20%3F;plantDryMassBoatMass:double%20%3F;filterBlankRep1:string%20%3F;filterBlankRep2:string%20%3F])

## Attributes


### Own

 * [adjAshFreeDryMass](adjAshFreeDryMass.md)  <sub>OPT</sub>
    * Description: Combusted mass of the sample, multiplied to account for lab subsampling
    * range: [Double](types/Double.md)
 * [alternateFieldSampleVolume](alternateFieldSampleVolume.md)  <sub>OPT</sub>
    * Description: Sample volume collected in the field, remeasured in the domain lab to account for any discrepancy or addition of sample due to porewater or other sampling factors
    * range: [Double](types/Double.md)
 * [analysisType](analysisType.md)  <sub>OPT</sub>
    * Description: Type of analysis at external lab
    * range: [String](types/String.md)
 * [ashMassBoatMass](ashMassBoatMass.md)  <sub>OPT</sub>
    * Description: Combusted mass of the sample and weigh boat
    * range: [Double](types/Double.md)
 * [boatMass](boatMass.md)  <sub>OPT</sub>
    * Description: Mass of the weigh boat
    * range: [Double](types/Double.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [domainFilterVolume](domainFilterVolume.md)  <sub>OPT</sub>
    * Description: Volume of material passed through filter at domain lab
    * range: [Double](types/Double.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [dryMassBoatMass](dryMassBoatMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of the sample and weigh boat
    * range: [Double](types/Double.md)
 * [fieldSampleVolume](fieldSampleVolume.md)  <sub>OPT</sub>
    * Description: Sample volume collected in the field
    * range: [Double](types/Double.md)
 * [filterBlankRep1](filterBlankRep1.md)  <sub>OPT</sub>
    * Description: Identifier for blank filter replicate 1
    * range: [String](types/String.md)
 * [filterBlankRep2](filterBlankRep2.md)  <sub>OPT</sub>
    * Description: Identifier for blank filter replicate 2
    * range: [String](types/String.md)
 * [filterNumber](filterNumber.md)  <sub>OPT</sub>
    * Description: Number of filter
    * range: [String](types/String.md)
 * [labSampleVolume](labSampleVolume.md)  <sub>OPT</sub>
    * Description: Sample volume subsampled in the lab
    * range: [Double](types/Double.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [originalFieldSampleVolume](originalFieldSampleVolume.md)  <sub>OPT</sub>
    * Description: Original sample volume collected in the field before adjustments
    * range: [Double](types/Double.md)
 * [parentSampleCode](parentSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a parent sample
    * range: [String](types/String.md)
 * [parentSampleID](parentSampleID.md)  <sub>OPT</sub>
    * Description: Parent sampleID of sample being processed
    * range: [String](types/String.md)
 * [plantAdjAshFreeDryMass](plantAdjAshFreeDryMass.md)  <sub>OPT</sub>
    * Description: Combusted mass of the sample, multiplied to account for lab subsampling for the whole plant from which the epiphyton samples are scraped
    * range: [Double](types/Double.md)
 * [plantAshMassBoatMass](plantAshMassBoatMass.md)  <sub>OPT</sub>
    * Description: Combusted mass of the sample and weigh boat for the whole plant from which the epiphyton samples are scraped
    * range: [Double](types/Double.md)
 * [plantBoatMass](plantBoatMass.md)  <sub>OPT</sub>
    * Description: Mass of the weigh boat for the whole plant from which the epiphyton samples are scraped
    * range: [Double](types/Double.md)
 * [plantDryMass](plantDryMass.md)  <sub>OPT</sub>
    * Description: Dry mass of plant(s) sampled
    * range: [Double](types/Double.md)
 * [plantDryMassBoatMass](plantDryMassBoatMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of the sample and weigh boat for the whole plant from which the epiphyton samples are scraped
    * range: [Double](types/Double.md)
 * [plantSurfaceArea](plantSurfaceArea.md)  <sub>OPT</sub>
    * Description: Estimated surface area of plant(s) sampled
    * range: [Double](types/Double.md)
 * [preservativeType](preservativeType.md)  <sub>OPT</sub>
    * Description: Type of preservative used in the sample
    * range: [String](types/String.md)
 * [preservativeVolume](preservativeVolume.md)  <sub>OPT</sub>
    * Description: Volume of preservative used in the sample
    * range: [Double](types/Double.md)
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
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [storageDays](storageDays.md)  <sub>OPT</sub>
    * Description: Total number of days clipped biomass was stored between collection and processing
    * range: [Double](types/Double.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:alg_domainLabChemistry_pub |

