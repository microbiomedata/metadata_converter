
# Type: mcc_taxonTableMetadata_16S_in




URI: [neon:MccTaxonTableMetadata16SIn](https://data.neonscience.org/MccTaxonTableMetadata16SIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


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
    * inherited from: None
 * [analyteConcentration](analyteConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of analyte
    * range: [Double](types/Double.md)
    * inherited from: None
 * [percentFilterAnalyzed](percentFilterAnalyzed.md)  <sub>OPT</sub>
    * Description: Fraction of the filter sampled (%)
    * range: [Double](types/Double.md)
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

### Inherited from fsp_spectralData_pub:

 * [reviewedBy](reviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed the data prior to submission
    * range: [String](types/String.md)
 * [downloadFileName](downloadFileName.md)  <sub>OPT</sub>
    * Description: The name of the user-downloaded file that is linked to the record
    * range: [String](types/String.md)
 * [downloadFileUrl](downloadFileUrl.md)  <sub>OPT</sub>
    * Description: The URL of the file linked to the record
    * range: [String](types/String.md)
 * [software](software.md)  <sub>OPT</sub>
    * Description: Name and version of the software used to process the data
    * range: [String](types/String.md)
    * inherited from: None
 * [spectralSampleCode](spectralSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a spectral sample
    * range: [String](types/String.md)
    * inherited from: None
 * [spectralSampleID](spectralSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a spectral sample
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from inv_dnaExtractionStandard_pub:

 * [deprecatedVialID](deprecatedVialID.md)  <sub>OPT</sub>
    * Description: Identifier on vial label, if different from standard ID
    * range: [String](types/String.md)
    * inherited from: None
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
    * inherited from: None
 * [processedBy](processedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who processed the sample(s)
    * range: [String](types/String.md)
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

### Inherited from inv_pcrAmplificationStandard_pub:

 * [forwardPrimer](forwardPrimer.md)  <sub>OPT</sub>
    * Description: DNA sequence of forward primer
    * range: [String](types/String.md)
    * inherited from: None
 * [reversePrimer](reversePrimer.md)  <sub>OPT</sub>
    * Description: DNA sequence of reverse primer
    * range: [String](types/String.md)
    * inherited from: None
 * [targetGene](targetGene.md)  <sub>OPT</sub>
    * Description: Targeted gene or locus name
    * range: [String](types/String.md)
 * [ampliconConcentration](ampliconConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of amplicon DNA used for sequencing reaction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ampliconPooledStatus](ampliconPooledStatus.md)  <sub>OPT</sub>
    * Description: Indicates whether multiple PCR reactions were pooled
    * range: [String](types/String.md)
    * inherited from: None
 * [targetSubfragment](targetSubfragment.md)  <sub>OPT</sub>
    * Description: Name of subfragment of a gene or locus
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from inv_taxonomyRaw_pub:

 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
    * inherited from: None
 * [individualCount](individualCount.md)  <sub>OPT</sub>
    * Description: Number of individuals of the same type
    * range: [String](types/String.md)
 * [identifiedDate](identifiedDate.md)  <sub>OPT</sub>
    * Description: Date on which the sample, individual, or specimen was identified
    * range: [Time](types/Time.md)
    * inherited from: None
 * [identificationRemarks](identificationRemarks.md)  <sub>OPT</sub>
    * Description: Comments or notes about the identification
    * range: [String](types/String.md)
    * inherited from: None
 * [kingdom](kingdom.md)  <sub>OPT</sub>
    * Description: The scientific name of the kingdom in which the taxon is classified
    * range: [String](types/String.md)
 * [phylum](phylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the phylum or division in which the taxon is classified
    * range: [String](types/String.md)
 * [class](class.md)  <sub>OPT</sub>
    * Description: The scientific name of the class in which the taxon is classified
    * range: [String](types/String.md)
 * [order](order.md)  <sub>OPT</sub>
    * Description: The scientific name of the order in which the taxon is classified
    * range: [String](types/String.md)
 * [family](family.md)  <sub>OPT</sub>
    * Description: The scientific name of the family in which the taxon is classified
    * range: [String](types/String.md)
 * [subfamily](subfamily.md)  <sub>OPT</sub>
    * Description: The scientific name of the subfamily in which the organism is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [genus](genus.md)  <sub>OPT</sub>
    * Description: The scientific name of the genus in which the organism is classified
    * range: [String](types/String.md)
 * [subgenus](subgenus.md)  <sub>OPT</sub>
    * Description: The scientific name of the subgenus in which the taxon is classified. Values should include the genus to avoid homonym confusion
    * range: [String](types/String.md)
    * inherited from: None
 * [specificEpithet](specificEpithet.md)  <sub>OPT</sub>
    * Description: The specific epithet (second part of the species name) of the scientific name applied to the taxon
    * range: [String](types/String.md)
 * [infraspecificEpithet](infraspecificEpithet.md)  <sub>OPT</sub>
    * Description: The infraspecific epithet (scientific name below the rank of species) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [tribe](tribe.md)  <sub>OPT</sub>
    * Description: The scientific name of the tribe in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [taxonDatabaseName](taxonDatabaseName.md)  <sub>OPT</sub>
    * Description: Name of the taxonomic database
    * range: [String](types/String.md)
    * inherited from: None
 * [taxonDatabaseID](taxonDatabaseID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the taxon within the database
    * range: [String](types/String.md)
    * inherited from: None
 * [subsamplePercent](subsamplePercent.md)  <sub>OPT</sub>
    * Description: Percent of the total sample contained in the subsample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [invertebrateLifeStage](invertebrateLifeStage.md)  <sub>OPT</sub>
    * Description: Macroinvertebrate stage of development (larva, pupa, adult)
    * range: [String](types/String.md)
    * inherited from: None
 * [sizeClass](sizeClass.md)  <sub>OPT</sub>
    * Description: Size class of individual(s)
    * range: [String](types/String.md)
    * inherited from: None
 * [immatureSpecimen](immatureSpecimen.md)  <sub>OPT</sub>
    * Description: Sample contains immature specimen(s) for which target level of identification cannot be achieved
    * range: [String](types/String.md)
    * inherited from: None
 * [distinctTaxon](distinctTaxon.md)  <sub>OPT</sub>
    * Description: Taxon is known to be distinct within the sample, used for species richness metrics
    * range: [String](types/String.md)
    * inherited from: None
 * [qcChecked](qcChecked.md)  <sub>OPT</sub>
    * Description: Whether or not QC procedure was performed
    * range: [String](types/String.md)
    * inherited from: None
 * [indeterminateSpecies](indeterminateSpecies.md)  <sub>OPT</sub>
    * Description: Sample contains specimen(s) not well-described in the literature, not all taxa for a group are included in the literature, or observed characters are such that they do not fit described taxa. See accompanying identificationRemarks
    * range: [String](types/String.md)
    * inherited from: None
 * [subphylum](subphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the subphylum in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subclass](subclass.md)  <sub>OPT</sub>
    * Description: The scientific name of the subclass in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infraclass](infraclass.md)  <sub>OPT</sub>
    * Description: The scientific name of the infraclass in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [superorder](superorder.md)  <sub>OPT</sub>
    * Description: The scientific name of the superorder in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [suborder](suborder.md)  <sub>OPT</sub>
    * Description: The scientific name of the suborder in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infraorder](infraorder.md)  <sub>OPT</sub>
    * Description: The scientific name of the infraorder in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [superfamily](superfamily.md)  <sub>OPT</sub>
    * Description: The scientific name of the superfamily in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subtribe](subtribe.md)  <sub>OPT</sub>
    * Description: The scientific name of the subtribe in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [estimatedTotalCount](estimatedTotalCount.md)  <sub>OPT</sub>
    * Description: Estimated total count of individuals within a sample, of given taxon, life stage, and size class
    * range: [Double](types/Double.md)
    * inherited from: None
 * [subkingdom](subkingdom.md)  <sub>OPT</sub>
    * Description: The scientific name of the subkingdom in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infrakingdom](infrakingdom.md)  <sub>OPT</sub>
    * Description: The scientific name of the infrakingdom in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [superclass](superclass.md)  <sub>OPT</sub>
    * Description: The scientific name of the superclass in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
    * inherited from: None
 * [superphylum](superphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the superphylum in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infraphylum](infraphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the infraphylum in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from mcc_swTaxonTableMetadata_ITS_pub:

 * [targetTaxonGroup](targetTaxonGroup.md)  <sub>OPT</sub>
    * Description: Taxonomic group targeted
    * range: [String](types/String.md)

### Inherited from mcc_taxonTableMetadata_ITS_in:

 * [completeTaxonomy](completeTaxonomy.md)  <sub>OPT</sub>
    * Description: Full taxonomic hierarchy for identified organism
    * range: [String](types/String.md)
 * [dnaSampleCodeDataFrame](dnaSampleCodeDataFrame.md)  <sub>OPT</sub>
    * Description: Barcode copy of sample to a data frame column
    * range: [String](types/String.md)
 * [dnaSampleIDDataFrame](dnaSampleIDDataFrame.md)  <sub>OPT</sub>
    * Description: Identifier copy of sample to a data frame column
    * range: [String](types/String.md)
 * [domain](domain.md)  <sub>OPT</sub>
    * Description: The scientific name of the domain in which the taxon is classified
    * range: [String](types/String.md)
 * [communitySubsampleCode](communitySubsampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a microbial community composition subsample
    * range: [String](types/String.md)
 * [communitySubsampleFate](communitySubsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a microbial community composition subsample
    * range: [String](types/String.md)
 * [communitySubsampleID](communitySubsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with the microbial community composition subsample
    * range: [String](types/String.md)

### Inherited from mic_dnaExtraction_in:

 * [subsampleID](subsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with each subsample per sampleID
    * range: [String](types/String.md)
 * [sampleClass](sampleClass.md)  <sub>OPT</sub>
    * Description: Class of a sample
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticSampleFate](geneticSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a genetic sample
    * range: [String](types/String.md)
    * inherited from: None
 * [samplePercent](samplePercent.md)  <sub>OPT</sub>
    * Description: Percent of sample processed
    * range: [Double](types/Double.md)
    * inherited from: None
 * [subsampleCode](subsampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a subsample
    * range: [String](types/String.md)
 * [subsampleFate](subsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a subsample
    * range: [String](types/String.md)
 * [sequenceAnalysisType](sequenceAnalysisType.md)  <sub>OPT</sub>
    * Description: The general type of sequencing to be conducted on a sample
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from mms_rawDataFiles_in:

 * [dnaSampleFate](dnaSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a DNA sample
    * range: [String](types/String.md)
 * [parentFolderName](parentFolderName.md)  <sub>OPT</sub>
    * Description: Name of parent folder in which the file was uploaded
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from vst_shrubgroup_pub:

 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
    * inherited from: None
 * [identificationReferences](identificationReferences.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) used to derive the specific taxon concept; including field guide editions, books, or versions of NEON keys used
    * range: [String](types/String.md)
    * inherited from: None
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
    * inherited from: None
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
    * inherited from: None
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
    * inherited from: None
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
    * inherited from: None
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
    * inherited from: None
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
    * range: [String](types/String.md)
 * [taxonRank](taxonRank.md)  <sub>OPT</sub>
    * Description: The lowest level taxonomic rank that can be determined for the individual or specimen
    * range: [String](types/String.md)
    * inherited from: None
 * [subplotID](subplotID.md)  <sub>OPT</sub>
    * Description: Identifier for the NEON subplot
    * range: [String](types/String.md)
    * inherited from: None
 * [canopyArea](canopyArea.md)  <sub>OPT</sub>
    * Description: Area of the group canopy
    * range: [Double](types/Double.md)
    * inherited from: None
 * [deadPercent](deadPercent.md)  <sub>OPT</sub>
    * Description: Percent of a given species, within a group, that is dead
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groupID](groupID.md)  <sub>OPT</sub>
    * Description: Identifier for a group of individuals being measured
    * range: [String](types/String.md)
    * inherited from: None
 * [livePercent](livePercent.md)  <sub>OPT</sub>
    * Description: Percent of a given species, within a group, that is alive
    * range: [Double](types/Double.md)
    * inherited from: None
 * [meanHeight](meanHeight.md)  <sub>OPT</sub>
    * Description: The mean of multiple height measurements
    * range: [Double](types/Double.md)
    * inherited from: None
 * [nestedSubplotID](nestedSubplotID.md)  <sub>OPT</sub>
    * Description: Numeric identifier for nested subplot ID within a subplotID
    * range: [String](types/String.md)
    * inherited from: None
 * [volumePercent](volumePercent.md)  <sub>OPT</sub>
    * Description: Percent of the total volume of a group attributed to a particular species
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
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
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
 * [dnaSampleID](dnaSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for DNA sample
    * range: [String](types/String.md)
 * [dnaSampleCode](dnaSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a DNA sample
    * range: [String](types/String.md)
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
| **Mappings:** | | neon:mcc_taxonTableMetadata_16S_in |
| **In Subsets:** | | DP0.10081.001 |

