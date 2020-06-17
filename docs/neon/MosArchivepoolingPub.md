
# Type: mos_archivepooling_pub




URI: [neon:MosArchivepoolingPub](https://data.neonscience.org/MosArchivepoolingPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [archiveIDCode](archiveIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of the Archive sample
    * range: [String](types/String.md)
 * [archiveVialIDList](archiveVialIDList.md)  <sub>OPT</sub>
    * Description: Identifier(s) for the vial(s) containing specimens for archive
    * range: [String](types/String.md)
 * [archivedCount](archivedCount.md)  <sub>OPT</sub>
    * Description: Number of individuals in the archive vial
    * range: [String](types/String.md)

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

### Inherited from csd_pressureGaugeRelationship_pub:

 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
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

### Inherited from zoo_dnaRawDataFiles_pub:

 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
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
    * inherited from: None
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
| **Mappings:** | | neon:mos_archivepooling_pub |

