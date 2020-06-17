
# Type: cfc_chlorophyllBatchQA_in




URI: [neon:CfcChlorophyllBatchQAIn](https://data.neonscience.org/CfcChlorophyllBatchQAIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [standardChlAConc](standardChlAConc.md)  <sub>OPT</sub>
    * Description: Known chlorophyll A concentration in a standard
    * range: [Double](types/Double.md)

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

### Inherited from cfc_chlorophyll_pub:

 * [extractionStartDate](extractionStartDate.md)  <sub>OPT</sub>
    * Description: The start date-time for an extraction event
    * range: [Time](types/Time.md)
    * inherited from: None
 * [receivedCondition](receivedCondition.md)  <sub>OPT</sub>
    * Description: Condition of the sample on the date it was received
    * range: [String](types/String.md)
    * inherited from: None
 * [chlCarotWavelength1](chlCarotWavelength1.md)  <sub>OPT</sub>
    * Description: The first wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength1Abs](chlCarotWavelength1Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the first wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength2](chlCarotWavelength2.md)  <sub>OPT</sub>
    * Description: The second wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength2Abs](chlCarotWavelength2Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the second wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength3](chlCarotWavelength3.md)  <sub>OPT</sub>
    * Description: The third wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength3Abs](chlCarotWavelength3Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the third wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength4](chlCarotWavelength4.md)  <sub>OPT</sub>
    * Description: The fourth wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength4Abs](chlCarotWavelength4Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the fourth wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlorophyllSampleCode](chlorophyllSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a chlorophyll sample
    * range: [String](types/String.md)
    * inherited from: None
 * [chlorophyllSampleID](chlorophyllSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a chlorophyll sample
    * range: [String](types/String.md)
    * inherited from: None
 * [extractCarotConc](extractCarotConc.md)  <sub>OPT</sub>
    * Description: Calculated total carotenoid concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
 * [extractChlAConc](extractChlAConc.md)  <sub>OPT</sub>
    * Description: Calculated chlorophyll A concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
 * [extractChlBConc](extractChlBConc.md)  <sub>OPT</sub>
    * Description: Calculated chlorophyll B concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
 * [extractionLength](extractionLength.md)  <sub>OPT</sub>
    * Description: The duration of an extraction event
    * range: [Double](types/Double.md)
    * inherited from: None
 * [handlingQF](handlingQF.md)  <sub>OPT</sub>
    * Description: Quality flag for sample handling
    * range: [String](types/String.md)
    * inherited from: None
 * [relativeAccuracyScale](relativeAccuracyScale.md)  <sub>OPT</sub>
    * Description: Indicator for the mean relative accuracy of standards analyzed as unknowns with a run of samples
    * range: [String](types/String.md)
    * inherited from: None
 * [solventVolume](solventVolume.md)  <sub>OPT</sub>
    * Description: Volume of solvent used in the extraction
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from cfc_elementsBatchQA_in:

 * [qaQF](qaQF.md)  <sub>OPT</sub>
    * Description: Quality flag for quality control sample
    * range: [String](types/String.md)
 * [knownBoronConc](knownBoronConc.md)  <sub>OPT</sub>
    * Description: Known concentration of boron in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownCalciumConc](knownCalciumConc.md)  <sub>OPT</sub>
    * Description: Known concentration of calcium in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownCopperConc](knownCopperConc.md)  <sub>OPT</sub>
    * Description: Known concentration of copper in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownIronConc](knownIronConc.md)  <sub>OPT</sub>
    * Description: Known concentration of iron in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownMagnesiumConc](knownMagnesiumConc.md)  <sub>OPT</sub>
    * Description: Known concentration of magnesium in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownManganeseConc](knownManganeseConc.md)  <sub>OPT</sub>
    * Description: Known concentration of manganese in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownPhosphorusConc](knownPhosphorusConc.md)  <sub>OPT</sub>
    * Description: Known concentration of phophorus in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownPotassiumConc](knownPotassiumConc.md)  <sub>OPT</sub>
    * Description: Known concentration of potassium in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownSulfurConc](knownSulfurConc.md)  <sub>OPT</sub>
    * Description: Known concentration of sulfur in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownZincConc](knownZincConc.md)  <sub>OPT</sub>
    * Description: Known concentration of zinc in standard reference material on a dry mass basis
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
    * inherited from: None
 * [downloadFileUrl](downloadFileUrl.md)  <sub>OPT</sub>
    * Description: The URL of the file linked to the record
    * range: [String](types/String.md)
    * inherited from: None
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

