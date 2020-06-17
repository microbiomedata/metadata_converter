
# Type: mos_archivepooling_in




URI: [neon:MosArchivepoolingIn](https://data.neonscience.org/MosArchivepoolingIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Inherited from amc_fieldCellCounts_in:

 * [parentSampleFate](parentSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a parent sample
    * range: [String](types/String.md)
    * inherited from: None
 * [archiveFilteredSampleVolume](archiveFilteredSampleVolume.md)  <sub>OPT</sub>
    * Description: Volume of water filtered for microbial archive
    * range: [String](types/String.md)
    * inherited from: None
 * [archiveSampleCode](archiveSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of archive sample
    * range: [String](types/String.md)
 * [archiveSampleCond](archiveSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of the archive sample
    * range: [String](types/String.md)
    * inherited from: None
 * [cellCountLabSampleMedium](cellCountLabSampleMedium.md)  <sub>OPT</sub>
    * Description: Physical form of the cell count specimen
    * range: [String](types/String.md)
    * inherited from: None
 * [cellCountPreservantVolume](cellCountPreservantVolume.md)  <sub>OPT</sub>
    * Description: Volume of preservative added to cell count sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cellCountSampleCond](cellCountSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of the cell count sample
    * range: [String](types/String.md)
    * inherited from: None
 * [cellCountSampleVolume](cellCountSampleVolume.md)  <sub>OPT</sub>
    * Description: Volume of water collected for cell count analysis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [geneticFilteredSampleVolume](geneticFilteredSampleVolume.md)  <sub>OPT</sub>
    * Description: Volume of filtered water for genetic analysis of microbes
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticLabSampleMedium](geneticLabSampleMedium.md)  <sub>OPT</sub>
    * Description: Physical form of the genetic specimen
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticSampleCond](geneticSampleCond.md)  <sub>OPT</sub>
    * Description: Condition of the genetic sample
    * range: [String](types/String.md)
    * inherited from: None
 * [archiveLabSampleMedium](archiveLabSampleMedium.md)  <sub>OPT</sub>
    * Description: Physical form of the archive specimen
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from apl_biomass_pub:

 * [processingDate](processingDate.md)  <sub>OPT</sub>
    * Description: Date that sample was processed (i.e., sorted or pinned) in the domain lab
    * range: [Time](types/Time.md)
 * [dryMass](dryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of sample or subsample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [wetMass](wetMass.md)  <sub>OPT</sub>
    * Description: Fresh mass of the sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [wetMassSubsample](wetMassSubsample.md)  <sub>OPT</sub>
    * Description: Fresh mass of the subsample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [boatMass](boatMass.md)  <sub>OPT</sub>
    * Description: Mass of the weigh boat
    * range: [Double](types/Double.md)
    * inherited from: None
 * [dryMassBoatMass](dryMassBoatMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of the sample and weigh boat
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ashMassBoatMass](ashMassBoatMass.md)  <sub>OPT</sub>
    * Description: Combusted mass of the sample and weigh boat
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fieldID](fieldID.md)  <sub>OPT</sub>
    * Description: Identifier for sample generated in the field
    * range: [String](types/String.md)
    * inherited from: None
 * [benthicArea](benthicArea.md)  <sub>OPT</sub>
    * Description: Area of the benthos sampled
    * range: [Double](types/Double.md)
    * inherited from: None
 * [adjDryMass](adjDryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of the sample, multiplied to account for lab subsampling
    * range: [Double](types/Double.md)
    * inherited from: None
 * [adjAshFreeDryMass](adjAshFreeDryMass.md)  <sub>OPT</sub>
    * Description: Combusted mass of the sample, multiplied to account for lab subsampling
    * range: [Double](types/Double.md)
    * inherited from: None
 * [arealAdjDryMass](arealAdjDryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of the sample, multiplied to account for lab subsampling and the area sampled based on samplerType
    * range: [Double](types/Double.md)
    * inherited from: None
 * [arealAdjAshFreeDryMass](arealAdjAshFreeDryMass.md)  <sub>OPT</sub>
    * Description: Combusted mass of the sample, multiplied to account for lab subsampling and the area sampled based on samplerType
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chemSubsampleID](chemSubsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with chemistry subsample per sampleID
    * range: [String](types/String.md)
    * inherited from: None
 * [chemSubsampleBarcode](chemSubsampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of chemistry subsample
    * range: [String](types/String.md)
    * inherited from: None
 * [fieldIDCode](fieldIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of a fieldID
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from csd_pressureGaugeRelationship_pub:

 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
    * inherited from: None
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
    * inherited from: None
 * [assetID](assetID.md)  <sub>OPT</sub>
    * Description: MxAssetID from the calibration file
    * range: [String](types/String.md)
    * inherited from: None
 * [calCertificateFile](calCertificateFile.md)  <sub>OPT</sub>
    * Description: Calibration certificate file
    * range: [String](types/String.md)
    * inherited from: None
 * [calculatedStage](calculatedStage.md)  <sub>OPT</sub>
    * Description: Stage calculated from the sum of the water column height and sensorStaffGaugeOffset
    * range: [Double](types/Double.md)
    * inherited from: None
 * [calcWaterColumnHeight](calcWaterColumnHeight.md)  <sub>OPT</sub>
    * Description: Calculated water column height based off of the calibratedPressMean
    * range: [Double](types/Double.md)
    * inherited from: None
 * [calibratedPressMean](calibratedPressMean.md)  <sub>OPT</sub>
    * Description: Mean calibrated surface water pressure
    * range: [Double](types/Double.md)
    * inherited from: None
 * [calibratedPressObsCount](calibratedPressObsCount.md)  <sub>OPT</sub>
    * Description: Number of observations included in the calibratedPressMean
    * range: [Double](types/Double.md)
    * inherited from: None
 * [calibratedPressStdDev](calibratedPressStdDev.md)  <sub>OPT</sub>
    * Description: Stanrdard deviation of calibrated surface water pressure
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gaugeHeight](gaugeHeight.md)  <sub>OPT</sub>
    * Description: Height of water at staff gauge
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sensorStaffGaugeOffset](sensorStaffGaugeOffset.md)  <sub>OPT</sub>
    * Description: Offset between the pressure sensor and the staff gauge; i.e. the staff gauge reading when the water level is just at a reading of 0 pressure
    * range: [Double](types/Double.md)
    * inherited from: None
 * [calibrationID](calibrationID.md)  <sub>OPT</sub>
    * Description: Calibration ID that corresponds to the ID assigned by CI to a set of calibration factors for a measurement stream
    * range: [String](types/String.md)
    * inherited from: None
 * [gaugeCollectDate](gaugeCollectDate.md)  <sub>OPT</sub>
    * Description: Date of the gauge height reading collection event
    * range: [String](types/String.md)
    * inherited from: None
 * [stationHorizontalID](stationHorizontalID.md)  <sub>OPT</sub>
    * Description: Horizontal code for station
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from inv_dnaExtractionStandard_pub:

 * [deprecatedVialID](deprecatedVialID.md)  <sub>OPT</sub>
    * Description: Identifier on vial label, if different from standard ID
    * range: [String](types/String.md)
 * [geneticSampleID](geneticSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for the genetic sample
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticSampleCode](geneticSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a genetic sample
    * range: [String](types/String.md)
    * inherited from: None
 * [nucleicAcidConcentration](nucleicAcidConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of extracted nucleic acids
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sampleMaterial](sampleMaterial.md)  <sub>OPT</sub>
    * Description: The material in which a sample was embedded prior to the sampling event
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleMass](sampleMass.md)  <sub>OPT</sub>
    * Description: Mass of sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [dnaPooledStatus](dnaPooledStatus.md)  <sub>OPT</sub>
    * Description: Indicates whether multiple DNA extracts were pooled
    * range: [String](types/String.md)
    * inherited from: None
 * [dnaProcessedBy](dnaProcessedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the individual who processed the sample(s)
    * range: [String](types/String.md)
    * inherited from: None
 * [nucleicAcidQuantMethod](nucleicAcidQuantMethod.md)  <sub>OPT</sub>
    * Description: Nucleic acid quantitative method
    * range: [String](types/String.md)
    * inherited from: None
 * [nucleicAcidPurity](nucleicAcidPurity.md)  <sub>OPT</sub>
    * Description: Purity of nucleic acid sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [standardCreationLocation](standardCreationLocation.md)  <sub>OPT</sub>
    * Description: Name of the location where the standard sample was created
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from inv_dnaStandardTaxon_pub:

 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [createdBy](createdBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who created the record
    * range: [String](types/String.md)
    * inherited from: None
 * [dnaStandardSampleCode](dnaStandardSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of DNA standard sample
    * range: [String](types/String.md)
    * inherited from: None
 * [dnaStandardSampleID](dnaStandardSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for the DNA standard sample
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from ltr_chemistrySubsampling_in:

 * [cnSampleFate](cnSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a carbon-nitrogen sample
    * range: [String](types/String.md)
    * inherited from: None
 * [archiveSampleFate](archiveSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of archived sample
    * range: [String](types/String.md)
 * [massSampleFateList](massSampleFateList.md)  <sub>OPT</sub>
    * Description: List of fates of mass samples
    * range: [String](types/String.md)
    * inherited from: None
 * [massSampleMixtureFate](massSampleMixtureFate.md)  <sub>OPT</sub>
    * Description: Fate of mixture of mass samples
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from mam_barcoding_in:

 * [specimenSource](specimenSource.md)  <sub>OPT</sub>
    * Description: Physical source from which individual was obtained
    * range: [String](types/String.md)
    * inherited from: None
 * [archiveID](archiveID.md)  <sub>OPT</sub>
    * Description: Identifier for the archive sample
    * range: [String](types/String.md)
 * [archiveLaboratoryName](archiveLaboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the archive sample
    * range: [String](types/String.md)
    * inherited from: None
 * [archiveFacilityID](archiveFacilityID.md)  <sub>OPT</sub>
    * Description: Identifier at archive facility
    * range: [String](types/String.md)
 * [associatedSpecimens](associatedSpecimens.md)  <sub>OPT</sub>
    * Description: A list of specimens associated with the subject specimen at the time of its collection. References to other specimen identifiers should be preceded by the relationship
    * range: [String](types/String.md)
    * inherited from: None
 * [associatedTaxa](associatedTaxa.md)  <sub>OPT</sub>
    * Description: A list of taxa associated with the taxon at the time of its collection. References to taxa are preceded by the relationship
    * range: [String](types/String.md)
    * inherited from: None
 * [externalURLs](externalURLs.md)  <sub>OPT</sub>
    * Description: Pipe-delimited list of web accessible links that provide additional information about the specimen
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleStatus](sampleStatus.md)  <sub>OPT</sub>
    * Description: Status of sample for downstream processing and/or analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [wellCoordinates](wellCoordinates.md)  <sub>OPT</sub>
    * Description: Location of sample in multi-well storage box or plate
    * range: [String](types/String.md)
    * inherited from: None
 * [identifier](identifier.md)  <sub>OPT</sub>
    * Description: Full name of primary individual who assigned the specimen to a taxonomic group
    * range: [String](types/String.md)
    * inherited from: None
 * [identifierEmail](identifierEmail.md)  <sub>OPT</sub>
    * Description: E-mail address of the primary identifier
    * range: [String](types/String.md)
    * inherited from: None
 * [identifierInstitution](identifierInstitution.md)  <sub>OPT</sub>
    * Description: The full name of the institutional or organizational affiliation of the identifier
    * range: [String](types/String.md)
    * inherited from: None
 * [reproduction](reproduction.md)  <sub>OPT</sub>
    * Description: The presumed method of reproduction
    * range: [String](types/String.md)
    * inherited from: None
 * [trappingDays](trappingDays.md)  <sub>OPT</sub>
    * Description: Decimal days between trap setting and collecting events
    * range: [Double](types/Double.md)
    * inherited from: None
 * [depth](depth.md)  <sub>OPT</sub>
    * Description: For organisms collected beneath the surface of a water body
    * range: [Double](types/Double.md)
    * inherited from: None
 * [depthPrecision](depthPrecision.md)  <sub>OPT</sub>
    * Description: A numerical representation of the precision of the depth given in meters and is represented as greater or less than the depth value
    * range: [Double](types/Double.md)
    * inherited from: None
 * [eventTime](eventTime.md)  <sub>OPT</sub>
    * Description: The time or time of day during which the sample was collected
    * range: [String](types/String.md)
    * inherited from: None
 * [netDepth](netDepth.md)  <sub>OPT</sub>
    * Description: Deployment depth of the net
    * range: [Double](types/Double.md)
    * inherited from: None
 * [plateID](plateID.md)  <sub>OPT</sub>
    * Description: Identifier of the multi-well storage plate
    * range: [String](types/String.md)
    * inherited from: None
 * [BOLDsequenceURL](BOLDsequenceURL.md)  <sub>OPT</sub>
    * Description: Sequence from BOLD
    * range: [String](types/String.md)
    * inherited from: None
 * [BOLDtraceURL](BOLDtraceURL.md)  <sub>OPT</sub>
    * Description: Trace from BOLD
    * range: [String](types/String.md)
    * inherited from: None
 * [NEONsequenceURL](NEONsequenceURL.md)  <sub>OPT</sub>
    * Description: Sequence from BOLD hosted in NEON ECS
    * range: [String](types/String.md)
    * inherited from: None
 * [NEONtraceURL](NEONtraceURL.md)  <sub>OPT</sub>
    * Description: Trace from BOLD hosted in NEON ECS
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from mos_archivepooling_pub:

 * [archiveVialIDList](archiveVialIDList.md)  <sub>OPT</sub>
    * Description: Identifier(s) for the vial(s) containing specimens for archive
    * range: [String](types/String.md)
 * [archivedCount](archivedCount.md)  <sub>OPT</sub>
    * Description: Number of individuals in the archive vial
    * range: [String](types/String.md)
 * [archiveIDCode](archiveIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of the Archive sample
    * range: [String](types/String.md)

### Inherited from mos_pathogenresults_pub:

 * [testingVialID](testingVialID.md)  <sub>OPT</sub>
    * Description: Identifier for the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
    * range: [String](types/String.md)
    * inherited from: None
 * [testNumber](testNumber.md)  <sub>OPT</sub>
    * Description: Test number in a sequence of tests
    * range: [String](types/String.md)
    * inherited from: None
 * [finalResult](finalResult.md)  <sub>OPT</sub>
    * Description: Whether or not this is the conclusive test result for this sample
    * range: [String](types/String.md)
    * inherited from: None
 * [locus](locus.md)  <sub>OPT</sub>
    * Description: Name of genetic marker sequenced
    * range: [String](types/String.md)
    * inherited from: None
 * [percentIdentity](percentIdentity.md)  <sub>OPT</sub>
    * Description: Percent match between sample and reference sequence
    * range: [String](types/String.md)
    * inherited from: None
 * [sequenceDatabase](sequenceDatabase.md)  <sub>OPT</sub>
    * Description: Name of database where sequence is stored
    * range: [String](types/String.md)
    * inherited from: None
 * [sequenceDatabaseID](sequenceDatabaseID.md)  <sub>OPT</sub>
    * Description: Identifier for sample in sequence database
    * range: [String](types/String.md)
    * inherited from: None
 * [extractDepleted](extractDepleted.md)  <sub>OPT</sub>
    * Description: Whether or not sample extract is depleted
    * range: [String](types/String.md)
    * inherited from: None
 * [startCollectDate](startCollectDate.md)  <sub>OPT</sub>
    * Description: Earliest known collection date for this sample
    * range: [Time](types/Time.md)
 * [endCollectDate](endCollectDate.md)  <sub>OPT</sub>
    * Description: Latest known collection date for this sample
    * range: [Time](types/Time.md)
 * [testingVialIDCode](testingVialIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from scs_archivedata_in:

 * [archiveMedium](archiveMedium.md)  <sub>OPT</sub>
    * Description: Method of preservation for the sample or specimen
    * range: [String](types/String.md)
 * [archiveGuid](archiveGuid.md)  <sub>OPT</sub>
    * Description: Globally unique identifier for the archive sample
    * range: [String](types/String.md)
    * inherited from: None
 * [archiveSampleClass](archiveSampleClass.md)  <sub>OPT</sub>
    * Description: Class of an archive sample
    * range: [String](types/String.md)
    * inherited from: None
 * [storageTemperature](storageTemperature.md)  <sub>OPT</sub>
    * Description: The temperature in Centigrade at which the sample is to be stored at the archive facility
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from spc_perbiogeosample_in:

 * [labProjID](labProjID.md)  <sub>OPT</sub>
    * Description: Identifier for soil physical properties analyses
    * range: [String](types/String.md)
    * inherited from: None
 * [biogeoTotWeight](biogeoTotWeight.md)  <sub>OPT</sub>
    * Description: Total dry weight of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoTotWeight2To5](biogeoTotWeight2To5.md)  <sub>OPT</sub>
    * Description: Total dry weight of the 2-5 mm size fraction of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoTotWeight5To20](biogeoTotWeight5To20.md)  <sub>OPT</sub>
    * Description: Total dry weight of the 5-20 mm size fraction of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoTotWeight20To75](biogeoTotWeight20To75.md)  <sub>OPT</sub>
    * Description: Total dry weight of the 20-75 mm size fraction of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gypsum](gypsum.md)  <sub>OPT</sub>
    * Description: Gypsum content of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [caco3](caco3.md)  <sub>OPT</sub>
    * Description: Carbonate content of the <2 mm fraction experssed as calcium carbonate
    * range: [Double](types/Double.md)
    * inherited from: None
 * [caNh4d](caNh4d.md)  <sub>OPT</sub>
    * Description: Ammonium acetate extractable Calcium from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [kNh4d](kNh4d.md)  <sub>OPT</sub>
    * Description: Ammonium acetate extractable potassium from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [mgNh4d](mgNh4d.md)  <sub>OPT</sub>
    * Description: Ammonium acetate extractable magnesium from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [naNh4d](naNh4d.md)  <sub>OPT</sub>
    * Description: Ammonium acetate extractable sodium from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cecdNh4](cecdNh4.md)  <sub>OPT</sub>
    * Description: Ammonium acetate cation exchange capacity (CEC) of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [alSatCecd33](alSatCecd33.md)  <sub>OPT</sub>
    * Description: Aluminum saturation of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [baseSumCecd10](baseSumCecd10.md)  <sub>OPT</sub>
    * Description: Sum of Ammonium acetate extractable bases from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bsesatCecd10](bsesatCecd10.md)  <sub>OPT</sub>
    * Description: Base saturation of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ececCecd33](ececCecd33.md)  <sub>OPT</sub>
    * Description: Effective cation exchange capacity (CEC) of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [alKcl](alKcl.md)  <sub>OPT</sub>
    * Description: KCl extractable aluminum from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [feKcl](feKcl.md)  <sub>OPT</sub>
    * Description: KCl extractable iron from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [mnKcl](mnKcl.md)  <sub>OPT</sub>
    * Description: KCl extractable manganese from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [phCacl2](phCacl2.md)  <sub>OPT</sub>
    * Description: pH of the <2 mm fraction in CaCl2
    * range: [Double](types/Double.md)
    * inherited from: None
 * [phH2o](phH2o.md)  <sub>OPT</sub>
    * Description: pH of the <2 mm fraction in water
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ec12pre](ec12pre.md)  <sub>OPT</sub>
    * Description: 1:2 Electrical conductivity of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bSatx](bSatx.md)  <sub>OPT</sub>
    * Description: Boron in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [brSatx](brSatx.md)  <sub>OPT</sub>
    * Description: Bromine in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [caSatx](caSatx.md)  <sub>OPT</sub>
    * Description: Calcium in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [clSatx](clSatx.md)  <sub>OPT</sub>
    * Description: Chlorine in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [co3Satx](co3Satx.md)  <sub>OPT</sub>
    * Description: Carbonate in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ecSatp](ecSatp.md)  <sub>OPT</sub>
    * Description: Electrical conductivity of the saturated paste from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [flSatx](flSatx.md)  <sub>OPT</sub>
    * Description: Florine in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [hco3Sx](hco3Sx.md)  <sub>OPT</sub>
    * Description: Bicarbonate in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [kSatx](kSatx.md)  <sub>OPT</sub>
    * Description: Potassium in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [mgSatx](mgSatx.md)  <sub>OPT</sub>
    * Description: Magnesium in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [naSatx](naSatx.md)  <sub>OPT</sub>
    * Description: Sodium in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [no2Satx](no2Satx.md)  <sub>OPT</sub>
    * Description: Nitrite in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [no3Satx](no3Satx.md)  <sub>OPT</sub>
    * Description: Nitrate in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [pSatx](pSatx.md)  <sub>OPT</sub>
    * Description: Phosphate in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [phSp](phSp.md)  <sub>OPT</sub>
    * Description: pH of the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [resist](resist.md)  <sub>OPT</sub>
    * Description: Resistivity of the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [so4Satx](so4Satx.md)  <sub>OPT</sub>
    * Description: Sulfate in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cTot](cTot.md)  <sub>OPT</sub>
    * Description: Total carbon of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [nTot](nTot.md)  <sub>OPT</sub>
    * Description: Total nitrogen of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sTot](sTot.md)  <sub>OPT</sub>
    * Description: Total sulfur of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [eoc](eoc.md)  <sub>OPT</sub>
    * Description: Estimated organic carbon of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [analysisStartDate](analysisStartDate.md)  <sub>OPT</sub>
    * Description: The start date or dateTime of analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [archiveFate](archiveFate.md)  <sub>OPT</sub>
    * Description: Fate of the Archive sample
    * range: [String](types/String.md)
 * [caco3Conc](caco3Conc.md)  <sub>OPT</sub>
    * Description: Carbonate concentration of the <2 mm fraction expressed as calcium carbonate
    * range: [Double](types/Double.md)
    * inherited from: None
 * [carbonTot](carbonTot.md)  <sub>OPT</sub>
    * Description: Total carbon concentration of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [estimatedOC](estimatedOC.md)  <sub>OPT</sub>
    * Description: Estimated organic carbon concentration of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gypsumConc](gypsumConc.md)  <sub>OPT</sub>
    * Description: Gypsum concentration of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [nitrogenTot](nitrogenTot.md)  <sub>OPT</sub>
    * Description: Total nitrogen concentration of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sulfurTot](sulfurTot.md)  <sub>OPT</sub>
    * Description: Total sulfur concentration of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [waterSatx](waterSatx.md)  <sub>OPT</sub>
    * Description: Water content on a mass basis of the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoNrcsFate](biogeoNrcsFate.md)  <sub>OPT</sub>
    * Description: Fate of the sample used by NRCS for biogeochemistry measurements
    * range: [String](types/String.md)
    * inherited from: None
 * [sandVeryCoarseContent](sandVeryCoarseContent.md)  <sub>OPT</sub>
    * Description: Very coarse sand (1-2 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [acidity](acidity.md)  <sub>OPT</sub>
    * Description: Extractable acidity measured as the amount of acid neutralized in BaCl2-TEA at pH 8.2
    * range: [Double](types/Double.md)
    * inherited from: None
 * [acidOxalateMethod](acidOxalateMethod.md)  <sub>OPT</sub>
    * Description: Methods used for acid oxalate extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [acidOxalateMethodPub](acidOxalateMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for acid oxalate extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [acidOxalateProcessedDate](acidOxalateProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for acid oxalate extraction
    * range: [Time](types/Time.md)
    * inherited from: None
 * [airDryOvenDryMethod](airDryOvenDryMethod.md)  <sub>OPT</sub>
    * Description: Methods used for air-dried to oven-dried ratio analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [airDryOvenDryMethodPub](airDryOvenDryMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for air-dried to oven-dried ratio analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [airDryOvenDryProcessedDate](airDryOvenDryProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for air-dried to oven-dried ratio analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [airDryOvenDryRatio](airDryOvenDryRatio.md)  <sub>OPT</sub>
    * Description: Airdry to ovendry ratio of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [alCitDithionate](alCitDithionate.md)  <sub>OPT</sub>
    * Description: Dithionite citrate extractable aluminum content, indicates the amount of aluminum substituted for iron in iron oxides, reported as weight percent on the <2mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [alOxalate](alOxalate.md)  <sub>OPT</sub>
    * Description: Total soil Al as estimated by the ammonium oxalate extraction method, reported as weight percent on the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [archiveCode](archiveCode.md)  <sub>OPT</sub>
    * Description: Barcode of the archive sample
    * range: [String](types/String.md)
    * inherited from: None
 * [archiveRemarks](archiveRemarks.md)  <sub>OPT</sub>
    * Description: Remarks from sample archiving
    * range: [String](types/String.md)
    * inherited from: None
 * [Bray1PExtractable](Bray1PExtractable.md)  <sub>OPT</sub>
    * Description: Total phosphorus extracted by the Bray 1 solution
    * range: [Double](types/Double.md)
    * inherited from: None
 * [Bray1PMethod](Bray1PMethod.md)  <sub>OPT</sub>
    * Description: Method used for Bray extraction phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [Bray1PMethodPub](Bray1PMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for Bray extraction phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [Bray1PProcessedDate](Bray1PProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for Bray extraction phosphorus analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [caco3Method](caco3Method.md)  <sub>OPT</sub>
    * Description: Method used for calcium carbonate analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [caco3MethodPub](caco3MethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for calcium carbonate analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [caco3ProcessedDate](caco3ProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for calcium carbonate analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [cecMethod](cecMethod.md)  <sub>OPT</sub>
    * Description: Method used for cation exchange capacity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [cecMethodPub](cecMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for cation exchange capacity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [cecProcessedDate](cecProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for cation exchange capacity analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [citrateDithioMethod](citrateDithioMethod.md)  <sub>OPT</sub>
    * Description: Methods used for citrate dithionate extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [citrateDithioMethodPub](citrateDithioMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for citrate dithionate extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [citrateDithioProcessedDate](citrateDithioProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for citrate dithionate extraction
    * range: [Time](types/Time.md)
    * inherited from: None
 * [ctonRatio](ctonRatio.md)  <sub>OPT</sub>
    * Description: Ratio of total Carbon to total Nitrogen of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ecMethod](ecMethod.md)  <sub>OPT</sub>
    * Description: Method used for electrical conductivity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [ecMethodPub](ecMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for electrical conductivity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [ecProcessedDate](ecProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for electrical conductivity analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [extractAcidityMethod](extractAcidityMethod.md)  <sub>OPT</sub>
    * Description: Method used for acidity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [extractAcidityMethodPub](extractAcidityMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for acidity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [extractAcidityProcessedDate](extractAcidityProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for acidity analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [feCitDithionate](feCitDithionate.md)  <sub>OPT</sub>
    * Description: Dithionite citrate extractable iron, a general measure of total pedogenic iron, reported as weight percent on the <2mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [feOxalate](feOxalate.md)  <sub>OPT</sub>
    * Description: Total soil noncrystalline iron as measured by the ammonium oxalate extraction method, reported as weight percent on the <2mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gypsumMethod](gypsumMethod.md)  <sub>OPT</sub>
    * Description: Method used for gypsum analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [gypsumMethodPub](gypsumMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for gypsum analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [gypsumProcessedDate](gypsumProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for gypsum analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [h2oReten15BarMethod](h2oReten15BarMethod.md)  <sub>OPT</sub>
    * Description: Methods used for water retention analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [h2oReten15BarMethodPub](h2oReten15BarMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for water retention analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [h2oReten15BarProcessedDate](h2oReten15BarProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for water retention analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [KClExtractMethod](KClExtractMethod.md)  <sub>OPT</sub>
    * Description: Method used for routine KCl extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [KClExtractMethodPub](KClExtractMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for KCl extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [KClExtractProcessedDate](KClExtractProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for KCl extraction
    * range: [Time](types/Time.md)
    * inherited from: None
 * [MehlichIIIPMethod](MehlichIIIPMethod.md)  <sub>OPT</sub>
    * Description: Method used for Mehlich phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [MehlichIIIPMethodPub](MehlichIIIPMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for Mehlich phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [MehlichIIIPProcessedDate](MehlichIIIPProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for Mehlich phosphorus analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [MehlichIIITotP](MehlichIIITotP.md)  <sub>OPT</sub>
    * Description: Total phosphorus extracted by the Mehlich III solution
    * range: [Double](types/Double.md)
    * inherited from: None
 * [mnCitDithionate](mnCitDithionate.md)  <sub>OPT</sub>
    * Description: Dithionite citrate extractable manganese content, reported as weight percent on the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [mnOxalate](mnOxalate.md)  <sub>OPT</sub>
    * Description: Total soil manganese content fraction held in noncrystalline compounds as measured by the ammonium oxalate extraction method and reported as milligrams per kilogram on a <2 mm base
    * range: [Double](types/Double.md)
    * inherited from: None
 * [OlsenPExtractable](OlsenPExtractable.md)  <sub>OPT</sub>
    * Description: Total phosphorus extracted by the Olsen solution
    * range: [Double](types/Double.md)
    * inherited from: None
 * [OlsenPMethod](OlsenPMethod.md)  <sub>OPT</sub>
    * Description: Method used for Olsen phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [OlsenPMethodPub](OlsenPMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for Olsen phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [OlsenPProcessedDate](OlsenPProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for Olsen phosphorus analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [optDensityOxalate](optDensityOxalate.md)  <sub>OPT</sub>
    * Description: Optical density of the ammonium oxalate soil extract
    * range: [Double](types/Double.md)
    * inherited from: None
 * [pOxalate](pOxalate.md)  <sub>OPT</sub>
    * Description: Soil phosphorus measured by the ammonium oxalate extraction method
    * range: [Double](types/Double.md)
    * inherited from: None
 * [processingRemarks](processingRemarks.md)  <sub>OPT</sub>
    * Description: Remarks from sample processing
    * range: [String](types/String.md)
    * inherited from: None
 * [routinepHProcessedDate](routinepHProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for routine pH analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [routinepHMethod](routinepHMethod.md)  <sub>OPT</sub>
    * Description: Method used for routine pH analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [routinepHMethodPub](routinepHMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for routine pH analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [satPasteMethod](satPasteMethod.md)  <sub>OPT</sub>
    * Description: Method used for saturated paste analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [satPasteMethodPub](satPasteMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for saturated paste analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [satPasteProcessedDate](satPasteProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for saturated paste analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [siliconCitrateDithionate](siliconCitrateDithionate.md)  <sub>OPT</sub>
    * Description: Dithionite citrate extractable silicon, reported as weight percent on the <2mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [siOxalate](siOxalate.md)  <sub>OPT</sub>
    * Description: Total soil silica content as measured by the ammonium oxalate extraction method, reported as a weight percent on a <2 mm base
    * range: [Double](types/Double.md)
    * inherited from: None
 * [TotalNCSMethod](TotalNCSMethod.md)  <sub>OPT</sub>
    * Description: Methods used for total carbon, nitrogen and sulfur analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [TotalNCSMethodPub](TotalNCSMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for total carbon, nitrogen and sulfur analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [TotalNCSProcessedDate](TotalNCSProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for total carbon, nitrogen and sulfur analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [waterRetention15Bar](waterRetention15Bar.md)  <sub>OPT</sub>
    * Description: Water content after equilibration at 15 bars water tension, reported as gravimetric percent on the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from zoo_dnaRawDataFiles_pub:

 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
    * inherited from: None
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
    * inherited from: None
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
    * inherited from: None
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
    * inherited from: None
 * [processedDate](processedDate.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event
    * range: [Time](types/Time.md)
    * inherited from: None
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
    * inherited from: None
 * [dnaSampleID](dnaSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for DNA sample
    * range: [String](types/String.md)
    * inherited from: None
 * [dnaSampleCode](dnaSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a DNA sample
    * range: [String](types/String.md)
    * inherited from: None
 * [sequencerRunID](sequencerRunID.md)  <sub>OPT</sub>
    * Description: Identifier for the sequencing run
    * range: [String](types/String.md)
    * inherited from: None
 * [rawDataFileName](rawDataFileName.md)  <sub>OPT</sub>
    * Description: Name of file or folder containing raw data, including file extension
    * range: [String](types/String.md)
    * inherited from: None
 * [rawDataFilePath](rawDataFilePath.md)  <sub>OPT</sub>
    * Description: The system path identifying the raw data file location
    * range: [String](types/String.md)
    * inherited from: None
 * [sequencingFacilityID](sequencingFacilityID.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is sequencing samples
    * range: [String](types/String.md)
    * inherited from: None
 * [rawDataFileDescription](rawDataFileDescription.md)  <sub>OPT</sub>
    * Description: Description of the contents and type of file
    * range: [String](types/String.md)
    * inherited from: None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mos_archivepooling_in |

