
# Type: mos_pathogenresults_in




URI: [neon:MosPathogenresultsIn](https://data.neonscience.org/MosPathogenresultsIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [sampleCompromised](sampleCompromised.md)  <sub>OPT</sub>
    * Description: Indicator of compromised sample integrity; 'other' requires further specification in remarks
    * range: [String](types/String.md)
 * [testingVialIDFate](testingVialIDFate.md)  <sub>OPT</sub>
    * Description: Fate of the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
    * range: [String](types/String.md)

### Inherited from apl_taxonomyProcessed_pub:

 * [scientificNameAuthorship](scientificNameAuthorship.md)  <sub>OPT</sub>
    * Description: Name of the individual(s) who designated the scientific name of the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [testMethod](testMethod.md)  <sub>OPT</sub>
    * Description: Method used to conduct test
    * range: [String](types/String.md)
 * [qcTaxonomyStatus](qcTaxonomyStatus.md)  <sub>OPT</sub>
    * Description: Sample chosen as part of 10% of samples for quality control (QC)
    * range: [String](types/String.md)
    * inherited from: None
 * [algalType](algalType.md)  <sub>OPT</sub>
    * Description: Informal taxonomic grouping of algal species
    * range: [String](types/String.md)
    * inherited from: None
 * [algalParameter](algalParameter.md)  <sub>OPT</sub>
    * Description: Parameter used for analysis of algal assemblages
    * range: [String](types/String.md)
    * inherited from: None
 * [algalParameterValue](algalParameterValue.md)  <sub>OPT</sub>
    * Description: Value of the algalParameter
    * range: [Double](types/Double.md)
    * inherited from: None
 * [algalParameterUnit](algalParameterUnit.md)  <sub>OPT</sub>
    * Description: Unit of measure associated with the algalParameter
    * range: [String](types/String.md)
    * inherited from: None
 * [variety](variety.md)  <sub>OPT</sub>
    * Description: The variety (infraspecific name below the rank of infraspecific epithet) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [section](section.md)  <sub>OPT</sub>
    * Description: The scientific name of the section in which the organism is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [superdivision](superdivision.md)  <sub>OPT</sub>
    * Description: The scientific name of the superdivision in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [division](division.md)  <sub>OPT</sub>
    * Description: The scientific name of the division in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subdivision](subdivision.md)  <sub>OPT</sub>
    * Description: The scientific name of the subdivision in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infradivision](infradivision.md)  <sub>OPT</sub>
    * Description: The scientific name of the infradivision in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [parvdivision](parvdivision.md)  <sub>OPT</sub>
    * Description: The scientific name of the parvdivision in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subsection](subsection.md)  <sub>OPT</sub>
    * Description: The scientific name of the subsection in which the organism is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subspecies](subspecies.md)  <sub>OPT</sub>
    * Description: The subspecies (infraspecific name below the rank of infraspecific epithet) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [subvariety](subvariety.md)  <sub>OPT</sub>
    * Description: The subvariety (infraspecific name below the rank of variety) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [subform](subform.md)  <sub>OPT</sub>
    * Description: The subform (infraspecific name below the rank of form) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [form](form.md)  <sub>OPT</sub>
    * Description: The form (infraspecific name below the rank of infraspecific epithet) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [speciesGroup](speciesGroup.md)  <sub>OPT</sub>
    * Description: The unofficial species group into which the taxon is categorized
    * range: [String](types/String.md)
    * inherited from: None
 * [perBottleSampleVolume](perBottleSampleVolume.md)  <sub>OPT</sub>
    * Description: Sample volume per bottle in milliliters
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from asi_POMExternalLabDataPerSample_pub:

 * [sampleType](sampleType.md)  <sub>OPT</sub>
    * Description: Type of sample
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleVolumeFiltered](sampleVolumeFiltered.md)  <sub>OPT</sub>
    * Description: Volume of water filtered onto the filter for external analysis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [externalRemarks](externalRemarks.md)  <sub>OPT</sub>
    * Description: External lab notes; free text comments accompanying the record
    * range: [String](types/String.md)
    * inherited from: None
 * [analyte](analyte.md)  <sub>OPT</sub>
    * Description: Analyte or parameter measured
    * range: [String](types/String.md)
    * inherited from: None
 * [method](method.md)  <sub>OPT</sub>
    * Description: Published method used for analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
    * inherited from: None
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
    * inherited from: None
 * [filterSize](filterSize.md)  <sub>OPT</sub>
    * Description: Filter diameter
    * range: [Double](types/Double.md)
    * inherited from: None
 * [plantAlgaeLabUnits](plantAlgaeLabUnits.md)  <sub>OPT</sub>
    * Description: Standard units of measure used by the plant and algae external laboratory
    * range: [String](types/String.md)
    * inherited from: None
 * [externalLabDataQF](externalLabDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for external lab data
    * range: [String](types/String.md)
    * inherited from: None
 * [batchID](batchID.md)  <sub>OPT</sub>
    * Description: Identifier for batch or analytical run
    * range: [String](types/String.md)
 * [analyteConcentration](analyteConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of analyte
    * range: [Double](types/Double.md)
    * inherited from: None
 * [percentFilterAnalyzed](percentFilterAnalyzed.md)  <sub>OPT</sub>
    * Description: Fraction of the filter sampled (%)
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from asi_externalLabH2OIsotopes_pub:

 * [receivedBy](receivedBy.md)  <sub>OPT</sub>
    * Description: Anonymized name of lab personnel receiving the shipment
    * range: [String](types/String.md)
    * inherited from: None
 * [receivedDate](receivedDate.md)  <sub>OPT</sub>
    * Description: Date a sample was received
    * range: [Time](types/Time.md)
 * [d18OsdWater](d18OsdWater.md)  <sub>OPT</sub>
    * Description: Standard deviation of d18O of replicate H2O samples
    * range: [Double](types/Double.md)
    * inherited from: None
 * [d2HsdWater](d2HsdWater.md)  <sub>OPT</sub>
    * Description: Standard deviation of d2H of replicate H2O samples
    * range: [Double](types/Double.md)
    * inherited from: None
 * [instrumentSN](instrumentSN.md)  <sub>OPT</sub>
    * Description: Serial number of instrument used to analyze sample
    * range: [String](types/String.md)
    * inherited from: None
 * [isotopeH2OExternalLabQF](isotopeH2OExternalLabQF.md)  <sub>OPT</sub>
    * Description: Quality flag for samples with high standard deviation (del2Hsd >=0.75 or del18Osd>=0.2) of H2O isotope samples. High standard deviations are flagged with a 1, else flag set to 0
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

### Inherited from inv_markerGeneSequencingStandard_pub:

 * [testProtocolVersion](testProtocolVersion.md)  <sub>OPT</sub>
    * Description: The protocol version used to test the sample
    * range: [String](types/String.md)
 * [processedBy](processedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who processed the sample(s)
    * range: [String](types/String.md)
    * inherited from: None
 * [linkerPrimerSequence](linkerPrimerSequence.md)  <sub>OPT</sub>
    * Description: DNA sequence of linker primer used in a multiplexed DNA sequencing run
    * range: [String](types/String.md)
    * inherited from: None
 * [reverseLinkerPrimerSequence](reverseLinkerPrimerSequence.md)  <sub>OPT</sub>
    * Description: DNA sequence of linker primer used on reverse stand in a multiplexed DNA sequencing run
    * range: [String](types/String.md)
    * inherited from: None
 * [sequencingMethod](sequencingMethod.md)  <sub>OPT</sub>
    * Description: Method used for DNA sequencing
    * range: [String](types/String.md)
    * inherited from: None
 * [sequencingConcentration](sequencingConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of nucleic acid used for sequencing
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sampleTotalReadNumber](sampleTotalReadNumber.md)  <sub>OPT</sub>
    * Description: Total number of sequence reads in a sample
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleFilteredReadNumber](sampleFilteredReadNumber.md)  <sub>OPT</sub>
    * Description: Number of sequence reads that pass quality filtering
    * range: [String](types/String.md)
    * inherited from: None
 * [maxFilteredReadLength](maxFilteredReadLength.md)  <sub>OPT</sub>
    * Description: Maximum sequence read length for a sample
    * range: [String](types/String.md)
    * inherited from: None
 * [minFilteredReadLength](minFilteredReadLength.md)  <sub>OPT</sub>
    * Description: Minimum sequence read length for a sample
    * range: [String](types/String.md)
    * inherited from: None
 * [averageFilteredReadQuality](averageFilteredReadQuality.md)  <sub>OPT</sub>
    * Description: Average quality of sequence reads in a sample after quality filtering
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ambiguousBasesNumber](ambiguousBasesNumber.md)  <sub>OPT</sub>
    * Description: Number of sequence reads in a quality filtered sample with more than 1 ambiguous base
    * range: [String](types/String.md)
    * inherited from: None
 * [barcodeSequence](barcodeSequence.md)  <sub>OPT</sub>
    * Description: DNA sequence of barcode primer used in a multiplexed DNA sequencing run
    * range: [String](types/String.md)
    * inherited from: None
 * [qaqcStatus](qaqcStatus.md)  <sub>OPT</sub>
    * Description: Status of internal QAQC
    * range: [String](types/String.md)
    * inherited from: None
 * [replicate](replicate.md)  <sub>OPT</sub>
    * Description: Sample replicate
    * range: [String](types/String.md)
    * inherited from: None
 * [instrument_model](instrument_model.md)  <sub>OPT</sub>
    * Description: The model identifier of the sequencing instrument
    * range: [String](types/String.md)
    * inherited from: None
 * [ncbiProjectID](ncbiProjectID.md)  <sub>OPT</sub>
    * Description: Identifier for the NCBI project associated with the sample
    * range: [String](types/String.md)
    * inherited from: None
 * [illuminaAdapterKit](illuminaAdapterKit.md)  <sub>OPT</sub>
    * Description: Identifier for the adapter sequences kit manufactured for use with Illumina sequencing technology
    * range: [String](types/String.md)
    * inherited from: None
 * [illuminaIndex1](illuminaIndex1.md)  <sub>OPT</sub>
    * Description: Oligonucleotide sequence of the 5-prime index used to identify a unique sample in an Illumina-based sequencing run
    * range: [String](types/String.md)
    * inherited from: None
 * [illuminaIndex2](illuminaIndex2.md)  <sub>OPT</sub>
    * Description: Oligonucleotide sequence of the 3-prime index used to identify a unique sample in an Illumina-based sequencing run
    * range: [String](types/String.md)
    * inherited from: None
 * [library_layout](library_layout.md)  <sub>OPT</sub>
    * Description: Layout for a library
    * range: [String](types/String.md)
    * inherited from: None
 * [library_selection](library_selection.md)  <sub>OPT</sub>
    * Description: Type of nucleic acid selection method used for a library
    * range: [String](types/String.md)
    * inherited from: None
 * [library_source](library_source.md)  <sub>OPT</sub>
    * Description: Source of genetic material for sequencing library
    * range: [String](types/String.md)
    * inherited from: None
 * [library_strategy](library_strategy.md)  <sub>OPT</sub>
    * Description: Strategy used for nucleic acid sequencing for a sample library
    * range: [String](types/String.md)
    * inherited from: None
 * [analysisCodeFileName](analysisCodeFileName.md)  <sub>OPT</sub>
    * Description: File name of code used for data analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [primerSetID](primerSetID.md)  <sub>OPT</sub>
    * Description: Identifier for the primer set used
    * range: [String](types/String.md)
    * inherited from: None
 * [processedSeqFileName](processedSeqFileName.md)  <sub>OPT</sub>
    * Description: File name of quality filtered sequence data
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from mos_pathogenqa_in:

 * [testedDate](testedDate.md)  <sub>OPT</sub>
    * Description: Date test was conducted
    * range: [Time](types/Time.md)
 * [controlType](controlType.md)  <sub>OPT</sub>
    * Description: Control type for test or experiment
    * range: [String](types/String.md)
    * inherited from: None
 * [criteriaMet](criteriaMet.md)  <sub>OPT</sub>
    * Description: Whether or not criteria are met
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from mos_pathogenresults_pub:

 * [testingVialID](testingVialID.md)  <sub>OPT</sub>
    * Description: Identifier for the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
    * range: [String](types/String.md)
 * [testNumber](testNumber.md)  <sub>OPT</sub>
    * Description: Test number in a sequence of tests
    * range: [String](types/String.md)
 * [finalResult](finalResult.md)  <sub>OPT</sub>
    * Description: Whether or not this is the conclusive test result for this sample
    * range: [String](types/String.md)
 * [locus](locus.md)  <sub>OPT</sub>
    * Description: Name of genetic marker sequenced
    * range: [String](types/String.md)
 * [percentIdentity](percentIdentity.md)  <sub>OPT</sub>
    * Description: Percent match between sample and reference sequence
    * range: [String](types/String.md)
 * [sequenceDatabase](sequenceDatabase.md)  <sub>OPT</sub>
    * Description: Name of database where sequence is stored
    * range: [String](types/String.md)
 * [sequenceDatabaseID](sequenceDatabaseID.md)  <sub>OPT</sub>
    * Description: Identifier for sample in sequence database
    * range: [String](types/String.md)
 * [extractDepleted](extractDepleted.md)  <sub>OPT</sub>
    * Description: Whether or not sample extract is depleted
    * range: [String](types/String.md)
 * [startCollectDate](startCollectDate.md)  <sub>OPT</sub>
    * Description: Earliest known collection date for this sample
    * range: [Time](types/Time.md)
 * [endCollectDate](endCollectDate.md)  <sub>OPT</sub>
    * Description: Latest known collection date for this sample
    * range: [Time](types/Time.md)
 * [testingVialIDCode](testingVialIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
    * range: [String](types/String.md)

### Inherited from scs_shipmentCreation_in:

 * [sampleVolume](sampleVolume.md)  <sub>OPT</sub>
    * Description: Sample volume in milliliters
    * range: [Double](types/Double.md)
    * inherited from: None
 * [shipDate](shipDate.md)  <sub>OPT</sub>
    * Description: Date shipment sent by domain lab
    * range: [Time](types/Time.md)
    * inherited from: None
 * [numVialsSampleID](numVialsSampleID.md)  <sub>OPT</sub>
    * Description: Number of vials associated with a sampleID
    * range: [String](types/String.md)
    * inherited from: None
 * [senderID](senderID.md)  <sub>OPT</sub>
    * Description: Identifier for the facility or technician sending the sample or specimen
    * range: [String](types/String.md)
 * [containerID](containerID.md)  <sub>OPT</sub>
    * Description: The identifier for the container in which the sample is located
    * range: [String](types/String.md)
    * inherited from: None
 * [containerMass](containerMass.md)  <sub>OPT</sub>
    * Description: Mass of the container in grams
    * range: [Double](types/Double.md)
    * inherited from: None
 * [destinationFacility](destinationFacility.md)  <sub>OPT</sub>
    * Description: Name of institution to which shipment was sent
    * range: [String](types/String.md)
    * inherited from: None
 * [filterVolume](filterVolume.md)  <sub>OPT</sub>
    * Description: Volume of material passed through filter
    * range: [Double](types/Double.md)
    * inherited from: None
 * [holdingTime](holdingTime.md)  <sub>OPT</sub>
    * Description: The holding time associated with the samples
    * range: [Time](types/Time.md)
    * inherited from: None
 * [quarantineStatus](quarantineStatus.md)  <sub>OPT</sub>
    * Description: An indicator of whether the samples being shipped have associated quarantine restrictions
    * range: [String](types/String.md)
    * inherited from: None
 * [sentTo](sentTo.md)  <sub>OPT</sub>
    * Description: Name of person or institution to which shipment was sent following identifications or analyses
    * range: [String](types/String.md)
    * inherited from: None
 * [shipmentMethod](shipmentMethod.md)  <sub>OPT</sub>
    * Description: The method of shipment
    * range: [String](types/String.md)
    * inherited from: None
 * [shipmentService](shipmentService.md)  <sub>OPT</sub>
    * Description: The name of the company performing shipment fulfillment
    * range: [String](types/String.md)
    * inherited from: None
 * [shippedFrom](shippedFrom.md)  <sub>OPT</sub>
    * Description: Named location from which the sample was shipped
    * range: [String](types/String.md)
    * inherited from: None
 * [trackingNumber](trackingNumber.md)  <sub>OPT</sub>
    * Description: The tracking number assigned by the shipment fulfillment organization
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from tck_pathogen_pub:

 * [testingID](testingID.md)  <sub>OPT</sub>
    * Description: Identifier for the group of specimens for testing
    * range: [String](types/String.md)
    * inherited from: None
 * [testResult](testResult.md)  <sub>OPT</sub>
    * Description: Result of the test
    * range: [String](types/String.md)
 * [testPathogenName](testPathogenName.md)  <sub>OPT</sub>
    * Description: The name of the pathogen
    * range: [String](types/String.md)
 * [testedBy](testedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who tested the sample
    * range: [String](types/String.md)
 * [testingIDCode](testingIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of a test sample
    * range: [String](types/String.md)
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
| **Mappings:** | | neon:mos_pathogenresults_in |

