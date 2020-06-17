
# Type: cfc_chlorophyll_in




URI: [neon:CfcChlorophyllIn](https://data.neonscience.org/CfcChlorophyllIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [chlorophyllSampleFate](chlorophyllSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a chlorophyll sample
    * range: [String](types/String.md)

### Inherited from amc_cellCounts_in:

 * [cellCountSampleID](cellCountSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for the cell count sample
    * range: [String](types/String.md)
    * inherited from: None
 * [cellCountSampleFate](cellCountSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a cell count sample
    * range: [String](types/String.md)
    * inherited from: None
 * [cellCountSampleCode](cellCountSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a cell count sample
    * range: [String](types/String.md)
    * inherited from: None
 * [analysisMagnification](analysisMagnification.md)  <sub>OPT</sub>
    * Description: Magnification used during analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [analysisVolume](analysisVolume.md)  <sub>OPT</sub>
    * Description: Volume in milliliters of sample analyzed
    * range: [Double](types/Double.md)
    * inherited from: None
 * [batchReferenceCount](batchReferenceCount.md)  <sub>OPT</sub>
    * Description: Automated count of reference image for the batch
    * range: [String](types/String.md)
    * inherited from: None
 * [enumerationDifference](enumerationDifference.md)  <sub>OPT</sub>
    * Description: Percent difference in enumeration between the original sample and the quality checked sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [numberOfFieldsAnalyzed](numberOfFieldsAnalyzed.md)  <sub>OPT</sub>
    * Description: Number of fields analyzed for microbial cell count
    * range: [String](types/String.md)
    * inherited from: None
 * [rawMicrobialAbundance](rawMicrobialAbundance.md)  <sub>OPT</sub>
    * Description: Raw microbial abundance, not corrected for preservative volume
    * range: [String](types/String.md)
    * inherited from: None
 * [totalCellCount](totalCellCount.md)  <sub>OPT</sub>
    * Description: Total number of cells counted in the analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [dilutionFactor](dilutionFactor.md)  <sub>OPT</sub>
    * Description: The factor by which the sample was diluted prior to analysis
    * range: [Double](types/Double.md)
 * [qcAnalyzedBy](qcAnalyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample for quality control
    * range: [String](types/String.md)
    * inherited from: None

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

### Inherited from cfc_chlorophyll_pub:

 * [extractionStartDate](extractionStartDate.md)  <sub>OPT</sub>
    * Description: The start date-time for an extraction event
    * range: [Time](types/Time.md)
 * [receivedCondition](receivedCondition.md)  <sub>OPT</sub>
    * Description: Condition of the sample on the date it was received
    * range: [String](types/String.md)
 * [chlCarotWavelength1](chlCarotWavelength1.md)  <sub>OPT</sub>
    * Description: The first wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
 * [chlCarotWavelength1Abs](chlCarotWavelength1Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the first wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
 * [chlCarotWavelength2](chlCarotWavelength2.md)  <sub>OPT</sub>
    * Description: The second wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
 * [chlCarotWavelength2Abs](chlCarotWavelength2Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the second wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
 * [chlCarotWavelength3](chlCarotWavelength3.md)  <sub>OPT</sub>
    * Description: The third wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
 * [chlCarotWavelength3Abs](chlCarotWavelength3Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the third wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
 * [chlCarotWavelength4](chlCarotWavelength4.md)  <sub>OPT</sub>
    * Description: The fourth wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
 * [chlCarotWavelength4Abs](chlCarotWavelength4Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the fourth wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
 * [chlorophyllSampleCode](chlorophyllSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a chlorophyll sample
    * range: [String](types/String.md)
 * [chlorophyllSampleID](chlorophyllSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a chlorophyll sample
    * range: [String](types/String.md)
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
 * [handlingQF](handlingQF.md)  <sub>OPT</sub>
    * Description: Quality flag for sample handling
    * range: [String](types/String.md)
 * [relativeAccuracyScale](relativeAccuracyScale.md)  <sub>OPT</sub>
    * Description: Indicator for the mean relative accuracy of standards analyzed as unknowns with a run of samples
    * range: [String](types/String.md)
 * [solventVolume](solventVolume.md)  <sub>OPT</sub>
    * Description: Volume of solvent used in the extraction
    * range: [Double](types/Double.md)

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

### Inherited from inv_taxonomyRaw_pub:

 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
    * inherited from: None
 * [individualCount](individualCount.md)  <sub>OPT</sub>
    * Description: Number of individuals of the same type
    * range: [String](types/String.md)
    * inherited from: None
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
    * inherited from: None
 * [phylum](phylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the phylum or division in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [class](class.md)  <sub>OPT</sub>
    * Description: The scientific name of the class in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [order](order.md)  <sub>OPT</sub>
    * Description: The scientific name of the order in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [family](family.md)  <sub>OPT</sub>
    * Description: The scientific name of the family in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subfamily](subfamily.md)  <sub>OPT</sub>
    * Description: The scientific name of the subfamily in which the organism is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [genus](genus.md)  <sub>OPT</sub>
    * Description: The scientific name of the genus in which the organism is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subgenus](subgenus.md)  <sub>OPT</sub>
    * Description: The scientific name of the subgenus in which the taxon is classified. Values should include the genus to avoid homonym confusion
    * range: [String](types/String.md)
    * inherited from: None
 * [specificEpithet](specificEpithet.md)  <sub>OPT</sub>
    * Description: The specific epithet (second part of the species name) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
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
 * [superphylum](superphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the superphylum in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infraphylum](infraphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the infraphylum in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from ltr_ligninBatchQA_in:

 * [analysisEndDate](analysisEndDate.md)  <sub>OPT</sub>
    * Description: The end date or dateTime of analysis
    * range: [Time](types/Time.md)
    * inherited from: None
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

### Inherited from ltr_lignin_in:

 * [ligninSampleBarcode](ligninSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a lignin sample
    * range: [String](types/String.md)
    * inherited from: None
 * [ligninSampleFate](ligninSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a lignin sample
    * range: [String](types/String.md)
    * inherited from: None
 * [ligninSampleID](ligninSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a lignin sample
    * range: [String](types/String.md)
    * inherited from: None
 * [accuracyQF](accuracyQF.md)  <sub>OPT</sub>
    * Description: Quality flag for quality assurance materials associated with the run
    * range: [String](types/String.md)
    * inherited from: None
 * [measurementQF](measurementQF.md)  <sub>OPT</sub>
    * Description: Quality flag for sample measurement
    * range: [String](types/String.md)

### Inherited from sme_microbialBiomass_pub:

 * [biomassCode](biomassCode.md)  <sub>OPT</sub>
    * Description: Barcode of biomass sample
    * range: [String](types/String.md)
    * inherited from: None
 * [biomassID](biomassID.md)  <sub>OPT</sub>
    * Description: Identifier for biomass sample
    * range: [String](types/String.md)
    * inherited from: None
 * [freshMass](freshMass.md)  <sub>OPT</sub>
    * Description: Total fresh mass of a sample
    * range: [Double](types/Double.md)
 * [lipid2OH10To0Concentration](lipid2OH10To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 2-hydroxydecanoate, 2OH10:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid2OH12To0Concentration](lipid2OH12To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 2-hydroxydodecanoate, 2OH12:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid2OH14To0Concentration](lipid2OH14To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 2-hydroxytetradecanoate, 2OH14:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid2OH16To0Concentration](lipid2OH16To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 2-hydroxyhexadecanoate, 2OH16:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid3OH12To0Concentration](lipid3OH12To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 3-hydroxydodecanoate, 3OH12:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid3OH14To0Concentration](lipid3OH14To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 3-hydroxytetradecanoate, 3OH14:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [aC15To0Concentration](aC15To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of 12-methyltetradecanoic acid methyl ester, a-c15:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c10To0Concentration](c10To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of decanoate methyl ester, c10:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c11To0Concentration](c11To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of undecanoate methyl ester, c11:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c12To0Concentration](c12To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of dodecanoic acid, or lauric acid, methyl ester, c12:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c13To0Concentration](c13To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tridecanoic acid methyl ester, c13:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c14To0Concentration](c14To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tetradecanoic acid, or myristic acid, methyl ester, c14:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c14To1Concentration](c14To1Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-9-tetradecenoic acid, or myristoleic acid, methyl ester, c14:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c15To0Concentration](c15To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of pentadecanoic acid methyl ester, c15:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c15To1Concentration](c15To1Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-10-pentadecenoic acid methyl ester, c15:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c16To0Concentration](c16To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of hexadecanoic acid, or palmitic acid, methyl ester, c16:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c17To0Concentration](c17To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of heptadecanoic acid methyl ester, c17:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c17To1Concentration](c17To1Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-10-Heptadecenoic acid methyl ester, c17:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c18To0Concentration](c18To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of octadecanoic acid, or stearic acid, methyl ester, c18:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c18To1n11Concentration](c18To1n11Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of vaccenic acid or e-octadec-11-enoic acid, c18:1n11
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c18To3n3Concentration](c18To3n3Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis,cis,cis-9,12,15-octadecatrienoic acid, or alpha-linolenic acid, methyl ester, c18:3n3
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c18To3n6Concentration](c18To3n6Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of 6,9,12-octadecatrienoic acid, or gamma-linolenic acid, methyl ester, c18:3n6
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c19To0Concentration](c19To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of nonadecanoic acid methyl ester, c19:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To0Concentration](c20To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of arachidic acid methyl ester, c20:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To1Concentration](c20To1Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-11-eicosenoic acid methyl ester, c20:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To2Concentration](c20To2Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-11,14-eicosadienoic acid methyl ester, c20:2
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To3n3Concentration](c20To3n3Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-11,14,17-eicosatrienoic acid methyl ester, c20:3n3
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To3n6Concentration](c20To3n6Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-8,11,14-eicosatrienoic acid, or dihomo-gamma-linoleic acid, methyl ester, c20:3n6
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To4n6Concentration](c20To4n6Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-5,8,11,14-eicosatetraenoic acid, or arachidonic acid, methyl ester, c20:4n6
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To5n3Concentration](c20To5n3Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-5,8,11,14,17-eicosapentaenoic acid, or eicosapentaenoic acid, methyl ester, c20:5n3
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c21To0Concentration](c21To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of heneicosanoic acid methyl ester, c21:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c22To0Concentration](c22To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of docosanoic acid methyl ester, c22:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c22To1n9Concentration](c22To1n9Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-13-docosenoic acid, or erucic acid, methyl ester, c22:1n9
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c22To2Concentration](c22To2Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-13,16-docosadienoic acid methyl ester, c22:2
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c23To0Concentration](c23To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tricosanoic acid methyl ester, c23:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c24To0Concentration](c24To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tetracosanoic acid, or lignoceric acid, methyl ester, c24:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c24To1Concentration](c24To1Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-15-tetracosenoic acid, c24:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c8To0Concentration](c8To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of octanoate methyl ester, c8:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cis16To1n9Concentration](cis16To1n9Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl hexadecenoic acid, or palmitoleic acid, methyl ester, c16:1n9
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cis18To1n9Concentration](cis18To1n9Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-9-octadecenoic acid, or oleic acid, methyl ester, cis18:1n9
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cis18To2n912Concentration](cis18To2n912Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis,cis-9,12-octadecadienoic acid, or linoleic acid, or 18To2-omega-6, methyl ester, cis18:2n9-12
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cyclo17To0Concentration](cyclo17To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of the cyclopropyl C17To0 fatty acid methyl cis-9,10-methylenehexadecanoate, cyclo17:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cyclo19To0Concentration](cyclo19To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of the cyclopropyl C19To0 fatty acid methyl cis-9,10-methyleneoctadecanoate, cyclo19:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [extractionEfficiency](extractionEfficiency.md)  <sub>OPT</sub>
    * Description: Efficiency of sample extraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [freezeDryMass](freezeDryMass.md)  <sub>OPT</sub>
    * Description: Mass of sample after freeze drying
    * range: [Double](types/Double.md)
    * inherited from: None
 * [i15To0Concentration](i15To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of 13-methyltetradecanoic acid methyl ester, i15:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [i16To0Concentration](i16To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 14-methylpentadecanoate, i16:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [i17To0Concentration](i17To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 15-methylhexadecanoate, i17:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [trans18To1n9Concentration](trans18To1n9Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of trans-9-octadecenoic acid, or elaidic acid, methyl ester, trans18:1n9
    * range: [Double](types/Double.md)
    * inherited from: None
 * [trans18To2n912Concentration](trans18To2n912Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of trans-trans-9,12-octadecadienoic acid, or linoelaidic acid, methyl ester, trans18:2n9-12
    * range: [Double](types/Double.md)
    * inherited from: None
 * [totalLipidConcentration](totalLipidConcentration.md)  <sub>OPT</sub>
    * Description: Total lipid concentration calculated as the sum of all measured individual lipid components
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c16To1Cis11Concentration](c16To1Cis11Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl cis-11-hexadecenoate, 16:1 cis 11
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c17To0AnteisoConcentration](c17To0AnteisoConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 14-methyl-pentadecanoate, 17:0 anteiso
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c19To1Cis10Concentration](c19To1Cis10Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-10-nonadecenoic acid, methyl ester, c18:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c22To6CisConcentration](c22To6CisConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-4,7,10,13,16,19-docosahexaenoic acid, methyl ester
    * range: [Double](types/Double.md)
    * inherited from: None
 * [i14To0Concentration](i14To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tridecanoic acid, 12-methyl-, methyl ester, iso-14:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid10Methyl16To0Concentration](lipid10Methyl16To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 10-methyl-hexadecanoate, 10 Me-16:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid10Methyl17To0Concentration](lipid10Methyl17To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of heptadecanoic acid methyl ester, 10 Me-17:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid10Methyl18To0Concentration](lipid10Methyl18To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tuberculostearic acid methyl ester, 10 Me-18:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [extractEffStdConc](extractEffStdConc.md)  <sub>OPT</sub>
    * Description: Concentration of lipid standard used for measuring extraction efficiency with units defined by the analytical laboratory
    * range: [Double](types/Double.md)
    * inherited from: None
 * [analysisResultsQF](analysisResultsQF.md)  <sub>OPT</sub>
    * Description: Quality flag for sample analysis results
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from vst_shrubgroup_pub:

 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
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
    * inherited from: None
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
| **Mappings:** | | neon:cfc_chlorophyll_in |