### Inherited from ltr_ligninBatchQA_in:

 * [analysisEndDate](analysisEndDate.md)  <sub>OPT</sub>
    * Description: The end date or dateTime of analysis
    * range: [Time](types/Time.md)
 * [analyticalRepNumber](analyticalRepNumber.md)  <sub>OPT</sub>
    * Description: Number of the analytical replicate
    * range: [String](types/String.md)
 * [celluloseKnown](celluloseKnown.md)  <sub>OPT</sub>
    * Description: Known percent cellulose in quality assurance material or standard on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cellulosePercent](cellulosePercent.md)  <sub>OPT</sub>
    * Description: Percent cellulose on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ligninKnown](ligninKnown.md)  <sub>OPT</sub>
    * Description: Known percent lignin in quality assurance material or standard on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ligninPercent](ligninPercent.md)  <sub>OPT</sub>
    * Description: Percent lignin on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [qaMaterialQF](qaMaterialQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the quality assurance material
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from ltr_ligninSummary_in:

 * [analyteStandardDeviation](analyteStandardDeviation.md)  <sub>OPT</sub>
    * Description: Long-term average standard deviation values of the analyte, based on analysis of quality assurance reference materials or standards treated as unknowns
    * range: [Double](types/Double.md)
    * inherited from: None
 * [qaReferenceID](qaReferenceID.md)  <sub>OPT</sub>
    * Description: Identifier for quality assurance reference material or standard
    * range: [String](types/String.md)
 * [analyteKnownValue](analyteKnownValue.md)  <sub>OPT</sub>
    * Description: The known value of a given analyte for a quality assurance reference material or standard, with units tied to the analyte
    * range: [Double](types/Double.md)
    * inherited from: None
 * [analytePercentRecovery](analytePercentRecovery.md)  <sub>OPT</sub>
    * Description: Percent recovery of the analyte, based on analysis of quality assurance reference materials or standards treated as unknowns
    * range: [Double](types/Double.md)
    * inherited from: None
 * [analyteObservedValue](analyteObservedValue.md)  <sub>OPT</sub>
    * Description: The measured value of a given analyte for a standard reference material, with units tied to the analyte
    * range: [Double](types/Double.md)
    * inherited from: None
 * [analyteMetricsCount](analyteMetricsCount.md)  <sub>OPT</sub>
    * Description: Count of how many measurements were used to determine analyte metrics
    * range: [String](types/String.md)
    * inherited from: None
 * [qaReportingEndDate](qaReportingEndDate.md)  <sub>OPT</sub>
    * Description: End date for the quality assurance (QA) reporting period
    * range: [Time](types/Time.md)
    * inherited from: None
 * [qaReportingStartDate](qaReportingStartDate.md)  <sub>OPT</sub>
    * Description: Start date for the quality assurance (QA) reporting period
    * range: [Time](types/Time.md)
    * inherited from: None

### Inherited from wc_externalLabDataByAnalyte_in:

 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
    * inherited from: None
 * [coolerTemp](coolerTemp.md)  <sub>OPT</sub>
    * Description: Temperature of the cooler when the sample arrived at the external lab
    * range: [Double](types/Double.md)
    * inherited from: None
 * [externalLabMetadata](externalLabMetadata.md)  <sub>OPT</sub>
    * Description: The external lab's metadata
    * range: [String](types/String.md)
    * inherited from: None
 * [shipmentWarmQF](shipmentWarmQF.md)  <sub>OPT</sub>
    * Description: Quality Flag for cooler arriving at external lab too warm (above 6 C)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [uploadDate](uploadDate.md)  <sub>OPT</sub>
    * Description: Date the file was uploaded
    * range: [Time](types/Time.md)
    * inherited from: None
 * [analyteUnits](analyteUnits.md)  <sub>OPT</sub>
    * Description: Associated units of measure for analyte
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
    * inherited from: None
 * [runID](runID.md)  <sub>OPT</sub>
    * Description: A linking value provided by the external lab that associates the sample data to the run metadata, including QA values
    * range: [String](types/String.md)

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
| **Mappings:** | | neon:cfc_chlorophyllBatchQA_in |

